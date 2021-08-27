from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from .views import LogInView, SignUpView

router = DefaultRouter()

router.register(r"signup", SignUpView, basename="signup")

urlpatterns = [
    path(r"users/", include(router.urls)),
    path("api/log_in/", LogInView.as_view(), name="log_in"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
