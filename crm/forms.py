from django import forms
from .models import Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['company_name', 'type_of_company', 'gst_no',]

from django import forms
from .models import Lead

class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['company_name', 'requirement', 'status']  # include required fields
        widgets = {
            'requirement': forms.Textarea(attrs={'rows': 3}),
        }


from django import forms
from .models import Estimation, Lead

class EstimationForm(forms.ModelForm):
    class Meta:
        model = Estimation
        fields = [
            'quote_date', 'lead_no', 'validity_days', 'billing_address', 
            'shipping_address', 'discount', 'terms_conditions', 
            'sub_total', 'gst_amount', 'total'
        ]




from django import forms
from .models import Estimation

class ApprovalForm(forms.ModelForm):
    class Meta:
        model = Estimation
        fields = ['credit_days', 'po_number', 'po_date', 'po_received_date', 'po_attachment', 'remarks']


from django import forms
from .models import Estimation

class ApproveEstimationForm(forms.ModelForm):
    class Meta:
        model = Estimation
        fields = ['credit_days', 'po_number', 'po_date', 'po_received_date', 'po_attachment', 'remarks']
        widgets = {
            'po_date': forms.DateInput(attrs={'type': 'date'}),
            'po_received_date': forms.DateInput(attrs={'type': 'date'}),
        }










