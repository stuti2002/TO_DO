from django.db import models
import uuid
# Create your models here.
class Tasks(models.Model):
    title=models.CharField(max_length=30)
    desc=models.TextField()
    id=models.UUIDField(default=uuid.uuid4 ,editable=False ,primary_key=True)
    
    def __str__(self):
        return self.title