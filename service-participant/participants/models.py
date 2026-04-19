from django.db import models

class Participant(models.Model):
    # Identifiant unique (peut être lié à un User plus tard)
    participant_id = models.CharField(max_length=100, unique=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    role = models.CharField(
        max_length=20,
        choices=[('viewer', 'Viewer'), ('editor', 'Editor'), ('admin', 'Admin')],
        default='viewer'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"

    class Meta:
        verbose_name = "Participant"
        verbose_name_plural = "Participants"