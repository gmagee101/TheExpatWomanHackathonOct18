from django.shortcuts import render
from django.http import HttpResponse

from .forms import JobDescForm
from .engine import *

def index(request):
    if request.method == 'POST':
        form = JobDescForm(request.POST)
        if form.is_valid():
            list = create_list(form.cleaned_data['job_desc'])
            output = analyze_word_list(list)
            return render(
                    request,
                    'zerobias/analyze.html',
                    {
                        'input_text': form.cleaned_data['job_desc'].replace("\n", "<br>"),
                        'output_dict': output
                    }
                )
    else: # this was a 'GET' request or other type
        form = JobDescForm()
    return render(request, 'zerobias/index.html', {'form': form})
