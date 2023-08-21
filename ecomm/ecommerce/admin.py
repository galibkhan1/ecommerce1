from django.contrib import admin
from unicodedata import category

from .models import registeration ,Category , upload_product,demodb

# Register your models here.


# class register_dtls(admin.modelAdmin):
#     list_display = ['firstname', 'lastname', 'email']

admin.site.register(registeration)
admin.site.register(Category)
admin.site.register(upload_product)
admin.site.register(demodb)
