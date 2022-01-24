from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib.admin.models import LogEntry

from LoggingActivity.models import LogUserActivity


@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    description = f'user {user.username} logged in through page {request.META.get("HTTP_REFERER")}'
    LogUserActivity.objects.create(description=description)


@receiver(user_login_failed)
def log_user_login_failed(sender, credentials, request, **kwargs):
    description = f'user {credentials.get("username")} logged in failed through page {request.META.get("HTTP_REFERER")}'
    LogUserActivity.objects.create(description=description)


@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    description = f'user {user.username} logged out through page {request.META.get("HTTP_REFERER")}'
    LogUserActivity.objects.create(description=description)