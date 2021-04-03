from rest_framework import routers
from venda import views

router = routers.DefaultRouter()
router.register(r'', views.VendaListView, basename='vendas')
router.register(r'produtos', views.ProdutoListView, basename='produtos')
router.register(r'itensvenda', views.ItemVendaListView, basename='itensvenda')
