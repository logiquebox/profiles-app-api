from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import PermissionsMixin


class UserProfileManager(BaseUserManager):
  """user profile model manager"""
  def create_user(self, email, name, password=None):
    """handle creation of new user"""
    email = self.normalize_email(email)
    user = self.model(email=email, name=name)
    user.set_password(password)
    user.save(using=self._db)
    
    return user
  

  def create_superuser(self, email, name, password):
    """create new superuser with full details"""
    if not email:
      raise ValueError('All users must have a valid email address')

    user = self.create_user(email, name, password)
    user.is_superuser = True
    user.is_staff = True

    user.save(using=self._db)
    return user



class UserProfile(AbstractBaseUser, PermissionsMixin):
  """database model for user in the system"""
  email = models.EmailField(unique=True, max_length=254)
  name = models.CharField(max_length=254)
  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)
  
  objects = UserProfileManager()

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['name']

  def get_full_name(self):
    """Retrieve full name of users"""
    return self.name

  def get_short_name(self):
    """Retrieve short name of users"""
    return self.name
  
  def __str__(self):
    """Return string representation of users"""
    return self.email
  
