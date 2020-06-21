from django.urls import path
from . import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('medicine/',views.MedicineList.as_view()),
    path('medicine/manufacturer/<manufacturer>',views.MedicineListByManufacturer.as_view()),
    path('medicine/type/<type>',views.MedicineListByType.as_view()),
]


urlpatterns+= staticfiles_urlpatterns()
urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
