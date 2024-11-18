from django.shortcuts import render
import pyttsx3
from django.http import HttpResponse
import os

def converter(request):
    if request.method == "POST":
        # Initialize text-to-speech engine
        text_engine = pyttsx3.init()
        
        # Get the text input from the POST request
        name1 = request.POST.get('name')
        
        # Set the audio file path and name
        audio_filename = 'converted_audio.mp3'
        audio_filepath = os.path.join('media', audio_filename)
        
        # Convert text to speech
        text_engine.save_to_file(name1, audio_filepath)
        text_engine.runAndWait()

        # Open the audio file in binary mode for download
        with open(audio_filepath, 'rb') as audio_file:
            response = HttpResponse(audio_file.read(), content_type='audio/mpeg')
            response['Content-Disposition'] = f'attachment; filename="{audio_filename}"'
            return response

    # If request is not POST, render the default template
    return render(request, 'next.html')
