from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

def StringWithoutSlashValidator(value):
    if '/' in value:
        raise ValidationError(
            _('%(value)s no puede contener "/"'),
            params={'value': value},
        )