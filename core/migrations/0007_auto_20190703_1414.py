# Generated by Django 2.2.3 on 2019-07-03 14:14

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20190703_1119'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visit',
            old_name='participant',
            new_name='participant_id',
        ),
        migrations.AddField(
            model_name='visit',
            name='notes',
            field=models.TextField(blank=True, null=True, verbose_name='Visit Notes'),
        ),
        migrations.AddField(
            model_name='visit',
            name='program_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Program'),
            preserve_default=False,
        ),
    ]
