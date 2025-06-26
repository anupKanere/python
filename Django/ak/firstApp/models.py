from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class User(models.Model):
    EMP_TYPE = [
        ('PER' , 'PERMANENT'),
        ('INTR' , 'INTERN')
    ]
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='firstApp/images')
    # dob = models.DateField(default=timezone.now().date())
    dob = models.DateField(default=timezone.now)
    mobile_number = PhoneNumberField(blank=True, null=True)
    created = models.DateField(auto_now_add=True)
    emp_type = models.CharField(max_length=4 , choices=EMP_TYPE , default='INTR')

    def __str__(self):
        return self.name
