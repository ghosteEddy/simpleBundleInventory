from django import forms
from django.forms import widgets

class ItemForm(forms.Form):
    item_code = forms.CharField(label='SKU/Code', max_length=128, required=True)
    item_name = forms.CharField(label='Name', max_length=256, required=True, widget=forms.TextInput(attrs={'size':50}))
    item_unit = forms.CharField(label='Unit', max_length=64, required=True)
    item_description = forms.CharField(widget=forms.Textarea(attrs={"placeholder":"Max 1024 Characters","rows":5, "cols":40}))
    item_remark = forms.CharField(label='Remark', max_length=256, widget=forms.TextInput(attrs={'size':50}))
    add_shopee = forms.BooleanField(label='Shopee', required=False)
    add_lazada = forms.BooleanField(label='Lazada', required=False)