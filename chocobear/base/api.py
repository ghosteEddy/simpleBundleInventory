from django.http.response import HttpResponse
from django.utils import timezone
from .models import *
from .forms import *
import json

def addItem(request):
    form = ItemForm(request.POST)
    if form.is_valid():
        user = request.user.id
        data = form.cleaned_data
        item = Item(item_code=data['item_code'], item_name=data['item_name'],item_unit=data['item_unit'], item_description=data['item_description'], item_remark=data['item_remark'], updated_by=user)
        item.save()
        return 0
    return -1

def editItem(request, item_id):
    form = ItemForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        item = Item.objects.get(id=item_id)
        item.updateData(data)
        item.save()
        return 0
    return 1

def getAllItems(request):
    allItems = Item.objects.filter(is_deleted=False).order_by('-id')
    response = {}
    response['total_items'] = allItems.count()
    response['items'] = list(allItems.values('id', 'item_code', 'item_name', 'item_unit', 'item_description', 'item_remark', 'in_stock'))
    return response

def deleteItem(request):
    targetId = json.loads(request.body)['item_id']
    item = Item.objects.get(id=targetId)
    item.is_deleted = True
    item.updated_on = timezone.now()
    item.save()
    return 0
    