from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Customer, Food, User, Order

# Create your views here.
def login(request):
    # Indicator if login was successful
    global is_loggedin

    # Checks if sign up was successful
    exists = "signup_success" in globals()
    if exists == True:
        if signup_success == True:
            # Get list of globals
            globals_list = globals()
            messages.success(request, "Account Created Successfully")
            
            # Change signup_success variable to false after message was created
            globals_list['signup_success'] = False

    if request.method == "POST":
        user = request.POST.get("uname")
        pwd = request.POST.get("pw")

        # Checks username first and then password. Failure means password is invalid
        if User.objects.filter(username=user).exists() == True:
            if User.objects.filter(password=pwd).exists() == True:
                # Indicates that log in is successful
                is_loggedin = True
                return redirect("view_orders")
            else:
                is_loggedin = False
                messages.error(request, "Invalid Password")

        # Checks password first and then user. Failure means Username is invalid
        elif User.objects.filter(password=pwd).exists() == True:
            if User.objects.filter(username=user).exists() == True:
                # Indicates that log in is successful
                is_loggedin = True
                return redirect("view_orders    ")
            else:
                is_loggedin = False
                messages.error(request, "Invalid Username")

        # If both username and passowrd are invalid
        else: 
            messages.error(request, "Invalid Username and Password")

    return render(request, "login.html")

def signup(request):
    # Indicator if sign up was successful
    global signup_success

    if request.method == "POST":
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")

        if User.objects.filter(username=user).exists() == True:
            messages.error(request, "User already exists")
        else:
            # Set sign up success indicator to true if user creation was successful
            signup_success = True
            User.objects.create(username=user, password=pwd)
            return redirect("login")
        
    return render(request, "signup.html")


#####BLOCK LINE FOR CUSTOMER, FOOD, AND ORDER #####

def viewcustomerlist(request):
    # Checks if logged in indicator is in global space
    exists = "is_loggedin" in globals()

    # Authentication to check if user is logged in
    if exists == True:
        if is_loggedin == True:
            customerlist = Customer.objects.all()
            return render(request, "customer_list.html", {'customer':customerlist}) #CHANGE VIEWS
        else:
            return redirect("login")#LOGIN REDIRECT FIX
    else:
        return redirect("login")#LOGIN REDIRECT FIX

def addcustomer(request):
    exists = "is_loggedin" in globals()
    
    if exists == True:
        if is_loggedin == True:
       
            if(request.method=="POST"):
                customername = request.POST.get('customername')
                address = request.POST.get('address')
                city = request.POST.get('city')
                

                if Customer.objects.filter(customername=customername).exists() ==   True: 
                    return render(request, "add_customer.html")#NEEDS TEMPLATE REDIRECT
        
                else:
                        Customer.objects.create(customername=customername, address=address, city=city)
                return redirect(viewcustomerlist)#NEEDS TEMPLATE REDIRECT
            
            return render(request, 'add_customer.html')# NEEDS TEMPLATE REDIRECT
        else:
            return redirect("login")#LOGIN REDIRECT FIX
    else:
        return redirect("login")#LOGIN REDIRECT FIX

def deletecustomer(request, pk):
    Customer.objects.filter(pk=pk).delete()
    return redirect('addcustomer') #Fix redirect

def viewcustomer(request, pk):
    customerlist = get_object_or_404(Customer, pk=pk)
    return render(request, "customer_details.html", {"c": customerlist}) ## REPLACE TEMPLATE

def viewfoodlist(request):
    # Checks if logged in indicator is in global space
    exists = "is_loggedin" in globals()

    # Authentication to check if user is logged in
    if exists == True:
        if is_loggedin == True:
            foodlist = Food.objects.all()
            return render(request, "food_list.html", {"foodlist":foodlist}) #CHANGE VIEWS
        else:
            return redirect("login")#LOGIN REDIRECT FIX
    else:
        return redirect("login")#LOGIN REDIRECT FIX

def addfood(request):
    exists = "is_loggedin" in globals()

    if exists == True:
        if is_loggedin == True:
       
            if(request.method=="POST"):
                name = request.POST.get('foodname')
                description = request.POST.get('description')
                price = request.POST.get('price')
                created_at = request.POST.get('created_at')
                

                if Food.objects.filter(name=name).exists() ==   True: 
                    return render(request, "add_food.html")#NEEDS TEMPLATE REDIRECT
        
                else:
                    Food.objects.create(name=name, description=description, price=price, created_at=created_at)
                return redirect('addfood')#NEEDS TEMPLATE REDIRECT
            
            return render(request, 'add_food.html')# NEEDS TEMPLATE REDIRECT
        else:
            return redirect("login")#LOGIN REDIRECT FIX
    else:
        return redirect("login")#LOGIN REDIRECT FIX

def updatefood(request, pk):
    if(request.method=="POST"):
        description = request.POST.get('description')
        price = request.POST.get('price')
        created_at = request.POST.get('created_at')

        if Food.objects.filter(description=description, price=price, created_at = created_at).exists() == True:
            food = get_object_or_404(Food, pk=pk)
            return render(request, 'update_food.html', {'f':food})
            
        else:
            Food.objects.filter(pk=pk).update(description = description, price = price, created_at = created_at)
            food = get_object_or_404(Food, pk=pk)
            return render(request, 'update_food.html', {'f':food})

    else:
        food = get_object_or_404(Food, pk=pk)
        return render(request, 'update_food.html', {'f':food})

def updatecustomer(request, pk):
    if(request.method=="POST"):
        customername = request.POST.get('customername')
        address = request.POST.get('address')
        city = request.POST.get('city')

        if Customer.objects.filter(customername = customername, address = address, city = city).exists() == True:
            customer = get_object_or_404(Customer, pk=pk)
            return render(request, "update_customer.html", {'c':customer}) 
        else:
            Customer.objects.filter(pk=pk).update(customername = customername, address = address, city = city)
            customer = get_object_or_404(Customer, pk=pk)
            return render(request, "update_customer.html", {'c':customer})

    else:
        customer = get_object_or_404(Customer, pk=pk)
        return render(request, "update_customer.html", {'c':customer})    

def deletefood(request, pk):
    Food.objects.filter(pk=pk).delete()
    return redirect('addfood')

def viewfood(request, pk):
    foodlist = get_object_or_404(Food, pk=pk)
    return render(request, "food_details.html", {"f": foodlist})

def view_orders(request):
    # Checks if logged in indicator is in global space
    exists = "is_loggedin" in globals()

    # Authentication to check if user is logged in
    if exists == True:
        if is_loggedin == True:
            orderer = Order.objects.all()
            return render(request, "orders.html", {"orders":orderer})
        else:
            return redirect("login")
    else:
        return redirect("login")

def addorder(request):
    # Checks if logged in indicator is in global space
    exists = "is_loggedin" in globals()

    if exists == True:
        if is_loggedin == True:
            if(request.method=="POST"):
                food_pk = request.POST.get('food')
                qty = request.POST.get('qty')
                ordered_at = request.POST.get('ordered_at')
                cust_pk = request.POST.get('cust_order')
                payment_mode = request.POST.get('payment_mode')

                # Gets supplier object based on supplier name
                food = Food.objects.get(name=food_pk)
                cust_order = Customer.objects.get(customername=cust_pk)

                # Checks if the water bottle already exists
                if Order.objects.filter(food=food, cust_order=cust_order).exists() == True:
                    # Gets list of suppliers to be sent to HTML form
                    fooder = Food.objects.all()
                    customerget = Customer.objects.all()
                    messages.error(request, "Item Already exists")
                    return render(request, 'add_order.html', {"foodlist":fooder, 'customer': customerget})
                else: 
                    Order.objects.create(food=food, qty=qty, ordered_at=ordered_at, cust_order = cust_order, payment_mode = payment_mode)
                    return redirect(view_orders)

            # Gets list of suppliers to be sent to HTML form
            fooder = Food.objects.all()
            customerget = Customer.objects.all()
            return render(request, 'add_order.html', {"foodlist":fooder, 'customer': customerget})
        else:
            return redirect("login")
    else:
        return redirect("login")


def updateorder(request, pk):
    if(request.method=="POST"):
        food_pk = request.POST.get('food')
        qty = request.POST.get('qty')
        ordered_at = request.POST.get('ordered_at')
        cust_pk = request.POST.get('cust_order')
        payment_mode = request.POST.get('payment_mode')

        food = Food.objects.get(name=food_pk)
        cust_order = Customer.objects.get(customername=cust_pk)

        if Order.objects.filter(food=food, qty=qty, ordered_at=ordered_at, cust_order = cust_order, payment_mode = payment_mode).exists() == True:
            order = get_object_or_404(Order, pk=pk)
            customer_details = Customer.objects.all()
            food_details = Food.objects.all()
            messages.error(request, "Details already exist")
            return render(request, 'update_order.html', {'o': order, 'foodlist': food_details, 'customer': customer_details})
        else:
            Order.objects.filter(pk=pk).update(food=food, qty=qty, ordered_at=ordered_at, cust_order = cust_order, payment_mode = payment_mode)
            order = get_object_or_404(Order, pk=pk)
            messages.success(request, "Details Updated")

            # Get suppliers and send these as choices for HTML form
            customer_details = Customer.objects.all()
            food_details = Food.objects.all()
            return render(request, 'update_order.html', {'o': order, 'foodlist': food_details, 'customer': customer_details})
    else:
        order = get_object_or_404(Order, pk=pk)

        # Get suppliers and send as choices for HTML form
        customer_details = Customer.objects.all()
        food_details = Food.objects.all()
        return render(request, 'update_order.html', {'o': order, 'foodlist': food_details, 'customer': customer_details})

def deleteorder(request, pk):
    Order.objects.filter(pk=pk).delete()
    messages.success(request, "Order deleted successfully")
    return redirect('view_orders')

def order_details(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, "order_details.html", {"o": order})



