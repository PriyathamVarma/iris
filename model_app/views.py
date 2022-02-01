from django.shortcuts import render
from joblib import load
from django.http import HttpResponse, HttpResponseRedirect
from model_app.models import Leaf

# forms imports
from . import forms

model = load('../savedModels/RandomForestClassifier.joblib')

# Create your views here.
def predictor(request):
    data = Leaf.objects.order_by('id')

    if request.method == "POST":
        
        #form = forms.FormNamedata(request.POST)

            new = Leaf()
        
            print("Validation Success")


        
            sepal_length = request.POST.get('sepal_length')
            sepal_width  = request.POST.get('sepal_width')
            petal_length = request.POST.get('petal_length')
            petal_width  = request.POST.get('petal_width')
            # Predictions    
            y_predictions = model.predict([[sepal_length,sepal_width,petal_length,petal_width]])  

            new.sepal_length = request.POST.get('sepal_length')
            new.sepal_width = request.POST.get('sepal_width')
            new.petal_length = request.POST.get('petal_length')
            new.petal_width = request.POST.get('petal_width')

            if y_predictions[0] == 0:
                value = "Red"
            elif y_predictions[0] == 1:
                value = "Blue"
            elif y_predictions[0] == 2:
                value = "Green"


            new.predictions = value

            new.save()

            print(type(y_predictions[0]))          

    form = forms.FormName()                      
    my_dict = {'data':data,'form':form}
    return render(request,'index.html',my_dict)    


    