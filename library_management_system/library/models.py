from django.db import models
from django.contrib.auth.models import User
from django.db import connections
# Create your models here.

class admin_signup(models.Model):
    au=models.OneToOneField(User,on_delete=models.CASCADE)
    admin_address=models.CharField(max_length=20)
    admin_number=models.IntegerField(max_length=20)
    

class book_details(models.Model):
    Book_Name=models.CharField(max_length=50)
    Book_Image=models.FileField(upload_to="images")
    Book_Description=models.TextField(max_length=1000)
    Book_date=models.CharField(max_length=50)
    class Meta:
        db_table="library_book_details"