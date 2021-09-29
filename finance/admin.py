from django.contrib import admin
from .models import Fee
# Register your models here.


class FeeAdmin(admin.ModelAdmin):
    list_display = ['name_of_student', 'roll_no_of_student', 'fee_receivable', 'fee_received']



admin.site.register(Fee, FeeAdmin)

