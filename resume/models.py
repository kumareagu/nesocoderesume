from django.db import models
# Create your models here.
class Profile(models.Model):
    content=models.CharField(max_length=200)

class Experience(models.Model):
    jobtitle=models.CharField(max_length=300)
    summary=models.CharField(max_length=300)

class keySkills(models.Model):
    languages=models.CharField(max_length=20)

class Education(models.Model):
    Qualification=models.CharField(max_length=69)
    percentage=models.IntegerField()
    college=models.CharField(max_length=70)

class Training(models.Model):
    institute=models.CharField(max_length=40)
    duration=models.IntegerField()
    instructor=models.CharField(max_length=30)
