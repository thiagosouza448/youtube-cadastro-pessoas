from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views

from .views import PessoaViewSet

router = routers.DefaultRouter()
router.register('pessoas', PessoaViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-auth/', views.obtain_auth_token)
]
