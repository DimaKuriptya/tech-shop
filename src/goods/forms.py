from django import forms


class FilterForm(forms.Form):
    choices = (
        ('id', 'По даті додавання'),
        ('price', 'Від дешевих до дорогих'),
        ('-price', 'Від дорогих до дешевих')
    )
    is_discounted = forms.BooleanField(label='Товар зі знижкою', required=False)
    order_by = forms.ChoiceField(choices=choices, label='Сортувати')
