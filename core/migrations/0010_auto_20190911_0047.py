# Generated by Django 2.2.2 on 2019-09-11 04:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_merge_20190823_2213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visit',
            name='program',
        ),
        migrations.CreateModel(
            name='ProgramServiceMap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Program')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Service')),
            ],
        ),
        migrations.AddField(
            model_name='visit',
            name='program_service_map',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.ProgramServiceMap'),
        ),
    ]
