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
