from django.conf.urls import url
from . import views

urlpatterns = [
    # /recipes/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /recipes/register/
    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    # /recipes/login/
    url(r'^login/$', views.login_user, name='login_user'),

    # /recipes/logout/
    url(r'^logout/$', views.logout_user, name='logout_user'),

    # /recipes/id/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # /recipes/add/
    url(r'^add/$', views.RecipeCreate.as_view(), name='add'),

    # /recipes/comment/
    url(r'^comment/$', views.CommentCreate.as_view(), name='comment'),

    # /recipes/update/id/
    url(r'update/(?P<pk>[0-9]+)/$', views.RecipeUpdate.as_view(), name='update'),

    # /recipes/delete/
    url(r'delete/(?P<pk>[0-9]+)/$', views.RecipeDelete.as_view(), name='delete'),

]
