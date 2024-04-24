from django.db import models

# Create your models here.
class Patient(models.Model):
    patient_id = models.CharField(primary_key=True,max_length=80)
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    medical_history = models.TextField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
