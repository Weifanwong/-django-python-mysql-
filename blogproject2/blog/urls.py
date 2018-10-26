from . import views 
from django.conf.urls import url

app_name = 'blog'

urlpatterns =[
#url(r'^$',views.index),
url(r'^$',views.index2),
url(r'^post/(?P<pk>[0-9]+)/$',views.detail,name='detail'),
url(r'^category/(?P<category_name>\w+)/$',views.get,name='get')
#url(r'^detail/(?P<category>[0-9]+)/$',views.show_by_cate)
#url(r'2',views.detail),
]
