from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ServiceTrackRequests(models.Model):
    REQUEST_TYPES= [
        ('Gas Leak', 'Gas Leak'),
        ('Gas Pipe Repair', 'Gas Pipe Repair'),
        ('New Connection', 'New Connection'),
        ('Billing Issue', 'Billing Issue'),
        ('Other', 'Other'),
    ]

    STATUS_STATE = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

    SEVERITY_LEVEL = [
        (1, 'High Priority'),
        (2, 'Medium Priority'),
        (3, 'Low Priority'),
    ]

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    req_type = models.CharField(max_length=50, choices=REQUEST_TYPES)
    desc = models.TextField()
    attachment = models.FileField(upload_to='attachments/', null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUS_STATE, default='Pending')
    severity = models.PositiveSmallIntegerField(choices=SEVERITY_LEVEL, default=3)
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.req_type} - {self.customer.username} (Created At: {self.created_at.astimezone().strftime('%Y-%m-%d %H:%M:%S')}) (Severity: {self.severity}) - {self.status}"
    
class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField()
    phone_num = models.CharField(max_length=15)