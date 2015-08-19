from django.conf.urls import include, url


from . import views


urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^$', views.teelist, name='teelist'),
    url(r'^2', views.teelist2, name='teelist2'),
    url(r'^traded', views.teelistTraded, name='teelistTraded'),
]

