from django.urls import include, path

from .api.urls import urlpatterns as api_v1

urlpatterns = [path('v1/', include(api_v1))]
