# Generated by Django 3.2.12 on 2022-04-22 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hagelandse101', '0003_auto_20220418_1158'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DatacollectorEdition',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'dataCollector_edition',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DatacollectorParticipation',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('ticket_id', models.CharField(max_length=30)),
                ('qr_code', models.CharField(max_length=20)),
                ('number', models.IntegerField()),
                ('bagage_service', models.IntegerField()),
            ],
            options={
                'db_table': 'dataCollector_participation',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DatacollectorPerson',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
                ('telephone_number', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'dataCollector_person',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DatacollectorPosition',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('time', models.DateTimeField()),
                ('latitude', models.FloatField()),
                ('deviation', models.FloatField()),
                ('distance', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
            options={
                'db_table': 'dataCollector_position',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DatacollectorTshirt',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('size', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'dataCollector_tshirt',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.RemoveField(
            model_name='badge',
            name='Editie',
        ),
        migrations.RemoveField(
            model_name='badge_toekenning',
            name='Badge',
        ),
        migrations.RemoveField(
            model_name='badge_toekenning',
            name='Deelname',
        ),
        migrations.RemoveField(
            model_name='controlepunt',
            name='Editie',
        ),
        migrations.RemoveField(
            model_name='deelname',
            name='Deelnemer',
        ),
        migrations.RemoveField(
            model_name='deelname',
            name='Editie',
        ),
        migrations.RemoveField(
            model_name='passage',
            name='Controlepunt',
        ),
        migrations.RemoveField(
            model_name='passage',
            name='Deelname',
        ),
        migrations.DeleteModel(
            name='Route',
        ),
        migrations.DeleteModel(
            name='TShirt',
        ),
        migrations.DeleteModel(
            name='Badge',
        ),
        migrations.DeleteModel(
            name='Badge_toekenning',
        ),
        migrations.DeleteModel(
            name='Controlepunt',
        ),
        migrations.DeleteModel(
            name='Deelname',
        ),
        migrations.DeleteModel(
            name='Deelnemer',
        ),
        migrations.DeleteModel(
            name='Editie',
        ),
        migrations.DeleteModel(
            name='Passage',
        ),
    ]