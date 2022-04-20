from django.urls import path
from django.contrib.auth import views as auth_views


from . import views

app_name = "accounts"
urlpatterns = [
    path("accountsprofile", views.ProfileView.as_view(), name="profile"),
    # django auth
    path(
        "laccounts/ogin",
        auth_views.LoginView.as_view(template_name="accounts/login.html"),
        name="login",
    ),
    path("logout", auth_views.LogoutView.as_view(), name="logout"),
]
