# import google.generativeai as genai
import os
import requests
import urllib.request
import json
from django.shortcuts import render
# Import the necessary libraries
import google.generativeai as genai
from django.conf import settings

# Set up the API key
# genai.configure(api_key=settings.API_KEY)





# Create your views here.

def index(request):
    if request.method =='POST':
        city = request.POST.get("city")
        print(city)
        # city2 = request.POST['city']
        source = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&appid=049079dc05fc612939db7a3685cdb1a5').read()
        list_of_data =json.loads(source)
        data = {
         "country_code": str(list_of_data['sys']['country']),
         "coordinates":str(list_of_data['coord']['lon']) +',' + str(list_of_data['coord']['lat']),
         "temp":str(list_of_data['main']['temp'])+'°C',
         "pressure":str(list_of_data['main']['pressure']),
         "humidity":str(list_of_data['main']['humidity']),
          "main":str(list_of_data['weather'][0]['main']),
          "description":str(list_of_data['weather'][0]['description']),
          "icon":str(list_of_data['weather'][0]['icon']),
        }
        print(data)
        
        

    else:
        data = { }
    return render(request,"main/index.html",data)









def get_all_ans(prompt):


    # genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))


    # Import the necessary libraries
    # import google.generativeai as genai
    # from django.conf import settings

# Set up the API key
    genai.configure(api_key=settings.API_KEY)

    model = genai.GenerativeModel('gemini-pro')
    # prompt="Can you provide an overview of the history of chandigarh city? "
    response = model.generate_content(prompt)
    # print(response.text)
    res=response.text



    return res





def baseai(request):


    if request.method =='POST':
         
        city = request.POST.get("cityx")
        
        print(city)
        
        
        
        

        prompt1=f"Can you suggest four places to visit in {city} with the current temperature in 4 key points ?"
        prompt2=f"Please provide a concise overview of the history of {city} city in four key points."

        print(prompt1)
        print(prompt2)
        



        ans_prompt1= get_all_ans(prompt1)

        ans_prompt2= get_all_ans(prompt2)
        # print(ans_prompt1)
        
        dict ={
            "travel":ans_prompt1,
            "history":ans_prompt2,
        }

    else:
        dict ={}


    return render(request, "main/baseai.html",dict)
    

    

def comingsoon(request):
    return render(request,"main/comingsoon.html")

        



    