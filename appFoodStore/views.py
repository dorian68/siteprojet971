from django.shortcuts import render
from django.http import HttpResponse
from .models import Article,Order

# Create your views here.

def index(request):
    return HttpResponse("Hello Dorian, prepare yourself to be meaningful")

def homeView(request):
    return render(request,"appFoodStore/base.html")

def cardView(request):
    context = {
        "data" : Article.objects.order_by("name")
    }
    return render(request,"appFoodStore/card.html",context)

def orderListView(request):
    context = {
        "orderList" : Order.objects.order_by("Order_id")
    }
    return render(request,"appFoodStore/order_list.html",context)
  
def addToChart(request):
    article = Article.objects.get(pk=request.GET.get('id',None))
    context = {
        "article" : article
    }
    if not article is None:
        print(article.image) 
    return render(request,"appFoodStore/addToChart.html",context)

def barChartView(request):
  production_data_2014 = [
    { "y": 105.48, "label": "Rice"},
    { "y": 86.53, "label": "Wheat"},
    { "y": 42.86, "label": "Coarse Cereals"},
    { "y": 17.15, "label": "Total Pulses"}
  ]
  production_data_2015 = [
    { "y": 104.41, "label": "Rice"},
    { "y": 92.29, "label": "Wheat"},
    { "y": 38.52, "label": "Coarse Cereals"},
    { "y": 16.35, "label": "Total Pulses"}
  ]
  production_data_2016 = [
    { "y": 108.86, "label": "Rice"},
    { "y": 96.64, "label": "Wheat"},
    { "y": 44.34, "label": "Coarse Cereals"},
    { "y": 22.14, "label": "Total Pulses"}
  ]
  return render(request, 'barChart.html', { "production_data_2014" : production_data_2014, "production_data_2015": production_data_2015, "production_data_2016": production_data_2016 })  

def AddItemToChart(article_id):
    Article.objects.raw("INSERT INTO appFoodStore_cart (cart_id,article_id,addedTime,quantity) VALUES ()")
    completion_state = 1
    return completion_state