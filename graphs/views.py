# views.py
import io
import pandas as pd
import matplotlib.pyplot as plt
from django.http import HttpResponse
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

def graph_view(request):
    # Example dataset
    #data = {'Category': ['A', 'B', 'C', 'D'], 'Values': [10, 20, 15, 25]}
    #df = pd.DataFrame(data)
    df=pd.read_csv('D:\\MyDjango\\myproject\\graphs\\Iris.csv')

    # Create a plot
    fig, ax = plt.subplots()
    ax.bar(df['Species'], df['SepalLengthCm'])
    ax.set_title('Sample Bar Chart')
    ax.set_xlabel('Category')
    ax.set_ylabel('Values')

    # Save the plot to a BytesIO object
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close(fig)

    # Return the image as a response
    return HttpResponse(buf.getvalue(), content_type='image/png')


from django.shortcuts import render

def display_graph_page(request):
    return render(request, 'graph.html')

# Create your views here.
