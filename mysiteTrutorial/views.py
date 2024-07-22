# I have Created This File - Indra 
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

#   Returns HttpResponse("home")

# def removepunc(request):
#     # Get the text
#     djtext = request.GET.get('text', 'default')
#     print(djtext)
#     # Analyze the text
#     return HttpResponse("remove punc")

# def about(request):
#     return HttpResponse("about Indra bhai <a href='/'> back</a>")

# def site(request):
#     return HttpResponse('''<h1> </h1><a href="https://www.youtube.com/"> indra</a> <h1> </h1>
#      <a href="https://www.siddharthacapital.com/mutual-fund/siddhartha-systematic-investment-scheme/"> thrau</a> <h1> </h1> <a href="https://docs.djangoproject.com/en/5.0/intro/tutorial01/"> django</a> <h1></h1>
#                         <a href="https://www.youtube.com/watch?v=AepgWsROO4k&t=153s"> video</a> <h1></h1> <a href="https://merolagani.com/CompanyDetail.aspx?symbol=AKJCL" share</a> $<a href='/'> back</a>$ ''')

def analyze(request):
    # Get the text
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    print(removepunc)
    print(djtext)
    if removepunc == "on":
        # analyzed = djtext
        punctuations= '''!()-[]{};:'"\,<>./?@#$%^&*_~`'''
        analyzed=""
        for char in djtext:
                if char not in punctuations:
                    analyzed= analyzed + char
                
        params = {'purpose' : 'remove punctuations', 'analyzed_text': analyzed}
            # Analyze the text
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error...")