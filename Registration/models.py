from django.db import models

# Create your models here.
class Session(models.Model):
    session_name = models.CharField(max_length=100)
    def __str__(self):
        return self.session_name

class Registration(models.Model):
    full_name = models.CharField(max_length=100)
    email_address = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=10, unique=True)
    session = models.ForeignKey(Session, on_delete=models.CASCADE, null=False, blank=False)
    dietary_preferences = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.full_name