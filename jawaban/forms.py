from django import forms


from .models import Jawaban

class JawabanModelForm(forms.ModelForm):
    jawaban = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Jawaban",                
                "class": "form-control"
            }
        ))

    class Meta:
        model = Jawaban
        fields = [
            'jawaban'
        ]
