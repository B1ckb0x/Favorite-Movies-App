from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        'movies_list': ['Hacksaw Ridge', 'Alpha Go', 
                        'Journey to the center of the earth', 'John wick',
                        'I.T', '500 days of summer', 'kevin from work',
                        'The office', 'Peaky blinders', 'billions'
                        ]
    }
    return render(request, 'movies/index.html', context)

def about(request):
    return render(request, 'movies/about.html')