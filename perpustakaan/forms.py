from django.forms import ModelForm
from perpustakaan.models import Buku
from django import forms


class formBuku(ModelForm):
    class Meta:
        model = Buku
        fields = '__all__'
      #  fields = ['judul', 'penulis']
      #  exclude = ['jumlah']

        widgets = {
            'judul': forms.TextInput({'class': 'form-control'}),
            'penulis': forms.TextInput({'class': 'form-control'}),
            'penerbit': forms.TextInput({'class': 'form-control'}),
            'jumlah': forms.NumberInput({'class': 'form-control'}),
            'kelompok': forms.Select({'class': 'form-select'}),
        }
