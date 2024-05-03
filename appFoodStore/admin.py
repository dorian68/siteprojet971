from django.contrib import admin

# Register your models here.
from .models import Article,Order

admin.site.register(Article)
admin.site.register(Order)