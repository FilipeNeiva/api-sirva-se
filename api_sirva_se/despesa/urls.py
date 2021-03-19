from rest_framework import routers
from despesa.views import DespesaList

router = routers.DefaultRouter()
router.register(r'', DespesaList, basename='despesas')