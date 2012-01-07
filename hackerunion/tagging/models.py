import re
from django.core.exceptions import ValidationError
from django.db import models


class Tag(models.Model):
    VALID_NAME_REGEX = re.compile(r'[a-z0-9\+-]')
    
    name = models.CharField(max_length=32)
    
    def clean(self):
        for ch in self.name:
            if not Tag.VALID_NAME_REGEX.match(ch):
                raise ValidationError('Tag names may only contain letters,' +
                                      'numbers, dashes, and plus signs.')
    
    def __unicode__(self):
        return self.name
