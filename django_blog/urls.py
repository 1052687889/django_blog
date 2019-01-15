"""django_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

import xadmin
from django.urls import path,re_path,include
from .views import Home,page_not_found
from django.views.static import serve
from .settings import MEDIA_ROOT
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('ueditor/',include('DjangoUeditor.urls' )),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    re_path(r'media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    re_path(r'^captcha/', include('captcha.urls')),

    path('',Home.as_view(),name='home'),
    path('blog/', include('Article.urls')),
    path('about/',include('aboutme.urls')),
    path('users/',include('users.urls')),

]
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = 'page_not_found'