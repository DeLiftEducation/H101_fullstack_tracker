from django.db import models

# Create your models here.
from rest_framework import serializers


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DatacollectorEdition(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField()
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'dataCollector_edition'


class DatacollectorParticipation(models.Model):
    id = models.BigAutoField(primary_key=True)
    ticket_id = models.CharField(max_length=30)
    qr_code = models.CharField(max_length=20)
    number = models.IntegerField()
    bagage_service = models.IntegerField()
    edition = models.ForeignKey(DatacollectorEdition, models.DO_NOTHING)
    person = models.ForeignKey('DatacollectorPerson', models.DO_NOTHING)
    t_shirt = models.ForeignKey('DatacollectorTshirt', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dataCollector_participation'


class DatacollectorPerson(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    birth_date = models.DateField()
    telephone_number = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'dataCollector_person'


class DatacollectorPosition(models.Model):
    id = models.BigAutoField(primary_key=True)
    time = models.DateTimeField()
    latitude = models.FloatField()
    deviation = models.FloatField()
    distance = models.FloatField()
    longitude = models.FloatField()
    participation = models.ForeignKey(DatacollectorParticipation, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'dataCollector_position'


class DatacollectorTshirt(models.Model):
    id = models.BigAutoField(primary_key=True)
    size = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'dataCollector_tshirt'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
