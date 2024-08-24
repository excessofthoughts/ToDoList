from django.db import models


class TaskForm(models.Model):
    foooorm = models.CharField(max_length=202)
    complete = models.BooleanField(default=False)
    def __str__(self):
        return self.name