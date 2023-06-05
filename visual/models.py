from django.core.exceptions import ValidationError
from django.db import models


class Contract(models.Model):
    customer = models.CharField()
    seller = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id} Contract between {self.seller} and {self.customer}'


class Producer(models.Model):
    name = models.CharField()
    country = models.CharField()
    phone = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return f'{self.name} {self.country}'


class CreditApplication(models.Model):
    related_contract = models.OneToOneField(Contract, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if not self.related_contract.position_set.all():
            raise ValidationError('Contract must have related positions')
        super().clean()

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.id}'


class Position(models.Model):
    name = models.CharField()
    quantity = models.IntegerField()
    price_of_one = models.FloatField()
    related_contract = models.ForeignKey(Contract, on_delete=models.SET_NULL, null=True, blank=True)
    related_producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id} {self.name}'


