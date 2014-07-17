from django import forms
import datetime

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
	
    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class chkInForm(forms.Form):
	Name = forms.CharField()
	checkInTime = forms.DateField(initial=datetime.date.today)


