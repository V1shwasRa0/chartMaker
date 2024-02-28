from .views import *
from django.urls import path
urlpatterns=[
    path("",home,name="home"),
    path("insertview",insertview,name="insertview"),
    path("plot_view",plot_view,name="plot_view"),
    # path("export_view",export_view,name="export_view"),
    # path("dis_view",dis_view,name="dis_view"),
    path("download_view",download_view,name="download_view"),
    # path("hist_plot_view",hist_plot_view,name="hist_plot_view"),
    path("bar_plot_view",bar_plot_view,name="bar_plot_view"),
    path("pie_plot_view",pie_plot_view,name="pie_plot_view"),
    path("bar",bar,name="bar"),
    path("pie",pie,name="pie"),
    path("home",home,name="home"),
]