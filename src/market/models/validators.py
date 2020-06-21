from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

def StringWithoutSlashValidator(value):
    if '/' in value:
        raise ValidationError(
            _('%(value)s no puede contener "/"'),
            params={'value': value},
        )

def DiscountValidator(value):
    if (value % 5) == 0:
        is_ok = True
    elif (value % 33) == 0:
        is_ok = True
    else:
        is_ok = False

    if not is_ok:
        raise ValidationError(
            _('\'%(value)s\' no esta permitido. Por favor ingrese multiplo de 5 o 33.'),
            params={'value': value},
        )