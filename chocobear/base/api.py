from datetime import date
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
        if data['add_shopee'] == True or data['add_lazada'] == True:
            addBundleHelper(item, data)
        return 0
    return -1

def addBundleHelper(itemObj :Item, data :dict):
    item = Item.objects.get(id=itemObj.id)
    bundle = Bundle(bundleSKU=item.item_code, bundleName=item.item_name, bundleDescription=item.item_description, isShopee=data['add_shopee'], isLazada=data['add_lazada'])
    bundle.save()
    bundleDetail = BundleDetail(bundleId=bundle, item_id=item, item_amount=1)    
    bundleDetail.save()
    return 0

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

def updateInventory(request):
    data = json.loads(request.body)
    if(data['flowType'] == 'BUY'):
        flowType = 'IN'
    else:
        flowType = 'OUT'
    if(data['flowType'] == 'MANUAL'):
        if (int(data['update_amount']) > 0):
            flowType = 'IN'
        else:
            flowType = 'OUT'
            data['update_amount'] *= -1
    flowChannel = data['flowType']
    amount = data['update_amount']
    remark = data['update_remark']
    itemId = data['item_id']
    user = request.user.id
    update = Inventory(itemId=itemId, amount=amount, flowType=flowType, flowChannel=flowChannel, remark=remark, updateBy=user)
    item = Item.objects.get(id=itemId)
    if flowType == 'IN':
        item.in_stock += int(amount)
    elif flowType == 'OUT':
        item.in_stock -= int(amount)
    item.save()
    update.save()
    return 0

def sellBundle(request):
    data = json.loads(request.body)
    flowType = 'OUT'
    flowChannel = data['flowType']
    amount = data['update_amount']
    remark = data['update_remark']
    itemId = data['item_id']
    user = request.user.id
    update = Inventory(itemId=itemId, amount=amount, flowType=flowType, flowChannel=flowChannel, remark=remark, updateBy=user)

    bundleId = data['bundle_id']
    bundleDetails = BundleDetail.objects.filter(bundleId=bundleId, is_deleted=False)
    for i in bundleDetails:
        item = Item.objects.get(id=i.item_id)
        item.in_stock = item.in_stock - amount * i.item_amount
        item.save()
    update.save()
    return 0

def createBundle(request):
    data = request.POST
    bundleSKU = data['SKU']
    bundleName = data['name']
    remark = data['remark']
    description = data['description']

    bundle = Bundle.objects.create(bundleSKU=bundleSKU, bundleName=bundleName, bundleDescription=description,remark=remark)
    bundle.save()
    bundleId = bundle.id
    
    for key in data:
        if 'item_' in key:
            itemId = int(key.split('_')[-1])
            item = Item.objects.get(id=itemId)
            itemAmount = int(data[key])
            bundleDetail = BundleDetail(bundleId=bundle, item_id=item, item_amount=itemAmount)
            bundleDetail.save()
    return 0

def getAllBundles(request, onlyChannel=''):
    if onlyChannel.lower == 'shopee':
        bundlesDetail = BundleDetail.objects.filter(is_deleted=False, isShopee=True).select_related('bundleId').select_related('item_id')
    elif onlyChannel == 'lazada':
        bundlesDetail = BundleDetail.objects.filter(is_deleted=False).select_related('bundleId').select_related('item_id')
    else:
        bundlesDetail = BundleDetail.objects.filter(is_deleted=False).select_related('bundleId').select_related('item_id')
    data = {}
    for i in bundlesDetail:
        bundle = i.bundleId
        item = i.item_id

        itemDetail = {}
        itemDetail['id'] = item.id
        itemDetail['name'] = item.item_name
        itemDetail['SKU'] = item.item_code
        itemDetail['amount'] = i.item_amount

        ## try add detail to bundle
        try:
            data[bundle.id]['items'].append(itemDetail)
        
        ## create new bundle
        except:
            buffer = {}
            buffer['bundleName'] = bundle.bundleName
            buffer['bundleId'] = bundle.id
            buffer['bundleSKU'] = bundle.bundleSKU
            buffer['bundleRemark'] = bundle.remark
            buffer['bundleDescription'] = bundle.bundleDescription
            buffer['isShopee'] = bundle.isShopee
            buffer['isLazada'] = bundle.isLazada

            data[bundle.id] = buffer
            data[bundle.id]['items'] = [itemDetail]

    result = []    
    for i in data:
        result.append(data[i])
    return {'bundles' : result}