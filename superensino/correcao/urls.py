from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'listas', views.listaViewSet)
router.register(r'questoes', views.questaoViewSet)
router.register(r'respondidas', views.respondidasViewSet)
router.register(r'corretas', views.corretasViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]