from django.db import models

class TodoList(models.Model):
    item = models.CharField(max_length=255)
    completed = models.BooleanField(default= False)


    def __str__(self):
        return self.item