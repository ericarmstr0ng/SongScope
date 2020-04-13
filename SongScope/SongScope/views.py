from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse

from bpandora.utils import playlist_tracker, track_data, album_data, load_data
from .forms import RawProductForm, SongSelectionForm
from rest_framework.views import APIView
from rest_framework.response import Response


def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})


def chart_view(request, *args, **kwargs):
    return render(request, "chart.html", {})


def playlist_view(request, *args, **kwargs):
    inputSearch = RawProductForm
    selectedTrack = SongSelectionForm
    context = {
        "input_form": inputSearch,
        "selection_form": selectedTrack
    }
    if request.method == "POST":
        inputSearch = RawProductForm(request.POST)
        searchResults = SongSelectionForm(request.POST)

        if inputSearch.is_valid():
            artist = inputSearch.cleaned_data['userInput']
            queryset = playlist_tracker(artist)
            payload = load_data(queryset, artist)

            context = {
                "input_form": inputSearch,
                "object_list": queryset,
                "paycontent": payload
            }
        if searchResults.is_valid():
            userInput = inputSearch.cleaned_data['userInput']
            track_id = searchResults.cleaned_data['songSelection']
            album_id = searchResults.cleaned_data['albumSelection']
            queryset = playlist_tracker(userInput)
            payload = load_data(queryset, userInput)

            if track_id:
                # track information
                dataset = track_data(track_id)

                # album information
                albumset = album_data(album_id)

                context = {
                    "input_form": inputSearch,
                    "object_list": queryset,
                    "paycontent": payload,
                    "datacontent": dataset,
                    "albumcontent": albumset,
                    "songName": searchResults.cleaned_data['track'],
                    "artist": searchResults.cleaned_data['artist']
                }
            else:
                context = {
                    "input_form": inputSearch,
                    "object_list": queryset,
                    "paycontent": payload
                }
    return render(request, "chart.html", context)


def get_data(request, *args, **kwargs):
    labels = ["Acousticness", "Danceability", "Energy", "Instrumentalness", "Liveness", "Speechiness"]
    default_items = [1, 23, 2, 3, 12, 2]
    data = {
        "labels": labels,
        "default": default_items,
    }

    return JsonResponse(data)


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        labels = ["Acousticness", "Danceability", "Energy", "Instrumentalness", "Liveness", "Speechiness"]
        default_items = [1, 23, 2, 3, 12, 2]
        data = {
            "labels": labels,
            "default": default_items,
        }
        return Response(data)
