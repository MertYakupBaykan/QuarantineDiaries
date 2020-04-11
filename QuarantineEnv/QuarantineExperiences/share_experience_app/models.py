from django.db import models

# Create your models here.
class ExperienceItem(models.Model):
    title = models.TextField()
    content = models.TextField()
    user = models.TextField()
    likes = models.IntegerField(default=0)

    def __str__(self):
        return "{}({})".format(self.title,self.id)
