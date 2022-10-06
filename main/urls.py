from django.urls import path

from board.urls import urlpatterns_for_redirect
from main.views import *

urlpatterns = [
    path('', Home_new_class.as_view(), name='home'),
    path('cabinet/', Cabinet.as_view(), name='cabinet'),
    path('register/', Register_class.as_view(), name='register'),
    path('companyCard/', CardAdd_or_edit.as_view(), name='companyCard'),
    path('update_or_create_card/', update_or_create_card, name='update_or_create_card'),
    path('edit_company/', edit_company, name='edit_company'),
    path('app-calendar/', CalenApp.as_view(), name='app-calendar'),
    path('setting/', Setting.as_view(), name='setting'),
    path('edit/', Edit, name='edit'),
    path('up/', Up, name='up'),
    path('target/', Target.as_view(), name='target'),
    path('clients/', Clients.as_view(), name='clients'),
    path('login/', Login, name='login'),
    path('logout/', Logout, name='logout'),
    path('smsgateway/', SmsGateway, name='smsgateway'),
    path('sms/', Sms.as_view(), name='sms'),
    path('getcalendar/', GetCalendar, name='getcalendar'),
    path('addevent/', AddEvent, name='addevent'),
    path('etiroz/', Etiroz.as_view(), name='etiroz'),
    path('objectionwrite/', ObjectWrite, name='objectionwrite'),
    path('object/', Obj, name='object'),
    path('delete/', Delete, name='delete'),
    path('edito/', Edito, name='edito'),
    path('save/', Save, name='save'),
    path('ckeditor/', Ckeditor, name='ckeditor'),
    path('adduser/', AddUser, name='adduser'),
    path('debt/', Debt.as_view(), name='debt'),
    path('hodim/', Hodim.as_view(), name='hodim'),
    path('calenedit/', CalenEdit, name='calenedit'),
    path('caleneditform/', CalenEditForm, name='caleneditform'),
    path('calendel/', CalenDel, name='calendel'),
    path('saveeditcalen/', SaveEditCalen, name='saveeditcalen'),
    path('addnotes/', AddNotes, name='addnotes'),
    path('debthistory/', DebtHistory, name='debthistory'),
    path('adddebt/', AddDebt, name='adddebt'),
    path('adddebtor/', AddDebtor, name='adddebtor'),
    path('editspin/', EditSpin, name='editspin'),
    path('postevent/', PostEvent, name='postevent'),
    path('delevent/', DelEvent, name='delevent'),
    path('editevent/', EditEvent, name='editevent'),
    path('main_statistika/', main_statistika, name='main_statistika'),
    path('addhodim/', AddHodim, name='addhodim'),
    path('deletehodim/', DeleteHodim, name='deletehodim'),
    path('importLead/', importLead, name='importLead'),
    path('addtoken/', addtoken, name='addtoken'),
    path('addsms/', addsms, name='addsms'),
    path('addsmsto/', addsmsto, name='addsmsto'),
    path('edituser/', EditUser, name='edituser'),
    path('edithodim/', EditHodim, name='edithodim'),
    path('getregion/', GetRegion, name='getregion'),
    path('gethodim/', GetHodim, name='gethodim'),
    path('products/', Product_list_class.as_view(), name='products'),
    path('add_product/', add_product, name='add_product'),
    path('edit_product/<int:pk>/', edit_product, name='edit_product'),
    path('sms_template_status_change/', sms_template_status_change, name='sms_template_status_change'),
    path('newsmstemplate/', NewSMSTemplate_class.as_view(), name='newsmstemplate'),
    path('search_lead/', search_lead, name='search_lead'),
    path('filter_lead/', filter_lead, name='filter_lead'),
    path('save_sms_template/', save_sms_template, name='save_sms_template'),

    path('editsmstemplate/<int:pk>/', EditSMSTemplate_class.as_view(), name='editsmstemplate'),
    path('delete_sms_template/<int:pk>/', delete_sms_template, name='delete_sms_template'),


    path('add_payment_type/', add_payment_type, name='add_payment_type'),
    path('edit_payment_type/<int:pk>/', edit_payment_type, name='edit_payment_type'),

]+urlpatterns_for_redirect
