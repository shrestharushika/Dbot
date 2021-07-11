from django.shortcuts import render,HttpResponse
import pickle
import pandas as pd 

# Create your views here.
def home(request):
    return render(request,'chat.html')



def get_predictions(Glucose,BloodPressure,bmi,Age):
    model=pickle.load(open('gNB.sav','rb'))  
    
    data=[[Glucose,BloodPressure,bmi,Age]]
    print(bmi,"bmi")
    # print(data," inputs")
    prediction=model.predict(data)
    if prediction == 0:
        return 'No'
    elif prediction == 1:
        return 'Yes' 
    else:
        return 'None'    

def form(request):
    return render(request,'Form.html')

def value(request):
    Glucose=int(request.GET['Glucose'])
    BloodPressure=int(request.GET['BloodPressure'])
    height=int(request.GET['height'])
    weight=int(request.GET['weight'])
    Age=int(request.GET['Age'])
    height=height/100
    bmi=(weight/height**2)
    print(bmi)
    result=get_predictions(Glucose,BloodPressure,bmi,Age)

    return render(request,'result.html',{'result':result})

    