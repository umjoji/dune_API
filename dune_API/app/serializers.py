from rest_framework import serializers
from .models import (
    Author,
    Book,
    Comic,
    Director,
    Illustrator,
    Quote,
    Movie,
    Series,
    ShortStories,
)
# from django.contrib.auth.models import User


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = (
            'id',
            'first_name',
            'last_name',
        )


class BookSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(many=True)

    class Meta:
        model = Book
        fields = (
            'id',
            'title',
            'author',
            'year_of_release',
            'summary',
        )


class ComicSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(many=True)
    illustrator = serializers.StringRelatedField(many=True)

    class Meta:
        model = Comic
        fields = (
            'id',
            'title',
            'author',
            'illustrator',
            'year_of_release',
            'summary',
        )


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = (
            'id',
            'first_name',
            'last_name',
            'bio',
        )


class MovieSerializer(serializers.ModelSerializer):
    director = serializers.StringRelatedField(many=True)

    class Meta:
        model = Movie
        fields = (
            'id',
            'title',
            'director',
            'year_of_release',
            'summary',
        )


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = (
            'id',
            'quote',
        )


class IllustratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Illustrator
        fields = (
            'id',
            'first_name',
            'last_name',
            'bio',
        )


class SeriesSerializer(serializers.ModelSerializer):
    director = serializers.StringRelatedField(many=True)

    class Meta:
        model = Series
        fields = (
            'id',
            'title',
            'director',
            'year_of_release',
            'summary',
        )


class ShortStoriesSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(many=True)

    class Meta:
        model = ShortStories
        fields = (
            'id',
            'title',
            'author',
            'year_of_release',
            'summary',
        )
