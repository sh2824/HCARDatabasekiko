from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .filters import ArtistFilter
from .models import *
from .forms import ArtistSearchForm, StorageSearchForm


def home(request):
    # corresponds with home.html <form method="POST" action="{% url 'home' %}">
    # if the action is POST
    if request.method == 'POST':
        # keys correspond to the name attribute in the form
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in.")
            return redirect('home')
        else:
            messages.success(request, "There was an error logging in.")
            return redirect('home')
    # else the action is GET, so we just serve the home page
    else:
        # myFilter = ArtistFilter()
        # artist_fname = Artist.artist_fname
        # artist_lname = Artist.artist_lname
        # context = {'artist_fname':artist_fname, 'artist_lname':artist_lname, 'myFilter':myFilter}
        # print(request.GET)
        # Django ORM database query
        # https://docs.djangoproject.com/en/5.1/topics/db/queries/
        # Entry.objects.filter(pub_date__year=2006)
        # Artist.objects.all()
        # if we have a search param,
        return render(request, 'home.html', {'foo':'bar'})


# note: function is called login_user so that it doesn't conflict with imported functions
def login_user(request):
    pass


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')


def artists(request):
    artists = Artist.objects.all()
    return render(request, 'artists.html', {'artists': artists})
    return redirect('artists')

# ADDED THIS ONE
def art(request):
    art = Artwork.objects.all()
    return render(request, 'artworks.html', {'art': art})
    return redirect('art')


# ADDED THIS ONE 
def artist_profile(request, pk):
    if request.user.is_authenticated:
        # look up artist
        artist_profile = Artist.objects.get(artist_id=pk)
        return render(request, 'artist.html', {'artist_profile': artist_profile})
    else:
        messages.success(request, "You Must Be Logged In To View That Page")
        return redirect('home')

# ADDED THIS ONE 
def artwork_profile(request, pk):
    if request.user.is_authenticated:
        # look up artwork
        artwork_profile = Artwork.objects.get(art_num=pk)
        return render(request, 'artwork.html', {'artwork_profile': artwork_profile})
    else:
        messages.success(request, "You Must Be Logged In To View That Page")
        return redirect('home')

def artist_search(request):
    form = ArtistSearchForm(request.GET)
    artists = []

    if form.is_valid():
        artist_fname = form.cleaned_data.get("artist_fname")
        artist_lname = form.cleaned_data.get("artist_lname")

        query = {}
        if artist_fname:
            query["artist_fname__icontains"] = artist_fname
        if artist_lname:
            query["artist_lname__icontains"] = artist_lname

        if query:
            artists = Artist.objects.filter(**query)

    return render(request, "artist_search.html", {"form": form, "artists": artists})

def storage_search(request):
    form = StorageSearchForm(request.GET)
    storages = []

    if form.is_valid():
        storage_loc = form.cleaned_data.get("storage_loc")
        storage_city = form.cleaned_data.get("storage_city")
        storage_room = form.cleaned_data.get("storage_room")

        query = {}
        if storage_loc:
            query["storage_loc__icontains"] = storage_loc
        if storage_city:
            query["storage_city__icontains"] = storage_city
        if storage_room:
            query["storage_room__icontains"] = storage_room

        if query:
            storages = Storage.objects.filter(**query)

    return render(request, "storage_search.html", {"form": form, "storages": storages})

def storage(request, pk):
    if request.user.is_authenticated:
        # look up storage
        storage_profile = Storage.objects.get(storage_id=pk)
        return render(request, 'storage.html', {'storage_profile': storage_profile})
    else:
        messages.success(request, "You Must Be Logged In To View That Page")
        return redirect('home')