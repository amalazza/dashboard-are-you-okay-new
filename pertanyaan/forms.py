from django import forms


from .models import Pertanyaan

class PertanyaanModelForm(forms.ModelForm):
    judul = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Judul",                
                "class": "form-control"
            }
        ))

    class Meta:
        model = Pertanyaan
        fields = [
            'pertanyaan'
        ]
