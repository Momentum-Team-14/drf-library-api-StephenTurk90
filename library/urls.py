from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from library import views

urlpatterns = [
    path('book/', views.BookList.as_view(), name="book-list"),
    path('book/<int:pk>/', views.BookDetail.as_view(), name="book-detail"),
    path('track/', views.TrackList.as_view(), name="track-list"),
    path('track/<int:pk>/', views.TrackDetail.as_view(), name="track-detail"),
    path('note/', views.NoteList.as_view(), name="note-list"),
    path('note/<int:pk>/', views.NoteDetail.as_view(), name="note-detail"),
    path('', views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)