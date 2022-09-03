from django.http import HttpResponse


def index(request):
    return HttpResponse('Hi, luck!')


def group(request):
    return HttpResponse('Star Wars')


# В урл мы ждем парметр, и нужно его прередать в функцию для использования
def group_pack(request, slug: 'dv'):
    return HttpResponse('dart veider')