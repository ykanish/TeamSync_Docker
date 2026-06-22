from django.contrib import admin

# Register your models here.
from .models import Workspace, WorkspaceMember, Channel

admin.site.register(Workspace)
admin.site.register(WorkspaceMember)
admin.site.register(Channel)