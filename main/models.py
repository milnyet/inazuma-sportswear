import uuid
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    pilihan_category = [
        ('jersey', 'Jersey'),
        ('sepatu', 'Sepatu'),
        ('lain-lain', 'Lain-Lain'),
        ('celana', 'Celana'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, default="")
    price = models.PositiveIntegerField(default=0)
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(choices=pilihan_category, default='lain-lain')
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name