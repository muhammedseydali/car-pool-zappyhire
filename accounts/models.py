from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self,username,phone_number,email,dob,profile_picture,password=None):
            if not email:
                raise ValueError('Email Address Is Mandatory')
            
            user = self.model(
                email = self.normalize_email(email),
                username = username,
                phone_number = phone_number,
                dob = dob,
                profile_picture = profile_picture     
            )
            user.set_password(password)
            user.save(using = self._db) 
            return user 
        
    def create_superuser(self,username,phone_number,email,dob,profile_picture,password):
            user = self.create_user(
                email = self.normalize_email(email),
                username=username,
                phone_number=phone_number,
                password=password,
                dob = dob,
                profile_picture = profile_picture
            ) 
            user.is_admin = True
            user.is_active = True
            user.is_staff = True
            user.is_superadmin = True
            user.save(using=self._db)
            return user   

class Account(AbstractBaseUser):
    username = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15,unique=False,blank=True)
    email = models.EmailField(max_length=100,unique=True)
    dob = models.DateField()
    profile_picture = models.ImageField(upload_to='images/',null=True)
    password = models.CharField(max_length=255)
    companion = models.ManyToManyField("Account", blank=True)
    #required
    date_joined = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superadmin = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','phone_number','dob','profile_picture']
    
    objects = MyAccountManager()
    
    def __str__(self):
        return self.username
    
    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self,add_label):
        return True

