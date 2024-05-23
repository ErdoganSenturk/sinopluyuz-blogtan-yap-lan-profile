from django import forms
from .models import Sinopluyuz



class SinopluForm(forms.ModelForm):
    class Meta:
        model = Sinopluyuz
        fields = ["sehir", 'kategori', "first_name", "last_name", "number", "content", "image1"]  

        labels = {"sehir": "Şehir", "kategori":"Faaliyet Alanı",  "first_name": "Adınız","last_name": "Soyadınız",
        "number": "GSM","content": "Hakkınızda","image1": "Profil resminiz",}
  
