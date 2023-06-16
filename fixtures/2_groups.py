from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

from apps.categories.models import Category
from apps.users.models import User

simple_user_group = Group.objects.get_or_create(name="Simple user")[0]

categtory_content_type = ContentType.objects.get_for_model(Category)
category_permissions = Permission.objects.filter(content_type=categtory_content_type)

simple_user_group.permissions.set(category_permissions)

permission_user = User.objects.get(username="permission_user")
permission_user.groups.add(simple_user_group)
