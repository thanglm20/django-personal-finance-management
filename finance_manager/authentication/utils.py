from django.contrib.auth.tokens import PasswordResetTokenGenerator
from six import text_type
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.utils.encoding import force_bytes, force_str, DjangoUnicodeDecodeError


class AppTokenGenerator(PasswordResetTokenGenerator):

    def _make_hash_value(self, user, timestamp):
        return (text_type(user.is_active) + text_type(user.pk) + text_type(timestamp))


account_activation_token = AppTokenGenerator()


def send_email_to_user(funcor):
    def sender(request, user, email):
        current_site = get_current_site(request)
        email_subject, link, content = funcor(request, user, email)
        activate_url = 'http://'+current_site.domain+link
        send_mail(
            email_subject,
            'Hi '+user.username + content + '\n' + activate_url,
            'noreply@gmail.com',
            [email],
            fail_silently=False
        )
    return sender

@send_email_to_user
def send_email_active(request, user, email):
    uid  = urlsafe_base64_encode(force_bytes(user.pk))
    token =  account_activation_token.make_token(user)
    link = reverse('authen-activate', kwargs={'uidb64': uid, 'token': token})
    subject = "Activate account"
    content = ", Please click on this link to activate your account\n"
    return subject, link, content


@send_email_to_user
def send_email_resetpassword(request, user, email):
    uid  = urlsafe_base64_encode(force_bytes(user.pk))
    token =  account_activation_token.make_token(user)
    link = reverse('authen-resetpassword-confirm', kwargs={'uidb64': uid, 'token': token})
    subject = "Reset password"
    content = f", Your account is: \"{user.username}\", Please click on this link to reset your password\n"
    return subject, link, content