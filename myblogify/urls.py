from django.urls import path
#from . import views
from .views import HomeView, ArticalDetailView, AddPostView, UpdatePostView, DeletPostView, AddCategoryView, LikeView, CategoryView, CategoryListView, AddCommentView

urlpatterns = [
    #path('',views.home,name = "home"),
    path('', HomeView.as_view(), name = "home"),
    path('article/<int:pk>',ArticalDetailView.as_view(), name = "artical-details"),
    path('add_post/', AddPostView.as_view(), name = 'add_post'),
    path('add_category/', AddCategoryView.as_view(), name = 'add_category'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name = 'update_post'),
    path('article/<int:pk>/delet', DeletPostView.as_view(), name = 'delet_post'),
    path('like/<int:pk>', LikeView, name = 'like_post'),
    path('category/<str:cats>/', CategoryView, name = 'category'),
    path('category-list/', CategoryListView, name = 'category-list'),
    path('article/<int:pk>/comment', AddCommentView.as_view(), name = 'add_comment'),
]