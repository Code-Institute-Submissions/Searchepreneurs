from django.db import models
from django.utils import timezone


# Models for the 'review' app


class Review(models.Model):
    RATING_CHOICES = [(i, i) for i in range(1, 11)]

    review_username = models.CharField(max_length=150, null=False)
    review_service = models.CharField(max_length=254, null=False)
    rating = models.PositiveIntegerField(choices=RATING_CHOICES)
    review_title = models.CharField(max_length=100, null=False)
    review_description = models.TextField(max_length=120)
    review_image = models.ImageField(upload_to='images', blank=True)
    date_created = models.DateTimeField(blank=True, default=timezone.now)
    last_edited = models.DateTimeField(blank=True, default=timezone.now)

    def __str__(self):
        return "{0}-{1}-{2} @ {3}".format(self.review_username,
                                          self.rating,
                                          self.review_title,
                                          self.date_created)
