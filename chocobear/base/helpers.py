from .models import *

def getItemById(itemId :int):
    item = Item.objects.get(id=itemId)
    return item.getDictData()