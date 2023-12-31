from django.shortcuts import render
from rest_framework import generics, permissions, status
from django.http import HttpResponse
from django.template import loader
from rest_framework.response import Response
from rest_framework.views import APIView
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

from .serializers import (
    AuthorSerializer,
    BookSerializer,
    ComicSerializer,
    DirectorSerializer,
    IllustratorSerializer,
    QuoteSerializer,
    MovieSerializer,
    SeriesSerializer,
    ShortStoriesSerializer,
)


# Create your views here.


def index(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())


def quotes(request):
    quotes = Quote.objects.all().values()  # get all members
    template = loader.get_template('quotes.html')
    context = {
        'quotes': quotes,
    }
    return HttpResponse(template.render(context, request))


def books(request):
    books = Book.objects.all().values()  # get all members
    template = loader.get_template('books.html')
    context = {
        'books': books,
    }
    return HttpResponse(template.render(context, request))


def movies(request):
    movies = Movie.objects.all().values()  # get all members
    template = loader.get_template('movies.html')
    context = {
        'movies': movies,
    }
    return HttpResponse(template.render(context, request))


def comics(request):
    quotes = Comic.objects.all().values()  # get all members
    template = loader.get_template('comics.html')
    context = {
        'comics': comics,
    }
    return HttpResponse(template.render(context, request))


def short_stories(request):
    short_stories = ShortStories.objects.all().values()  # get all members
    template = loader.get_template('short_stories.html')
    context = {
        'short_stories': short_stories,
    }
    return HttpResponse(template.render(context, request))


def series(request):
    series = Series.objects.all().values()  # get all members
    template = loader.get_template('series.html')
    context = {
        'series': series,
    }
    return HttpResponse(template.render(context, request))


def book_details(request, pk):
    book = Book.objects.get(pk=pk)
    template = loader.get_template('books_detail.html')
    context = {
        'book': book,
    }
    return HttpResponse(template.render(context, request))


def movie_details(request, pk):
    movie = Movie.objects.get(pk=pk)
    template = loader.get_template('movies_detail.html')
    context = {
        'movie': movie,
    }
    return HttpResponse(template.render(context, request))


def comic_details(request, pk):
    comic = Comic.objects.get(pk=pk)
    template = loader.get_template('comics_detail.html')
    context = {
        'comic': comic,
    }
    return HttpResponse(template.render(context, request))


def series_details(request, pk):
    series = Series.objects.get(pk=pk)
    template = loader.get_template('series_details.html')
    context = {
        'series': series,
    }
    return HttpResponse(template.render(context, request))


def short_stories_details(request, pk):
    short_stories = ShortStories.objects.get(pk=pk)
    template = loader.get_template('short_stories_detail.html')
    context = {
        'short_stories': short_stories,
    }
    return HttpResponse(template.render(context, request))


# class AllAuthorsView(APIView):

#     def get(self, request, format=None):
#         authors = Author.objects.all()

#         if not authors:
#             # Return a custom error response if there are no authors
#             return Response(
#                 {'error': 'No authors found.'},
#                 status=status.HTTP_404_NOT_FOUND
#             )

#         serializer = AuthorSerializer(authors, many=True)
#         return Response(serializer.data)


# class AuthorDetailView(APIView):

#     def get_object(self, pk):
#         try:
#             return Author.objects.get(pk=pk)
#         except Author.DoesNotExist as e:
#             return e

#     def get(self, request, pk, format=None):
#         author = self.get_object(pk)

#         if isinstance(author, Author):
#             serializer = AuthorSerializer(author)
#             return Response(serializer.data)
#         else:
#             # Return a custom error response
#             return Response(
#                 {'error': 'Author does not exist.'},
#                 status=status.HTTP_404_NOT_FOUND
#             )

    # def put(self, request, pk, format=None):
    #     author = self.get_object(pk)
    #     serializer = AuthorSerializer(author, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(
    #         serializer.errors, status=status.HTTP_400_BAD_REQUEST
    #     )

    # def delete(self, request, pk, format=None):
    #     author = self.get_object(pk)
    #     author.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


class AllBookView(APIView):

    def get(self, request, format=None):
        books = Book.objects.all()

        if not books:
            # Return a custom error response if there are no books
            return Response(
                {'error': 'No books found.'},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)


class BookDetailView(APIView):

    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist as e:
            return e

    def get(self, request, pk, format=None):

        book = self.get_object(pk)
        if isinstance(book, Book):
            serializer = BookSerializer(book)
            return Response(serializer.data)
        else:
            # Return a custom error response
            return Response(
                {'error': 'Book does not exist.'},
                status=status.HTTP_404_NOT_FOUND
            )

#     def put(self, request, pk, format=None):
#         book = self.get_object(pk)
#         serializer = BookSerializer(book, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(
#             serializer.errors, status=status.HTTP_400_BAD_REQUEST
#         )

#     def delete(self, request, pk, format=None):
#         book = self.get_object(pk)
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class AllComicView(APIView):

    def get(self, request, format=None):
        comics = Comic.objects.all()

        if not comics:
            # Return a custom error response if there are no comics
            return Response(
                {'error': 'No comics found.'},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = ComicSerializer(comics, many=True)
        return Response(serializer.data)


class ComicDetailView(APIView):

    def get_object(self, pk):
        try:
            return Comic.objects.get(pk=pk)
        except Comic.DoesNotExist as e:
            return e

    def get(self, request, pk, format=None):
        comic = self.get_object(pk)

        if isinstance(comic, Comic):
            serializer = ComicSerializer(comic)
            return Response(serializer.data)
        else:
            # Return a custom error response
            return Response(
                {'error': 'Comic does not exist.'},
                status=status.HTTP_404_NOT_FOUND
            )

#     def put(self, request, pk, format=None):
#         comic = self.get_object(pk)
#         serializer = ComicSerializer(comic, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(
#             serializer.errors, status=status.HTTP_400_BAD_REQUEST
#         )

#     def delete(self, request, pk, format=None):
#         comic = self.get_object(pk)
#         comic.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)




# class DirectorDetailView(APIView):

#     def get_object(self, pk):
#         try:
#             return Director.objects.get(pk=pk)
#         except Director.DoesNotExist as e:
#             return e

#     def get(self, request, pk, format=None):
#         director = self.get_object(pk)

#         if isinstance(director, Director):
#             serializer = DirectorSerializer(director)
#             return Response(serializer.data)
#         else:
#             # Return a custom error response
#             return Response(
#                 {'error': 'Director does not exist.'},
#                 status=status.HTTP_404_NOT_FOUND
# )

    # def put(self, request, pk, format=None):
    #     director = self.get_object(pk)
    #     serializer = DirectorSerializer(director, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(
    #         serializer.errors, status=status.HTTP_400_BAD_REQUEST
    #     )

    # def delete(self, request, pk, format=None):
    #     director = self.get_object(pk)
    #     director.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

class AllQuoteView(APIView):

    def get(self, request, format=None):
        quotes = Quote.objects.all()

        if not quotes:
            # Return a custom error response if there are no quotes
            return Response(
                {'error': 'No quotes found.'},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = QuoteSerializer(quotes, many=True)
        return Response(serializer.data)


class QuoteDetailView(APIView):

    def get_object(self, pk):
        try:
            return Quote.objects.get(pk=pk)
        except Quote.DoesNotExist as e:
            return e

    def get(self, request, pk, format=None):
        quote = self.get_object(pk)

        if isinstance(quote, Quote):
            serializer = QuoteSerializer(quote)
            return Response(serializer.data)
        else:
            # Return a custom error response
            return Response(
                {'error': 'Quote does not exist.'},
                status=status.HTTP_404_NOT_FOUND
            )

    # def put(self, request, pk, format=None):
    #     quote = self.get_object(pk)
    #     serializer = QuoteSerializer(quote, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(
    #         serializer.errors, status=status.HTTP_400_BAD_REQUEST
    #     )

    # def delete(self, request, pk, format=None):
    #     quote = self.get_object(pk)
    #     quote.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


# class IllustratorDetailView(APIView):

#     def get_object(self, pk):
#         try:
#             return Illustrator.objects.get(pk=pk)
#         except Illustrator.DoesNotExist as e:
#             return e

#     def get(self, request, pk, format=None):
#         illustrator = self.get_object(pk)

#         if isinstance(illustrator, Illustrator):
#             serializer = IllustratorSerializer(illustrator)
#             return Response(serializer.data)
#         else:
#             # Return a custom error response
#             return Response(
#                 {'error': 'Illustrator does not exist.'},
#                 status=status.HTTP_404_NOT_FOUND
#             )

    # def put(self, request, pk, format=None):
    #     illustrator = self.get_object(pk)
    #     serializer = IllustratorSerializer(illustrator, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(
    #         serializer.errors, status=status.HTTP_400_BAD_REQUEST
    #     )

    # def delete(self, request, pk, format=None):
    #     illustrator = self.get_object(pk)
    #     illustrator.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


class AllMovieView(APIView):

    def get(self, request, format=None):
        movies = Movie.objects.all()

        if not movies:
            # Return a custom error response if there are no movies
            return Response(
                {'error': 'No movies found.'},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)


class MovieDetailView(APIView):

    def get_object(self, pk):
        try:
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist as e:
            return e

    def get(self, request, pk, format=None):
        movie = self.get_object(pk)

        if isinstance(movie, Movie):
            serializer = MovieSerializer(movie)
            return Response(serializer.data)
        else:
            # Return a custom error response
            return Response(
                {'error': 'Movie does not exist.'},
                status=status.HTTP_404_NOT_FOUND
            )

    # def put(self, request, pk, format=None):
    #     movie = self.get_object(pk)
    #     serializer = MovieSerializer(movie, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(
    #         serializer.errors, status=status.HTTP_400_BAD_REQUEST
    #     )

    # def delete(self, request, pk, format=None):
    #     movie = self.get_object(pk)
    #     movie.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


class AllSeriesView(APIView):

    def get(self, request, format=None):
        series = Series.objects.all()

        if not series:
            # Return a custom error response if there are no series
            return Response(
                {'error': 'No series found.'},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = SeriesSerializer(series, many=True)
        return Response(serializer.data)


class SeriesDetailView(APIView):

    def get_object(self, pk):
        try:
            return Series.objects.get(pk=pk)
        except Series.DoesNotExist as e:
            return e

    def get(self, request, pk, format=None):
        series = self.get_object(pk)

        if isinstance(series, Series):
            serializer = SeriesSerializer(series)
            return Response(serializer.data)
        else:
            # Return a custom error response
            return Response(
                {'error': 'Series does not exist.'},
                status=status.HTTP_404_NOT_FOUND
            )

    # def put(self, request, pk, format=None):
    #     series = self.get_object(pk)
    #     serializer = SeriesSerializer(series, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(
    #         serializer.errors, status=status.HTTP_400_BAD_REQUEST
    #     )

    # def delete(self, request, pk, format=None):
    #     series = self.get_object(pk)
    #     series.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


class AllShortStoriesView(APIView):

    def get(self, request, format=None):
        short_stories = ShortStories.objects.all()

        if not short_stories:
            # Return a custom error response if there are no short stories
            return Response(
                {'error': 'No short stories found.'},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = ShortStoriesSerializer(short_stories, many=True)
        return Response(serializer.data)


class ShortStoriesDetailView(APIView):

    def get_object(self, pk):
        try:
            return ShortStories.objects.get(pk=pk)
        except ShortStories.DoesNotExist as e:
            return e

    def get(self, request, pk, format=None):
        short_story = self.get_object(pk)

        if isinstance(short_story, ShortStories):
            serializer = ShortStoriesSerializer(short_story)
            return Response(serializer.data)
        else:
            # Return a custom error response
            return Response(
                {'error': 'Short story does not exist.'},
                status=status.HTTP_404_NOT_FOUND
            )

    # def put(self, request, pk, format=None):
    #     shortstories = self.get_object(pk)
    #     serializer = ShortStoriesSerializer(shortstories, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(
    #         serializer.errors, status=status.HTTP_400_BAD_REQUEST
    #     )

    # def delete(self, request, pk, format=None):
    #     shortstories = self.get_object(pk)
    #     shortstories.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
