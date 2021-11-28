from django import forms
from django.forms.models import ModelForm
from django import forms
from .models import Item

class ItemForm(forms.Form):
    item_code = forms.CharField(label='SKU/Code', max_length=128, required=True)
    item_name = forms.CharField(label='Name', max_length=256, required=True)
    item_unit = forms.CharField(label='Unit', max_length=64, required=True)
    item_description = forms.CharField(widget=forms.Textarea(attrs={"placeholder":"Max 1024 Characters","rows":5, "cols":40}))
    item_remark = forms.CharField(label='Remark', max_length=256, required=True)

    def edit(self, item :dict):
        self.item_code = forms.CharField(label='SKU/Code', max_length=128, required=True, placeholder=['item_code'])
        self.item_name = forms.CharField(label='Name', max_length=256, required=True, placeholder=['item_name'])
        self.item_unit = forms.CharField(label='Unit', max_length=64, required=True, placeholder=item['item_unit'])
        self.item_description = forms.CharField(widget=forms.Textarea(attrs={"placeholder":item['item_placeholder'],"rows":5, "cols":40}))
        self.item_remark = forms.CharField(label='Remark', max_length=256, required=True, placeholder=item['item_remark'])
        return self