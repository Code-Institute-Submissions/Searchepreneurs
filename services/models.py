from django.db import models


# Models for the 'services' app


class Service(models.Model):
    name = models.CharField(max_length=254, default="")
    description = models.TextField()
    feature1 = models.CharField(max_length=100, blank=True)
    feature2 = models.CharField(max_length=100, blank=True)
    feature3 = models.CharField(max_length=100, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    most_popular = models.BooleanField(default=False)
    pages_audited = models.FloatField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['price']
