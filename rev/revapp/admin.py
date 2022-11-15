from django.contrib import admin
from .models import Command
from .models import User

admin.site.unregister(User)
admin.site.register(Command)
admin.site.register(User)



# from django.contrib.auth.models import Group, Permission
# from django.contrib.contenttypes.models import ContentType


# new_group, created = Group.objects.get_or_create(name='admin ')
# proj_add_perm = Permission.objects.get(name='Can add project')
# new_group.permissions.add(proj_add_perm)
#
# new_group, created = Group.objects.get_or_create(name='Standard User')
# proj_add_perm = Permission.objects.get(name='Can add project')
# new_group.permissions.add(proj_add_perm)
#
#
# new_group, created = Group.objects.get_or_create(name='Limited Access User')
# proj_add_perm = Permission.objects.get(name='Can add project')
# new_group.permissions.add(proj_add_perm)
#
#
# new_group, created = Group.objects.get_or_create(name='Super admin')
# proj_add_perm = Permission.objects.get(name='Can add project')
# new_group.permissions.add(proj_add_perm)

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import User


new_group, created = Group.objects.get_or_create(name='Super admin')
proj_add_perm = Permission.objects.get(name='Can add project')
new_group.permissions.add(proj_add_perm)

new_group, created = Group.objects.get_or_create(name='Limited Access User')
proj_add_perm = Permission.objects.get(name='Can add project')
new_group.permissions.add(proj_add_perm)

new_group, created = Group.objects.get_or_create(name='Standard User')
proj_add_perm = Permission.objects.get(name='Can add project')
new_group.permissions.add(proj_add_perm)



new_group, created = Group.objects.get_or_create(name='admin ')
proj_add_perm = Permission.objects.get(name='Can add project')
new_group.permissions.add(proj_add_perm)


