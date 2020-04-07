import sys
import os
from django.conf import settings  # 配置使用模块


DEBUG = True
# SECRET_KEY=os.environ.get('SECRET_KEY',os.urandom(32)) # os.urandom返回一个有32个byte那么长的一个string，适合用于加密。
SECRET_KEY = 'SECRET_KEY', '(t*nq991pz%$eaj!(av)%9vt1q7%pcjsjlj8((+n=ozy=_d!1='
BASE_DIR = os.path.dirname(__file__)
print('BASE_DIR=', BASE_DIR)
settings.configure(
    DEBUG=DEBUG,
    SECRET_KEY=SECRET_KEY,
    ROOT_URLCONF='sitebuilder.urls',
    MIDDLEWARE_CLASSES=(
        # 'django.middleware.common.CommonMiddleware',
        # 'django.middleware.csrf.CsrfViewMiddleware',
        # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
    INSTALLED_APPS=(
        'django.contrib.staticfiles',
        'sitebuilder',
        'compressor',
    ),
    TEMPLATES=(
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True,
        },
    ),

    STATIC_URL='/static/',
    SITE_PAGES_DIRECTORY=os.path.join(BASE_DIR, 'pages'),
    SITE_OUTPUT_DIRECTORY=os.path.join(BASE_DIR, '_build'),
    STATIC_ROOT=os.path.join(BASE_DIR, '_build', 'static'),
    # STATICFILES_STORAGE='django.contrib.staticfiles.storage.CachedStaticFilesStorage', # 缓存设置
    STATICFILES_FINDERS=(               # 压缩静态文件配置
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
        'compressor.finders.CompressorFinder',
    )
)


if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
