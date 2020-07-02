from django.conf.urls import url
from . import views

urlpatterns=[
    url(r"^detail/(?P<id>\d+)/$",views.post_detail),
    ##?P for parameter
]