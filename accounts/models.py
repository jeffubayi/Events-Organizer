from django.db import models
from django.contrib.auth.models import User

class userPofile(models.Model):
    user = models.OneToOneFields(User,on_delete= models.CASCADE,related_name="profile")
    description = models.TextField(blank = True,null=True)
    location = models.charField(max_length = 30,blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    updated_on =  models.DateTimeField(auto_now=True)
    is_creator = models.BooleanField(default = False)

    def __str__ (self):
        self.user.username