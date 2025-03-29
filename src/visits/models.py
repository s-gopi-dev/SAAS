from django.db import models

# Create your models here.
class PageVisit(models.Model):
    """
    Model to track page visits.
    """
    # Fields to store information about the page visit
    page_url = models.CharField(max_length=255)
    path = models.CharField(max_length=255, null=True, blank=True)
    visit_time = models.DateTimeField(auto_now_add=True)
    user_ip = models.GenericIPAddressField(null=True, blank=True)

    # def __str__(self):
    #     return f"PageVisit(page_url={self.page_url},PageVisit(page_url={self.path}, visit_time={self.visit_time}, user_ip={self.user_ip})"