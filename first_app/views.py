from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import ALbum


class IndexView(generic.ListView):
    template_name = 'first_temp.html'

    def get_queryset(self):
        return ALbum.objects.all()


class DetailView(generic.DetailView):
    model = ALbum
    template_name = 'detail.html'


class CreateAlbum(CreateView):
    model = ALbum
    template_name = 'album_form.html'
    fields = ['artist', 'albumTitle', 'genre', 'albumImage']


class UpdateAlbum(UpdateView):
    model = ALbum
    template_name = 'album_form.html'
    fields = ['artist', 'albumTitle', 'genre', 'albumImage']


class DeleteAlbum(DeleteView):
    model = ALbum
    success_url = reverse_lazy('first_app:index')


# from django.shortcuts import render, get_object_or_404
# from .models import ALbum, Song

# # Create your views here.

# def index(req):
#     all_album = ALbum.objects.all()
#     return render(req, 'first_temp.html', {'all_album': all_album})

# def detail(req, album_id):
#     # album = ALbum.objects.get(pk=album_id)
#     album = get_object_or_404(ALbum, pk=album_id)
#     return render(req, 'detail.html', {'album': album})

# def favourite(req, album_id):
#     album = get_object_or_404(ALbum, pk=album_id)
#     try:
#         selected_song = album.song_set.get(pk=req.POST['song'])
#     except (KeyError, Song.DoesNotExist):
#         return render(req, 'detail.html', {
#             'album': album,
#             'error_message': 'You do not have the song!',
#         })
#     else:
#         selected_song.favourite = True
#         selected_song.save()
#         return render(req, 'detail.html', {'album': album})
