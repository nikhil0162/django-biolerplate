from django.urls import include, path
from rest_framework.routers import DefaultRouter

from cooking_core.helpers.views import UserModelViewSetHp

routers = DefaultRouter()

routers.register('', UserModelViewSetHp, basename='users')

urlpatterns = [path('', include(routers.urls))]
