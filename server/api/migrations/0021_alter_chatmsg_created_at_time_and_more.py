# Generated by Django 4.2.6 on 2023-12-08 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_alter_chatmsg_created_at_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatmsg',
            name='created_at_time',
            field=models.CharField(default='7:52:02 pm', max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='created_at_time',
            field=models.CharField(default='7:52:02 pm', max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='groupmessage',
            name='created_at_time',
            field=models.CharField(default='7:52:02 pm', max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.CharField(blank=True, default='8th December 2023 7:52:02 pm', editable=False, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='created_at',
            field=models.CharField(blank=True, default='8th December 2023 7:52:02 pm', editable=False, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='end_date',
            field=models.CharField(blank=True, default='8th December 2023 7:52:02 pm', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.CharField(blank=True, default='8th December 2023 7:52:02 pm', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='updated_at',
            field=models.CharField(blank=True, default='8th December 2023 7:52:02 pm', editable=False, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='projectmembers',
            name='role',
            field=models.CharField(choices=[('Client', 'Client'), ('Leader', 'Leader'), ('Member', 'Member'), ('Mentor', 'Mentor')], default='Member', max_length=20),
        ),
        migrations.AlterField(
            model_name='team',
            name='created_at',
            field=models.CharField(blank=True, default='8th December 2023 7:52:02 pm', editable=False, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='updated_at',
            field=models.CharField(blank=True, default='8th December 2023 7:52:02 pm', editable=False, max_length=255, null=True),
        ),
    ]
