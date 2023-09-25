from django.urls import path, include
from .views import (
    BookDetailView,
    ComicDetailView,
    MovieDetailView,
    QuoteDetailView,
    SeriesDetailView,
    ShortStoriesDetailView,
    AllBookView,
    AllComicView,
    AllMovieView,
    AllQuoteView,
    AllSeriesView,
    AllShortStoriesView,
    IndexView
)

urlpatterns = [
    # path('author/<int:pk>/', AuthorDetailView.as_view(), name='author'),
    path('', IndexView.as_view(), name='index'),
    path('quotes/', AllQuoteView.as_view(), name='quotes'),
    path('quotes/<int:pk>/', QuoteDetailView.as_view()), #name='quote'),
    path('books/', AllBookView.as_view(), name='books'),
    path('books/<int:pk>/', BookDetailView.as_view()), #name='book'),
    path('comics/', AllComicView.as_view(), name='comics'),
    path('comics/<int:pk>/', ComicDetailView.as_view()), #name='comic'),
    # path('director/<int:pk>/', DirectorDetailView.as_view(), name='director'),
    path('movies/', AllMovieView.as_view(), name='movies'),
    path('movies/<int:pk>/', MovieDetailView.as_view()), #name='movie'),
    path('series/', AllSeriesView.as_view(), name='series'),
    path('series/<int:pk>/', SeriesDetailView.as_view()), #name='series'),
    path('short_stories/', AllShortStoriesView.as_view(), name='short_stories'),
    path('short_stories/<int:pk>/', ShortStoriesDetailView.as_view(),
         name='short_stories'),
    # path('illustrator/<int:pk>/', IllustratorDetailView.as_view(),
        #  name='illustrator'),
]
