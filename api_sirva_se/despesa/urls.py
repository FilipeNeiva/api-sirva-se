from rest_framework import routers
from despesa.views import *

router = routers.DefaultRouter()
router.register(r'', DespesaList, basename='despesas')
router.register(r'itensDespesa',ItemDespesaListView , basename='itensDespesa')