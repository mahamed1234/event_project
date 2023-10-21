from django.urls import include, path

from rest_framework import routers
from eventproject.users.views import UserViewSet

from eventproject.events import views as events_views
from django.contrib import admin
 

 

from rest_framework_simplejwt.views import (

    TokenObtainPairView,

    TokenRefreshView,

)

 

router = routers.DefaultRouter()

router.register(r"Events", events_views.EventViewSet, basename="Event")
router.register(r'users', UserViewSet)

 

# Wire up our API using automatic URL routing.

# Additionally, we include login URLs for the browsable API.

urlpatterns = [

  path("admin/", admin.site.urls),

    path("", include(router.urls)),

    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),

    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    

]

 