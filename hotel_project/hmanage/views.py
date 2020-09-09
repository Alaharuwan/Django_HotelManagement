from django.shortcuts import render
from django.http import HttpResponse
from hmanage.models import ReceptionHallPackage
from hmanage.models import ReceptionHallBook
import pyodbc

#redirecting the requrest to the add page of hmanage


def home (request):
    return render(request,'hmanage/addres.html')

def editResPackage(request):
    return render(request,'hmanage/editResPackage.html')

def editres(request):
    return render(request,'hmanage/editres.html')



def addrespackage (request):
    conn = pyodbc.connect('Driver={Sql Server};'
                          'Server=DESKTOP-PG66PFU\MSSQLSERVER01;'
                          'Database=GagaAddara_Hotel_DB;'
                          'Trusted_Connection=Yes;')
    if request.method == "POST":
         
            insertdata = ReceptionHallPackage()
            insertdata.theme       = request.POST.get('theme')
            insertdata.price       = request.POST.get('price')
            insertdata.description = request.POST.get('description')
            cursor                 = conn.cursor()
            cursor.execute("insert into ReceptionHallPackage (theme, price, description) values ('"+insertdata.theme+"','"+ insertdata.price+"','"+insertdata.description+"')")
            cursor.commit()
            return render(request, 'addResPackage.html')


    else:
            return render(request, 'addResPackage.html')

  
def listpackage(request):
    conn = pyodbc.connect('Driver={Sql Server};'
                          'Server=DESKTOP-PG66PFU\MSSQLSERVER01;'
                          'Database=GagaAddara_Hotel_DB;'
                          'Trusted_Connection=Yes;')
    if request.method == "POST":
        if request.POST.get('RH_packageID'):

            insertdata = ReceptionHallPackage()
            insertdata.RH_packageID = request.POST.get('RH_packageID')
            cursor = conn.cursor()
            cursor.execute("DELETE FROM ReceptionHallPackage WHERE RH_packageID ='"+insertdata.RH_packageID+"'")
            cursor.commit()
            
            cursor.execute("select * from ReceptionHallPackage")
            result = cursor.fetchall()
            return render(request, 'viewResPackage.html',{'ReceptionHallPackage':result})


    #view packages
    cursor = conn.cursor()
    cursor.execute("select * from ReceptionHallPackage")
    result = cursor.fetchall()
    return render(request, 'viewResPackage.html',{'ReceptionHallPackage':result})



    

def addres(request):

    conn = pyodbc.connect('Driver={Sql Server};'
                          'Server=DESKTOP-PG66PFU\MSSQLSERVER01;'
                          'Database=GagaAddara_Hotel_DB;'
                          'Trusted_Connection=Yes;')
                          
    if request.method == "POST":
        insertdata = ReceptionHallBook()
        insertdata.cusId       = request.POST.get('cusId')
        insertdata.theme       = request.POST.get('theme')
        insertdata.date        = request.POST.get('date')
        insertdata.timeFrom    = request.POST.get('timeFrom')
        insertdata.timeTo      = request.POST.get('timeTo')
        cursor                 = conn.cursor()
        cursor.execute("insert into ReceptionHallBooking (cusId, theme, date, timeFrom, timeTo) values ('"+str(insertdata.cusId)+"','"+str(insertdata.theme)+"','"+insertdata.date+"','"+insertdata.timeFrom+"','"+insertdata.timeTo+"')")
        cursor.commit()
        return render(request, 'addres.html')
    else:
        return render(request, 'addres.html')


def listres(request):
    conn = pyodbc.connect('Driver={Sql Server};'
                          'Server=DESKTOP-PG66PFU\MSSQLSERVER01;'
                          'Database=GagaAddara_Hotel_DB;'
                          'Trusted_Connection=Yes;')
    if request.method == "POST":
        if request.POST.get('RH_reserveID'):

            insertdata = ReceptionHallBook()
            insertdata.RH_reserveID = request.POST.get('RH_reserveID')
            cursor = conn.cursor()
            cursor.execute("DELETE FROM ReceptionHallBooking WHERE RH_reserveID ='"+insertdata.RH_reserveID+"'")
            cursor.commit()
            
            cursor.execute("select * from ReceptionHallBooking")
            result = cursor.fetchall()
            return render(request, 'viewres.html',{'ReceptionHallBook':result})


    #view packages
    cursor = conn.cursor()
    cursor.execute("select * from ReceptionHallBooking")
    result = cursor.fetchall()
    return render(request, 'viewres.html',{'ReceptionHallBook':result})
    

# Create your views here.
