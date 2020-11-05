from django.db import models

# Create your models here.

class StockList(models.Model):
    code = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=45, blank=True, null=True)

    def add_stock(self):
        self.save()

    class Meta:
        managed = False
        db_table = 'stock_list'