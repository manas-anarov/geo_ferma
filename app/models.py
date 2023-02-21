from django.contrib.gis.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser


class Farmer(AbstractUser):
    phone = models.CharField(max_length=250, default='Телефон')

    def __str__(self):
        return self.username


class Culture(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Season(models.Model):
    SEASON_CHOICES = (
        (1, 'Spring'),
        (2, 'Summer'),
        (3, 'Autumn'),
        (4, 'Winter'),
    )
    season_number = models.IntegerField(validators=[MaxValueValidator(4), MinValueValidator(1)], choices=SEASON_CHOICES)
    year = models.IntegerField(
        validators=[MinValueValidator(2023), MaxValueValidator(9999)]
    )

    def __str__(self):
        return f'{self.get_season_number_display()} {self.year}'


class Plot(models.Model):
    farmer = models.ForeignKey('Farmer', on_delete=models.CASCADE)
    culture = models.ForeignKey('Culture', on_delete=models.CASCADE)
    season = models.ForeignKey('Season', on_delete=models.CASCADE)
    contour = models.PointField(srid=4326)

    def __str__(self):
        return f'{self.farmer.username}-{self.season}'
