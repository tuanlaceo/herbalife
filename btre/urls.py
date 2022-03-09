
from xml.dom.minidom import Document
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
# nhap lib cho lenh sau :+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.conf import settings 
from django.conf.urls.static import static
##
urlpatterns = [
    path('', include('pages.urls')),  # doi huong  den  tat ca page urls
    path('listings/', include('listings.urls')),
    path('admin/', admin.site.urls), #duong dan danh cho admin
    path('account/', include('account.urls')),
    path('contacts/', include('contacts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
