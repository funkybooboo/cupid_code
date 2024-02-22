# Generated by Django 5.0.2 on 2024-02-22 01:24

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('role', models.CharField(choices=[('Dater', 'Dater'), ('Cupid', 'Cupid'), ('Manager', 'Manager')], max_length=7)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Gig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(0, 'Unclaimed'), (1, 'Claimed'), (2, 'Complete'), (3, 'Dropped')])),
                ('date_time_of_request', models.DateTimeField()),
                ('date_time_of_claim', models.DateTimeField(null=True)),
                ('date_time_of_completion', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Quest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('budget', models.DecimalField(decimal_places=2, max_digits=10)),
                ('items_requested', models.TextField()),
                ('pickup_location', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Cupid',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('accepting_gigs', models.BooleanField()),
                ('gigs_completed', models.IntegerField()),
                ('gigs_failed', models.IntegerField()),
                ('payment', models.TextField()),
                ('status', models.IntegerField(choices=[(0, 'Offline'), (1, 'Gigging'), (2, 'Available')])),
                ('cupid_cash_balance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('location', models.TextField()),
                ('average_rating', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Dater',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone_number', models.CharField(max_length=10)),
                ('budget', models.DecimalField(decimal_places=2, max_digits=10)),
                ('communication_preference', models.IntegerField(choices=[(0, 'Email'), (1, 'Text')])),
                ('description', models.TextField()),
                ('dating_strengths', models.TextField()),
                ('dating_weaknesses', models.TextField()),
                ('interests', models.TextField()),
                ('past', models.TextField()),
                ('nerd_type', models.TextField()),
                ('relationship_goals', models.TextField()),
                ('ai_degree', models.TextField()),
                ('cupid_cash_balance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('location', models.TextField()),
                ('average_rating', models.DecimalField(decimal_places=2, max_digits=10)),
                ('suspended', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='BankAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('routing_number', models.TextField()),
                ('account_number', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('star_rating', models.IntegerField()),
                ('date_time', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('gig', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.gig')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('from_ai', models.BooleanField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.TextField()),
                ('cvv', models.TextField()),
                ('expiration', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='gig',
            name='quest',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.quest'),
        ),
        migrations.AddField(
            model_name='gig',
            name='cupid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.cupid'),
        ),
        migrations.AddField(
            model_name='gig',
            name='dater',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.dater'),
        ),
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField()),
                ('location', models.TextField()),
                ('description', models.TextField()),
                ('status', models.TextField(choices=[('planned', 'Planned'), ('occuring', 'Occuring'), ('past', 'Past'), ('canceled', 'Canceled')])),
                ('budget', models.DecimalField(decimal_places=2, max_digits=10)),
                ('dater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.dater')),
            ],
        ),
    ]
