from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date

# Create your models here.


class Quote(models.Model):
    """Model representing a quote."""

    id = models.AutoField(
        primary_key=True, help_text="Unique ID for this quote")
    quote = models.CharField(max_length=200, help_text="Enter a quote.")

    def __str__(self) -> str:
        """String for returning quote object."""
        return self.quote

    def get_absolute_url(self):
        """Returns the url to access a detail record for this quote."""
        return reverse('quote', args=[str(self.id)])


class Book(models.Model):
    """Model representing a book."""

    id = models.AutoField(
        primary_key=True, help_text="Unique ID for this book")
    title = models.CharField(max_length=200, help_text="Enter a book title.")
    year_of_release = models.PositiveSmallIntegerField()
    author = models.ManyToManyField('Author')

    wiki_url = models.CharField(max_length=200)

    summary = models.TextField(
        max_length=1000, help_text='Enter a brief description of the book',
        blank=True,)
    # isbn = models.CharField('ISBN', max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')

    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above
    # genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')

    # def display_genre(self):
    #     """Create a string for the Genre. This is required to display genre in Admin"""
    #     return ', '.join(genre.name for genre in self.genre.all()[:3])

    # display_genre.short_description = 'Genre'

    def __str__(self) -> str:
        """String for representing model object."""
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('book', args=[str(self.id)])  # type: ignore


class Author(models.Model):
    """Model representing an author"""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    # date_of_birth = models.IntegerField('Date of Birth', null=True, blank=True)
    # date_of_death = models.IntegerField('Died', null=True, blank=True)

    class Meta:
        ordering = ['first_name', 'last_name']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance"""
        return reverse('author', args=[str(self.id)])  # type: ignore

    def __str__(self) -> str:
        """String for representing model object"""
        return f"{self.first_name}, {self.last_name}"


class Comic(models.Model):
    """Model representing a comic book."""
    id = models.AutoField(
        primary_key=True, help_text="Unique ID for this comic")
    title = models.CharField(max_length=200, help_text="Enter a comic title.")
    year_of_release = models.PositiveSmallIntegerField()

    author = models.ManyToManyField("Author")

    illustrator = models.ManyToManyField("Illustrator", blank=True)
    wiki_url = models.CharField(max_length=200, blank=True)

    summary = models.TextField(
        max_length=1000, help_text='Enter a brief description of the comic',
        blank=True)
    # isbn = models.CharField('ISBN', max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')

    # ManyToManyField used because genre can contain many comics. Comics can cover many genres.
    # Genre class has already been defined so we can specify the object above
    # genre = models.ManyToManyField(Genre, help_text='Select a genre for this comic')

    # def display_genre(self):
    #     """Create a string for the Genre. This is required to display genre in Admin"""
    #     return ', '.join(genre.name for genre in self.genre.all()[:3])

    # display_genre.short_description = 'Genre'

    def __str__(self) -> str:
        """String for representing model object"""
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this comic."""
        return reverse('comic', args=[str(self.id)])  # type: ignore


class Illustrator(models.Model):
    """Model representing an illustrator"""

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    # date_of_birth = models.IntegerField('Date of Birth', null=True, blank=True)
    # date_of_death = models.IntegerField('Died', null=True, blank=True)

    class Meta:
        ordering = ['first_name', 'last_name']

    def get_absolute_url(self):
        """Returns the url to access a particular illustrator instance"""
        return reverse('illustrator', args=[str(self.id)])  # type: ignore

    def __str__(self) -> str:
        """String for representing model object"""
        return f'{self.first_name}, {self.last_name}'


class Movie(models.Model):
    """Model representing a movie."""
    id = models.AutoField(
        primary_key=True, help_text="Unique ID for this movie")
    title = models.CharField(max_length=200, help_text="Enter a movie title.")
    year_of_release = models.PositiveSmallIntegerField()

    director = models.ManyToManyField("Director")
    wiki_url = models.CharField(max_length=200)

    summary = models.TextField(
        max_length=1000, help_text='Enter a brief description of the movie',
        blank=True)
    # isbn = models.CharField('ISBN', max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')

    # ManyToManyField used because genre can contain many movies. Movies can cover many genres.
    # Genre class has already been defined so we can specify the object above
    # genre = models.ManyToManyField(Genre, help_text='Select a genre for this movie')

    # def display_genre(self):
    #     """Create a string for the Genre. This is required to display genre in Admin"""
    #     return ', '.join(genre.name for genre in self.genre.all()[:3])

    # display_genre.short_description = 'Genre'

    def __str__(self) -> str:
        """String for representing model object"""
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this movie."""
        return reverse('movie', args=[str(self.id)])  # type: ignore


class Director(models.Model):
    """Model representing a director"""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    # date_of_birth = models.IntegerField('Date of Birth', null=True, blank=True)
    # date_of_death = models.IntegerField('Died', null=True, blank=True)

    class Meta:
        ordering = ['first_name', 'last_name']

    def get_absolute_url(self):
        """Returns the url to access a particular director instance"""
        return reverse('director', args=[str(self.id)])  # type: ignore

    def __str__(self) -> str:
        """String for representing model object"""
        return f'{self.first_name}, {self.last_name}'


class Series(models.Model):
    """Model representing a series"""
    id = models.AutoField(
        primary_key=True, help_text="Unique ID for this series")
    title = models.CharField(max_length=200, help_text="Enter a series title.")
    year_of_release = models.PositiveSmallIntegerField()

    director = models.ManyToManyField("Director")
    wiki_url = models.CharField(max_length=200)

    summary = models.TextField(
        max_length=1000, help_text='Enter a brief description of the series',
        blank=True)
    # isbn = models.CharField('ISBN', max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')

    # ManyToManyField used because genre can contain many series. Series can cover many genres.
    # Genre class has already been defined so we can specify the object above
    # genre = models.ManyToManyField(Genre, help_text='Select a genre for this series')

    # def display_genre(self):
    #     """Create a string for the Genre. This is required to display genre in Admin"""
    #     return ', '.join(genre.name for genre in self.genre.all()[:3])

    # display_genre.short_description = 'Genre'

    def __str__(self) -> str:
        """String for representing model object"""
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this series."""
        return reverse('series', args=[str(self.id)])  # type: ignore


class ShortStories(models.Model):
    """Model representing a short story."""
    id = models.AutoField(
        primary_key=True,
        help_text="Unique ID for this short story")
    title = models.CharField(
        max_length=200, help_text="Enter a short story title.")
    year_of_release = models.PositiveSmallIntegerField()

    author = models.ManyToManyField("Author")
    wiki_url = models.CharField(max_length=200)

    summary = models.TextField(
        max_length=1000, help_text='Enter a brief description of the short story',
        blank=True)
    # isbn = models.CharField('ISBN', max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')

    # ManyToManyField used because genre can contain many short stories. Short stories can cover many genres.
    # Genre class has already been defined so we can specify the object above
    # genre = models.ManyToManyField(Genre, help_text='Select a genre for this short story')

    # def display_genre(self):
    #     """Create a string for the Genre. This is required to display genre in Admin"""
    #     return ', '.join(genre.name for genre in self.genre.all()[:3])

    # display_genre.short_description = 'Genre'

    def __str__(self) -> str:
        """String for representing model object"""
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this short story."""
        return reverse('short_story', args=[str(self.id)])  # type: ignore
