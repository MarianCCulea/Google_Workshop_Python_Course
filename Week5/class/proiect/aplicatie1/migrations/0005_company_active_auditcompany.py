# Generated by Django 4.2 on 2023-05-10 15:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aplicatie1', '0004_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='active',
            field=models.BooleanField(default=1),
        ),
        migrations.CreateModel(
            name='AuditCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('website', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=1)),
                ('company', models.IntegerField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicatie1.location')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]