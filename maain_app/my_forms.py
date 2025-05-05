from django import forms

from maain_app.models import Customer


class CustomerForm(forms.ModelForm):
    password = forms.CharField( widget=forms.PasswordInput)
    gender = forms.ChoiceField(choices=[('Male','Male'),('Female','Female')], widget=forms.RadioSelect)
    dob = forms.DateField( widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Customer
        fields = ['names', 'email', 'phone', 'password', 'weight', 'height', 'gender', 'dob']



# pip install crispy-bootstrap5
# pip install crispy-bootstrap5