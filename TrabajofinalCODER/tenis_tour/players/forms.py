from django import forms

class PlayerForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.FloatField()
    is_active = forms.BooleanField(required=False)
    country= forms.CharField(max_length=100)

class ResultForm(forms.Form):
    name=forms.CharField(max_length=100)
    tournament=forms.CharField(max_length=100)
    result=forms.CharField(max_length=100)
    points_earned=forms.IntegerField()