from django.urls import path
from . import views

app_name = 'Tracks'
urlpatterns = [
    path('songs/', views.tracks_list, name='songs'),
    path('albums/', views.albums_list, name='albums'),
    path('albums/detail/<slug:slug>', views.album_details, name='album_detail'),
    path('songs/detail/<slug:slug>', views.track_details, name='track_detail'),
    path('category/detail/<slug:slug>', views.category_details, name='category_detail'),
    path('artist/detail/<slug:slug>', views.artist_details, name='artist_detail'),
    path('search/', views.search, name='search'),
]
