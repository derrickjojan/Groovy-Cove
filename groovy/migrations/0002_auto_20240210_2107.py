# Generated by Django 3.2.7 on 2024-02-10 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groovy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_payment_eventchild',
            name='Event_id',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='tbl_payment_eventchild',
            name='Payment_id',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='tbl_payment_master',
            name='Cust_id',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='tbl_payment_planchild',
            name='Payment_id',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='tbl_payment_planchild',
            name='Plan_id',
            field=models.CharField(max_length=120),
        ),
    ]