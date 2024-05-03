from django.urls import path
from . import views

urlpatterns = [
    #path("", views.index, name="index"),
    #path("", views.homeView,name="home"),
    path("",views.cardView,name="card"),
    path("order",views.orderListView,name="orderList"),
    path("barChart",views.barChartView,name="barChart"),
    path("addToChart/",views.addToChart,name="addToChart")
]