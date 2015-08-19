from django.shortcuts import render


from .forms import qidForm


def index(request):
    form = qidForm()
    context = {'form': form}
    return render(request, 'index.html', context)

