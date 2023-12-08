# Generated by Django 4.1.13 on 2023-12-08 15:27

import api.models.community
import api.models.projects
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_projects_given', models.IntegerField(default=0)),
                ('number_of_projects_completed', models.IntegerField(default=0)),
                ('rating', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('grp_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('grp_name', models.CharField(max_length=50)),
                ('created_at_date', models.CharField(default='8th December 2023', max_length=225, null=True)),
                ('created_at_time', models.CharField(default='8:57:00 pm', max_length=225, null=True)),
                ('grp_admin', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='admin', to=settings.AUTH_USER_MODEL)),
                ('grp_members', models.ManyToManyField(blank=True, default=None, null=True, related_name='members', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Milestone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('due_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('start_date', models.CharField(blank=True, default='8th December 2023 8:57:00 pm', max_length=255, null=True)),
                ('end_date', models.CharField(blank=True, default='8th December 2023 8:57:00 pm', max_length=255, null=True)),
                ('bid_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(default='Open', max_length=20)),
                ('project_doc', models.FileField(blank=True, null=True, upload_to=api.models.projects.__prd__file__path__)),
                ('Learning_resources', models.TextField(blank=True, default=None, null=True, verbose_name='Learning Resources')),
                ('related_techstacks', models.JSONField(blank=True, default=list, null=True)),
                ('project_timeline', models.JSONField(blank=True, default=None, null=True)),
                ('created_at', models.CharField(blank=True, default='8th December 2023 8:57:00 pm', editable=False, max_length=255, null=True)),
                ('updated_at', models.CharField(blank=True, default='8th December 2023 8:57:00 pm', editable=False, max_length=255, null=True)),
                ('chat_group_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.group')),
                ('created_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_projects', to='api.client')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectRequirementDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_overview', models.TextField()),
                ('original_requirements', models.TextField()),
                ('project_goals', models.TextField()),
                ('user_stories', models.TextField()),
                ('system_architecture', models.TextField()),
                ('tech_stacks', models.TextField()),
                ('requirement_pool', models.TextField()),
                ('ui_ux_design', models.TextField()),
                ('development_methodology', models.TextField()),
                ('security_measures', models.TextField()),
                ('testing_strategy', models.TextField()),
                ('scalability_and_performance', models.TextField()),
                ('deployment_plan', models.TextField()),
                ('maintenance_and_support', models.TextField()),
                ('risks_and_mitigations', models.TextField()),
                ('compliance_and_regulations', models.TextField()),
                ('budget_and_resources', models.TextField()),
                ('timeline_and_milestones', models.TextField()),
                ('communication_plan', models.TextField()),
                ('anything_unclear', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Talent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skills', models.JSONField(blank=True, default=list, null=True)),
                ('learning_resources', models.JSONField(blank=True, default=list, editable=False, null=True)),
                ('rating', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('no_projects_completed', models.IntegerField(default=0)),
                ('deadline_missed', models.IntegerField(default=0)),
                ('project_cancelled', models.IntegerField(default=0)),
                ('currently_working_on', models.ManyToManyField(blank=True, default=None, null=True, related_name='current_projects_of_talent', to='api.project')),
                ('user', models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='talent', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Workflow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.CharField(blank=True, default='8th December 2023 8:57:00 pm', editable=False, max_length=255, null=True)),
                ('updated_at', models.CharField(blank=True, default='8th December 2023 8:57:00 pm', editable=False, max_length=255, null=True)),
                ('created_by', models.ManyToManyField(null=True, related_name='created_teams', to='api.talent')),
                ('members', models.ManyToManyField(related_name='team_members', to='api.talent')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teams_project', to='api.project')),
                ('team_leader', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='team_leaders', to='api.talent')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectProgressReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
                ('project_completion_percentage', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('milestone_accomplished', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.milestone')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='progress_reports', to='api.project')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectMembers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('Member', 'Member'), ('Leader', 'Leader'), ('Mentor', 'Mentor'), ('Client', 'Client')], default='Member', max_length=20)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='api.project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='prd',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='PRD', to='api.projectrequirementdocument'),
        ),
        migrations.AddField(
            model_name='project',
            name='workflow',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='workflow', to='api.workflow'),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('images', models.JSONField(blank=True, default=list, editable=False, null=True)),
                ('date', models.CharField(blank=True, default='8th December 2023 8:57:00 pm', editable=False, max_length=255, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to=api.models.community.__post__path__)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skills', models.JSONField(blank=True, default=list, editable=False, null=True)),
                ('rating', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('no_projects_mentored', models.IntegerField(default=0)),
                ('currently_mentoring', models.ManyToManyField(null=True, related_name='current_projects_of_mentor', to='api.project')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='mentor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GroupMessage',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('message', models.TextField()),
                ('created_at_date', models.CharField(default='8th December 2023', max_length=225, null=True)),
                ('created_at_time', models.CharField(default='8:57:00 pm', max_length=225, null=True)),
                ('ai', models.BooleanField(blank=True, default=False, null=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.group')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='client',
            name='current_projects',
            field=models.ManyToManyField(blank=True, default=None, null=True, related_name='current_projects_of_client', to='api.project'),
        ),
        migrations.AddField(
            model_name='client',
            name='user',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='ChatMsg',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('message', models.TextField()),
                ('created_at_date', models.CharField(default='8th December 2023', max_length=225, null=True)),
                ('created_at_time', models.CharField(default='8:57:00 pm', max_length=225, null=True)),
                ('ai', models.BooleanField(blank=True, default=False, null=True)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_messages', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_messages', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
