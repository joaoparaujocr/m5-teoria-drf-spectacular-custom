from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from .views import AccountView

urlpatterns = [
    path('token-auth/', obtain_auth_token),
    path('accounts/', AccountView.as_view()),
]