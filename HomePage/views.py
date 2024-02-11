from django.shortcuts import render, get_object_or_404
from Tracks.models import Track, Album, Artist


# Create your views here.


def recent(request):
    recent_tracks = Track.objects.all()[:12]
    artists_list = Artist.objects.all()[:10]
    recent_albums = Album.objects.all()[:6]
    return render(request, 'HomePage/index.html', context={'recent_tracks': recent_tracks, 'artists_list': artists_list,
                                                           'recent_albums': recent_albums})
