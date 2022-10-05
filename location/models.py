from django.db import models

DIFFICULTY = (
    ('Easy', 'Easy'),
    ('Medium', 'Medium'),
    ('Hard', 'Hard')
)


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


class Location(models.Model):
    title = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='location')
    description = models.TextField()
    leisure = models.ForeignKey(Leisure, on_delete=models.CASCADE, related_name='location')
    difficulty = models.CharField(choices=DIFFICULTY, max_length=10)


class Image(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='location')
