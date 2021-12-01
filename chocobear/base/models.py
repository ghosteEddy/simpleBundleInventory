from typing import get_args
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone, dates

from django.utils.translation import gettext_lazy as _

# Create your models here.
class CUser(AbstractUser):
    pass

class Item(models.Model):
    item_code = models.CharField(max_length=128)
    item_name = models.CharField(max_length=256)
    in_stock = models.BigIntegerField(default=0)
    item_unit = models.CharField(max_length=64, null=True, blank=True)
    item_description = models.TextField(max_length=1024, null=True, blank=True)
    item_remark = models.CharField(max_length=512, null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True, blank=True)
    updated_on = models.DateTimeField(auto_now_add=True, blank=True)
    updated_by = models.BigIntegerField()

    def getDictData(self):
        needed = ['item_code', 'item_name', 'in_stock', 'item_unit', 'item_description', 'item_remark']
        data = {}
        for i in needed:
            data[i] = getattr(self,i)
        return data      
    
    def updateData(self, data :dict):
        self.item_code = data['item_code']
        self.item_name = data['item_name']
        self.item_unit = data['item_unit']
        self.item_description = data['item_description']
        self.item_remark = data['item_remark']
        return self

    def __str__(self):
        return str(self.id)

class Inventory(models.Model):
    class FlowType(models.TextChoices):
        IN = 'IN', _('In')
        OUT = 'OUT', _('Out')
    class FlowChannel(models.TextChoices):
        BUY = 'Buy', _('Buy')
        FB = 'Facebook', _('Facebook')
        SHOPEE = 'Shopee', _('Shopee')
        LAZADA = 'Lazada', _('Lazada')
    
    date = models.DateField(auto_now_add=True)
    flowType = models.CharField(max_length=3, choices=FlowType.choices)
    flowChannel = models.CharField(max_length=10, choices=FlowChannel.choices)
    itemId = models.BigIntegerField()
    amount = models.IntegerField()
    remark = models.CharField(max_length=64, null=True, blank=True)
    updateBy = models.BigIntegerField(default = 0)
    updated_on = models.DateTimeField(auto_now_add=True, blank=True)