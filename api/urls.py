from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^bundle/(?P<bundle_id>[0-9]+)/click$', views.bundle_click, name="bundle_click"),
]
