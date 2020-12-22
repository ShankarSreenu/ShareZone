from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class message(models.Model):
    text=models.CharField(max_length=100)
    to_user=models.ForeignKey(User,on_delete=models.CASCADE)
    from_user=models.CharField(max_length=25)
    time=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.from_user

    

