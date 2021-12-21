from django.db import models

# Create your models here.
class Employee(models.Model):
    employee_id = models.IntegerField()
    name = models.CharField(max_length=200)
    email_id = models.EmailField(max_length=256)
    mobile_number = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return f"{str(self.employee_id)} {str(self.name)}"


