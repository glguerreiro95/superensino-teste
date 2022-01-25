from django.urls import include, path
from rest_framework import routers
from . import views
from rest_framework import generics

router = routers.DefaultRouter()
router.register(r'questoes', views.questaoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('resumo', views.resumo_exercicios, name='resumo'),
    path('listas', views.exercicios_por_lista, name='listas'),
]