from django.db import models

class Todo(models.Model):
    task = models.CharField(max_length=50)
    complete = models.BooleanField( default=False )

    def __str__(self):
        return self.task
