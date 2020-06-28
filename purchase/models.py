from django.db import models
from services.models import Service
from django.contrib.auth.models import User

# Models for the 'purchase' app


class Purchase(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=50, blank=True)
    username = models.CharField(max_length=150, null=False)
    country = models.CharField(max_length=40, blank=False)
    region = models.CharField(max_length=40, blank=False)
    date = models.DateField()

    def __str__(self):
        return "{0}-{1}-{2}-{3}".format(self.id,
                                        self.date,
                                        self.full_name,
                                        self.username)


class Client(models.Model):
    purchase = models.ForeignKey(
        Purchase,
        null=False,
        on_delete=models.CASCADE
    )
    service = models.ForeignKey(
        Service,
        null=False,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User,
        null=False,
        on_delete=models.CASCADE
    )
    client_email = models.EmailField(max_length=50)
    client_url = models.URLField(max_length=200)
    client_description = models.TextField(max_length=800, blank=False, default="none")
    client_date = models.DateField(default="0", blank=False)
    audit_done = models.BooleanField(default=False)
    review_done = models.BooleanField(default=False)

    def __str__(self):
        return "{0}-{1}-{2} @ {3}".format(self.service.name,
                                          self.user.username,
                                          self.client_url,
                                          self.purchase.date)
