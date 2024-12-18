from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Item(models.Model):
    STATUS_CHOICES = [
        ('LOST', 'Lost'),
        ('FOUND', 'Found'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='item_pics')
    status = models.CharField(max_length=5, choices=STATUS_CHOICES)
    location = models.CharField(max_length=255)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)
    award_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    award_description = models.TextField(null=True, blank=True, help_text="Describe the reward you're offering for finding your item")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('item-detail', kwargs={'pk': self.pk})