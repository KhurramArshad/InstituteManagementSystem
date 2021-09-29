from django import forms
from .models import Fee


# class StudentPictureForm(forms.ModelForm):
#     class Meta:
#         model = Students
#         fields = ('student_picture',)

class FeeForm(forms.ModelForm):
    class Meta:
        model = Fee
        fields = ('received_Date', 'fee_received',)
        widgets = {
            'received_Date': forms.DateInput(format=('%m/%d/%Y'),
                                             attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                    'type': 'date'}),
        }
