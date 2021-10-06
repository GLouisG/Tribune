from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
import datetime as dt
from django.shortcuts import render
from .models import Article
from django.db.models.base import ObjectDoesNotExist

# Create your views here.
def welcome(request):
  return render(request, 'welcome.html')

def news_of_day(request):
    date = dt.date.today()
    news =  Article.todays_news()
    return render(request, 'all-news/today-news.html', {"date": date, "news": news},)   
    #accessible using /news/today

def past_days_news(request,past_date):

    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown raised if date can't be assigned
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(news_of_day)

    news = Article.days_news(date)
    return render(request, 'all-news/past-news.html', {"date": date, "news":news})

def search_results(request):

    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Article.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-news/search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-news/search.html',{"message":message})

def article(request,article_id):
    try:
        article = Article.objects.get(id = article_id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request,"all-news/article.html", {"article":article})
# We import the HttpResponse class from the django.http module. This will be responsible for returning a response to a user. We then define the function welcome which will be our view function. This function takes one argument request. This argument contains the information of the current web request that has triggered this view and is an instance of the django.http.HttpRequest class. This argument must be the first parameter for our view functions.  We then return an instance of the HttpResponse class, and pass in a string response.  
#We import the render function from the django.shortcuts module. We then call the render function and pass in the request as the first object and then pass in the template file.

#{"date": date,} we call the render function w/ 3 argumentsThe request, the template file, and a dictionary of values referred to as the Context in Django







# def convert_dates(dates):

#     # Function that gets the weekday number for the date.
#     day_number = dt.date.weekday(dates)

#     days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

#     # Returning the actual day of the week
#     day = days[day_number]
#     return day  