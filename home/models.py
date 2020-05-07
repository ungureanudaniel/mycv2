from django.db import models
from wagtail_resume.models import BaseResumePage
from wagtail.core.models import Page


class HomePage(Page):
    pass

# home/models.py

class ResumePage(BaseResumePage):
    pass
