from django.shortcuts import render,HttpResponse
from .models import *
from .utils import *
from django.shortcuts import get_object_or_404
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.utils.text import slugify

from django.core.files.uploadedfile import InMemoryUploadedFile

# Create your views here.
def home(request):
    qs = objects2.objects.all()
    return render(request,"home.html")

def bar(request):
    return render(request,"bar.html")

def pie(request):
    return render(request,"pie.html")

def bar(request):
    return render(request,"bar.html")

def pie(request):
    return render(request,"pie.html")

def insertview(request):
    a=int(request.GET["n2"])
    b=request.GET["n1"]
    e=objects2(obj1=b,obj2=a)
    e.save()
    return render(request,"home.html",{"msg":"Record Inserted"})

def plot_view(request):
    qs = objects2.objects.all()
    x = [i.obj1 for i in qs]
    y = [j.obj2 for j in qs]
    chart = get_plot(x,y)
    return render(request,"home.html",{"chart":chart,"x":x,"y":y})

def bar_plot_view(request):
    qs = objects2.objects.all()
    x = [i.obj1 for i in qs]
    y = [j.obj2 for j in qs]
    chart = bar_plot(x,y)
    return render(request,"bar.html",{"chart":chart,"x":x,"y":y})

def pie_plot_view(request):
    qs = objects2.objects.all()
    x = [i.obj1 for i in qs]
    y = [j.obj2 for j in qs]
    chart = pie_plot(x,y)
    return render(request,"pie.html",{"chart":chart,"x":x,"y":y})


# def hist_plot_view(request):
#     qs = objects2.objects.all()
#     data = [i for i in qs]
#     return render(request,"home.html",{"data":"data"})

# def export_view(request):
#     # save_plot()
#     graph=request.FILES['image']
#     e=ImageModel(image_field=graph)
#     e.save()

#     products = ImageModel.objects.all()
#     content={'products':products}
#     return render(request,'home.html',content)
    # image_model = get_object_or_404(ImageModel)
    # image_content = default_storage.open(image_model.image_field.name).read()
    # response = HttpResponse(image_content, content_type='image/png')
    # response['Content-Disposition'] = f'attachment; filename={slugify(Image_model.image_field.name)}.png'

    # return response

# def dis_view(request):    
#     products = ImageModel.objects.all()
#     content={'products':products}
#     return render(request,'home.html',content)

def download_view(request):

    e=ImageModel.delete_all_except_latest()
    
    image_model = get_object_or_404(ImageModel)
    image_content = default_storage.open(image_model.image_field.name).read()
    response = HttpResponse(image_content, content_type='image/png')
    response['Content-Disposition'] = f'attachment; filename={slugify(image_model.image_field.name)}.png'

    return response


# def direct_view(request):
#     img = decodeDesignImage(data)
#     img_io = io.BytesIO()
#     img.save(img_io, format='JPEG')
#     design.image = InMemoryUploadedFile(img_io, field_name=None, name=token+".jpg", content_type='image/jpeg', size=img_io.tell, charset=None)
#     design.save()