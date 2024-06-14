from django.contrib import admin
from .models import YogaPath, Yogasana
from .models import YogaPath, Yogasana, YogaPathAssociation

class YogaPathAssociationInline(admin.TabularInline):
    model = YogaPathAssociation
    extra = 1  # Number of extra inline forms to display

class YogaPathAdmin(admin.ModelAdmin):
    inlines = (YogaPathAssociationInline,)

admin.site.register(YogaPath, YogaPathAdmin)
admin.site.register(Yogasana)
admin.site.register(YogaPathAssociation)
