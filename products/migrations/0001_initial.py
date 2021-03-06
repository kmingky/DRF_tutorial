# Generated by Django 4.0.5 on 2022-06-21 14:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='제목')),
                ('thumbnail', models.FileField(upload_to='static', verbose_name='썸네일')),
                ('description', models.TextField(verbose_name='설명')),
                ('register_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='등록일자')),
                ('exposure_start_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='노출시작일')),
                ('exposure_end_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='노출종료일')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='작성자')),
            ],
        ),
    ]
