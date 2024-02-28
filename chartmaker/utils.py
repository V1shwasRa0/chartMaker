import matplotlib.pyplot as plt
import base64
from io import BytesIO
from .models import *
from django.core.files.uploadedfile import InMemoryUploadedFile
# import pandas as pd
import io
from PIL import Image

def decodeDesignImage(data):
    # try:
    data1 = base64.b64encode(data)
    data1 = data1.decode('UTF-8')
    buf = io.BytesIO(data)
    img = Image.open(buf)
    return img
    # except:
    #     return None



def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()

    img = decodeDesignImage(image_png)
    img_io = io.BytesIO()
    img.save(img_io, format='PNG')
    token="img1"
    e = ImageModel(image_field = InMemoryUploadedFile(img_io, field_name=None, name=token+".png", content_type='image/png', size=img_io.tell, charset=None))
    e.save()

    graph = base64.b64encode(image_png)

    graph = graph.decode('utf-8')    
    buffer.close()
    return graph

def get_plot(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(8,5))
    plt.title("Fruits price")
    plt.plot(x,y)
    plt.xticks(rotation=45)
    plt.xlabel('fruits')
    plt.ylabel('price')
    plt.tight_layout()
    graph = get_graph()
    # plt.savefig('C:/sem4project/chartmaker/static/img1.png')
    return graph

def bar_plot(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(8,5))
    plt.title("Fruits price")
    plt.bar(x,y,width=0.4)
    plt.xticks(rotation=45)
    plt.xlabel('fruits')
    plt.ylabel('price')
    plt.tight_layout()
    graph = get_graph()
    return graph

def pie_plot(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(8,5))
    plt.title("Fruits price")
    plt.pie(y, labels=x)
    plt.xticks(rotation=45)
    # plt.xlabel('fruits')
    # plt.ylabel('price')
    plt.tight_layout()
    graph = get_graph()
    return graph
