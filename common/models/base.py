from django.db import models


class Base(models.Model):
    is_active = models.BooleanField(default=True, db_default=True)
    
    
    class Meta:
        abstract = True