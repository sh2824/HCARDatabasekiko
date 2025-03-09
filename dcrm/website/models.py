from django.db import models
import time

from django.db import models
import uuid

class Artist(models.Model):
    artist_id = models.CharField(primary_key=True, max_length=5, unique=True, default='AH001')  # Default to 'AH001'
    artist_lname = models.CharField(max_length=50, blank=True, null=True)
    artist_fname = models.CharField(max_length=50, blank=True, null=True)
    artist_site = models.CharField(max_length=100, blank=True, null=True)
    artist_email = models.CharField(max_length=100, blank=True, null=True)
    artist_bio = models.CharField(max_length=800, blank=True, null=True)
    artist_phone = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'artist'

    def save(self, *args, **kwargs):
        if not self.artist_id:  # Check if artist_id is not set
            # Example of default format using initials + number, here you can use your custom logic
            self.artist_id = f'{self.artist_fname[:2].upper()}{str(Artist.objects.count() + 1).zfill(3)}'
        super().save(*args, **kwargs)



class Storage(models.Model):
    storage_id = models.CharField(primary_key=True, max_length=7)
    storage_loc = models.CharField(max_length=40, blank=True, null=True)
    storage_type = models.CharField(max_length=20, blank=True, null=True)
    storage_city = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'storage'


class Artwork(models.Model):
    art_num = models.CharField(primary_key=True, max_length=8)
    art_title = models.CharField(max_length=50, blank=True, null=True)
    creation_date = models.DateField(blank=True, null=True)
    art_medium = models.CharField(max_length=50, blank=True, null=True)
    is_sold = models.CharField(max_length=1, blank=True, null=True)
    art_size = models.CharField(max_length=50, blank=True, null=True)
    artist = models.ForeignKey(Artist, models.DO_NOTHING, blank=False, null=False)
    storage = models.ForeignKey(Storage, models.DO_NOTHING, blank=False, null=False)
    # picture = models.ImageField(name=str(time.time()), upload_to="media/")

    class Meta:
        managed = True
        db_table = 'artwork'


class FlatFile(models.Model):
    file = models.OneToOneField('Storage', models.DO_NOTHING, primary_key=True)
    letter_code = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'flat_file'


class Rack(models.Model):
    rack = models.OneToOneField('Storage', models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = True
        db_table = 'rack'


class Sale(models.Model):
    sale_id = models.CharField(primary_key=True, max_length=7)
    art_num = models.ForeignKey(Artwork, models.DO_NOTHING, db_column='art_num', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sale'

class WallSpace(models.Model):
    wall = models.OneToOneField(Storage, models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = True
        db_table = 'wall_space'


# ------------------

# class AuthGroup(models.Model):
#     name = models.CharField(unique=True, max_length=150)
#
#     class Meta:
#         managed = True
#         db_table = 'auth_group'
#
#
# class AuthGroupPermissions(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#     permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)
#
#     class Meta:
#         managed = True
#         db_table = 'auth_group_permissions'
#         unique_together = (('group', 'permission'),)
#
#
# class AuthPermission(models.Model):
#     name = models.CharField(max_length=255)
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
#     codename = models.CharField(max_length=100)
#
#     class Meta:
#         managed = True
#         db_table = 'auth_permission'
#         unique_together = (('content_type', 'codename'),)
#
#
# class AuthUser(models.Model):
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField(blank=True, null=True)
#     is_superuser = models.IntegerField()
#     username = models.CharField(unique=True, max_length=150)
#     first_name = models.CharField(max_length=150)
#     last_name = models.CharField(max_length=150)
#     email = models.CharField(max_length=254)
#     is_staff = models.IntegerField()
#     is_active = models.IntegerField()
#     date_joined = models.DateTimeField()
#
#     class Meta:
#         managed = True
#         db_table = 'auth_user'
#
#
# class AuthUserGroups(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#
#     class Meta:
#         managed = True
#         db_table = 'auth_user_groups'
#         unique_together = (('user', 'group'),)
#
#
# class AuthUserUserPermissions(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)
#
#     class Meta:
#         managed = True
#         db_table = 'auth_user_user_permissions'
#         unique_together = (('user', 'permission'),)
#
#
# class DjangoAdminLog(models.Model):
#     action_time = models.DateTimeField()
#     object_id = models.TextField(blank=True, null=True)
#     object_repr = models.CharField(max_length=200)
#     action_flag = models.PositiveSmallIntegerField()
#     change_message = models.TextField()
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#
#     class Meta:
#         managed = True
#         db_table = 'django_admin_log'
#
#
# class DjangoContentType(models.Model):
#     app_label = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)
#
#     class Meta:
#         managed = True
#         db_table = 'django_content_type'
#         unique_together = (('app_label', 'model'),)
#
#
# class DjangoMigrations(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()
#
#     class Meta:
#         managed = True
#         db_table = 'django_migrations'
#
#
# class DjangoSession(models.Model):
#     session_key = models.CharField(primary_key=True, max_length=40)
#     session_data = models.TextField()
#     expire_date = models.DateTimeField()
#
#     class Meta:
#         managed = True
#         db_table = 'django_session'

