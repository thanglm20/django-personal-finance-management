from .views import RegistrationView, UsernameValidationView, \
EmailValidationView, VerificationView, LoginView, LogoutView, \
ResetPassword, ResetPasswordConfirm
from django.urls import path
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
     path('register', RegistrationView.as_view(), name="authen-register"), # name is to set for url in html
     path('login', LoginView.as_view(), name="authen-login"),
     path('logout', LogoutView.as_view(), name="logout"),
     path('reset-password', ResetPassword.as_view(), name="authen-reset-password"),
     path('validate-username', csrf_exempt(UsernameValidationView.as_view()),
          name="validate-username"),
     path('validate-email', csrf_exempt(EmailValidationView.as_view()),
          name='validate_email'),
     path('activate/<uidb64>/<token>', VerificationView.as_view(), name='authen-activate'),
     path('reset-password-confirm/<uidb64>/<token>', ResetPasswordConfirm.as_view(), name='authen-resetpassword-confirm'),

]


