# Ex.05 Design a Website for Server Side Processing
# Date:06-10-2025
# AIM:
To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side.

# FORMULA:
P = I2R
P --> Power (in watts)
 I --> Intensity
 R --> Resistance

# DESIGN STEPS:
## Step 1:
Clone the repository from GitHub.

## Step 2:
Create Django Admin project.

## Step 3:
Create a New App under the Django Admin project.

## Step 4:
Create python programs for views and urls to perform server side processing.

## Step 5:
Create a HTML file to implement form based input and output.

## Step 6:
Publish the website in the given URL.

# PROGRAM :
```
math.html

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Power Calculating</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #ffb35cff;
            margin: 0;
            padding: 0;
        }

        fieldset {
            max-width: 500px;
            margin: 100px auto;
            border-radius: 10px;
            background-color: white;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
            padding: 30px;
        }

        legend {
            font-size: 22px;
            font-weight: bold;
            padding: 0 10px;
            color: #2c3e50;
        }

        h2, h3 {
            text-align: center;
            margin-bottom: 20px;
        }

        form {
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        label {
            margin-top: 10px;
            font-weight: 600;
        }

        input {
            width: 80%;
            padding: 8px;
            margin-top: 5px;
            border: 1px solid #ff8484ff;
            border-radius: 5px;
            font-size: 16px;
        }

        button {
            margin-top: 10px;
            padding: 10px 20px;
            background-color: #7fff69ff;
            color: black;
            border: none;
            font-size: 20px;
            border-radius: 10px;
            cursor: hand cursor;
        }

        button:hover {
            background-color: #0056b3;
        }

        p {
            font-size: 18px;
        }
    </style>
</head>
<body>
    <legend style="color=red;" align="center">Wanna know What's The Power</legend>
    <fieldset>
        <legend style="color=red;" align="center">ROHITH S</legend>    
        <h2>Power Calculator</h2>
        <form method="POST">
            {% csrf_token %}
            <label>Current (ampere):</label>
            <input type="number" name="Current" required>
            
            <label>Resistance (ohm):</label>
            <input type="number" name="resistance" required>
            
            <button type="submit">Calculate Power</button>
        </form>

        {% if power %}
        <h2>P  = I<sup>2</sup> × R</h2>
        <h3>Input Values</h3>
        <p align="center">Current: {{Current}} (A) <br>Resistance: {{resistance}} (Ω) </p>
        <h3>Power: {{power}} watt</h3>
        {% endif %}
    </fieldset>
</body>
</html>

views.py

from django.shortcuts import render
def calculate_power(request):
    P = 1
    I=0
    R=0
    if request.method=="POST":
        I+=float(request.POST.get("Current"))
        R+=float(request.POST.get("resistance"))
        P*=(I**2)*R
        print(f"Current: {I} ampere,resistance: {R} ohm,Power: {P} watt")
        return render(request,'app5/math.html',{"Current":I,"resistance":R,"power":P})
    return render(request,'app5/math.html',{"Current":I,"resistance":R,"power":P})

urls.py

from django.contrib import admin
from django.urls import path
from app5 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.calculate_power,name="calculate_power"),
]

```
# SERVER SIDE PROCESSING:
![alt text](<pro5/pro5/Screenshot 2025-10-06 101705.png>)
# HOMEPAGE:
![alt text](<pro5/pro5/Screenshot 2025-10-06 101357.png>)
# RESULT:
The program for performing server side processing is completed successfully.
