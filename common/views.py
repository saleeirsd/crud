from django.shortcuts import render,redirect
from .models import Customer
from .models import Seller
from random import randint
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.

def home(request):
    return render(request,'common/home.html')

def custlogin(request):
    msg = ''
    if request.method == 'POST':
        cemail = request.POST['cemail']
        cpassword = request.POST['cpassword']
        try : 
         customer = Customer.objects.get(email=cemail , password = cpassword)
         return redirect('customer:index')
        except :
            msg = "invalid credential"
    return render(request,'common/customerlogin.html',{'message':msg})

def custregistration(request):
    msg =''
    if request.method == 'POST':
        cname = request.POST['custmer_name']
        email = request.POST['email']
        address = request.POST['address']
        phone = request.POST['phone']
        gender = request.POST['gender']
        password = request.POST['password']

        try:
            customer = Customer(customer_name = cname,email = email, address = address, phone = phone, gender = gender, password = password)
            customer.save()
            msg = 'successfully registered'
        except:
            msg = 'invalid credential'


    return render(request,'common/customerregist.html',{'message':msg})

def sellerlogin(request):
    if request.method =='POST':
        email = request.POST['semail']
        password =request.POST['spassword']
        try:
             seller =Seller.objects.get(email = email , password =password)
             return redirect('seller:index')
        except:
            msg = 'user name or password incorrect'

    return render(request,'common/sellerlogin.html')

def sellerregistration(request):
    msg = ""
    if request.method == 'POST':
        sname = request.POST['seller_name']
        email = request.POST['email']
        address = request.POST['address']
        phone = request.POST['phone']
        gender = request.POST['gender']
        company_name = request.POST['company_name']
        holder_name = request.POST['holder_name']
        ifsc = request.POST['ifsc']
        branch = request.POST['branch']
        acc_number = request.POST['acc_number']
        image = request.FILES['image']
        user_name = randint(1111,9999)
        pwd = 'sell'+str(user_name)+'-'+phone[6:10]
        
        seller = Seller(seller_name = sname,email = email, address = address,
        phone = phone, gender = gender, company_name = company_name,
        holder_name = holder_name, ifsc = ifsc , branch = branch, account_number = acc_number, pic = image,user_name=user_name,password=pwd)
        seller.save()
        msg = 'created successfully'        
        email_subject = 'account name and password'
        email_content = 'user name :  '+str(user_name)+'password :   '+pwd
        send_mail(
            email_subject, 
            email_content,
            settings.EMAIL_HOST_USER,
            [email,]
        ) 


    return render(request,'common/seller_reg.html',{'message':msg})
