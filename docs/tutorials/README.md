# django-qtauth 

修改settings设置：
```
# 添加Django应用
INSTALLED_APPS = [
    ..., 
    'django_qtauth'
]

# 修改Auth用户模型
AUTH_USER_MODEL = 'django_qtauth.models.AuthUser'

# 修改REST Framework的默认Auth和Permission类
REST_FRAMEWORK = {
    ...,
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'django_qtauth.authentication.QtAuthentication'
    ],
    ...,
    'DEFAULT_PERMISSION_CLASSES': [
        'django_qtauth.permissions.IsStaff',
    ],
}
```