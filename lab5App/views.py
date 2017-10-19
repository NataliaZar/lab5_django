from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

def home(request):
    par = {
        'header': 'Home'
    }
    return render(request, 'home.html', context=par)


class ProdactsView(View):

    def get(self, request):

        data = {
            'prodacts':[
                {
                    'title': 'Морковь',
                    'id': 1
                },
                {
                    'title': 'Огурцы',
                    'id': 2
                }
            ]
        }
        return render(request, 'prodacts.html', data)


class ProdactView(View):

    def get(self, request, id):

        data = {
            'prodact':
                {
                    'id': id
                }
        }
        return render(request, 'prodact.html', data)