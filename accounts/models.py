from django.db import models

# Create your models here.
class students_regitser(models.Model):
    name = models.CharField(max_length=30)
    phn = models.CharField(max_length=10)
    Branch=models.CharField(max_length=10)
    RN=models.CharField(max_length=10)
    idd=models.CharField(max_length=50)
    psw=models.CharField(max_length=20)


class staff_regitser(models.Model):
    name = models.CharField(max_length=50)
    phn = models.CharField(max_length=10)
    Branch=models.CharField(max_length=255)
    RN=models.CharField(max_length=10)
    idd=models.CharField(max_length=255)
    psw=models.CharField(max_length=255)



class upload(models.Model):
    mail = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media')
    text=models.CharField(max_length=255)
    uploaded_at = models.CharField(max_length=255)

