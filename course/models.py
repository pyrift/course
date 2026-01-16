from django.db import models
from django.db.models import ManyToManyField

class Branch(models.Model):
    branch_name = models.CharField(max_length = 100)

    def __str__(self):
        return self.branch_name

class Burning(models.Model):
    burning = models.CharField(max_length=100)

    def __str__(self):
        return self.burning

class Infaration(models.Model):
    young = models.IntegerField()
    thought = models.TextField()
    direction =  ManyToManyField(Burning)
    created_at = models.DateTimeField(auto_now_add=True)
    phone_number = models.IntegerField()
    select_branch = models.ManyToManyField(Branch)
    telegram_urls = models.CharField(max_length = 100)

    def __str__(self):
        return self.telegram_urls