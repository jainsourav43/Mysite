class ExtrasForm(forms.ModelForm):

    class Meta:
        model = Extras
        fields = ['roll_no', 'date', 'item', 'quantity']