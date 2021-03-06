from django.urls import path, include
from django.views.decorators.cache import cache_page

from .views import *

urlpatterns = [
    # path('', cache_page(60)(PostHome.as_view()), name='home'),
    path('', PostHome.as_view(), name='home'),
    # path('', index, name='home'),
    # path('category/<slug:cat_slug>/', show_category, name='category'),
    path('about/', about, name='about'),
    path('addpost/', AddPost.as_view(), name='addpost'),
    path('contacts/', contacts, name='contacts'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),

    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),

    path('category/<slug:cat_slug>/', PostCategory.as_view(), name='category'),
]
