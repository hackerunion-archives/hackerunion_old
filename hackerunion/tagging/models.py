import re
from django.core.exceptions import ValidationError
from django.db import models


def legal_tag_name(name):
    VALID_NAME_REGEX = re.compile(r'[a-z0-9\+-]')
    for ch in name:
        if not VALID_NAME_REGEX.match(ch):
            raise ValidationError('Tag names may only contain letters, '
                                  'numbers, dashes, and plus signs.')


class Tag(models.Model):
    name = models.CharField(max_length=32, validators=[legal_tag_name])
    
    def __unicode__(self):
        return self.name
