from django.contrib import admin
from .models import adminmodel
# Register your models here.
@admin.register(adminmodel)
class superadmin(admin.ModelAdmin):
    list_display=['id','email','password']