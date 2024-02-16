from django.http import HttpResponse
from django.http import JsonResponse
from django.urls import reverse
from django.shortcuts import render
from django.shortcuts import redirect
from datetime import datetime, timedelta
from django.utils import timezone
from django.contrib import messages
# FILE UPLOAD AND VIEW
from  django.core.files.storage import FileSystemStorage
# SESSION
from django.conf import settings
from .models import *
from decimal import Decimal


def first(request):
    testimonials = tbl_feedback.objects.filter(Type='review',Status='1')
    res = tbl_category.objects.all()
    result = tbl_event.objects.filter(E_Status=1)

    today = datetime.now().date()

    payments = tbl_payment_master.objects.all()

    for payment in payments:
    # Fetch associated child plans for the payment
        payment_plans = tbl_payment_planchild.objects.filter(Payment_id=payment.id)
    
        for plan in payment_plans:
        # Determine if the plan is monthly or annually based on the 'Type' column
            plan_type = plan.Type.lower()  # Assuming 'Type' values are stored in lowercase
        
            if plan_type == "monthly":
                days_to_add = 30
            elif plan_type == "annually":
                days_to_add = 365
            else:
                continue  # Skip this plan and move to the next one
            
        # Convert payment.Payment_date to a datetime.date object
            payment_date = payment.Payment_date
        
        # Calculate the expiration date by adding days_to_add to the payment date
            expiration_date = payment_date + timedelta(days=days_to_add)
        
        # Check if the expiration date is before today's date
            if expiration_date < today:
            # Update the payment status to expired (status = 0)
                payment.Status = 0
                payment.save()

    staff_assignments = tbl_staff_assign.objects.all()

    for assignment in staff_assignments:
        assignment_date = datetime.strptime(assignment.Date, '%Y-%m-%d').date()
        if assignment_date < today:
            assignment.Status = 0
            assignment.save()


    user_id = request.session.get('user_id')
    plans = []
    user_data = {}

    if user_id:
        cust = tbl_customer.objects.get(id=user_id)
        login_data = cust.Cust_Username  # Accessing the related login object directly
        if login_data:
            user_data = {
                'user_type': login_data.user_type,
                'join_date': login_data.join_date,
            }
        payment_master = tbl_payment_master.objects.filter(Cust_id=user_id,Status=1)

        for payment in payment_master:
            pay_id = payment.id
            payment_planchildren = tbl_payment_planchild.objects.filter(Payment_id=pay_id)

            for payment_planchild in payment_planchildren:
                plan_id = payment_planchild.Plan_id
                if plan_id in ['8', '9', '10']:
                    plan = tbl_plan.objects.get(id=plan_id)
                    plan_data = {
                        'Plan_name': plan.P_Name,
                    }
                    plans.append(plan_data)
    else:
        cust = None

    return render(request, 'index.html', {'category': res, 'event': result, 'cust': cust, 'plans': plans, 'user_data': user_data, 'testimonials': testimonials})


def index(request):
    testimonials = tbl_feedback.objects.filter(Type='review',Status='1')
    res = tbl_category.objects.all()
    result = tbl_event.objects.filter(E_Status=1)

    today = datetime.now().date()

    payments = tbl_payment_master.objects.all()

    for payment in payments:
    # Fetch associated child plans for the payment
        payment_plans = tbl_payment_planchild.objects.filter(Payment_id=payment.id)
    
        for plan in payment_plans:
        # Determine if the plan is monthly or annually based on the 'Type' column
            plan_type = plan.Type.lower()  # Assuming 'Type' values are stored in lowercase
        
            if plan_type == "monthly":
                days_to_add = 30
            elif plan_type == "annually":
                days_to_add = 365
            else:
                continue  # Skip this plan and move to the next one
            
        # Convert payment.Payment_date to a datetime.date object
            payment_date = payment.Payment_date
        
        # Calculate the expiration date by adding days_to_add to the payment date
            expiration_date = payment_date + timedelta(days=days_to_add)
        
        # Check if the expiration date is before today's date
            if expiration_date < today:
            # Update the payment status to expired (status = 0)
                payment.Status = 0
                payment.save()

    staff_assignments = tbl_staff_assign.objects.all()

    for assignment in staff_assignments:
        assignment_date = datetime.strptime(assignment.Date, '%Y-%m-%d').date()
        if assignment_date < today:
            assignment.Status = 0
            assignment.save()

    user_id = request.session.get('user_id')
    plans = []
    user_data = {}

    if user_id:
        cust = tbl_customer.objects.get(id=user_id)
        login_data = cust.Cust_Username  # Accessing the related login object directly
        if login_data:
            user_data = {
                'user_type': login_data.user_type,
                'join_date': login_data.join_date,
            }
        payment_master = tbl_payment_master.objects.filter(Cust_id=user_id,Status=1)

        for payment in payment_master:
            pay_id = payment.id
            payment_planchildren = tbl_payment_planchild.objects.filter(Payment_id=pay_id)

            for payment_planchild in payment_planchildren:
                plan_id = payment_planchild.Plan_id
                if plan_id in ['8', '9', '10']:
                    plan = tbl_plan.objects.get(id=plan_id)
                    plan_data = {
                        'Plan_name': plan.P_Name,
                    }
                    plans.append(plan_data)
    else:
        cust = None

    return render(request, 'index.html', {'category': res, 'event': result, 'cust': cust, 'plans': plans, 'user_data': user_data, 'testimonials': testimonials})






def contact(request):
    res = tbl_category.objects.all()
    result = tbl_event.objects.all()
    user_id = request.session.get('user_id')
    plans = []
    user_data = {}

    if user_id:
        cust = tbl_customer.objects.get(id=user_id)
        login_data = cust.Cust_Username  # Accessing the related login object directly
        if login_data:
            user_data = {
                'user_type': login_data.user_type,
                'join_date': login_data.join_date,
            }
        payment_master = tbl_payment_master.objects.filter(Cust_id=user_id,Status=1)

        for payment in payment_master:
            pay_id = payment.id
            payment_planchildren = tbl_payment_planchild.objects.filter(Payment_id=pay_id)

            for payment_planchild in payment_planchildren:
                plan_id = payment_planchild.Plan_id
                if plan_id in ['8', '9', '10']:
                    plan = tbl_plan.objects.get(id=plan_id)
                    plan_data = {
                        'Plan_name': plan.P_Name,
                    }
                    plans.append(plan_data)
    else:
        cust = None

    return render(request, 'contact.html', {'category': res, 'event': result, 'cust': cust, 'plans': plans, 'user_data': user_data})

def register(request):
    cat = tbl_category.objects.all()
    return render(request,'register.html',{'category': cat})

def regis(request):
    if request.method == "POST":
        # Retrieve form data
        entered_email = request.POST.get("email")
        entered_phno = request.POST.get("phno")
        entered_fname = request.POST.get("fname")
        entered_mname = request.POST.get("mname")
        entered_lname = request.POST.get("lname")
        entered_dob = request.POST.get("dob")
        entered_gender = request.POST.get("gender")
        entered_state = request.POST.get("state")
        entered_city = request.POST.get("city")
        entered_pin = request.POST.get("pin")
        entered_pass = request.POST.get("password")
        entered_eimg = request.FILES.get("img")  # Get uploaded image

        # Save image to the file system and get the file path
        if entered_eimg:
            fs = FileSystemStorage()
            filename = fs.save(entered_eimg.name, entered_eimg)
            img_path = fs.url(filename)
        else:
            img_path = None

        # Create and save customer object
        today_date = timezone.now().date()
        lg = tbl_login.objects.create(
            username=entered_email,
            password=entered_pass,
            join_date=today_date,
            user_type='user'
        )

        # Use the retrieved instance when creating the tbl_customer instance
        exe = tbl_customer(
            Cust_Username=lg,
            Cust_Phno=entered_phno,
            Cust_Fname=entered_fname,
            Cust_Mname=entered_mname,
            Cust_Lname=entered_lname,
            Cust_Dob=entered_dob,
            Cust_Gender=entered_gender,
            Cust_State=entered_state,
            Cust_City=entered_city,
            Cust_Pin=entered_pin,
            Cust_Status='1',
            Cust_Img=img_path  # Save image path to database
        )
        exe.save()

        # Create and save login object

    return redirect('index')

def addstaff(request):
    return render(request,'addstaff.html')

def staffreg(request):
    if request.method == "POST":
        entered_fname = request.POST.get("fname")
        entered_mname = request.POST.get("mname")
        entered_lname = request.POST.get("lname")
        entered_date = request.POST.get("date")
        entered_phno = request.POST.get("phno")
        entered_gender = request.POST.get("gender")
        entered_state = request.POST.get("state")
        entered_city = request.POST.get("city")
        entered_pin = request.POST.get("pin")
        entered_email = request.POST.get("email")
        entered_pass = request.POST.get("password")
        entered_type = request.POST.get("type")
        today_date = timezone.now().date()

        lg=tbl_login.objects.create(username=entered_email,password=entered_pass,join_date=today_date,user_type='staff')
        exe=tbl_staff(S_Fname=entered_fname,S_Mname=entered_mname,S_Lname=entered_lname,S_Phno=entered_phno,S_Startdate=entered_date,S_Gender=entered_gender,S_State=entered_state,S_City=entered_city,S_Pin=entered_pin,S_Username=lg,S_type=entered_type,S_Status='1')
        exe.save()
    return redirect(staffselect)

def sdeactivate(request, id):
    obj = tbl_staff.objects.get(id=id)
    obj.S_Status = 0
    obj.save()
    request.session['error_message'] = "Staff Account have been Deactivated."
    return redirect(staffselect)

def sactivate(request, id):
    obj = tbl_staff.objects.get(id=id)
    obj.S_Status = 1
    obj.save()
    request.session['error_message'] = "Staff Account have been Activated."
    return redirect(staffselect)


def login(request):
    cat = tbl_category.objects.all()
    error_message = request.session.pop('error_message', None)
    return render(request, 'login.html',{'category': cat, 'error_message': error_message})

def log(request):
    entered_email = request.POST.get('email')
    entered_password = request.POST.get('password')

    if entered_email == "admin@gmail.com" and entered_password == "Admin@123":
        request.session['admin_id'] = 999
        request.session['admin_email'] = entered_email
        request.session['admin_password'] = entered_password
        return redirect('index')

    user = tbl_customer.objects.filter(Cust_Username=entered_email).first()
    staff = tbl_staff.objects.filter(S_Username=entered_email).first()

    if user:
        user_login_data = tbl_login.objects.filter(username=entered_email).first()
        if user_login_data and user_login_data.password == entered_password:
            if user.Cust_Status == 1:
                request.session['user_id'] = user.id
                return redirect('index')
            else:
                return render(request, 'login.html', {'error_message': 'Account is Deactivated Contact Admin'})
    elif staff:
        staff_login_data = tbl_login.objects.filter(username=entered_email).first()
        if staff_login_data and staff_login_data.password == entered_password:
            if staff.S_Status == '1':
                request.session['staff_id'] = staff.id
                return redirect('index')
            else:
                return render(request, 'login.html', {'error_message': 'Account is Deactivated Contact Admin'})

    return render(request, 'login.html', {'error_message': 'Incorrect email or password.'})



        
def admin(request):
    total_customers = tbl_customer.objects.count()
    total_staff = tbl_staff.objects.count()
    total_plans = tbl_plan.objects.count()
    total_events = tbl_event.objects.count()
    total_event_bookings = tbl_payment_eventchild.objects.count()
    total_plan_bookings = tbl_payment_planchild.objects.count()
    total_reviews = tbl_feedback.objects.count()
    total_maintenance = tbl_maintenance.objects.count()

    return render(request, 'dashboard.html', {
        'total_customers': total_customers,
        'total_staff': total_staff,
        'total_plans': total_plans,
        'total_events': total_events, 
        'total_event_bookings': total_event_bookings,
        'total_plan_bookings': total_plan_bookings,
        'total_reviews': total_reviews,
        'total_maintenance': total_maintenance,
    })


def categoryselect(request):
    res=tbl_category.objects.all()
    return render(request, 'categorylist.html', {'result':res})

def addcategory(request):
    return render(request,'addcategory.html')

def categoryadd(request):
    if request.method == "POST":
        entered_name = request.POST.get("name")
        entered_desc = request.POST.get("desc")
        entered_cimage = request.FILES.get("cimage")
        fs = FileSystemStorage()
        filename = fs.save(entered_cimage.name, entered_cimage)
        lg=tbl_category(Cat_Name=entered_name,Cat_Desc=entered_desc,Cat_Img=filename)
        lg.save()
    return redirect(categoryselect)


def fdeactivate(request, id):
    obj = tbl_facility.objects.get(id=id)
    obj.Status = 0
    obj.save()
    request.session['error_message'] = "Facility have been Deactivated."
    return redirect(facilityselect)

def factivate(request, id):
    obj = tbl_facility.objects.get(id=id)
    obj.Status = 1
    obj.save()
    request.session['error_message'] = "Facility have been Activated."
    return redirect(facilityselect)

def facilityselect(request):
    facilities = tbl_facility.objects.all()
    facility_list = []

    for facility in facilities:
        if facility.staff_id.id == 999:
            staff_name = 'admin'
        elif tbl_staff.objects.filter(id=facility.staff_id).exists():
            staff = tbl_staff.objects.get(id=facility.staff_id)
            staff_name = f"{staff.S_Fname} {staff.S_Lname}"
        else:
            staff_name = None

        category = facility.Cat_id  # Cat_id is already a tbl_category instance
        facility_list.append({'facility': facility, 'staff_name': staff_name, 'category': category})
    error_message = request.session.pop('error_message', None)
    return render(request, 'facilitylist.html', {'result': facility_list,'error_message': error_message})




def addfacility(request):
    res = tbl_category.objects.all()
    return render(request, 'addfacility.html', {'result': res})

def facilityadd(request):
    if request.method == "POST":
        entered_category = request.POST.get("category")  # Convert to integer
        entered_fname = request.POST.get("fname")
        entered_fdesc = request.POST.get("fdesc")
        entered_fmodel = request.FILES.get("fmodel")
        fs = FileSystemStorage()
        filename = fs.save(entered_fmodel.name, entered_fmodel)
        if 'admin_id' in request.session:
            id = request.session['admin_id']
        elif 'staff_id' in request.session:
            id = request.session['staff_id']    
        staff_instance = tbl_staff.objects.get(id=id)       
        cat_instance = tbl_category.objects.get(id=entered_category)  # Fetch the tbl_category instance
        lg = tbl_facility(Cat_id=cat_instance, staff_id=staff_instance, F_Name=entered_fname, F_Desc=entered_fdesc, F_Model=filename,Status=1)
        lg.save()
    return redirect(facilityselect)


def pdeactivate(request, id):
    obj = tbl_plan.objects.get(id=id)
    obj.P_Status = 0
    obj.save()
    request.session['error_message'] = "Plan have been Deactivated."
    return redirect(planselect)

def pactivate(request, id):
    obj = tbl_plan.objects.get(id=id)
    obj.P_Status = 1
    obj.save()
    request.session['error_message'] = "Plan have been Activated."
    return redirect(planselect)


def planselect(request):
    plans = tbl_plan.objects.all()
    staff_name = None
    for plan in plans:
        if plan.staff_id.id == 999:  # Check the id attribute of staff_id
            staff_name = 'admin'
        elif tbl_staff.objects.filter(id=plan.staff_id.id).exists():
            staff = tbl_staff.objects.get(id=plan.staff_id.id)
            staff_name = f"{staff.S_Fname} {staff.S_Lname}"
        else:
            staff_name = None
    error_message = request.session.pop('error_message', None)
    return render(request, 'planlist.html', {'result': plans, 'staff': staff_name, 'error_message': error_message})




def addplan(request):
    return render(request, 'addplan.html')

def planadd(request):
    if request.method == "POST":
        entered_pname = request.POST.get("pname")
        entered_ptype = request.POST.get("ptype")
        entered_pprice = request.POST.get("pprice")
        entered_valid = request.POST.get("pvalid")
        entered_pdesc = request.POST.get("pdesc")
        
        if 'admin_id' in request.session:
            staff_id = request.session['admin_id']
        elif 'staff_id' in request.session:
            staff_id = request.session['staff_id']     

        # Fetch the tbl_staff object directly using the staff_id
        staff_instance = tbl_staff.objects.get(id=staff_id)

        # Assign the staff_instance to the staff_id field
        lg = tbl_plan(
            P_Name=entered_pname,
            P_Desc=entered_pdesc,
            P_Price=entered_pprice,
            P_Type=entered_ptype,
            P_Valid=entered_valid,
            staff_id=staff_instance,  # Assign the staff_instance
            P_Status='1'
        )
        lg.save()
        
    return redirect(planselect)

def staffselect(request):
    res = tbl_staff.objects.exclude(id=999)  # Exclude the entry with id 999
    error_message = request.session.pop('error_message', None)
    return render(request, 'stafflist.html', {'result': res, 'error_message': error_message})


def time(request):
    res = tbl_category.objects.all()
    plans = tbl_plan.objects.filter(P_Type='tickets',P_Status=1)
    result_list = []

    for plan in plans:
        description_list = [item.split('  ') for item in plan.P_Desc.split(', ')]
        result_list.append({'plan': plan, 'description_list': description_list , 'price': plan.P_Price, 'valid':plan.P_Valid})
        
    pack = tbl_plan.objects.filter(P_Type='packages')
    package_list = []

    for i in pack:
        pack_list = [item.split('  ') for item in i.P_Desc.split(', ')]
        package_list.append({'plan': i, 'pack_list': pack_list , 'price': i.P_Price, 'valid':i.P_Valid})

    member = tbl_plan.objects.filter(P_Type='memberships')
    membership_list = []

    for j in member:
        member_list = [item.split('  ') for item in j.P_Desc.split(', ')]
        membership_list.append({'plan': j, 'member_list': member_list , 'price': j.P_Price, 'valid':j.P_Valid})

    
    user_id = request.session.get('user_id')
    plans = []
    user_data = {}

    if user_id:
        cust = tbl_customer.objects.get(id=user_id)
        login_data = cust.Cust_Username  # Accessing the related login object directly
        if login_data:
            user_data = {
                'user_type': login_data.user_type,
                'join_date': login_data.join_date,
            }
        payment_master = tbl_payment_master.objects.filter(Cust_id=user_id,Status=1)

        for payment in payment_master:
            pay_id = payment.id
            payment_planchildren = tbl_payment_planchild.objects.filter(Payment_id=pay_id)

            for payment_planchild in payment_planchildren:
                plan_id = payment_planchild.Plan_id
                if plan_id in ['8', '9', '10']:
                    plan = tbl_plan.objects.get(id=plan_id)
                    plan_data = {
                        'Plan_name': plan.P_Name,
                    }
                    plans.append(plan_data)
    else:
        cust = None
        
    return render(request, 'time.html', {'results': result_list, 'package':package_list,'category': res, 'membership':membership_list, 'cust': cust, 'plans': plans, 'user_data': user_data})

def cdeactivate(request, id):
    obj = tbl_customer.objects.get(id=id)
    obj.Cust_Status = 0
    obj.save()
    request.session['error_message'] = "Customer Account have been Deactivated."
    return redirect(custselect)

def cactivate(request, id):
    obj = tbl_customer.objects.get(id=id)
    obj.Cust_Status = 1
    obj.save()
    request.session['error_message'] = "Customer Account have been Activated."
    return redirect(custselect)


def custselect(request):
    res=tbl_customer.objects.all()
    error_message = request.session.pop('error_message', None)
    return render(request, 'custlist.html',{'result':res, 'error_message': error_message})


def edeactivate(request, id):
    obj = tbl_event.objects.get(id=id)
    obj.E_Status = 0
    obj.save()
    request.session['error_message'] = "Event have been Deactivated."
    return redirect(eventselect)

def eactivate(request, id):
    obj = tbl_event.objects.get(id=id)
    obj.E_Status = 1
    obj.save()
    request.session['error_message'] = "Event have been Activated."
    return redirect(eventselect)


def eventselect(request):
    res=tbl_event.objects.all()
    staff_name = None
    for i in res:
        if i.staff_id.id == 999:
            staff_name = 'admin'
        elif tbl_staff.objects.filter(id=i.staff_id).exists():
            staff = tbl_staff.objects.get(id=i.staff_id)
            staff_name = f"{staff.S_Fname} {staff.S_Lname}"
        else:
            staff_name = None
    error_message = request.session.pop('error_message', None)
    return render(request, 'eventlist.html', {'result': res, 'staff': staff_name, 'error_message': error_message})

def addevent(request):
    return render(request, 'addevent.html')

def eventadd(request):
    if request.method == "POST":
        entered_ename = request.POST.get("ename")
        entered_eprice = request.POST.get("eprice")
        entered_ecpty = request.POST.get("ecpty")
        entered_edesc = request.POST.get("edesc")
        entered_eimg = request.FILES.get("eimage")
        fs = FileSystemStorage()
        filename = fs.save(entered_eimg.name, entered_eimg)
        if 'admin_id' in request.session:
            id = request.session['admin_id']
        elif 'staff_id' in request.session:
            id = request.session['staff_id']           
        staff_instance = tbl_staff.objects.get(id=id)    
        lg=tbl_event(E_Name=entered_ename,E_Desc=entered_edesc,E_Price=entered_eprice,E_Cpty=entered_ecpty,staff_id=staff_instance,E_Status='1',E_Img=filename)
        lg.save()
    return redirect(eventselect)

def package(request):
    return render(request, 'package.html')

def eventpg(request):
    cat = tbl_category.objects.all()
    res = tbl_event.objects.filter(E_Status=1)
    user_id = request.session.get('user_id')
    plans = []
    user_data = {}

    if user_id:
        cust = tbl_customer.objects.get(id=user_id)
        login_data = cust.Cust_Username  # Accessing the related login object directly
        if login_data:
            user_data = {
                'user_type': login_data.user_type,
                'join_date': login_data.join_date,
            }
        payment_master = tbl_payment_master.objects.filter(Cust_id=user_id,Status=1)

        for payment in payment_master:
            pay_id = payment.id
            payment_planchildren = tbl_payment_planchild.objects.filter(Payment_id=pay_id)

            for payment_planchild in payment_planchildren:
                plan_id = payment_planchild.Plan_id
                if plan_id in ['8', '9', '10']:
                    plan = tbl_plan.objects.get(id=plan_id)
                    plan_data = {
                        'Plan_name': plan.P_Name,
                    }
                    plans.append(plan_data)
    else:
        cust = None
    return render(request, 'event.html', {'result': res, 'category': cat, 'cust': cust, 'plans': plans, 'user_data': user_data})


def facilityview(request,id):
    res = tbl_category.objects.all()
    f_result = tbl_facility.objects.filter(Cat_id=id,Status=1)
    cat_info = tbl_category.objects.get(id=id)
    user_id = request.session.get('user_id')
    plans = []
    user_data = {}

    if user_id:
        cust = tbl_customer.objects.get(id=user_id)
        login_data = cust.Cust_Username  # Accessing the related login object directly
        if login_data:
            user_data = {
                'user_type': login_data.user_type,
                'join_date': login_data.join_date,
            }
        payment_master = tbl_payment_master.objects.filter(Cust_id=user_id,Status=1)

        for payment in payment_master:
            pay_id = payment.id
            payment_planchildren = tbl_payment_planchild.objects.filter(Payment_id=pay_id)

            for payment_planchild in payment_planchildren:
                plan_id = payment_planchild.Plan_id
                if plan_id in ['8', '9', '10']:
                    plan = tbl_plan.objects.get(id=plan_id)
                    plan_data = {
                        'Plan_name': plan.P_Name,
                    }
                    plans.append(plan_data)
    else:
        cust = None
        
    return render(request, 'facility.html', {'f_result': f_result,'category': res, 'cat_info': cat_info, 'cust': cust, 'plans': plans, 'user_data': user_data})

def eventview(request,id):
    res = tbl_category.objects.all()
    event_info = tbl_event.objects.get(id=id)
    events= tbl_event.objects.filter(E_Status=1)
    user_id = request.session.get('user_id')
    plans = []
    user_data = {}

    if user_id:
        cust = tbl_customer.objects.get(id=user_id)
        login_data = cust.Cust_Username  # Accessing the related login object directly
        if login_data:
            user_data = {
                'user_type': login_data.user_type,
                'join_date': login_data.join_date,
            }
        payment_master = tbl_payment_master.objects.filter(Cust_id=user_id,Status=1)

        for payment in payment_master:
            pay_id = payment.id
            payment_planchildren = tbl_payment_planchild.objects.filter(Payment_id=pay_id)

            for payment_planchild in payment_planchildren:
                plan_id = payment_planchild.Plan_id
                if plan_id in ['8', '9', '10']:
                    plan = tbl_plan.objects.get(id=plan_id)
                    plan_data = {
                        'Plan_name': plan.P_Name,
                    }
                    plans.append(plan_data)
    else:
        cust = None
    error_message = request.session.pop('error_message', None)
    return render(request, 'eventview.html', {'f_result': event_info,'category': res, 'result':events, 'cust': cust, 'plans': plans, 'user_data': user_data, 'error_message':error_message})



def eventbook(request, id):
    if 'user_id' not in request.session:
        request.session['error_message'] = "You need to login to access this page."
        return redirect('login')  # Assuming 'login' is the name of your login view or URL
    
    res = tbl_category.objects.all()
    event_info = tbl_event.objects.get(id=id)
    events= tbl_event.objects.filter(E_Status=1)
    cust_id = request.session.get('user_id')
    cust_info = tbl_customer.objects.get(id=cust_id)
    cards = tbl_card.objects.filter(C_Cust=cust_id)

    user_id = request.session.get('user_id')
    plans = []
    user_data = {}

    if user_id:
        cust = tbl_customer.objects.get(id=user_id)
        login_data = cust.Cust_Username  # Accessing the related login object directly
        if login_data:
            user_data = {
                'user_type': login_data.user_type,
                'join_date': login_data.join_date,
            }
        payment_master = tbl_payment_master.objects.filter(Cust_id=user_id,Status=1)

        for payment in payment_master:
            pay_id = payment.id
            payment_planchildren = tbl_payment_planchild.objects.filter(Payment_id=pay_id)

            for payment_planchild in payment_planchildren:
                plan_id = payment_planchild.Plan_id
                if plan_id in ['8', '9', '10']:
                    plan = tbl_plan.objects.get(id=plan_id)
                    plan_data = {
                        'Plan_name': plan.P_Name,
                    }
                    plans.append(plan_data)
    else:
        cust = None

    if request.method == "POST":
        from_date = request.POST.get("from")
        request.session['fdate'] = from_date
        to_date = request.POST.get("to")
        request.session['tdate'] = to_date
        user_id = request.session.get('user_id')

        # Calculate the number of days and total price
        from_date_obj = datetime.strptime(from_date, '%Y-%m-%d')
        to_date_obj = datetime.strptime(to_date, '%Y-%m-%d')
        overlapping_events = tbl_payment_eventchild.objects.filter(
            Event_id=id,
            Booked_from__lte=to_date_obj,
            Booked_to__gte=from_date_obj
        ).exists()

        if overlapping_events:
            request.session['error_message'] = "This event is already booked for the selected dates."
            return redirect(f"../eventview/{id}")


        days_difference = (to_date_obj - from_date_obj).days + 1
        total_price = event_info.E_Price * days_difference

        membership_discount = 0

        if request.session.get('user_id'):
            membership_plans = tbl_payment_planchild.objects.filter(Plan_id__in=[8, 9, 10])

            if membership_plans.exists():
                payment_ids = membership_plans.values_list('Payment_id', flat=True)  # Use flat=True to flatten the result
                for pay in payment_ids:
                    payment_master = tbl_payment_master.objects.filter(id=pay, Cust_id=user_id,Status=1).first()
                    if payment_master:
                        planmasterid = payment_master.id
                        pla = tbl_payment_planchild.objects.filter(Payment_id=planmasterid)
                        for plan in pla:
                            if plan.Plan_id == '8':
                                if days_difference >= 5:
                                    membership_discount = 5
                                else:
                                    membership_discount = 0
                                break
                            elif plan.Plan_id == '9':
                                if days_difference >= 7:
                                    membership_discount = 10
                                else:
                                    membership_discount = 5
                                break
                            elif plan.Plan_id == '10':
                                if days_difference >= 5:
                                    membership_discount = 15
                                else:
                                    membership_discount = 10
                                break

        # Apply discount to total price
        request.session['discount'] = membership_discount
        discounted_price = total_price - (total_price * membership_discount / 100)

        return render(request, 'eventbook.html', {
            'f_result': event_info,
            'category': res,
            'c_result': cust_info,
            'card': cards,
            'from_date': from_date,
            'to_date': to_date,
            'total_price': total_price,
            'membership_discount': membership_discount,
            'discounted_price': discounted_price,
            'cust': cust, 
            'plans': plans, 
            'user_data': user_data
        })

    else:
        from_date = request.session.get('fdate')
        to_date = request.session.get('tdate')
        user_id = request.session.get('user_id')

        from_date_obj = datetime.strptime(from_date, '%Y-%m-%d')
        to_date_obj = datetime.strptime(to_date, '%Y-%m-%d')
        days_difference = (to_date_obj - from_date_obj).days + 1
        total_price = event_info.E_Price * days_difference

        membership_discount = 0

        if request.session.get('user_id'):
            membership_plans = tbl_payment_planchild.objects.filter(Plan_id__in=[8, 9, 10])

            if membership_plans.exists():
                payment_ids = membership_plans.values_list('Payment_id', flat=True)  # Use flat=True to flatten the result
                for pay in payment_ids:
                    payment_master = tbl_payment_master.objects.filter(id=pay, Cust_id=user_id,Status=1).first()
                    if payment_master:
                        planmasterid = payment_master.id
                        pla = tbl_payment_planchild.objects.filter(Payment_id=planmasterid)
                        for plan in pla:
                            if plan.Plan_id == '8':
                                if days_difference >= 5:
                                    membership_discount = 5
                                else:
                                    membership_discount = 0
                                break
                            elif plan.Plan_id == '9':
                                if days_difference >= 7:
                                    membership_discount = 10
                                else:
                                    membership_discount = 5
                                break
                            elif plan.Plan_id == '10':
                                if days_difference >= 5:
                                    membership_discount = 15
                                else:
                                    membership_discount = 10
                                break
        
        # Apply discount to total price
        request.session['discount'] = membership_discount
        discounted_price = total_price - (total_price * membership_discount / 100)

        return render(request, 'eventbook.html', {
            'f_result': event_info,
            'category': res,
            'c_result': cust_info,
            'card': cards,
            'from_date': from_date,
            'to_date': to_date,
            'total_price': total_price,
            'membership_discount': membership_discount,
            'discounted_price': discounted_price,
            'cust': cust, 
            'plans': plans, 
            'user_data': user_data
        })




def cardselect(request,id):
    event_id=id
    return render(request, 'card.html', {'event_id': event_id})

def plancardselect(request,id):
    plan_id=id
    return render(request, 'plancard.html', {'plan_id': plan_id})

def add_card(request,id):
        if request.method == "POST":
            entered_cname = request.POST.get("cname")
            entered_cnum = request.POST.get("cnum")
            entered_cdate = request.POST.get("cdate")
            entered_ccvv = request.POST.get("ccvv")
            if 'user_id' in request.session:
                uid = request.session['user_id']          
            cust_instance = tbl_customer.objects.get(id=uid)
        lg=tbl_card(C_Name=entered_cname,C_Number=entered_cnum,C_Cust=cust_instance,C_Date=entered_cdate,C_Cvv=entered_ccvv,C_Status='1')
        lg.save()
        return redirect(f"../eventbook/{id}")

def add_plancard(request,id):
        if request.method == "POST":
            entered_cname = request.POST.get("cname")
            entered_cnum = request.POST.get("cnum")
            entered_cdate = request.POST.get("cdate")
            entered_ccvv = request.POST.get("ccvv")
            if 'user_id' in request.session:
                uid = request.session['user_id']  
            cust_instance = tbl_customer.objects.get(id=uid)         
        lg=tbl_card(C_Name=entered_cname,C_Number=entered_cnum,C_Cust=cust_instance,C_Date=entered_cdate,C_Cvv=entered_ccvv,C_Status='1')
        lg.save()
        return redirect(f"../planpay/{id}")

def planpay(request, id):
    # Check if user_id exists in session
    if 'user_id' not in request.session:
        request.session['error_message'] = "You need to login to access this page."
        return redirect('login')  
    
    # Check if the user already has an active membership plan of ids 8, 9, or 10
    existing_membership_plans = tbl_payment_planchild.objects.filter(Plan_id__in=[8, 9, 10])
    
    plant =tbl_payment_master.objects.filter(Cust_id=request.session['user_id'],Status=1)
    for plans in plant:
        if existing_membership_plans.exists():
            plan = tbl_plan.objects.filter(id=id).first()
            if plan and plan.id in [8, 9, 10]:
                messages.warning(request, "You already have an active membership plan.")
                return redirect('time')


    # Proceed with the rest of the view logic for payment
    res = tbl_category.objects.all()
    plan_id = tbl_plan.objects.get(id=id)
    cust_id = request.session['user_id']
    cust_info = tbl_customer.objects.get(id=cust_id)
    cards = tbl_card.objects.filter(C_Cust=cust_id)

    user_id = request.session.get('user_id')
    plans = []
    user_data = {}

    if user_id:
        cust = tbl_customer.objects.get(id=user_id)
        login_data = tbl_login.objects.filter(username=cust.Cust_Username).first()  
        if login_data:
            user_data = {
                'join': login_data.join_date,
                'type': login_data.user_type,
            }
        payment_master = tbl_payment_master.objects.filter(Cust_id=user_id,Status=1)

        for payment in payment_master:
            pay_id = payment.id
            payment_planchildren = tbl_payment_planchild.objects.filter(Payment_id=pay_id)

            for payment_planchild in payment_planchildren:
                plan_pid = payment_planchild.Plan_id
                if plan_pid in ['8', '9', '10']:
                    plan = tbl_plan.objects.get(id=plan_pid)
                    plan_data = {
                        'Plan_name': plan.P_Name,
                    }
                    plans.append(plan_data)
    else:
        cust = None

    return render(request, 'planbook.html', {'result': plan_id, 'category': res, 'c_result': cust_info, 'card': cards, 'cust': cust, 'plans': plans, 'user_data': user_data})





def addpay(request):
    if request.method == "POST":
        card_id = request.POST.get('card_id')
        card_instance = tbl_card.objects.get(id=card_id)  # Fetch tbl_card instance instead of tbl_customer
        card_cvv = card_instance.C_Cvv  # Access CVV directly from card_instance
        entered_cvv = request.POST.get('cvv')
        event_id = request.POST.get('event_id')
        from_date=request.POST.get('from')
        to_date=request.POST.get('to')
        cust_id=request.session['user_id']
        today_date = timezone.now().date()
        price = request.POST.get('price')

        if entered_cvv == card_cvv:
            lg=tbl_payment_master.objects.create(Cust_id=cust_id,Card_id=card_instance,Payment_date=today_date,Total_price=price,Status='1')
            new_payment_id = lg.id
            res = tbl_payment_eventchild.objects.create(Payment_id=new_payment_id,Event_id=event_id,Booked_from=from_date,Booked_to=to_date,Price=price)
            pay_id = res.id
            return redirect(f"../esuccess/{pay_id}")
        else:
            messages.error(request, 'CVV verification failed')
            return redirect(f"../eventbook/{event_id}")
    else:
        messages.error(request, 'Error')
        return redirect(f"../eventbook/{event_id}")
    
def addpayplan(request):
    if request.method == "POST":
        card_id = request.POST.get('card_id')
        card_instance = tbl_card.objects.get(id=card_id)  # Fetch tbl_card instance instead of tbl_customer
        card_cvv = card_instance.C_Cvv  # Access CVV directly from card_instance
        entered_cvv = request.POST.get('cvv')
        plan_id = request.POST.get('plan_id')
        cust_id=request.session['user_id']
        today_date = timezone.now().date()
        price = request.POST.get('total_price')
        type=request.POST.get('payment_frequency')

        if entered_cvv == card_cvv:
            lg=tbl_payment_master.objects.create(Cust_id=cust_id,Card_id=card_instance,Payment_date=today_date,Total_price=price,Status='1')
            new_payment_id = lg.id
            res = tbl_payment_planchild.objects.create(Payment_id=new_payment_id, Plan_id=plan_id, Price=price, Type=type)
            pay_id = res.id
            return redirect(f"../psuccess/{pay_id}")
        else:
            messages.error(request, 'CVV verification failed')
            return redirect(f"../planpay/{plan_id}")
    else:
        messages.error(request, 'Error')
        return redirect(f"../planpay/{plan_id}")

from datetime import datetime

def bookplan(request):
    payment_plan_children = tbl_payment_planchild.objects.all()
    booked_plans = []

    for payment_plan_child in payment_plan_children:
        payment_id = payment_plan_child.Payment_id
        plan_id = payment_plan_child.Plan_id

        payment_master = tbl_payment_master.objects.get(id=payment_id)

        customer = tbl_customer.objects.get(id=payment_master.Cust_id)

        plan = tbl_plan.objects.get(id=plan_id)

        # Format Payment_date to "Y-m-d" format
        formatted_date = payment_master.Payment_date.strftime('%Y-%m-%d')

        booked_plans.append({
            'no': payment_plan_child.id, 
            'payment_id': payment_master.id, 
            'customer_fname': customer.Cust_Fname, 
            'customer_lname': customer.Cust_Lname, 
            'plan_name': plan.P_Name, 
            'booked_date': formatted_date, 
            'price': payment_master.Total_price
        })
    error_message = request.session.pop('error_message', None)
    return render(request, 'bookplan.html', {'booked_plans': booked_plans, 'error_message': error_message})

def psearch(request):
    if request.method == "POST":
        from_date_str = request.POST.get('startDate')
        to_date_str = request.POST.get('endDate')
    
        if from_date_str and to_date_str:
            from_date = datetime.strptime(from_date_str, '%Y-%m-%d').date()
            to_date = datetime.strptime(to_date_str, '%Y-%m-%d').date()

            payment_plan_children = tbl_payment_planchild.objects.all()
            booked_plans = []

            for payment_plan_child in payment_plan_children:
                payment_id = payment_plan_child.Payment_id
                plan_id = payment_plan_child.Plan_id
                payment_master = tbl_payment_master.objects.get(id=payment_id)
                customer = tbl_customer.objects.get(id=payment_master.Cust_id)
                plan = tbl_plan.objects.get(id=plan_id)
                formatted_date = payment_master.Payment_date.strftime('%Y-%m-%d')
                if from_date <= payment_master.Payment_date <= to_date:  
                    booked_plans.append({
                        'no': payment_plan_child.id, 
                        'payment_id': payment_master.id, 
                        'customer_fname': customer.Cust_Fname, 
                        'customer_lname': customer.Cust_Lname, 
                        'plan_name': plan.P_Name, 
                        'booked_date': formatted_date, 
                        'price': payment_master.Total_price
                    })

            return render(request, 'bookplan.html', {'booked_plans': booked_plans})
        else:
            request.session['error_message'] = "select a valid dates"
            return redirect(bookplan)



def bookevent(request):
    payment_event_children = tbl_payment_eventchild.objects.all()
    booked_events = []

    for payment_event_child in payment_event_children:
        payment_id = payment_event_child.Payment_id
        event_id = payment_event_child.Event_id
        payment_master = tbl_payment_master.objects.get(id=payment_id)
        customer = tbl_customer.objects.get(id=payment_master.Cust_id)
        event = tbl_event.objects.get(id=event_id)
        booked_events.append({'no': payment_event_child.id,
                               'payment_id': payment_master.id,
                                'customer_fname': customer.Cust_Fname,
                                'customer_lname': customer.Cust_Lname, 
                                'plan_name': event.E_Name, 
                                'booked_date': payment_master.Payment_date, 
                                'from' : payment_event_child.Booked_from, 
                                'to': payment_event_child.Booked_to, 
                                'price': payment_master.Total_price})
    error_message = request.session.pop('error_message', None)
    return render(request, 'bookevent.html', {'booked_plans': booked_events, 'error_message': error_message})

def esearch(request):
    if request.method == "POST":
        from_date_str = request.POST.get('startDate')
        to_date_str = request.POST.get('endDate')
    
        if from_date_str and to_date_str:
            from_date = datetime.strptime(from_date_str, '%Y-%m-%d').date()
            to_date = datetime.strptime(to_date_str, '%Y-%m-%d').date()

            payment_event_children = tbl_payment_eventchild.objects.all()
            booked_events = []

            for payment_event_child in payment_event_children:
                payment_id = payment_event_child.Payment_id
                event_id = payment_event_child.Event_id
                payment_master = tbl_payment_master.objects.get(id=payment_id)
                customer = tbl_customer.objects.get(id=payment_master.Cust_id)
                event = tbl_event.objects.get(id=event_id)
                if from_date <= payment_master.Payment_date <= to_date:  
                    booked_events.append({'no': payment_event_child.id,
                                        'payment_id': payment_master.id,
                                        'customer_fname': customer.Cust_Fname,
                                        'customer_lname': customer.Cust_Lname, 
                                        'plan_name': event.E_Name, 
                                        'booked_date': payment_master.Payment_date, 
                                        'from' : payment_event_child.Booked_from, 
                                        'to': payment_event_child.Booked_to, 
                                        'price': payment_master.Total_price})
            return render(request, 'bookevent.html', {'booked_plans': booked_events})
        else:
            request.session['error_message'] = "select a valid dates"
            return redirect(bookevent)
            
        
def receipt(request, id):
    user_id = request.session.get('user_id')
    booked_events = []

    # Retrieve payment event children associated with the provided ID
    payment_event_children = tbl_payment_eventchild.objects.filter(id=id)

    for payment_event_child in payment_event_children:
        payment_id = payment_event_child.Payment_id
        event_id = payment_event_child.Event_id
        payment_master = tbl_payment_master.objects.get(id=payment_id)
        customer = tbl_customer.objects.get(id=payment_master.Cust_id)
        event = tbl_event.objects.get(id=event_id)
        booked_from = payment_event_child.Booked_from
        booked_to = payment_event_child.Booked_to
        from_date_obj = datetime.strptime(booked_from, '%Y-%m-%d')
        to_date_obj = datetime.strptime(booked_to, '%Y-%m-%d')
        days_difference = (to_date_obj - from_date_obj).days + 1

        membership_discount = 100 - ((payment_master.Total_price / (event.E_Price * days_difference)) * 100)

        # Append the details of the booked event to the list
        booked_events.append({
            'no': payment_event_child.id,
            'payment_id': payment_master.id,
            'city' : customer.Cust_City,
            'pin' : customer.Cust_Pin,
            'customer_fname': customer.Cust_Fname,
            'customer_lname': customer.Cust_Lname,
            'event_name': event.E_Name,
            'booked_date': payment_master.Payment_date,
            'from': payment_event_child.Booked_from,
            'to': payment_event_child.Booked_to,
            'price': payment_master.Total_price, 
            'per' : event.E_Price,
            'state' : customer.Cust_State,
            'discount' : membership_discount
        })

    return render(request, 'receipt.html', {'booked_events': booked_events})


def epreceipt(request, id):
    user_id = request.session.get('user_id')
    booked_events = []

    # Retrieve payment event children associated with the provided ID
    payment_event_children = tbl_payment_eventchild.objects.filter(id=id)

    for payment_event_child in payment_event_children:
        payment_id = payment_event_child.Payment_id
        event_id = payment_event_child.Event_id
        payment_master = tbl_payment_master.objects.get(id=payment_id)
        customer = tbl_customer.objects.get(id=payment_master.Cust_id)
        event = tbl_event.objects.get(id=event_id)
        booked_from = payment_event_child.Booked_from
        booked_to = payment_event_child.Booked_to
        from_date_obj = datetime.strptime(booked_from, '%Y-%m-%d')
        to_date_obj = datetime.strptime(booked_to, '%Y-%m-%d')
        days_difference = (to_date_obj - from_date_obj).days + 1

        membership_discount = 100 - ((payment_master.Total_price / (event.E_Price * days_difference)) * 100)

        # Append the details of the booked event to the list
        booked_events.append({
            'no': payment_event_child.id,
            'payment_id': payment_master.id,
            'city' : customer.Cust_City,
            'pin' : customer.Cust_Pin,
            'customer_fname': customer.Cust_Fname,
            'customer_lname': customer.Cust_Lname,
            'event_name': event.E_Name,
            'booked_date': payment_master.Payment_date,
            'from': payment_event_child.Booked_from,
            'to': payment_event_child.Booked_to,
            'price': payment_master.Total_price, 
            'per' : event.E_Price,
            'state' : customer.Cust_State,
            'discount' : membership_discount
        })

    return render(request, 'receipt.html', {'booked_events': booked_events})




def preceipt(request, id):
    user_id = request.session.get('user_id')
    booked_plans = []
    payment_plan_child = tbl_payment_planchild.objects.get(id=id)
    payment_id = payment_plan_child.Payment_id
    plan_id = payment_plan_child.Plan_id
    payment_master = tbl_payment_master.objects.get(id=payment_id)
    customer = tbl_customer.objects.get(id=payment_master.Cust_id)
    plan = tbl_plan.objects.get(id=plan_id)
    booked_plans.append({
        'no': payment_plan_child.id,
        'payment_id': payment_master.id,
        'city': customer.Cust_City,
        'pin': customer.Cust_Pin,
        'customer_fname': customer.Cust_Fname,
        'customer_lname': customer.Cust_Lname,
        'plan_name': plan.P_Name,
        'booked_date': payment_master.Payment_date,
        'price': payment_master.Total_price, 
        'state': customer.Cust_State,
    })

    return render(request, 'preceipt.html', {'booked_plans': booked_plans})

def spreceipt(request, id):
    user_id = request.session.get('user_id')
    booked_plans = []
    payment_plan_child = tbl_payment_planchild.objects.get(id=id)
    payment_id = payment_plan_child.Payment_id
    plan_id = payment_plan_child.Plan_id
    payment_master = tbl_payment_master.objects.get(id=payment_id)
    customer = tbl_customer.objects.get(id=payment_master.Cust_id)
    plan = tbl_plan.objects.get(id=plan_id)
    booked_plans.append({
        'no': payment_plan_child.id,
        'payment_id': payment_master.id,
        'city': customer.Cust_City,
        'pin': customer.Cust_Pin,
        'customer_fname': customer.Cust_Fname,
        'customer_lname': customer.Cust_Lname,
        'plan_name': plan.P_Name,
        'booked_date': payment_master.Payment_date,
        'price': payment_master.Total_price, 
        'state': customer.Cust_State,
    })

    return render(request, 'preceipt.html', {'booked_plans': booked_plans})



def cal(request):
    payments = tbl_payment_eventchild.objects.all()
    events = tbl_event.objects.all()
    return render(request, 'calendar.html', {'payments': payments, 'events': events})


def pcal(request):
    payments = tbl_payment_planchild.objects.all()
    plan = tbl_plan.objects.all()
    return render(request, 'plancalendar.html', {'payments': payments, 'plans': plan})


def get_events(request):
    payment_event_children = tbl_payment_eventchild.objects.all()

    events = []
    for payment_event_child in payment_event_children:
        payment_id = payment_event_child.Payment_id
        event_id = payment_event_child.Event_id

        payment_master = tbl_payment_master.objects.get(id=payment_id)
        customer = tbl_customer.objects.get(id=payment_master.Cust_id)
        event = tbl_event.objects.get(id=event_id)

        event_data = {
            'Event_id': payment_event_child.Event_id,
            'Booked_from': payment_event_child.Booked_from,
            'Booked_to' : payment_event_child.Booked_to,
            'Customer_fname': customer.Cust_Fname,
            'Customer_lname': customer.Cust_Lname,
            'Event_name': event.E_Name,
        }
        events.append(event_data)

    return JsonResponse(events, safe=False)

def get_plans(request):
    payment_plan_children = tbl_payment_planchild.objects.all()

    plans = []
    for payment_plan_child in payment_plan_children:
        payment_id = payment_plan_child.Payment_id
        plan_id = payment_plan_child.Plan_id

        payment_master = tbl_payment_master.objects.get(id=payment_id)
        customer = tbl_customer.objects.get(id=payment_master.Cust_id)
        plan = tbl_plan.objects.get(id=plan_id)

        plan_data = {
            'Plan_id': payment_plan_child.Plan_id,
            'Booked': payment_master.Payment_date,
            'Customer_fname': customer.Cust_Fname,
            'Customer_lname': customer.Cust_Lname,
            'Plan_name': plan.P_Name,
        }
        plans.append(plan_data)

    return JsonResponse(plans, safe=False)


def order(request):
    res = tbl_category.objects.all()
    result = tbl_event.objects.all()
    data = []
    cust_id = request.session.get('user_id')
    payment_master_entries = tbl_payment_master.objects.filter(Cust_id=cust_id)
    for payment_entry in payment_master_entries:
        pay_id = payment_entry.id
        plans = tbl_payment_planchild.objects.filter(Payment_id=pay_id)
        for plan in plans:
            plan_details = tbl_plan.objects.filter(id=plan.Plan_id).first()
            if plan_details:
                plan_data = {
                    'Payment_date': payment_entry.Payment_date,
                    'Card_id': payment_entry.Card_id,
                    'Plan_name': plan_details.P_Name,
                    'price' : plan.Price,
                    'valid' : plan_details.P_Valid,
                    'id' : plan_details.id,
                    'plan_id' : plan.id,
                    'status' : payment_entry.Status,
                }
                data.append(plan_data)


    for payment_entry in payment_master_entries:
        pay_id = payment_entry.id
        events = tbl_payment_eventchild.objects.filter(Payment_id=pay_id)
        for event in events:
            event_details = tbl_event.objects.filter(id=event.Event_id).first()
            if event_details:
                # Calculate refund amount
                refund_amount = event.Price * Decimal('0.1')  # Convert float to Decimal
                
                plan_data = {
                    'Payment_date': payment_entry.Payment_date,
                    'Event_name': event_details.E_Name,
                    'booked_from' : event.Booked_from,
                    'id' : event.id,
                    'booked_to' : event.Booked_to,
                    'price' : event.Price,
                    'refund_amount' : refund_amount,  # Pass refund amount
                    'status' : payment_entry.Status,
                }
                data.append(plan_data)

    user_id = request.session.get('user_id')
    plans = []
    user_data = {}

    if user_id:
        cust = tbl_customer.objects.get(id=user_id)
        login_data = cust.Cust_Username  # Accessing the related login object directly
        if login_data:
            user_data = {
                'user_type': login_data.user_type,
                'join_date': login_data.join_date,
            }
        payment_master = tbl_payment_master.objects.filter(Cust_id=user_id,Status=1)

        for payment in payment_master:
            pay_id = payment.id
            payment_planchildren = tbl_payment_planchild.objects.filter(Payment_id=pay_id)

            for payment_planchild in payment_planchildren:
                plan_id = payment_planchild.Plan_id
                if plan_id in ['8', '9', '10']:
                    plan = tbl_plan.objects.get(id=plan_id)
                    plan_data = {
                        'Plan_name': plan.P_Name,
                    }
                    plans.append(plan_data)
    else:
        cust = None
    return render(request, 'orders.html', {'data': data,'category': res, 'event': result, 'cust': cust, 'plans': plans, 'user_data': user_data})


def psuccess(request,id):
    id=id
    return render(request,'payment_suc.html', {'id':id})

def esuccess(request,id):
    id=id
    return render(request,'payment_eve.html', {'id':id})

def feedback(request):
    res = tbl_category.objects.all()
    result = tbl_event.objects.all()
    user_id = request.session.get('user_id')
    plans = []
    user_data = {}

    if user_id:
        cust = tbl_customer.objects.get(id=user_id)
        login_data = cust.Cust_Username  # Accessing the related login object directly
        if login_data:
            user_data = {
                'user_type': login_data.user_type,
                'join_date': login_data.join_date,
            }
        payment_master = tbl_payment_master.objects.filter(Cust_id=user_id,Status=1)

        for payment in payment_master:
            pay_id = payment.id
            payment_planchildren = tbl_payment_planchild.objects.filter(Payment_id=pay_id)

            for payment_planchild in payment_planchildren:
                plan_id = payment_planchild.Plan_id
                if plan_id in ['8', '9', '10']:
                    plan = tbl_plan.objects.get(id=plan_id)
                    plan_data = {
                        'Plan_name': plan.P_Name,
                    }
                    plans.append(plan_data)
    else:
        cust = None

    return render(request,'feedback.html', {'category': res, 'event': result, 'cust': cust, 'plans': plans, 'user_data': user_data})

def addfeed(request):
    if request.method == "POST":
        entered_name = request.POST.get("name")
        entered_msg = request.POST.get("message")
        entered_rating = request.POST.get("rating")
        user_id = request.session.get('user_id')
        today_date = timezone.now().date()
        cust_instance = tbl_customer.objects.get(id=user_id)

        res=tbl_feedback(Cust_id=cust_instance,Name=entered_name,Msg=entered_msg,rating=entered_rating,Date=today_date,Type='review',Status=1)
        res.save()
    return redirect(index)

def addcontact(request):
    if request.method == "POST":
        entered_name = request.POST.get("name")
        entered_msg = request.POST.get("message")
        entered_rating = request.POST.get("rating")
        if 'admin_id' in request.session:
            user_id = request.session['admin_id']
        elif 'staff_id' in request.session:
            user_id = request.session['staff_id']
        elif 'user_id' in request.session:
            user_id = request.session['user_id']
        else:
            request.session['error_message'] = "You need to login to Submit a Query."
            return redirect('login')  
        cust_instance = tbl_customer.objects.get(id=user_id)
        today_date = timezone.now().date()

        res=tbl_feedback(Cust_id=cust_instance,Name=entered_name,Msg=entered_msg,rating=0,Date=today_date,Type='contact')
        res.save()

        return redirect(index)


def editevent(request, id):
    dtl = tbl_event.objects.filter(id=id)
    return render(request, 'editevent.html', {'detail': dtl})

def eventedit(request):
    if request.method == "POST":
        id = request.POST.get("id") 
        entered_name = request.POST.get("ename")
        entered_price = request.POST.get("eprice")
        entered_cpty = request.POST.get("ecpty")
        entered_desc = request.POST.get("edesc")
        entered_img = request.FILES.get("eimage")
        if 'admin_id' in request.session:
            staff_id = request.session['admin_id']
        elif 'staff_id' in request.session:
            staff_id = request.session['staff_id']
        else:
            return redirect('login')  

        event = tbl_event.objects.get(id=id)
        event.E_Name = entered_name
        event.E_Desc = entered_desc
        event.E_Cpty = entered_cpty
        event.E_Price = entered_price
        
        if entered_img:
            fs = FileSystemStorage()
            filename = fs.save(entered_img.name, entered_img)
            event.E_Image = filename 
        
        event.staff_id = staff_id
        event.E_Status = '1'
        event.save()
        
        return redirect(eventselect)
    else:
        request.session['error_message'] = "Incorrect Details."
        return redirect(eventselect)
    

def editfacility(request, id):
    dtl = tbl_facility.objects.filter(id=id)
    return render(request, 'editfacility.html', {'detail': dtl})

def facilityedit(request):
    if request.method == "POST":
        id = request.POST.get("id") 
        entered_name = request.POST.get("fname")
        entered_cat = request.POST.get("category")
        entered_desc = request.POST.get("fdesc")
        entered_fmodel = request.FILES.get("fmodel")
        if 'admin_id' in request.session:
            staff_id = request.session['admin_id']
        elif 'staff_id' in request.session:
            staff_id = request.session['staff_id']
        else:
            return redirect('login')  

        facility = tbl_facility.objects.get(id=id)
        facility.F_Name = entered_name
        facility.F_Desc = entered_desc
        facility.Cat_id = entered_cat
        if entered_fmodel:
            fs = FileSystemStorage()
            filename = fs.save(entered_fmodel.name, entered_fmodel)
            facility.F_Model = filename
        facility.staff_id = staff_id
        facility.save()
        return redirect(facilityselect)
    else:
        request.session['error_message'] = "Incorrect Details."
        return redirect(facilityselect)

def editplan(request, id):
    dtl = tbl_plan.objects.filter(id=id)
    return render(request, 'editplan.html', {'detail': dtl})

def planedit(request):
    if request.method == "POST":
        id = request.POST.get("id") 
        entered_name = request.POST.get("pname")
        entered_type = request.POST.get("ptype")
        entered_price = request.POST.get("pprice")
        entered_valid = request.POST.get("pvalid")
        entered_desc = request.POST.get("pdesc")
        
        # Get the current user's role
        if 'admin_id' in request.session:
            staff_id = request.session['admin_id']
        elif 'staff_id' in request.session:
            staff_id = request.session['staff_id']
        else:
            return redirect('login')  
        
        # Assuming tbl_plan is the model for the plan details
        exe = tbl_plan(id=id, P_Name=entered_name, P_Desc=entered_desc, P_Type=entered_type,
                            P_Price=entered_price, P_Valid=entered_valid, P_Status='1',
                            staff_id=staff_id)
        exe.save()
        return redirect(planselect)
    else:
        request.session['error_message'] = "Incorrect Details."
        return redirect(planselect)

def editcategory(request, id):
    dtl = tbl_category.objects.filter(id=id)
    return render(request, 'editcategory.html', {'detail': dtl})

def categoryedit(request):
    if request.method == "POST":
        id = request.POST.get("id") 
        entered_name = request.POST.get("name")
        entered_desc = request.POST.get("desc")
        entered_cimage = request.FILES.get("cimage")
        
        # Get the current user's role
        if 'admin_id' in request.session:
            staff_id = request.session['admin_id']
        elif 'staff_id' in request.session:
            staff_id = request.session['staff_id']
        else:
            return redirect('login')  
        
        # Assuming tbl_plan is the model for the plan details
        category = tbl_category.objects.get(id=id)
        category.Cat_Name = entered_name
        category.Cat_Desc = entered_desc
        if entered_cimage:
            fs = FileSystemStorage()
            filename = fs.save(entered_cimage.name, entered_cimage)
            category.Cat_Img = filename
        category.save()
        return redirect(categoryselect)
    else:
        request.session['error_message'] = "Incorrect Details."
        return redirect(categoryselect)

def editstaff(request, id):
    dtl = tbl_staff.objects.filter(id=id)
    return render(request, 'editstaff.html', {'detail': dtl})

def staffedit(request):
    if request.method == "POST":
        id = request.POST.get("id")  # Assuming you have a hidden input field with id in the form
        entered_fname = request.POST.get("fname")
        entered_mname = request.POST.get("mname")
        entered_lname = request.POST.get("lname")
        entered_date = request.POST.get("date")
        entered_phno = request.POST.get("phno")
        entered_gender = request.POST.get("gender")
        entered_state = request.POST.get("state")
        entered_city = request.POST.get("city")
        entered_pin = request.POST.get("pin")
        entered_email = request.POST.get("email")
        entered_pass = request.POST.get("password")
        entered_type = request.POST.get("type")

        try:
            dtl = tbl_login.objects.get(username=entered_email)
            password = dtl.password
        except tbl_login.DoesNotExist:
            request.session['error_message'] = "Invalid email address."
            return redirect(staffselect)

        if entered_pass == password:
            # Assuming tbl_staff is the model for staff details
            exe = tbl_staff(id=id, S_Fname=entered_fname, S_Mname=entered_mname, S_Lname=entered_lname,
                            S_Phno=entered_phno, S_Startdate=entered_date, S_Gender=entered_gender,
                            S_State=entered_state, S_City=entered_city, S_Pin=entered_pin,
                            S_Username=entered_email, S_type=entered_type, S_Status='1')
            exe.save()
            return redirect(staffselect)
        else:
            request.session['error_message'] = "Incorrect password."
            return redirect(staffselect)


def rdeactivate(request, id):
    obj = tbl_feedback.objects.get(id=id)
    obj.Status = 0
    obj.save()
    request.session['error_message'] = "FeedBack have been Deactivated."
    return redirect(feedbackselect)

def ractivate(request, id):
    obj = tbl_feedback.objects.get(id=id)
    obj.Status = 1
    obj.save()
    request.session['error_message'] = "FeedBack have been Activated."
    return redirect(feedbackselect)


def feedbackselect(request):
    facilities = tbl_feedback.objects.all()
    error_message = request.session.pop('error_message', None)
    return render(request, 'feedbacklist.html', {'result': facilities,'error_message': error_message})


def mdeactivate(request, id):
    obj = tbl_maintenance.objects.get(id=id)
    is_assigned = tbl_staff_assign.objects.filter(Maintenance_id=id, Status=1).exists()
    if is_assigned:
        request.session['error_message'] = "Maintenance cannot be deactivated as it is assigned to Event."
    else:
        obj.Status = 0
        obj.save()
        request.session['error_message'] = "Maintenance has been deactivated."
    return redirect(maintenance)

def mactivate(request, id):
    obj = tbl_maintenance.objects.get(id=id)
    obj.Status = 1
    obj.save()
    request.session['error_message'] = "Maintenance have been Activated."
    return redirect(maintenance)


def maintenance(request):
    maintenance = tbl_maintenance.objects.all()
    if 'admin_id' in request.session:
        staff_id = request.session['admin_id']
        staff_name = 'admin'
    elif 'staff_id' in request.session:
        staff_id = request.session['staff_id']
        staff = tbl_staff.objects.get(id=staff_id)
        staff_name = f"{staff.S_Fname} {staff.S_Lname}"
    else:
        return redirect('login')
    error_message = request.session.pop('error_message', None)
    return render(request, 'maintenancelist.html', {'result': maintenance, 'staff_name': staff_name,'error_message': error_message})


def assignedlist(request):
    staff_assign = tbl_staff_assign.objects.all()
    if 'admin_id' in request.session:
        staff_id = request.session['admin_id']
        staff_name = 'admin'
    elif 'staff_id' in request.session:
        staff_id = request.session['staff_id']
        staff = tbl_staff.objects.get(id=staff_id)
        staff_name = f"{staff.S_Fname} {staff.S_Lname}"
    else:
        return redirect('login')
    assigned_data = []
    for assignment in staff_assign:
        maintenance = assignment.Maintenance_id
        event = assignment.Event_id
        if maintenance and event:
            assigned_data.append({
                'id': assignment.id,
                'maintenance_name': maintenance.M_name,
                'event_name': event.E_Name,
                'date': assignment.Date, 
                'status': assignment.Status 
            })
    error_message = request.session.pop('error_message', None)
    return render(request, 'assignedlist.html', {'result': assigned_data, 'staff_name': staff_name, 'error_message': error_message})



def addmaint(request):
    return render(request,'addmaint.html')

def maintadd(request):
    if request.method == "POST":
        entered_name = request.POST.get("name")
        entered_desc = request.POST.get("desc")

        if 'admin_id' in request.session:
            staff_id = request.session['admin_id']
        elif 'staff_id' in request.session:
            staff_id = request.session['staff_id']
        else:
            return redirect('login')  
        staff_instance = tbl_staff.objects.get(id=staff_id)
        exe = tbl_maintenance(M_name=entered_name,M_desc=entered_desc,Staff_id=staff_instance,Status='1')
        exe.save()
        return redirect(maintenance)
    
def assignstaff(request,id):
    maint_id=id
    res=tbl_event.objects.all()
    staff_name = None
    for i in res:
        if i.staff_id.id == 999:
            staff_name = 'admin'
        elif tbl_staff.objects.filter(id=i.staff_id).exists():
            staff = tbl_staff.objects.get(id=i.staff_id)
            staff_name = f"{staff.S_Fname} {staff.S_Lname}"
        else:
            staff_name = None
    return render(request, 'assignstaff.html', {'result': res, 'staff': staff_name, 'maint_id' : maint_id})

def assign(request):
    if request.method == "POST":
        main_id = request.POST.get("main_id")
        maint_instance = tbl_maintenance.objects.get(id=main_id)
        event_id = request.POST.get("event_id")
        event_instance = tbl_event.objects.get(id=event_id)
        date = request.POST.get('date')
        if 'admin_id' in request.session:
            staff_id = request.session['admin_id']
        elif 'staff_id' in request.session:
            staff_id = request.session['staff_id']
        else:
            return redirect('login')
        staff_instance = tbl_staff.objects.get(id=staff_id)
        # Check if Maintenance_id has already been assigned to the same event
        existing_assignment = tbl_staff_assign.objects.filter(Maintenance_id=maint_instance, Event_id=event_instance,Date=date).exists()
        if existing_assignment:
            request.session['error_message'] = "This maintenance has already been assigned to the same event on this Date."
            return redirect('assignedlist')
        
        # Save the assignment if it doesn't already exist
        exe = tbl_staff_assign(Maintenance_id=maint_instance, Event_id=event_instance, Staff_id=staff_instance, Date=date, Status='1')
        exe.save()
        return redirect('assignedlist')
    else:
        return redirect('login')
    
def editmaint(request,id):
    dtl = tbl_maintenance.objects.filter(id=id)
    return render(request,'editmaint.html', {'detail':dtl})

def maintedit(request):
    if request.method == "POST":
        id = request.POST.get("id") 
        entered_name = request.POST.get("name")
        entered_desc = request.POST.get("desc")
        
        # Get the current user's role
        if 'admin_id' in request.session:
            staff_id = request.session['admin_id']
        elif 'staff_id' in request.session:
            staff_id = request.session['staff_id']
        else:
            return redirect('login')  
        staff_instance = tbl_staff.objects.get(id=staff_id)
        # Assuming tbl_plan is the model for the plan details
        exe = tbl_maintenance(id=id, M_name=entered_name, M_desc=entered_desc, Staff_id=staff_instance, Status='1')
        exe.save()
        return redirect(maintenance)
    else:
        request.session['error_message'] = "Incorrect Details."
        return redirect(maintenance)
    
def editcust(request,id):
    cat = tbl_category.objects.all()
    dtl = tbl_customer.objects.filter(id=id)
    user_id = request.session.get('user_id')
    plans = []
    user_data = {}

    if user_id:
        cust = tbl_customer.objects.get(id=user_id)
        login_data = cust.Cust_Username  # Accessing the related login object directly
        if login_data:
            user_data = {
                'user_type': login_data.user_type,
                'join_date': login_data.join_date,
            }
        payment_master = tbl_payment_master.objects.filter(Cust_id=user_id,Status=1)

        for payment in payment_master:
            pay_id = payment.id
            payment_planchildren = tbl_payment_planchild.objects.filter(Payment_id=pay_id)

            for payment_planchild in payment_planchildren:
                plan_id = payment_planchild.Plan_id
                if plan_id in ['8', '9', '10']:
                    plan = tbl_plan.objects.get(id=plan_id)
                    plan_data = {
                        'Plan_name': plan.P_Name,
                    }
                    plans.append(plan_data)
    else:
        cust = None


    return render(request,'editcust.html',{'category': cat, 'detail' : dtl, 'cust': cust, 'plans': plans, 'user_data': user_data})
def custedit(request):
    if request.method == "POST":
        id = request.POST.get("id") 
        entered_email = request.POST.get("email")
        entered_pass = request.POST.get("password")

        # Check if the email and password match an existing user
        login_data = tbl_login.objects.filter(username=entered_email).first()
        if login_data and login_data.password == entered_pass:
            # Retrieve the customer object
            cust = tbl_customer.objects.get(id=id)
            
            # Update customer details
            cust.Cust_Phno = request.POST.get("phno")
            cust.Cust_Fname = request.POST.get("fname")
            cust.Cust_Mname = request.POST.get("mname")
            cust.Cust_Lname = request.POST.get("lname")
            cust.Cust_Dob = request.POST.get("dob")
            cust.Cust_Gender = request.POST.get("gender")
            cust.Cust_State = request.POST.get("state")
            cust.Cust_City = request.POST.get("city")
            cust.Cust_Pin = request.POST.get("pin")
            cust.Cust_Status = 1  # Assuming 1 means active, adjust as necessary
            
            # Handle file upload
            entered_eimg = request.FILES.get("img")
            if entered_eimg:
                fs = FileSystemStorage()
                filename = fs.save(entered_eimg.name, entered_eimg)
                cust.Cust_Img = filename
            
            # Save the changes
            cust.save()
            
            # Redirect to the appropriate page
            return redirect(index)
        else:
            # Display error message if email or password is incorrect
            messages.error(request, 'Incorrect email or password.')
            return redirect(index)
    
    # Redirect to index page if method is not POST
    return redirect(index)

def eventcancel(request,id):
        event_child = tbl_payment_eventchild.objects.get(id=id)
        payment_master = tbl_payment_master.objects.get(id=event_child.Payment_id)
        if payment_master:
            payment_master.Status = 2
            payment_master.save()
            return redirect(order)  # Assuming you have a URL named 'success_page'
        return redirect(first)

def plancancel(request,id):
        plan_child = tbl_payment_planchild.objects.get(id=id)
        payment_master = tbl_payment_master.objects.get(id=plan_child.Payment_id)
        if payment_master:
            payment_master.Status = 2
            payment_master.save()
            return redirect(order)  # Assuming you have a URL named 'success_page'
        return redirect(first)

def logout(request):
    session_keys = list(request.session.keys())
    for key in session_keys:
        del request.session[key]
    return redirect (first)
