from rest_framework import routers
from fiado.views import *

router = routers.DefaultRouter()
router.register(r'devedores', DevedorList, basename='devedores')
router.register(r'itensfiado', ItemFiadoListView, basename='itemfiado')
router.register(r'', FiadoList, basename='fiados')