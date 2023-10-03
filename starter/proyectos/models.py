# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ProyectosProyectos(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre_proyecto = models.CharField(max_length=30, blank=True, null=True)
    dia_final = models.DateField(blank=True, null=True)
    prioridad = models.CharField(max_length=4)
    dni_usuario = models.CharField(max_length=9)
    grupo = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = ' proyectos_proyectos'


class ProyectosProyectosOld(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre_proyecto = models.CharField(max_length=30, blank=True, null=True)
    dia_final = models.DateField(blank=True, null=True)
    prioridad = models.CharField(max_length=4)
    dni_usuario = models.CharField(max_length=9)
    grupo = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = ' proyectos_proyectos_old'


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)
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


class ProyectosTareas(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre_tarea = models.CharField(max_length=30, blank=True, null=True)
    hora_inicio = models.TimeField(blank=True, null=True)
    hora_final = models.TimeField(blank=True, null=True)
    des2 = models.CharField(max_length=8, blank=True, null=True)
    des1 = models.CharField(max_length=8, blank=True, null=True)
    id_proyecto = models.ForeignKey(ProyectosProyectos, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'proyectos_tareas'


class ProyectosTareasOld(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre_tarea = models.CharField(max_length=30, blank=True, null=True)
    hora_inicio = models.TimeField(blank=True, null=True)
    hora_final = models.TimeField(blank=True, null=True)
    des2 = models.CharField(max_length=8, blank=True, null=True)
    des1 = models.CharField(max_length=8, blank=True, null=True)
    id_proyecto_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'proyectos_tareas_old'


# from django.db import models

# # Create your models here.

# class Proyectos(models.Model):
#     # id = models.IntegerField(max_length=30)
#     nombre_proyecto = models.CharField(max_length=30)
#     dia_final = models.DateField()
#     prioridad = models.BooleanField()
#     dni_usuario = models.CharField(max_length=9)
#     grupo = models.CharField(max_length=30, blank=True)

#     class Meta:
#         verbose_name_plural = 'Proyectos'
#         verbose_name = 'Proyecto'

#     def get_absolute_url(self):
#      return reverse('proyectos:detail', kwargs={'pk': self.pk})

#     def __str__(self):
#         return self.nombre_proyecto


# class Tareas(models.Model):
#     # id = models.IntegerField(max_length=30)
#     nombre_tarea = models.CharField(max_length=30)
#     hora_inicio = models.DateField(blank=True)
#     hora_final = models.DateField(blank=True)
#     des2 = models.CharField(max_length=8, blank=True)
#     des1 = models.CharField(max_length=8, blank=True)
#    # id_proyecto = models.IntegerField(unique=False)
#     id_proyecto = models.ForeignKey(Proyectos, on_delete=models.CASCADE, unique=False, blank=True, null=True)

#     class Meta:
#         verbose_name_plural = 'Tareas'
#         verbose_name = 'Tarea'
    
#     def get_absolute_url(self):
#      return reverse('tareas:detail', kwargs={'pk': self.pk})

#     def __str__(self):
#         return self.nombre_tarea
