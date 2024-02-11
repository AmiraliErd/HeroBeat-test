from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from Tracks.models import Track, Album, Category, Artist, Comment
from django.core.paginator import Paginator

# Create your views here.


def tracks_list(request):
    tracks = Track.objects.all()
    page_number = request.GET.get('page')
    paginator = Paginator(tracks, 6)
    page_list = paginator.get_page(page_number)
    return render(request, 'Tracks/music.html', context={'tracks_list': page_list})


def albums_list(request):
    albums = Album.objects.all()
    page_number = request.GET.get('page')
    paginator = Paginator(albums, 32)
    page_list = paginator.get_page(page_number)
    return render(request, 'Tracks/ Album.html', context={'albums_list': page_list})


def track_details(request, slug):
    track = get_object_or_404(Track, slug=slug)

    if request.method == 'POST':
        user = request.POST.get('user')
        parent_id = request.POST.get('parent_id')
        body = request.POST.get('body')
        email = request.POST.get('email')
        Comment.objects.create(body=body, user=user, email=email, track=track, parent_id=parent_id)

    return render(request, 'Tracks/music_details.html', context={'track': track})


def category_details(request, slug):
    category = get_object_or_404(Category, slug=slug)
    tracks = category.tracks.all()
    page_number = request.GET.get('page')
    paginator = Paginator(tracks, 42)
    page_list = paginator.get_page(page_number)
    return render(request, 'Tracks/category_detail.html', context={'tracks': page_list, 'category': category})


def artist_details(request, slug):
    artist = get_object_or_404(Artist, slug=slug)
    albums = artist.albums.all()
    single_tracks = artist.tracks.filter(single=True)
    return render(request, 'Tracks/artist_details.html', context={'artist': artist, 'albums': albums, 'single_tracks': single_tracks})


def album_details(request, slug):
    album = get_object_or_404(Album, slug=slug)
    tracks = album.tracks.all()

    if request.method == 'POST':
        user = request.POST.get('user')
        parent_id = request.POST.get('parent_id')
        body = request.POST.get('body')
        email = request.POST.get('email')
        Comment.objects.create(body=body, user=user, email=email, album=album, parent_id=parent_id)

    return render(request, 'Tracks/Album_detail.html', context={'album': album, 'tracks_list': tracks})


def search(request):
    q = request.GET.get('q')
    lookups = Q(farsi_name__icontains=q) | Q(name__icontains=q)
    tracks = Track.objects.filter(lookups)
    albums = Album.objects.filter(lookups)
    return render(request, 'Tracks/search_result.html', {'tracks_list': tracks, 'albums_list': albums})






