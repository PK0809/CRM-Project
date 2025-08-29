﻿from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from crm import views
from crm.views import QuotationPDFView, report_list, export_report_excel, export_report_pdf
from crm.views import UserUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', views.user_list, name='user_list'),
    path('users/create/', views.create_user, name='user_create'),
    path('users/<int:pk>/edit/', UserUpdateView.as_view(), name='edit_user'),
    path('users/<int:user_id>/delete/', views.delete_user, name='user_delete'),
    path('create-user/', views.create_user, name='create_user'),
    path('users/create/', views.create_user, name='create_user'),
    path('get-permissions/', views.get_permissions_by_role, name='get_permissions'),
    
    

    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),

    # Authentication
    path('', views.user_login, name='login_redirect'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    

    # Client
    path('client/', views.client_list, name='client'),
    path('client/add/', views.client_entry, name='client_entry'),
    path('client/add/ajax/', views.client_entry_ajax, name='client_entry_ajax'),
    path('client/edit/<int:client_id>/', views.edit_client, name='edit_client'),

    # Lead
    path('lead/', views.lead_list, name='lead'), 
    path('lead/', views.lead_list, name='lead_list'),
    path('lead/create/', views.lead_create, name='lead_create'),
    path('lead/add/', views.lead_create, name='lead_create'),  # optional alias
    path('lead/edit/<int:pk>/', views.lead_edit, name='lead_edit'),
    path('invoice/approval/', views.invoice_approval_table, name='invoice_approval_list'),
    path('get-pending-lead/', views.get_pending_lead, name='get_pending_lead'),
    path('get-pending-leads/', views.get_pending_leads, name='get_pending_leads'),

    # Estimation
    path('estimations/', views.estimation_list, name='estimation_list'),
    path('estimations/', views.estimation_list, name='estimation'),  # Optional alias
    path('create-quotation/', views.create_quotation, name='create_quotation'),
    path("estimation/", views.estimation_list, name="estimation_list"),
    path('estimation/<int:pk>/edit/', views.edit_estimation, name='estimation_edit'),
    path('estimation/<int:pk>/approve/', views.approve_estimation, name='approve_estimation'),
    path('estimation/<int:id>/approve/', views.approve_estimation, name='approve_estimation_by_id'),
    path('estimation/<int:pk>/reject/', views.reject_estimation, name='reject_invoice'),
    path('estimation/<int:pk>/status/<str:new_status>/', views.update_estimation_status, name='estimation_status'),
    path('estimation/<int:pk>/lost/', views.mark_lost, name='mark_lost'),
    path('estimation/<int:id>/review/', views.mark_under_review, name='mark_under_review'),
    path('estimation/view/<int:pk>/', views.estimation_detail_view, name='estimation_detail'),
    path('quotation/<int:pk>/pdf/', QuotationPDFView.as_view(), name='quotation_pdf'),
    path('get-gst-no/', views.get_gst_no, name='get_gst_no'),

    # Invoice
    path('invoice/', views.invoice_view, name='invoice'),
    path('invoices/', views.invoice_list_view, name='invoice_list'),
    path('invoice/view/<int:pk>/', views.invoice_detail_view, name='invoice_detail'),
    path('invoice/generate/<int:pk>/', views.generate_invoice_from_estimation, name='generate_invoice'),
    path('invoice/create/', views.create_invoice, name='create_invoice'),
    path('invoice/create/<int:estimation_id>/', views.create_invoice, name='create_invoice_from_estimation'),
    path('invoice/<int:pk>/update-payment-status/', views.update_payment_status, name='update_payment_status'),
    path('invoice/<int:invoice_id>/logs/', views.view_payment_logs, name='view_payment_logs'),
    path('invoices/pdf/<int:invoice_id>/', views.invoice_pdf_view, name='invoice_pdf'),
    path('invoices/approve/<int:est_id>/', views.approve_invoice, name='approve_invoice'),
    path('invoices/reject/<int:pk>/', views.reject_invoice, name='reject_invoice'),
    path('invoices/', views.invoice_approval_table, name='invoice_approval_table'),
    path('api/invoice/<int:invoice_id>/logs/', views.get_payment_logs, name='invoice_logs'),
    path('confirm-payment/<int:invoice_id>/', views.confirm_payment, name='confirm_payment'),
    path('confirm-payment/', views.confirm_payment, name='confirm_payment_fallback'),

    # Reports
    path('reports/', report_list, name='report_list'),
    path('reports/export/excel/', export_report_excel, name='export_report_excel'),
    path('reports/export/pdf/', export_report_pdf, name='export_report_pdf'),

    # Other Views
    path('purchase-order/', views.purchase_order_view, name='purchase_order'),
    path('bill/', views.bill_view, name='bill'),
    path('vendor/', views.vendor_view, name='vendor'),
    path('profile/', views.profile_view, name='profile'),

    # Redirects
    path('invoice/', RedirectView.as_view(url='/invoices/', permanent=True)),
]

# Static/Media files for development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
