from django.db import models


class Brand(models.Model):
    brand_id = models.AutoField(primary_key=True)
    brand_name = models.CharField(max_length=100)
    brand_piece = models.IntegerField(null=True, blank=True, default=0)
    brand_date = models.DateField(auto_now_add=True)
    brand_time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.brand_name}({self.brand_piece})"
