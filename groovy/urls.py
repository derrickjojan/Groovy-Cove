"""groovy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.first),
    path('index',views.index, name='index'),
    path('contact',views.contact, name='contact'),
    path('register',views.register),
    path('regist',views.regis),
    path('login',views.login, name='login'),
    path('log',views.log),
    path('logout',views.logout, name='logout'),
    path('dashboard', views.admin, name='admin'),
    path('staff',views.staffselect),
    path('addstaff',views.addstaff),
    path('staffregist',views.staffreg),
    path('cust',views.custselect),
    path('plan',views.planselect),
    path('addplan',views.addplan),
    path('padd',views.planadd),
    path('facility',views.facilityselect),
    path('addfacility',views.addfacility),
    path('category',views.categoryselect),
    path('addcategory',views.addcategory),
    path('catadd',views.categoryadd),
    path('facadd',views.facilityadd),
    path('event',views.eventselect),
    path('addevent',views.addevent),
    path('eadd',views.eventadd),
    path('time',views.time, name='time'),
    path('package',views.package),
    path('eventpg',views.eventpg, name='eventpg'),
    path('facility/<int:id>',views.facilityview),
    path('eventview/<int:id>',views.eventview, name='eventview'),
    path('eventbook/<int:id>', views.eventbook),
    path('card/<int:id>',views.cardselect),
    path('cadd/<int:id>', views.add_card, name='cadd'),
    path('payadd', views.addpay),
    path('planpay/<int:id>',views.planpay),
    path('plancard/<int:id>',views.plancardselect),
    path('plancadd/<int:id>', views.add_plancard),
    path('payplan', views.addpayplan),
    path('bookplan',views.bookplan),
    path('bookevent',views.bookevent),
    path('cal',views.cal, name='cal'),
    path('pcal',views.pcal, name='pcal'),
    path('api/events/', views.get_events, name='get_events'),
    path('api/plans/', views.get_plans, name='get_plans'),
    path('order',views.order),
    path('psuccess/<int:id>',views.psuccess),
    path('esuccess/<int:id>',views.esuccess),
    path('feedback',views.feedback),
    path('addfeed',views.addfeed),
    path('editstaff/<int:id>',views.editstaff, name='editstaff'),
    path('staffedit',views.staffedit),
    path('editplan/<int:id>',views.editplan, name='editplan'),
    path('planedit',views.planedit),
    path('editfacility/<int:id>',views.editfacility, name='editfacility'),
    path('facilityedit',views.facilityedit),
    path('editevent/<int:id>',views.editevent, name='editevent'),
    path('eventedit',views.eventedit),
    path('editcategory/<int:id>',views.editcategory, name='editcategory'),
    path('categoryedit',views.categoryedit),
    path('feedbackselect',views.feedbackselect),
    path('maintenance',views.maintenance),
    path('addmaint',views.addmaint),
    path('maintadd',views.maintadd, name='maintadd'),
    path('editmaint/<int:id>',views.editmaint, name='editmaint'),
    path('maintedit',views.maintedit),
    path('assignstaff/<int:id>',views.assignstaff, name='assignstaff'),
    path('assign',views.assign, name='assign'),
    path('assignedlist',views.assignedlist, name='assignedlist'),
    path('sdeactivate/<int:id>',views.sdeactivate),
    path('sactivate/<int:id>',views.sactivate),
    path('cdeactivate/<int:id>',views.cdeactivate),
    path('cactivate/<int:id>',views.cactivate),
    path('pdeactivate/<int:id>',views.pdeactivate),
    path('pactivate/<int:id>',views.pactivate),
    path('fdeactivate/<int:id>',views.fdeactivate),
    path('factivate/<int:id>',views.factivate),
    path('edeactivate/<int:id>',views.edeactivate),
    path('eactivate/<int:id>',views.eactivate),
    path('mdeactivate/<int:id>',views.mdeactivate),
    path('mactivate/<int:id>',views.mactivate),
    path('rdeactivate/<int:id>',views.rdeactivate),
    path('ractivate/<int:id>',views.ractivate),
    path('editcust/<int:id>',views.editcust),
    path('custedit',views.custedit),
    path('addcontact',views.addcontact),
    path('receipt/<int:id>',views.receipt),
    path('preceipt/<int:id>',views.preceipt),
    path('psearch',views.psearch),
    path('esearch',views.esearch),
    path('spreceipt/<int:id>',views.spreceipt),
    path('epreceipt/<int:id>',views.epreceipt),
    path('eventcancel/<int:id>',views.eventcancel),
    path('plancancel/<int:id>',views.plancancel),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


