from django.shortcuts import render, redirect
from django.views import View
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
from validate_email import validate_email
from django.contrib import messages
from django.core.mail import EmailMessage, get_connection
from django.utils.encoding import force_bytes, force_str, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.template.loader import render_to_string
from .utils import account_activation_token, send_email_active, send_email_resetpassword
from django.contrib import auth
from django.utils import timezone
import json
# Create your views here.


class EmailValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data['email']
        if not validate_email(email):
            return JsonResponse({'email_invalid': 'Email is invalid'}, status=400)
        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_used': "This email is used, please choose another"}, status=409)
        return JsonResponse({'email_valid': True})


class UsernameValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data['username']
        if not str(username).isalnum():
            return JsonResponse({'username_error': 'username should only contain alphanumeric characters'}, status=400)
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error': 'sorry username in use,choose another one '}, status=409)
        return JsonResponse({'username_valid': True})


class RegistrationView(View):
    def get(self, request):
        return render(request, 'authentication/register.html')

    def post(self, request):
        # GET USER DATA
        # VALIDATE
        # create a user account

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        context = {
            'fieldValues': request.POST
        }

        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
                # if len(password) < 6:
                #     messages.error(request, 'Password too short')
                #     return render(request, 'authentication/register.html', context)
                user = User.objects.create_user(username=username, email=email, last_login=timezone.now() )
                user.set_password(password)
                user.is_active = False
                user.save()
                send_email_active(request, user, email)
                messages.success(request, 'Account successfully created, Please check your email to activate this account.')
                return render(request, 'authentication/register.html')
        return render(request, 'authentication/register.html')


class VerificationView(View):
    def get(self, request, uidb64, token):
        try:
            id = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=id)

            if not account_activation_token.check_token(user, token):
                return redirect('authen-login'+'?message='+'User already activated')

            if user.is_active:
                return redirect('authen-login')
            user.is_active = True
            user.save()

            messages.success(request, 'Account activated successfully')
            return redirect('authen-login')

        except Exception as ex:
            pass

        return redirect('authen-login')


class LoginView(View):
    def get(self, request):
        return render(request, 'authentication/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        if username and password:
            user = auth.authenticate(username=username, password=password)

            if user:
                if user.is_active:
                    auth.login(request, user)
                    messages.success(request, 'Welcome, ' +
                                     user.username+' you are now logged in')
                    return redirect('expenses')
                messages.error(
                    request, 'Account is not active,please check your email')
                return render(request, 'authentication/login.html')
            messages.error(
                request, 'Invalid credentials,try again')
            return render(request, 'authentication/login.html')

        messages.error(
            request, 'Please fill all fields')
        return render(request, 'authentication/login.html')


class LogoutView(View):
    def post(self, request):
        auth.logout(request)
        messages.success(request, 'You have been logged out')
        return redirect('authen-login')


class ResetPassword(View):
    def get(self, request):
        return render(request, "authentication/reset-password.html")
    
    def post(self, request):
        email = request.POST['email']
        user = User.objects.get(email=email)
        user.is_active = False
        user.save()
        send_email_resetpassword(request, user,email)
        messages.success(request, 'The link is sent to your email, please follow instruction to reset password.')
        return render(request, 'authentication/reset-password.html')


class ResetPasswordConfirm(View):
   

    def get(self, request, uidb64, token):
        context = {
            "uid": uidb64,
            "token": token,
            "login": False
        }
        return render(request, 'authentication/reset-password-confirm.html', context)
    
    def post(self, request, uidb64, token):
        password = request.POST['password']
        context = {
            "uid": uidb64,
            "token": token,
            "login": True
        }
        id = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=id)
        if password == "":
            context['login'] = False
            messages.error(request, 'Reset password failed!')
            return render(request, 'authentication/reset-password-confirm.html', context)
        user.set_password(password)
        user.is_active = True
        user.save()
        messages.success(request, 'Reset password successfully')
        return render(request, 'authentication/reset-password-confirm.html', context)

    