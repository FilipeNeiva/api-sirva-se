from django.contrib import admin
from .models import *

admin.site.register(Mercearia)
admin.site.register(Produto)
admin.site.register(Venda)
admin.site.register(ItemVenda)

# Register your models here.
