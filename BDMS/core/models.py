from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver

# Create your models here.
class donarmodel(models.Model):
    gen=(('Male','Male'),('Female','Female'))
    groups=(('A+','A+'),('A-','A-'),('B+','B+'),('B-','B-'),('AB+','AB+'),('AB-','AB-'),('o+','o+'),('o-','o-'))
    name=models.CharField(max_length=70)
    phone=models.IntegerField()
    email=models.EmailField()
    age=models.IntegerField()
    gender=models.CharField(max_length=70,choices=gen,default="Male")
    bgroup=models.CharField(max_length=70,choices=groups,default="A+")
    address=models.TextField()
    message=models.TextField(null=True)
    image=models.FileField(default="Not Uploaded")

@receiver(post_delete,sender=donarmodel)
def delete_uploaded(sender,instance,**kwargs):
    instance.image.delete(False)


class contactmodel(models.Model):
    name=models.CharField(max_length=255)
    phone=models.IntegerField()
    email=models.EmailField()
    message=models.TextField()
