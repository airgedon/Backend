from django.db import models


class category(models.Model):
    product_category = models.CharField(max_length=100, default='')
    roduct_type = models.CharField(max_length=100, default='')
    product_name = models.CharField(max_length=100, default='название продукта')
    product_price = models.IntegerField(default=0)

    def __str__(self):
        return self.product_category


    


    

    
   

    
    
    
