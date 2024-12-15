from django.contrib import admin
from Expense.models import Category,Expense,users
# Register your models here.
admin.site.register(Category)
admin.site.register(Expense)
admin.site.register(users)


