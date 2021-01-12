from django.contrib import admin
from perpustakaan.models import Buku, Kelompok

# Register your models here.


class BukuAdmin(admin.ModelAdmin):
    """
    class untuk bagian admin
    """
    list_display = ['judul', 'penulis', 'penerbit', 'jumlah', 'kelompok']
    search_fields = ['judul', 'penulis', 'penerbit']
    list_filter = ['kelompok']
    list_per_page = 5


admin.site.register(Buku, BukuAdmin)
admin.site.register(Kelompok)
