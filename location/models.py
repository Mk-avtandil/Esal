from django.contrib.auth import get_user_model
from django.db import models

DIFFICULTY = (
    ('Easy', 'Easy'),
    ('Medium', 'Medium'),
    ('Hard', 'Hard')
)

User = get_user_model()


class Region(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='region')
    image_map = models.ImageField(upload_to='region')

    def __str__(self):
        return self.title


class Leisure(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, primary_key=True)

    def __str__(self) -> str:
        return self.title


class Location(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='location')
    description = models.TextField()
    leisure = models.ForeignKey(Leisure, on_delete=models.CASCADE, related_name='location')
    difficulty = models.CharField(choices=DIFFICULTY, max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.title


class Image(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='image')
    image = models.ImageField(upload_to='location')

    def __str__(self) -> str:
        return str(self.location)


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment')
    text = models.CharField(max_length=300)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='comment')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.author) + str(self.location)
