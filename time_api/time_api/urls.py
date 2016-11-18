from django.conf.urls import url, include
from django.contrib import admin

from time_tracking.views import entry_list, ProjectList, ProjectDetail, ProjectCreate, ProjectUpdate
from .routers import api_router

from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^v1/', include(api_router.urls)),
    url(r'^v1/api-token-auth/$', obtain_jwt_token),
]
