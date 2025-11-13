from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    phone = models.IntegerField(default=0)
    hire_date = models.DateTimeField(auto_now_add=True)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    location = models.CharField(max_length=100, default='Unknown')  

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.role.name}"

          
