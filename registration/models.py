from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)

    def __str__(self):
        return (self.email)

    def save(self, *args, **kwargs):
        """Populates username field with email. """
        if not self.username:
            self.username = self.email
        super(CustomUser,self).save(*args,**kwargs)
