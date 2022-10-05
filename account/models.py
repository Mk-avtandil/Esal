# from django.db import models
# from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
#
#
# # Create your models here.
#
#
# class UserManager(BaseUserManager):
#     """
#     Custom user model manager where email or username are the unique
#     identifiers
#     """
#
#     def create_user(self, email, username, password=None):
#         """
#         Create and save a User with given email and username
#         :param email:
#         :param username:
#         :param password:
#         :param extra_fields:
#         :return:
#         """
#         if email is None:
#             raise TypeError("Please enter a valid email address")
#         if username is None:
#             raise TypeError("Please enter a valid username")
#         email = self.normalize_email(email)
#         username = self.username
#         user = self.model(email=email, username=username)
#         user.is_active = False
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, email, password):
#         """
#         Create and save a superuser with the given email address
#         :param email:
#         :param password:
#         :param extra_fields:
#         :return:
#         """
#         if email is None:
#             raise TypeError("Superuser must have a username")
#         if password is None:
#             raise TypeError("Superuser must have a password")
#         user = self.create_user(
#             email=self.normalize_email(email),
#             password=password)
#         user.is_active = True
#         user.is_staff = True
#         user.is_superuser = True
#         user.save()
#         return user
#
#
# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     """
#     Attributes of a user
#     """
#     email = models.EmailField(max_length=30, primary_key=True)
#     username = models.CharField(max_length=20, unique=True)
#     profile_image = models.ImageField(null=True)
#     is_staff = models.BooleanField(default=False)
#
#     class Meta:
#         verbose_name = "User"
#         verbose_name_plural = "Users"
#         ordering = ["email"]
#
#     USERNAME_FIELD = "email"
#
#     objects = UserManager()
#
#     def __str__(self):
#         return str(self.email)
#
