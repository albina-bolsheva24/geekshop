from django import forms

from ordersapp.models import Order, OrderItem


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        exclude = ('user', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_texts = ''


class OrderItemForm(forms.ModelForm):
    price = forms.CharField(label='Цена (руб/шт)', required=False)

    class Meta:
        model = OrderItem
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_texts = ''
