from django.db import models

class tbl_login(models.Model):
    username = models.CharField(max_length=120, primary_key=True)
    password = models.CharField(max_length=25)
    user_type = models.CharField(max_length=50, null=True)
    join_date = models.DateField(null=True)


class tbl_customer(models.Model):
    Cust_Username = models.ForeignKey(tbl_login, on_delete=models.CASCADE)
    Cust_Phno = models.CharField(max_length=120)
    Cust_Fname = models.CharField(max_length=150)
    Cust_Mname = models.CharField(max_length=150)
    Cust_Lname = models.CharField(max_length=150)
    Cust_Dob = models.CharField(max_length=150)
    Cust_Gender = models.CharField(max_length=150)
    Cust_State = models.CharField(max_length=150)
    Cust_City = models.CharField(max_length=150)
    Cust_Pin = models.CharField(max_length=150)
    Cust_Status = models.IntegerField(default=0)
    Cust_Img = models.ImageField(upload_to='images/', null=True, blank=True)


class  tbl_staff(models.Model):
    S_Username=models.ForeignKey(tbl_login, on_delete=models.CASCADE)
    S_Phno=models.CharField(max_length=120)
    S_Fname=models.CharField(max_length=150)
    S_Mname=models.CharField(max_length=150)
    S_Lname=models.CharField(max_length=150)
    S_State=models.CharField(max_length=150)
    S_City=models.CharField(max_length=150)
    S_Pin=models.CharField(max_length=150)
    S_Gender=models.CharField(max_length=150)
    S_type=models.CharField(max_length=150)
    S_Startdate=models.CharField(max_length=150)
    S_Status=models.CharField(max_length=150)

class tbl_category(models.Model):
    Cat_Name=models.CharField(max_length=120)
    Cat_Desc=models.CharField(max_length=255)
    Cat_Img=models.ImageField(upload_to='event_images/', null=True, blank=True)

class tbl_facility(models.Model):
    Cat_id=models.ForeignKey(tbl_category, on_delete=models.CASCADE)
    staff_id=models.ForeignKey(tbl_staff, on_delete=models.CASCADE)
    F_Name=models.CharField(max_length=120)
    F_Desc=models.CharField(max_length=400)
    F_Model = models.FileField(upload_to='3d_models/', null=True, blank=True)
    Status = models.IntegerField(default=0)


class tbl_plan(models.Model):
    P_Name=models.CharField(max_length=120)
    P_Desc=models.CharField(max_length=255)
    P_Type=models.CharField(max_length=120)
    P_Price=models.DecimalField(max_digits=5, decimal_places=0)
    P_Valid=models.CharField(max_length=120,null=True)
    P_Status=models.CharField(max_length=255)
    staff_id=models.ForeignKey(tbl_staff, on_delete=models.CASCADE)

class tbl_event(models.Model):
    E_Name = models.CharField(max_length=120)
    E_Desc = models.CharField(max_length=500)
    E_Cpty = models.CharField(max_length=120)
    E_Price = models.DecimalField(max_digits=5, decimal_places=0)
    E_Status = models.CharField(max_length=120)
    staff_id = models.ForeignKey(tbl_staff, on_delete=models.CASCADE)
    E_Img = models.ImageField(upload_to='event_images/', null=True, blank=True)
    E_Model = models.FileField(upload_to='3d_models/', null=True, blank=True)

class tbl_card(models.Model):
    C_Number=models.CharField(max_length=120)
    C_Name=models.CharField(max_length=120)
    C_Date=models.CharField(max_length=120)
    C_Cust=models.ForeignKey(tbl_customer, on_delete=models.CASCADE)
    C_Status=models.CharField(max_length=120)
    C_Cvv=models.CharField(max_length=120)

class tbl_payment_master(models.Model):
    Cust_id = models.CharField(max_length=120)
    Card_id = models.ForeignKey(tbl_card, on_delete=models.CASCADE)
    Payment_date = models.DateField()
    Total_price = models.DecimalField(max_digits=5, decimal_places=0)
    Status = models.IntegerField(default=0)


class tbl_payment_eventchild(models.Model):
    Payment_id=models.CharField(max_length=120)
    Event_id=models.CharField(max_length=120)
    Booked_from=models.CharField(max_length=120)
    Booked_to=models.CharField(max_length=120)
    Price=models.DecimalField(max_digits=5, decimal_places=0)

class tbl_payment_planchild(models.Model):
    Payment_id=models.CharField(max_length=120)
    Plan_id=models.CharField(max_length=120)
    Type=models.CharField(max_length=120,null=True)
    Price=models.DecimalField(max_digits=5, decimal_places=0)

class tbl_feedback(models.Model):
    Cust_id=models.ForeignKey(tbl_customer, on_delete=models.CASCADE)
    Name=models.CharField(max_length=120,null=True)
    Msg=models.CharField(max_length=800)
    Type=models.CharField(max_length=120)
    Date=models.CharField(max_length=120)
    rating=models.CharField(max_length=120)
    Status = models.IntegerField(default=0)


class tbl_maintenance(models.Model):
    M_name=models.CharField(max_length=120)
    M_desc=models.CharField(max_length=255)
    Staff_id=models.ForeignKey(tbl_staff, on_delete=models.CASCADE)
    Status = models.IntegerField(default=0)

class tbl_staff_assign(models.Model):
    Maintenance_id=models.ForeignKey(tbl_maintenance, on_delete=models.CASCADE)
    Event_id=models.ForeignKey(tbl_event, on_delete=models.CASCADE)   
    Staff_id=models.ForeignKey(tbl_staff, on_delete=models.CASCADE)
    Date=models.CharField(max_length=120)
    Status = models.IntegerField(default=0)


