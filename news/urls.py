from django.contrib import admin
#from django.contrib.sitemaps.views import index
from django.urls import path
from .views import PostsList, PostDetail, PostSearch, SearchDetail, PostDelete, PostCreate, PostUpdate, \
    CategoryListView, subscribe, index
#from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', PostsList.as_view(), name='posts'),
    #path('<int:pk>', cache_page(300)(PostDetail.as_view())),
    path('<int:pk>', PostDetail.as_view()),
    path('search/', PostSearch.as_view()),
    path('post/<int:pk>', SearchDetail.as_view()),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('<int:pk>/update/', PostUpdate.as_view(), name='post_edit'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('categories/<int:pk>', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/subscribe', subscribe, name='subscribe'),
    path('categories/<int:pk>/subscribe/post_created_email/', CategoryListView.as_view(), name='post_created_email'),
    #path('index/', cache_page(60)(index), name='index'),
    path('index/', index, name='index'),
]
