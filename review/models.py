from django.db import models


# Models for the 'review' app


class Review(models.Model):
    RATING_CHOICES = [(i, i) for i in range(1, 10)]

    review_username = models.CharField(max_length=150, null=False)
    review_service = models.CharField(max_length=254, null=False)
    rating = models.CharField(choices=RATING_CHOICES, max_length=2)
    review_title = models.CharField(max_length=100, null=False)
    review_description = models.TextField()
    review_image = models.ImageField(upload_to='images')
    date_created = models.DateTimeField()
    last_edited = models.DateTimeField()

    def __str__(self):
        return "{0}-{1}-{2} @ {3}".format(self.review_username,
                                          self.rating,
                                          self.review_title,
                                          self.date_created)
