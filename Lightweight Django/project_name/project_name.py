
from django.urls import path  # url使用模块
from django.http import HttpResponse  # 视图使用模块
import sys
from django.conf import settings  # 配置使用模块
from django.core.wsgi import get_wsgi_application  # wsgi使用模块
import os

DEBUG = os.environ.get('DEBUG', 'on') == 'on'  # environ 环境变量，获取环境变量
# SECRET_KEY=os.environ.get('SECRET_KEY',os.urandom(32)) # os.urandom返回一个有32个byte那么长的一个string，适合用于加密。
SECRET_KEY = os.environ.get('SECRET_KEY', '{{ secret_key }}')
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')


settings.configure(
    DEBUG=DEBUG,
    SECRET_KEY=SECRET_KEY,
    ALLOWED_HOSTS=ALLOWED_HOSTS,
    ROOT_URLCONF=__name__,
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
)


def index(request):
    return HttpResponse('Hello World')


urlpatterns = [
    path('^$', index),
]
application = get_wsgi_application()


if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    print(DEBUG)
    execute_from_command_line(sys.argv)
