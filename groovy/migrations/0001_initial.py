# Generated by Django 3.2.7 on 2024-02-10 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('C_Number', models.CharField(max_length=120)),
                ('C_Name', models.CharField(max_length=120)),
                ('C_Date', models.CharField(max_length=120)),
                ('C_Status', models.CharField(max_length=120)),
                ('C_Cvv', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='tbl_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cat_Name', models.CharField(max_length=120)),
                ('Cat_Desc', models.CharField(max_length=255)),
                ('Cat_Img', models.ImageField(blank=True, null=True, upload_to='event_images/')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cust_Phno', models.CharField(max_length=120)),
                ('Cust_Fname', models.CharField(max_length=150)),
                ('Cust_Mname', models.CharField(max_length=150)),
                ('Cust_Lname', models.CharField(max_length=150)),
                ('Cust_Dob', models.CharField(max_length=150)),
                ('Cust_Gender', models.CharField(max_length=150)),
                ('Cust_State', models.CharField(max_length=150)),
                ('Cust_City', models.CharField(max_length=150)),
                ('Cust_Pin', models.CharField(max_length=150)),
                ('Cust_Status', models.IntegerField(default=0)),
                ('Cust_Img', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('E_Name', models.CharField(max_length=120)),
                ('E_Desc', models.CharField(max_length=500)),
                ('E_Cpty', models.CharField(max_length=120)),
                ('E_Price', models.DecimalField(decimal_places=0, max_digits=5)),
                ('E_Status', models.CharField(max_length=120)),
                ('E_Img', models.ImageField(blank=True, null=True, upload_to='event_images/')),
                ('E_Model', models.FileField(blank=True, null=True, upload_to='3d_models/')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_login',
            fields=[
                ('username', models.CharField(max_length=120, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=25)),
                ('user_type', models.CharField(max_length=50, null=True)),
                ('join_date', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='tbl_maintenance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('M_name', models.CharField(max_length=120)),
                ('M_desc', models.CharField(max_length=255)),
                ('Status', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='tbl_payment_master',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Payment_date', models.DateField()),
                ('Total_price', models.DecimalField(decimal_places=0, max_digits=5)),
                ('Status', models.IntegerField(default=0)),
                ('Card_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groovy.tbl_card')),
                ('Cust_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groovy.tbl_customer')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('S_Phno', models.CharField(max_length=120)),
                ('S_Fname', models.CharField(max_length=150)),
                ('S_Mname', models.CharField(max_length=150)),
                ('S_Lname', models.CharField(max_length=150)),
                ('S_State', models.CharField(max_length=150)),
                ('S_City', models.CharField(max_length=150)),
                ('S_Pin', models.CharField(max_length=150)),
                ('S_Gender', models.CharField(max_length=150)),
                ('S_type', models.CharField(max_length=150)),
                ('S_Startdate', models.CharField(max_length=150)),
                ('S_Status', models.CharField(max_length=150)),
                ('S_Username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groovy.tbl_login')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_staff_assign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.CharField(max_length=120)),
                ('Status', models.IntegerField(default=0)),
                ('Event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groovy.tbl_event')),
                ('Maintenance_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groovy.tbl_maintenance')),
                ('Staff_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groovy.tbl_staff')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('P_Name', models.CharField(max_length=120)),
                ('P_Desc', models.CharField(max_length=255)),
                ('P_Type', models.CharField(max_length=120)),
                ('P_Price', models.DecimalField(decimal_places=0, max_digits=5)),
                ('P_Valid', models.CharField(max_length=120, null=True)),
                ('P_Status', models.CharField(max_length=255)),
                ('staff_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groovy.tbl_staff')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_payment_planchild',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.CharField(max_length=120, null=True)),
                ('Price', models.DecimalField(decimal_places=0, max_digits=5)),
                ('Payment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groovy.tbl_payment_master')),
                ('Plan_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groovy.tbl_plan')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_payment_eventchild',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Booked_from', models.CharField(max_length=120)),
                ('Booked_to', models.CharField(max_length=120)),
                ('Price', models.DecimalField(decimal_places=0, max_digits=5)),
                ('Event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groovy.tbl_event')),
                ('Payment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groovy.tbl_payment_master')),
            ],
        ),
        migrations.AddField(
            model_name='tbl_maintenance',
            name='Staff_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groovy.tbl_staff'),
        ),
        migrations.CreateModel(
            name='tbl_feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=120, null=True)),
                ('Msg', models.CharField(max_length=800)),
                ('Type', models.CharField(max_length=120)),
                ('Date', models.CharField(max_length=120)),
                ('rating', models.CharField(max_length=120)),
                ('Status', models.IntegerField(default=0)),
                ('Cust_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groovy.tbl_customer')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_facility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('F_Name', models.CharField(max_length=120)),
                ('F_Desc', models.CharField(max_length=400)),
                ('F_Model', models.FileField(blank=True, null=True, upload_to='3d_models/')),
                ('Status', models.IntegerField(default=0)),
                ('Cat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groovy.tbl_category')),
                ('staff_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groovy.tbl_staff')),
            ],
        ),
        migrations.AddField(
            model_name='tbl_event',
            name='staff_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groovy.tbl_staff'),
        ),
        migrations.AddField(
            model_name='tbl_customer',
            name='Cust_Username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groovy.tbl_login'),
        ),
        migrations.AddField(
            model_name='tbl_card',
            name='C_Cust',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groovy.tbl_customer'),
        ),
    ]
