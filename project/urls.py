
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('accounts/', include('account.urls',namespace='accounts')),
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('jobs/',include('job.urls',namespace='jobs')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)