from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=30)
    farsi_title = models.CharField(null=True, blank=True, max_length=40)
    slug = models.SlugField(null=True, blank=True, unique=True)

    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.title)
        super(Category, self).save()


class Artist(models.Model):
    biography = models.TextField(null=True, blank=True)
    name = models.CharField(max_length=50)
    farsi_name = models.CharField(null=True, blank=True, max_length=40)
    image = models.ImageField(upload_to='artists')
    slug = models.SlugField(null=True, blank=True, unique=True)

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)
        super(Artist, self).save()


class Album(models.Model):
    name = models.CharField(max_length=50)
    farsi_name = models.CharField(null=True, blank=True, max_length=40)
    image = models.ImageField(upload_to='tracks')
    artist = models.ManyToManyField(Artist, related_name="albums")
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=True, blank=True, unique=True)

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)
        super(Album, self).save()

    class Meta:
        ordering = ('-created',)


class Track(models.Model):
    name = models.CharField(null=True, blank=True, max_length=40)
    farsi_name = models.CharField(null=True, blank=True, max_length=40)
    category = models.ManyToManyField(Category, related_name="tracks")
    artist = models.ManyToManyField(Artist, related_name="tracks")
    single = models.BooleanField(default=True)
    album = models.ForeignKey(Album, null=True, blank=True, on_delete=models.CASCADE, related_name="tracks")
    created = models.DateTimeField(auto_now_add=True)
    cover = models.ImageField(upload_to='tracks', null=True, blank=True)
    quality_320 = models.FileField(upload_to='files',  null=True, blank=True)
    quality_128 = models.FileField(upload_to='files', null=True, blank=True)
    lyric = models.TextField(null=True, blank=True)
    slug = models.SlugField(null=True, blank=True, unique=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)
        super(Track, self).save()

    def __str__(self):
        return f"{self.name} - {self.artist.first()}"

    class Meta:
        ordering = ('-created',)


class Comment(models.Model):
    track = models.ForeignKey(Track, on_delete=models.CASCADE, null=True, blank=True, related_name='comments')
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True, blank=True, related_name='comments')
    email = models.EmailField()
    user = models.CharField(max_length=30)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.body[:30]