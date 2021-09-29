from django import forms
from .models import Classes, Sections, Students


# class StudentPictureForm(forms.ModelForm):
#     class Meta:
#         model = Students
#         fields = ('student_picture',)

class ClassForm(forms.ModelForm):
    class Meta:
        model = Classes
        fields = ('name', 'category',)


class SectionForm(forms.ModelForm):
    class Meta:
        model = Sections
        fields = ('section_of_class', 'section_name',)


class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ('student_class', 'student_section', 'student_name', 'student_roll_number', 'student_cell', 'student_Whatsapp', 'student_address', 'student_picture', 'student_fee', 'student_status', 'fee_due_date',)

