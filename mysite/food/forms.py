from django import forms
from food.models import Item

class ItemForm(forms.ModelForm):
    class Meta :
        model = Item
        fields = ['prod_code' , 'for_user' , 'Item_name' , 'Item_desc' , 'Item_pric' , 'Item_image']
        