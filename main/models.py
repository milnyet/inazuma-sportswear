from django.db import models

class Product(models.Model):
    pilihan_category = [
        ('jersey', 'Jersey'),
        ('sepatu', 'Sepatu'),
        ('tidak ada', 'Tidak Ada'),
        ('celana', 'Celana'),
    ]#Saya kurang tahu bagaimana yang diinginkan bentuk category pada tugas sehingga saya mengambil inspirasi dari contoh pada tutorial 1.

    name = models.CharField
    price = models.PositiveIntegerField(default=0)
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(choices=pilihan_category, default='tidak ada')
    is_featured = models.BooleanField(default=False)
