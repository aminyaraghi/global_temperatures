from django.conf.urls import url
from django.urls.resolvers import URLPattern
from core import views


urlpatterns = [
    url(
        r'^api/(?P<city>[\w-]+)/(?P<date>[\w-]+)/$',
        views.get_patch_global_land_temperatures_by_city,
        name='get_patch_global_land_temperatures_by_city'
    ),
    url(
        r'^api/$',
        views.get_post_global_land_temperatures_by_city,
        name='get_post_global_land_temperatures_by_city'
    ),

]
