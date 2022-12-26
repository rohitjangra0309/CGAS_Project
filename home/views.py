from django.shortcuts import render, HttpResponse
from recipe_scrapers import scrape_me
from home import temp


def input(request):
    return render(request, 'home.html')

def scraper(request):
    data = request.GET['title']
    scraper = scrape_me(data)
    nameR = scraper.title()
    ing = scraper.ingredients()
    finalING = []
    for i in ing:
        finalING.append(i)
        
    finalNUT = []
    for i in finalING:
        templ = temp.extract(i)
        finalNUT.append(templ)

    return render(request, 'scraped.html', {'data': nameR, 'data1':finalING , 'data2':finalNUT})
    
