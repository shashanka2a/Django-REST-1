from django.db import models

# Create your models here.

class Bank(models.Model):
    ifsc	  = models.CharField(max_length=200,null=True,blank=True)
    bank_id   = models.CharField(max_length=200,null=True,blank=True)
    branch    = models.CharField(max_length=200,null=True,blank=True)
    address	  = models.CharField(max_length=500,null=True,blank=True)
    city      = models.CharField(max_length=200,null=True,blank=True)
    district  = models.CharField(max_length=200,null=True,blank=True)
    state     = models.CharField(max_length=200,null=True,blank=True)
    bank_name = models.CharField(max_length=200,null=True,blank=True)
    def __str__(self):
        return self.ifsc