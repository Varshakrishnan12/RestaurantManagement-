from django.db import models



# Create your models here.

class Feedback(models.Model):



    rating = models.PositiveIntegerField()

    comment = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)