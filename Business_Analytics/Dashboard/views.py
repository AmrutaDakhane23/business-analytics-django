from django.shortcuts import render,redirect
from .models import BusinessRecord
from datetime import date
# Create your views here.
def dashboard(request):
    #INSERTING DATA
    if BusinessRecord.objects.count()==0:
        BusinessRecord.objects.create(category="Product", value=5000, date=date(2025,1,10))
        BusinessRecord.objects.create(category="Product", value=3000, date=date(2025,1,11))
        BusinessRecord.objects.create(category="Department", value=7000, date= date(2025,1,12))
        BusinessRecord.objects.create(category="Department",value=4000,date = date(2025,1,14))

    records = BusinessRecord.objects.all()
    #FILTER DATA
    category = request.GET.get('category')

    if category and category.strip() != "":
        records = records.filter(category=category)
    
    #ANALYTICS LOGIC
    values = [r.value for r in records]

    if values :
        total = sum(values)
        average = total/len(values)
        highest = max(values)
        lowest = min(values)
    else :
        total = average = highest = lowest=0
    
    data = {
        "records":records,
        "total":total,
        "average":average,
        "highest":highest,
        "lowest":lowest
    }
    
    return render(request,"Dashboard\index.html",data)

def update_value(request,id):
    record = BusinessRecord.objects.get(id = id)
    record.value += 1000
    record.save()
    return redirect("/")