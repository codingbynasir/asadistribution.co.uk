from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Todo(models.Model):
    title=models.CharField(max_length=200)
    details=models.TextField()
    todo_date=models.DateField()
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    is_completed=models.BooleanField(default=False)
    def __str__(self):
        return self.title.title()