from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ExperienceItem(models.Model):
    title = models.TextField()
    content = models.TextField()
    user = models.TextField()
    likes = models.IntegerField(default=0)
    tag = models.TextField(default='activity')
    
    def __str__(self):
        return "{}({})".format(self.title,self.id)

class Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    experience = models.ForeignKey(ExperienceItem,on_delete=models.CASCADE)
