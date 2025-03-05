from django.urls import path
from .views import NewsListView, NewsCreateView, NewsUpdateView, NewsDeleteView, NewsDetailView

app_name = 'news'

urlpatterns = [
    path("", NewsListView.as_view(), name="news_list"),
    path("create/", NewsCreateView.as_view(), name="news_create"),
    path("<int:pk>/edit/", NewsUpdateView.as_view(), name="news_edit"),
    path("<int:pk>/delete/", NewsDeleteView.as_view(), name="news_delete"),
    path("<int:pk>/", NewsDetailView.as_view(), name="news_detail"),
]
