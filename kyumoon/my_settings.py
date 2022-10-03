# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bss',
        'USER': 'root',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
SECRET_KEY = 'django-insecure-$=ohcymv_lz3dshxrhr*xkb)+y7%ou!4=(o8o_%=xoq+vxlme('