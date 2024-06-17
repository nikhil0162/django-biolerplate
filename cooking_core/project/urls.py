from django.contrib import admin
from django.urls import include, path

from cooking_core.accounts.api.urls import urlpatterns as account_urls

urlpatterns = [path('admin/', admin.site.urls), path('api/users/', include(account_urls))]
