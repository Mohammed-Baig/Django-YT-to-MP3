from django.shortcuts import render, redirect
from django.http import HttpResponse
from pytubefix import YouTube
from pytubefix.cli import on_progress
import os

def index(request):
    return render(request, 'downloader/index.html')

def download_mp3(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        yt = YouTube(url, on_progress_callback=on_progress)
        ys = yt.streams.get_audio_only()
        output_path = ys.download(filename=f"{yt.title}.mp3")

        # Provide the file for download
        with open(output_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='audio/mpeg')
            response['Content-Disposition'] = f'attachment; filename="{yt.title}.mp3"'
            return response
    
    return redirect('index')
