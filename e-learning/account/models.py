from django.db import models

class TachersProfiles(models.Model):
    fname = models.CharField(max_length=70)
    lname = models.CharField(max_length=70)
    slug = models.SlugField(max_length=70, null=True, unique=True)
    info = models.TextField()
    pic = models.ImageField(upload_to="images/")
    level = models.CharField(max_length=70)
    age = models.IntegerField()

    def __str__(self):
        return self.fname