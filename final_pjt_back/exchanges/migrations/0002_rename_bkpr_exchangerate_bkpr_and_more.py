# Generated by Django 4.2.13 on 2024-05-16 05:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exchanges', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exchangerate',
            old_name='BKPR',
            new_name='bkpr',
        ),
        migrations.RenameField(
            model_name='exchangerate',
            old_name='CUR_NM',
            new_name='cur_nm',
        ),
        migrations.RenameField(
            model_name='exchangerate',
            old_name='CUR_UNIT',
            new_name='cur_unit',
        ),
        migrations.RenameField(
            model_name='exchangerate',
            old_name='DEAL_BAS_R',
            new_name='deal_bas_r',
        ),
        migrations.RenameField(
            model_name='exchangerate',
            old_name='TTB',
            new_name='ttb',
        ),
        migrations.RenameField(
            model_name='exchangerate',
            old_name='TTS',
            new_name='tts',
        ),
    ]
