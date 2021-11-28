from .models import *

def getItemById(itemId :int):
    item = Item.objects.get(id=itemId)
    print(item.getDictData())
    return 0