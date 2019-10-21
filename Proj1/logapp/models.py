from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse

class Profile(models.Model):
    users = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')


    def __str__(self):
        return self.users.username

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)






