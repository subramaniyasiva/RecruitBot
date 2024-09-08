from django.db import models

# Create your models here.
class details(models.Model):
    name=models.CharField(max_length=50)
    Age=models.IntegerField()
    mail=models.EmailField(max_length=254)
    contact=models.CharField(max_length=50)
    address = models.TextField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    linkedin=models.URLField(max_length=200)
    skills=models.TextField()
    Degree=models.CharField(max_length=50)
    Specialization=models.CharField(max_length=50)
    exp=models.CharField(max_length=50)
    prev_employer=models.CharField(max_length=50)
    Agreement=models.CharField( max_length=50)
    start_date=models.DateField(auto_now=False, auto_now_add=False)
    refby=models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
