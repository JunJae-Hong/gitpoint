from django.shortcuts import render
from app.models import Contacts
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    return render(request, 'index.html')

def index(request):
    contacts = Contacts.objects.all()
    paginator = Paginator(contacts,5) #몇페이지까지 보여줄건지 넘어가는 기능 
    page = request.GET.get('page')

    try: #try:젤 먼저 시도하는게 맞으면 실행 
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'index.html',{'contacts':contacts})