from rest_framework import routers
from fiado import views

router = routers.DefaultRouter()
router.register(r'devedores', views.DevedorList, basename='devedores')
router.register(r'', views.FiadoList, basename='fiados')