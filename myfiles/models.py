from django.db import models

# Create your models here.
class Kurs(models.Model):
    nomi = models.CharField(max_length=50)
    def __str__(self):
        return self.nomi

class Student(models.Model):
    ism = models.CharField(max_length=40)
    familiya = models.CharField(max_length=40)
    yoshi = models.IntegerField()
    manzil = models.CharField(max_length=100)
    yonalish = models.ForeignKey(Kurs,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)

class Ishxona(models.Model):
    ism = models.CharField(max_length=30)
    familiya = models.CharField(max_length=30)
    yosh = models.IntegerField()
    lavozim = models.CharField(max_length=50)
    ish_staji = models.IntegerField()
    sana = models.DateTimeField(auto_now=True)