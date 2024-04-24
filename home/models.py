from django.db import models

from userprofile.models import Patient

class Specialization(models.Model):
    specialization_id = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.specialization_id} - {self.name}'  



class Doctor(models.Model):
    doctor_id = models.CharField(primary_key=True,max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE)
    experience = models.IntegerField()
    professional_statement = models.TextField()
    # profile_picture = models.ImageField(upload_to='profile_pictures/')
    consultancy_fee = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'



class Appointment(models.Model):
    
    appointment_id = models.CharField(primary_key=True,max_length=50)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    status = models.CharField(max_length=20)

class Review(models.Model):
    review_id = models.CharField(max_length=50)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comments = models.TextField()