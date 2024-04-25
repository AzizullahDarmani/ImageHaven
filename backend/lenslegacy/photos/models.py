# from django.db import models
# from django.contrib.auth.models import AbstractUser

# class Photos(models.Model):
#     photoId = models.CharField(max_length=200, unique=True)
#     name = models.CharField(max_length=200)
#     description = models.TextField(max_length=200)
#     photoUrl = models.URLField()
    

#     def __str__ (self):
#         return self.user_name ; 




from django.db import models

class Photos(models.Model):
    photoId = models.IntegerField(unique=True)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    photoUrl = models.URLField()

    def __str__(self):
        return self.name
