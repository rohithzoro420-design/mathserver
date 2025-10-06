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