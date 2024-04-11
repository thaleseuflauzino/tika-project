from django.urls import path
from tika_app.views import extract_text


urlpatterns = [
    path('extract_text/', extract_text, name='extract_text'),
]
