
from io import BytesIO
from PIL import Image, ImageDraw
from django.conf.urls import url
from django import forms
from django.urls import path, re_path  # url使用模块
from django.http import HttpResponse, HttpResponseBadRequest  # 视图使用模块
import sys
from django.conf import settings  # 配置使用模块
from django.core.wsgi import get_wsgi_application  # wsgi使用模块
import os
from django.core.cache import cache  # 缓存
import hashlib
from django.views.decorators.http import etag  # 视图Etag
from django.urls import reverse
from django.shortcuts import render

DEBUG = os.environ.get('DEBUG', 'on') == 'on'  # environ 环境变量，获取环境变量
# SECRET_KEY=os.environ.get('SECRET_KEY',os.urandom(32)) # os.urandom返回一个有32个byte那么长的一个string，适合用于加密。
SECRET_KEY = os.environ.get(
    'SECRET_KEY', '_$+r%l2+h=l89-&8x09te(jbv2(gspx))rhegr(4$cg1f9wy2y')
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')
BASE_DIR = os.path.dirname(__file__)


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
    INSTALLED_APPS=(
        'django.contrib.staticfiles',
    ),
    # 模板文件路径
    TEMPLATES=(
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': (os.path.join(BASE_DIR, 'templates'),),
        },
    ),
    # 静态文件路径
    STATICFILES_DIRS=(
        os.path.join(BASE_DIR, 'static'),
    ),
    STATIC_URL='/static/'
)


# NOTE:图片处理

class ImageForm(forms.Form):
    """ Form to validate requested placeholder image. """
    height = forms.IntegerField(min_value=1, max_value=2000)
    width = forms.IntegerField(min_value=1, max_value=2000)

    def generate(self, image_format='PNG'):
        """ Generate an image of the given type and return as raw bytes """
        height = self.cleaned_data['height']
        width = self.cleaned_data['width']
        # 加入缓存
        # 通过宽度，高度，图片格式生成一个缓存键值
        key = '{}.{}.{}'.format(width, height, image_format)
        content = cache.get(key)  # 存储缓存键值
        if content is None:
            image = Image.new('RGB', (width, height))
            draw = ImageDraw.Draw(image)
            text = '{} X {}'.format(width, height)
            textwidth, textheight = draw.textsize(text)
            # TEST
            print('*******************************')
            print('height=', height)
            print('width=', width)
            print('image_format=', image_format)
            print('text=', text)
            print('textheight=', textheight)
            print('textwidth=', textwidth)
            print('*******************************')
            if textwidth < width and textheight < height:
                texttop = (height-textheight)//2
                # TEST
                print('texttop=', texttop)
                textleft = (width-textwidth)//2
                print('textleft=', textleft)
                print('*******************************')
                draw.text((textleft, texttop), text, fill=(255, 255, 255))
            content = BytesIO()
            image.save(content, image_format)
            content.seek(0)
            cache.set(key, content, 60*60)   # 通过键值将图片保存1小时
        return content


def generate_etag(request, width, height):
    """ 接收placeholder参数，使用hashlib返回一个基于width和height值变化的不透明的ETag值 """
    content = 'Placeholder:{0} X {1}'.format(width, height)
    return hashlib.sha1(content.encode('utf-8')).hexdigest()


@etag(generate_etag)
def placeholder(request, width, height):
    # FIXME:Rest of the view will go here
    form = ImageForm({'height': height, 'width': width})
    if form.is_valid():
        image = form.generate()
        # TODO:Generate image of requested size
        return HttpResponse(image, content_type='image/png')
    else:
        return HttpResponseBadRequest('Invalid Image Request')


# NOTE 视图
def index(request):
    example = reverse('placeholder', kwargs={'width': 50, 'height': 50})
    context = {
        'example': request.build_absolute_uri(example)
    }
    return render(request, 'home.html', context)


urlpatterns = [
    path('', index,name='homepage'),
    re_path('image/(?P<width>[0-9]+)x(?P<height>[0-9]+)/',
            placeholder, name='placeholder'),
]
# django 2.0后版本path不支持正则表达式，需要通过re_path来获取正则表达式的值
application = get_wsgi_application()


if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    print(DEBUG)
    execute_from_command_line(sys.argv)
