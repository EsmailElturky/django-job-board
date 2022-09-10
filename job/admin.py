from django.contrib import admin
from .models import Job,Category
from .models import  Apply
# Register your models here.

admin.site.register(Job)
admin.site.register(Category)
admin.site.register(Apply)