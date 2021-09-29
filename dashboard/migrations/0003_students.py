# Generated by Django 3.2.7 on 2021-09-22 05:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0002_sections'),
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=512)),
                ('student_roll_number', models.CharField(max_length=512)),
                ('student_cell', models.CharField(max_length=512)),
                ('student_Whatsapp', models.CharField(max_length=512)),
                ('student_address', models.CharField(max_length=1024)),
                ('student_picture', models.ImageField(default='images/studentPictures/ppic.png', upload_to='images/studentPictures/')),
                ('student_fee', models.CharField(max_length=512)),
                ('admissionDate', models.DateTimeField(auto_now_add=True)),
                ('student_status', models.CharField(choices=[('activated', 'Activated'), ('deactivated', 'Deactivated')], default='activated', max_length=30)),
                ('voucher_issued_status', models.BooleanField(default=False)),
                ('student_added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('student_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.classes')),
                ('student_section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.sections')),
            ],
        ),
    ]
