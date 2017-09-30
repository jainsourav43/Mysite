from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from .models import items
from .models import Extras
from django.views.decorators.csrf import csrf_exempt
from django.utils import six
from itertools import product,chain
from django.utils.deprecation import (
    DeprecationInstanceCheck, RemovedInDjango20Warning,
)

# Create your views here.

def home(request):
	return render(request,'Mess/hi.html')
def oye(request):
	return HttpResponse('<h1> Bye </h1>')

@csrf_exempt
def login_user(request):
    if request.method == "POST":
        username = request.POST['name']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        login(request,user)
        u = request.user
        if request.user.is_authenticated():
        	me = UserProfile.objects.filter(user=u)
	        typeid = me[0].type_id
	        amount = me[0].extra
	        rollno = me[0].roll_no
	        if user is not None:
	            if user.is_active:
	            	if typeid == "Student":# cheking whether user is student or Mess member
	            		 context={'roll':rollno,'amount':amount }
	            		 print(context)
	            		 obj=Extras.objects.filter(roll_no=rollno)#Multiple Rows having data
	            		 obj2=UserProfile.objects.filter(roll_no=rollno)
	            		 result_list=list(chain(obj,obj2))
	            		 #print(obj)
	            		 return render(request, 'Mess/display.html',{'obj': result_list})#rendering to Display.html
	            	else:
	                	return render(request, 'Mess/adddata.html')#rendering to adddata from where to URL Then to adddata function
	            else:
	                return render(request, 'Mess/studentln.html', {'error_message': 'Your account has been disabled'})#Error MEssage
	        else:
	            return render(request, 'Mess/studentln.html', {'error_message': 'Invalid login'})#error Message
    return render(request, 'Mess/studentln.html',{})#Rendering back to same page


@csrf_exempt
def adddata(request):
	if request.method =="POST":
		item=request.POST['Item']
		roll=request.POST['roll']
		qty=request.POST['quantity']
		date=request.POST['Date']
		obj1=UserProfile.objects.get(roll_no=roll)
		obj= items.objects.get(name = item , mess =obj1.mess)
		price=obj.cost*float(qty)
		obj2 = Extras(roll_no=roll, date=date, item=item ,quantity=qty,extra=price)
		obj2.save()
		obj1.extra=float(obj1.extra)+float(price)
		obj1.save()	
	return render(request,'Mess/adddata.html')


@csrf_exempt
def logout(request):
	return render(request,'Mess/login_user.html')
	
# def index(request,me):
# 	print("inindex")
# 	if me[0].type_id=="Student":
# 		roll= me[0].roll_no
# 		reg = me[0].reg_no
# 		amount = me[0].extra
# 		print(amount)
# 		display(request)
# 		return render(request, 'Mess/display.html')
# 	else:
# 		adddata(request)
# 		return render(request,'Mess/adddata.html')

# def display(request):
# 	return HttpResponse("HII Bro")

	# item=request.POST['item']
 #        roll=request.POST['roll']
 #        qty=request.POST['quantity']
 #        date=request.POST['Date']
 #        obj=items.objects.get(name=item)
 #        price=obj.cost*float(qty)
 #        obj1=UserProfile.objects.get(roll_no=roll)
 #        obj1.extra=float(obj1.extra)+float(price)
 #        obj1.save()
	# item=request.POST['Item']
	# 	roll=request.POST['roll']
	# 	qty=request.POST['quantity']
	# 	date=request.POST['Date']
	#     obj= items.objects.get(name = item)
	# 	price=obj.cost*float(qty)
	# 	obj2 = Extras(roll_no=roll, date=date, item=item ,quantity=qty,amount=price)
	# 	obj2.save()
	# 	obj1=UserProfile.objects.get(roll_no=roll)
	# 	obj1.extra=float(obj1.extra)+float(price)
	# 	obj1.save()