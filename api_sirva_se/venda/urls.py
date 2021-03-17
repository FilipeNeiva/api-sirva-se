from rest_framework import routers
from venda import views

router = routers.DefaultRouter()
router.register(r'', views.VendaList3, basename='vendas')