# Generated by Django 4.1.13 on 2023-12-09 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="chatmsg",
            name="created_at_date",
            field=models.CharField(
                default="9th December 2023", max_length=225, null=True
            ),
        ),
        migrations.AlterField(
            model_name="chatmsg",
            name="created_at_time",
            field=models.CharField(default="09:32:34 am", max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name="group",
            name="created_at_date",
            field=models.CharField(
                default="9th December 2023", max_length=225, null=True
            ),
        ),
        migrations.AlterField(
            model_name="group",
            name="created_at_time",
            field=models.CharField(default="09:32:34 am", max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name="groupmessage",
            name="created_at_date",
            field=models.CharField(
                default="9th December 2023", max_length=225, null=True
            ),
        ),
        migrations.AlterField(
            model_name="groupmessage",
            name="created_at_time",
            field=models.CharField(default="09:32:34 am", max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name="post",
            name="date",
            field=models.CharField(
                blank=True,
                default="9th December 2023 09:32:34 am",
                editable=False,
                max_length=255,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="created_at",
            field=models.CharField(
                blank=True,
                default="9th December 2023 09:32:34 am",
                editable=False,
                max_length=255,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="end_date",
            field=models.CharField(
                blank=True,
                default="9th December 2023 09:32:34 am",
                max_length=255,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="start_date",
            field=models.CharField(
                blank=True,
                default="9th December 2023 09:32:34 am",
                max_length=255,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="updated_at",
            field=models.CharField(
                blank=True,
                default="9th December 2023 09:32:34 am",
                editable=False,
                max_length=255,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="projectmembers",
            name="role",
            field=models.CharField(
                choices=[
                    ("Leader", "Leader"),
                    ("Client", "Client"),
                    ("Mentor", "Mentor"),
                    ("Member", "Member"),
                ],
                default="Member",
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="team",
            name="created_at",
            field=models.CharField(
                blank=True,
                default="9th December 2023 09:32:34 am",
                editable=False,
                max_length=255,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="team",
            name="updated_at",
            field=models.CharField(
                blank=True,
                default="9th December 2023 09:32:34 am",
                editable=False,
                max_length=255,
                null=True,
            ),
        ),
    ]
