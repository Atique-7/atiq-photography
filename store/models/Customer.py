from django.db import models
from django.core.validators import RegexValidator

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    password = models.CharField(max_length=500)

    @staticmethod
    def get_customer(email):
        try:
            return User.objects.get(email = email)
        except:
            return False
    
    def __str__(self):
        return self.first_name

    