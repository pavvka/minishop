from django.db import models
from django.conf import settings

from product.models import Product
from user.models import CustomUser

class Comment(models.Model):
    product = models.ForeignKey(Product, related_name='+', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField(blank=True, null=True)

    def get_absolute_url(self):
        return f'/{self.product.slug}/'