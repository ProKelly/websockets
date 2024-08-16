# notifications/signals.py
from django.contrib.auth.signals import user_logged_in
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

def notify_user_login(sender, user, request, **kwargs):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        f'notifications_{user.username}',
        {
            'type': 'send_notification',
            'message': f'Welcome back, {user.username}!',
        }
    )

user_logged_in.connect(notify_user_login)
