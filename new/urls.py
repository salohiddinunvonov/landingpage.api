from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path("slider/", SliderView.as_view()),
    path("info/<int:pk>/", InfoView.as_view()),
    path("practicesareas/", PracticesAreasView.as_view()),
    path("ourexpertise/<int:pk>/", OurExpertiseView.as_view()),
    path("blog/", BlogView.as_view()),
    path("flatication/", FlaticationGET),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)