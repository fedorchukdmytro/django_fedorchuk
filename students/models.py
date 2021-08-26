from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField(default=18)
    phone = models.CharField(max_length=30, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.age} {self.phone}"


class Logger(models.Model):
    method = models.CharField(max_length=6)
    path = models.CharField(max_length=20)
    execution_time = models.DecimalField(max_digits=15, decimal_places=10)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.method} {self.path} {self.execution_time}"

# class ContactUS(models.Model): 
#     title = models.CharField(max_length=100, required=True)
#     message = models.CharField(max_lenth=500, required=True)
#     email_from = models.EmailField(required=True)

#     def __str__(self):
#         return f"{self.title} {self.message} {self.email_from}"