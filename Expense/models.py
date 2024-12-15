from django.contrib.auth.models import User
from django.db import models



class users(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    job=models.CharField(max_length=30)
    education=models.CharField(max_length=30)
    salary=models.IntegerField()
    place=models.CharField(max_length=20)
    gender=models.CharField(max_length=10)
    email=models.CharField(max_length=20)

    def __str__(self):
        return self.name
class Category(models.Model):
    name=models.CharField(max_length=20)
    description=models.TextField()


    def __str__(self):
        return self.name



class Expense(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    amount=models.IntegerField()
    description=models.CharField(max_length=30)
    date=models.DateTimeField(auto_now_add=True)
    category_id=models.ForeignKey(Category,on_delete=models.CASCADE)




