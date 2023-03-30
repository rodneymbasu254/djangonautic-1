from django.contrib import admin
from django.urls import path,include
from.import views
from django.conf import settings
from django.conf.urls.static import static
from articles import views as article_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('articles/',include('articles.urls')),
    path('about/',views.about),
    path('',article_views.articles_list, name='home'),
]
if settings.DEBUG:
 urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])

if settings.DEBUG:
 urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
