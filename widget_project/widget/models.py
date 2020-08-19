from django.db import models

# Create your models here.
class Widget(models.Model):
    name = models.CharField(blank=False, max_length=50)
    description = models.CharField(blank=False, max_length=1000, default='')
    

    class Meta:
        verbose_name = "Widget"
        verbose_name_plural = "Widgets"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Widget_detail", kwargs={"pk": self.pk})
