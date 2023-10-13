from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class petList(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    age =models.IntegerField()
    image =models.ImageField(upload_to='images/') 
    # models.ImageField( upload_to=None, height_field=None, width_field=None, max_length=None)
    # user = models.ForeignKey(User, on_delete = models.CASCADE)
    
    # STATUS_CHOICES = [
    #     ('Available', 'Available'),
    #     ('Adoption Pending', 'Adoption Pending'),
    # ]
    
    # text = models.CharField(max_length=50)
    # title = models.CharField(max_length=50)
    # age = models.PositiveIntegerField()
    # gender = models.CharField(max_length=10)
    # description = models.TextField()
    # image_path = models.CharField(max_length=100)
    # status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    # suburb = models.CharField(max_length=50, blank=True)  # Allow blank for some records
    # state = models.CharField(max_length=50)
    # fee = models.DecimalField(max_digits=10)
    # date_added = models.DateTimeField(auto_created=True)
def __str__(self):
        return self.title