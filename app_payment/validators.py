import re

from rest_framework.serializers import ValidationError
from django.utils.translation import gettext_lazy as _

VALID_LINK = ["youtube.com", "youtu.be"]


class VideoLinkValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        link = dict(value).get(self.field)
        if link:
            if not link.lstrip("https://www.").split("/")[0] in VALID_LINK:
                raise ValidationError(_("The link to the video should only be from Youtube"))


class MaterialsValidator:
    def __init__(self, *args):
        self.fields = args

    def __call__(self, value):
        val_dict = {field: dict(value).get(field) for field in self.fields}
        reg = re.compile('^(https?:\/\/)?'  # протокол
                         '([\w-]{1,32}\.[\w-]{1,32})'  # домен
                         '[^\s@]*'  # любой не пробельный символ + @
                         '$')
        for field, value in val_dict.items():
            for value in value.split():
                text = bool(reg.match(value))
                if text:
                    if not value.lstrip("https://www.").split("/")[0] in VALID_LINK:
                        raise ValidationError(f'Invalid link: "{value}" in the "{field}" field. '
                                              f'You can only post links to youtube.com')
