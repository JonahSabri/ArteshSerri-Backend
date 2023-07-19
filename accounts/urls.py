from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = "accounts"

urlpatterns = [
    path("", views.IndexView.as_view(), name="info"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("signup/", views.SignupView.as_view(), name="signup"),
    # path("send-otp/", views.SendOTPToPhoneView.as_view(), name="send_otp"),
    # path("verify-otp/", views.VerifyOTPFromPhoneView.as_view(), name="verify_otp"),
    # path("forgot-password/", views.ForgotPasswordView.as_view(), name="forgot_password"),
]
