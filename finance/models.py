from django.db import models

class Transaction(models.Model):
    amount = models.CharField()
    income = models.BooleanField()
    category = models.CharField()
    created_at = models.DateTimeField()

    def __str__(self):
        return f'{self.amount} {self.income}'

class Category(models.Model):
    title = models.CharField()
