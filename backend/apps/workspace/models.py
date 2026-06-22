from django.db import models

# Create your models here.
class Workspace(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    description = models.TextField(blank=True, null=True)
    timezone = models.CharField(max_length=50, default='UTC')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class WorkspaceMember(models.Model):
    ROLE_CHOICES = [
        ('ADMIN', 'Admin'),
        ('OWNER', 'Owner'),
        ('MEMBER', 'Member'),
        ('GUEST', 'Guest'),    
    ]
    
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE, related_name='members')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='MEMBER')
    joined_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['workspace', 'user'], name='unique_workspace_member')
        ]
        
    def __str__(self):
        return f"{self.user.username} - {self.workspace.name}"
    
class Channel(models.Model):

    CHANNEL_TYPES = [
        ("PUBLIC", "Public"),
        ("PRIVATE", "Private"),
    ]

    workspace = models.ForeignKey(
        Workspace,
        on_delete=models.CASCADE,
        related_name="channels"
    )

    created_by = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE
    )

    name = models.CharField(
        max_length=100
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    channel_type = models.CharField(
        max_length=20,
        choices=CHANNEL_TYPES,
        default="PUBLIC"
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["workspace", "name"],
                name="unique_channel_per_workspace"
            )
        ]

    def __str__(self):
        return self.name