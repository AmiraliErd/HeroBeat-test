from Tracks.models import Category, Artist


def categories_list(request):
    categories = Category.objects.all()[:6]

    return {"categories": categories}


def artists_list(request):
    artists = Artist.objects.all()[:6]

    return {"artists": artists}
