"""
OAuth Client by Authlib
"""

from authlib.integrations.django_client import OAuth

oauth = OAuth()
oauth.register(
    name='qtcloud_idam',
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={'scope': 'openid email profile'}
)
