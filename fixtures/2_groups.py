from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

from apps.categories.models import Category
from apps.finances.models import Finance
from apps.users.models import User

permissions = []
simple_user_group = Group.objects.get_or_create(name="Simple user")[0]

# Category permissions
categtory_content_type = ContentType.objects.get_for_model(Category)
category_permissions = Permission.objects.filter(content_type=categtory_content_type)

# Finance permissions
finance_content_type = ContentType.objects.get_for_model(Finance)
finance_permissions = Permission.objects.filter(content_type=finance_content_type)

simple_user_group.permissions.clear()
simple_user_group.permissions.add(*category_permissions)
simple_user_group.permissions.add(*finance_permissions)


permission_user = User.objects.get(username="permission_user")
permission_user.groups.add(simple_user_group)
