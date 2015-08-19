from django.shortcuts import render


from teeswap.forms import qidForm
from .forms import teeForm, teeForm2
from .models import Tee


def teelist(request):
    if request.method == 'POST':
        form = qidForm(request.POST)
        qid = None
        matches = None
        exists = False
        if form.is_valid():
            qid = form.cleaned_data['qid']
            try:
                tee = Tee.objects.get(qid=qid)
                exists = True
            except Tee.DoesNotExist:
                exists = False
            if exists:
                matches = Tee.objects.filter(havesize=tee.wantsize, wantsize=tee.havesize)
                form = teeForm2(initial={'qid': qid})
    else:
        raise PermissionError
    if not exists:
        form = teeForm(initial={'qid': qid})

    context = {'qid': qid, 'exists': exists, 'form': form, 'matches': matches}
    return render(request, 'tee/teelist.html', context)

def teelist2(request):
    if request.method == 'POST':
        form = teeForm(request.POST)
        qid = None
        matches = None
        if form.is_valid():
            qid = form.cleaned_data['qid']
            havesize = form.cleaned_data['havesize']
            wantsize = form.cleaned_data['wantsize']
            havecolor = form.cleaned_data['havecolor']
            tee = Tee.objects.create(qid=qid, havesize=havesize, wantsize=wantsize, havecolor=havecolor)
            matches = Tee.objects.filter(havesize=wantsize, wantsize=havesize)
            form = teeForm2(initial={'qid': qid})
    else:
        raise PermissionError

    exists = True

    context = {'qid': qid, 'exists': exists, 'form': form, 'matches': matches}
    return render(request, 'tee/teelist.html', context)

def teelistTraded(request):
    if request.method == 'POST':
        form = teeForm2(request.POST)
        if form.is_valid():
            traded = form.cleaned_data['traded']
            qid = form.cleaned_data['qid']
            tee = Tee.objects.get(qid=qid)
            tee.traded = traded
            tee.save()
            return render(request, 'tee/ok.html', None)
    raise PermissionError
