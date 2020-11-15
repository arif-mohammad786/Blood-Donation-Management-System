from django.contrib import admin
from .models import donarmodel,contactmodel
# Register your models here.
@admin.register(donarmodel)
class admindonar(admin.ModelAdmin):
    list_display=['id','name','phone','email','age','gender','bgroup','address','message','image']



@admin.register(contactmodel)
class contactadmin(admin.ModelAdmin):
    list_display=['id','name','phone','email','message']
