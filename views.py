from django.shortcuts import render,redirect
from Note_taking_app.models import Customer,Blog,Admin
from Note_taking_app.forms import CustomerForms,BlogForms,BlogForm,AdminForms


# Create your views here.


def index(request):
    return render(request, "index.html", {})


def about(request):
    return render(request, "about.html", {})


def customer_regpage(request):
    return render(request,"customer_reg.html",{})


def customer_reg(request):
    if request.method=="POST":
        email=request.POST["email"]
        if Customer.objects.filter(email=email).exists():
            print("email already taken")
            return render(request,"customer_reg.html",{"msg":"email already taken"})
        else:
            form = CustomerForms(request.POST,request.FILES)
            if form.is_valid():
                print("errors:",form.errors)
                try:
                    form.save()
                    return render(request,"customer.html",{"msg":"Register successfully"})
                except Exception as e:
                    print(e)
            return render(request,"customer_reg.html",{"msg":"fail"})


def customer(request):
    return render(request, "customer.html", {})


def customer_login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        print(email, "", password)
        customer = Customer.objects.filter(email=email, password=password)
        if customer.exists():
            request.session['email'] = email
            return render(request, "customer_page.html", {"msg": email})
        else:
            return render(request, "customer.html", {"msg": "Invali data"})
    return render(request, "customer.html", {"msg": "not exist"})

def logout(request):
    request.session["email"] = ""
    del request.session["email"]
    return render(request, "customer.html", {"msg":"logout success"})


def customer_details_display(request):
    email = request.session['email']
    customer = Customer.objects.get(email=email)
    print('ram')
    return render(request, "customer_details.html", {"customer": customer})


def is_customer(request):
    if request.session.__contains__("email"):
        return True
    else:
        return False


def customer_password(request):
    if is_customer(request):
        if request.method == "POST":
            email = request.session["email"]
            password = request.POST["password"]
            newpassword = request.POST["newpassword"]
            try:
                user = Customer.objects.get(email=email, password=password)
                user.password = newpassword

                user.save()
                msg = 'password update successfully'
                return render(request, "customer.html", {"msg": msg})
            except:
                msg = 'invalid data'
                return render(request, "customer_password.html", {"msg": msg})
        return render(request, "customer_password.html", {})
    else:
        return render(request, "customer_page.html", {})

def customer_details_edit(request, email):
    user = Customer.objects.get(email=email)
    return render(request, "edit.html", {"customer": user})


def customer_details_update(request):
    if request.method == "POST":
        print("error:")
        email = request.POST["email"]
        print("hello")
        users = Customer.objects.get(email=email)
        users = CustomerForms(request.POST,request.FILES ,instance=users)
        print("error:", users.errors)
        if users.is_valid():
            print("error:", users.errors)
            users.save()
        return redirect("/customer_details_display")
    return redirect("/customer_details_display")


def customer_delete(request, email):
    user = Customer.objects.get(email=email)
    user.delete()
    return redirect("/customer_regpage")


def blog(request):
    email = request.session['email']
    customer = Customer.objects.get(email=email)
    if request.method == "POST":
        blog = BlogForm(request.POST, request.FILES)
        print('hi')
        print("Errors",blog.errors)
        if blog.is_valid():
            print(blog.errors)
            blog.save()
            return render(request, "add_blog.html", {"msg": "note added", "id": customer.id})
    return render(request, "add_blog.html", {"id": customer.id})


def display_blog(request):
    email = request.session['email']
    customer = Customer.objects.get(email=email)
    blog = Blog.objects.filter(customer_id=customer.id)
    print("hii")
    return render(request, "display_blog.html", {"blogs": blog})



def blog_edit(request, id):
    blog = Blog.objects.get(id=id)
    return render(request, "blog_edit.html", {"blog": blog})


def blog_update(request):
    global id
    email = request.session['email']
    customer = Customer.objects.get(email=email)
    if request.method == "POST":
        id = request.POST["id"]
        blog = Blog.objects.get(id=id)
        blog = BlogForm(request.POST, request.FILES, instance=blog)
        print('hi')
        print(blog.errors)
        if blog.is_valid():
            print(blog.errors)
            blog.save()
            blogs = Blog.objects.filter(customer_id=customer.id)
            return redirect("/display_blog", {"blog": blogs})
    return redirect ("/display_blog", {"id": id})


def blog_delete(request,id):
    blog=Blog.objects.get(id=id)
    blog.delete()
    return render(request,"add_blog.html",{})


def admin_log(request):
    if request.method == "POST":
        admin = request.POST["admin"]
        password = request.POST["password"]
        print(admin, "", password)
        customer = Admin.objects.filter(admin=admin, password=password)
        if customer.exists():
            request.session['admin'] = admin
            return render(request, "admin_page.html", {"msg": admin})
        else:
            return render(request, "admin.html", {"msg": "Invali data"})
    return render(request, "admin.html", {"msg": ""})

def admin_profile(request):
    return render(request,"admin_page.html",{})


def customer_profile(request):
    return render(request,"customer_page.html",{})



def is_admin(request):
    if request.session.__contains__("admin"):
        return True
    else:
        return False


def admin_password(request):
    if is_admin(request):
        if request.method == "POST":
            admin = request.session["admin"]
            password = request.POST["password"]
            newpassword = request.POST["newpassword"]
            try:
                admin = Admin.objects.get(admin=admin, password=password)
                admin.password = newpassword

                admin.save()
                msg = 'password update successfully'
                return render(request, "admin.html", {"msg": msg})
            except:
                msg = 'invalid data'
                return render(request, "admin_password.html", {"msg": msg})
        return render(request, "admin_password.html", {})
    else:
        return render(request, "admin_password.html", {})


def admin_logout(request):
    request.session["admin"] = ""
    del request.session["admin"]
    return render(request, "admin.html", {"msg":"logout success"})

def admin_customer(request):
    customer=Customer.objects.all()
    return render(request,"admin_customer.html",{"customers":customer})

def admin_delete(request, email):
    user = Customer.objects.get(email=email)
    user.delete()
    return redirect("/admin_customer")

def admin_notes(request):
    note=Blog.objects.all()
    return render(request,"admin_notes.html",{"blogs":note})