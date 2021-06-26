from django.shortcuts import render
from theatre.forms import *


def theatre(request):
    form = MaecenasForm()
    if request.method == 'POST':
        form = MaecenasForm(request.POST)
        if form.is_valid():
            print('saved')
            form.save()

    data = {
        'form': form,
    }
    return render(request, 'index.html', data)
