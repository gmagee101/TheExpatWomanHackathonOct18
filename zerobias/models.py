from django.db import models

# Create your models here.

from django.db import models

class Reason(models.Model):
    reason = models.CharField(max_length=1000)
    def __str__(self):
        return self.reason

class Highlight(models.Model):
    key = models.CharField(max_length=200)
    suggestions = models.CharField(max_length=1000)
    reason = models.ForeignKey(Reason, on_delete=models.CASCADE)
    def __str__(self):
        return self.key
