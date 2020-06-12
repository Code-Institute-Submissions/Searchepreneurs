from django.db import models


# Models for the 'services' app


class Service(models.Model):
    name = models.CharField(max_length=254, default="")
    description = models.TextField()
    price = models.DecimalField(decimal_places=2)
    most_popular = models.BooleanField(default=False)
    pages = models.FloatField()

    def __str__(self):
        return self.name
