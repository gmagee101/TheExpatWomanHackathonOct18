from django.shortcuts import render
from django.http import HttpResponse

from .forms import JobDescForm

def index(request):
    if request.method == 'POST':
        form = JobDescForm(request.POST)
        if form.is_valid():
            # TODO: process data!
            return render(request, 'zerobias/analyze.html', {'input_text': form.cleaned_data['job_desc'].replace("\n", "<br>")})
    else: # this was a 'GET' request or other type
        form = JobDescForm()
    return render(request, 'zerobias/index.html', {'form': form})
