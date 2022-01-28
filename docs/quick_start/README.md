# 快速入门

## 安装

在命令行使用pip安装包

```shell 
pip install drf-remote-auth -i https://quanttide-pypi.pkg.coding.net/qtapps-django/drf-remote-auth/simple
```

在Django项目的`settings.py`文件配置

```python 
# settings.py 

INSTALLED_APPS = [
    ...
    'rest_framework',
    ...
    'drf_remote_auth',
    ...
]

AUTH_USER_MODEL = 'drf_remote_auth.AuthUser'
```
