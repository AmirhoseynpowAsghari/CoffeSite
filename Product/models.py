from django.db import models
from datetime import datetime
from django.conf import settings

# Create your models here. 
class Product(models.Model):
    name           = models.CharField(max_length=150)
    description    = models.TextField()
    price          = models.DecimalField(max_digits=6,decimal_places=2)
    photo          = models.ImageField(verbose_name='Product Image', default="products/default_pro.jpg",upload_to='products/product-image/%Y/%m/%d/', null=True, blank=True)
    in_stock       = models.BooleanField(default=True)
    publish_date   = models.DateTimeField(default=datetime.now)
    likes          = models.IntegerField(default=0)                            
    reviews_count  = models.IntegerField(default=0)
    average_rating = models.FloatField(default=0.0)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('-publish_date',)
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
    
    def save(self, *args, **kwargs):
        if not self.photo:  
            self.photo = 'products/default_pro.jpg'
        super(Product, self).save(*args, **kwargs)

class Like(models.Model):
    user    = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name="likes_product")
    like_status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.get_user_fullname}-{self.product.name}-->{self.like_status}" 
    
    class Meta:
        unique_together = ("user", "product")
        ordering = ["product"]
