from django.db.models import OuterRef, Subquery, Exists
from django.db.models.functions import JSONObject, Coalesce
from django.shortcuts import render
from rest_framework import generics
from django.contrib.postgres.expressions import ArraySubquery

from store import models
from option.models import Option, OptionValue, PostOption, PostOptionValue
from store import serializers


class MainListAPIView(generics.ListAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer

    def get_queryset(self):
        qs = super().get_queryset().filter(
            parent__isnull=True
        ).annotate(
            categories=ArraySubquery(
                models.Category.objects.filter(
                    parent=OuterRef('pk')
                ).values(json=JSONObject(id="id", title="title"))
            )
        )

        return qs


class CategoryPostListAPIView(generics.ListAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.CategoryPostSerializer

    def get_queryset(self):
        posts = super().get_queryset()

        if self.kwargs.get('category_id'):
            posts = posts.filter(category_id=self.kwargs.get(
                'category_id'
            ))

        posts = posts.filter(
            category__parent_id=self.kwargs.get('parent_id')
        ).annotate(
            # get one option from PostOptionValue
            # where option typ is "Button"
            option=Subquery(
                PostOptionValue.objects.filter(
                    post_option__post=OuterRef('pk'),
                    post_option__option__typ='Button'
                ).values(
                    'option_value__value'
                )
            ),
            # Check user likes or don't like for the post
            is_like=Coalesce(
                Exists(self.request.user.favorite_posts.filter(
                    id=OuterRef('pk')
                )), False
            ))

        return posts


class PostDetailAPIView(generics.RetrieveAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostDetailSerializer




