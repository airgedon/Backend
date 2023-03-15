from django.db import models


class category(models.Model):
    category =  models.CharField(max_length=225),
    product_type = models.CharField(max_length=225),
    product_name = models.CharField(max_length=225),


    

    
   

    
    
    
