from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.constraints import UniqueConstraint
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

class CustomUser(AbstractUser):

    def __str__(self):
        return self.username


class Book(models.Models):
    title = models.CharField(max_length=200, blank=True, default='', help_text='Enter a book title')
    author = models.CharField(max_length=200, blank=True, defaul='', help_text='Enter the author')
    publication_date = models.DateField(blank=True, default='')
    genre = models.CharField(max=100, blank=True, default='', help_text='Enter genre')
    featured = models.BooleanField(default=False)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['title', 'author'], name='unique_title_author')
        ]

    def __str__(self):
        return self.title


class Note(models.Models):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name)
    book = models.ForeignKey
    created_at = models.DateField(auto_now_add=True)
    note = models.TextField(max_length=200, blank=True, null=True, help_text='Write your notes here')
    private = models.BooleanField(default=True)
    page = models.PositiveIntegerField(blank=True, null=True)


    def __str__(self):
        return self.note


class Track(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='track_users')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='track_books')
    WANT = 'WR'
    READING = 'RG'
    READ = 'RD'
    STATUS_CHOICES = [
        (WANT, 'Want to read'),
        (READING, 'Reading'),
        (READ, 'Read'),
    ]
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default=WANT)

    def __str__(self):
        return f'{self.status} {self.book}'


class Note(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='note_users')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='note_books')
    created_at = models.DateField(auto_now_add=True)
    note = models.TextField(max_length=200, blank=True, null=True, help_text='Write your notes here')
    private = models.BooleanField(default=True)
    page = models.PositiveIntegerField(blank=True, null=True)


    def __str__(self):
        return self.note