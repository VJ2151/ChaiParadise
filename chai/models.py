from django.db import models
from django.utils import timezone
from decimal import Decimal
from django.contrib.auth.models import User

# Create your models here.
class ChaiVariety(models.Model):
    CHAI_TYPE_CHOICE = [ 
        ('BL', 'Black'),
        ('GR', 'Green'),
        ('WH', 'White'),
        ('OOL', 'Oolong'),
        ('HER', 'Herbal'),
        ('MAS', 'Masala'),
        ('CH', 'Chai'), ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    detail_image = models.ImageField(upload_to='detail_chai/', blank=True, null=True)
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=3, choices=CHAI_TYPE_CHOICE)
    description = models.TextField(default='')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))

    def __str__(self):
        return self.name

class ChaiReview(models.Model):
    chai = models.ForeignKey(ChaiVariety, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=2,decimal_places=1, default=Decimal('0.0'))
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)    

    def __str__(self):
        return f'{self.user.username} review for {self.chai.name}'