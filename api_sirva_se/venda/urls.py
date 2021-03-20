from rest_framework import routers
from venda import views

router = routers.DefaultRouter()
router.register(r'produtos', views.ProdutoList, basename='produtos')
router.register(r'', views.VendaList, basename='vendas')