from django.db import models


class STVTERM(models.Model):
    stvterm_code = models.CharField(max_length=6, primary_key=True)
    stvterm_desc = models.CharField(max_length=30)
