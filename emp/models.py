from django.db import models


class role(models.Model):
    name = models.CharField(max_length=50, )
    
    def __str__(self): 
        return self.name

class department(models.Model):
    name = models.CharField(max_length=50)
    location=models.CharField(max_length=55)

    def __str__(self): 
        return self.name

class employee(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=40)
    dept=models.ForeignKey(department, on_delete=models.CASCADE)
    salary=models.IntegerField()
    role=models.ForeignKey(role,on_delete=models.CASCADE)
    phone = models.IntegerField()

    def __str__(self): 
        return f"{self.firstName} {self.lastName}"
# Create your models here.
