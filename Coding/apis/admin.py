from django.contrib import admin
from .models import localityDescription


#admin.site.register(localityDescription)
'''class localityDescriptionAdmin(admin.ModelAdmin):
    pass
   
   
admin.site.register(localityDescription, localityDescriptionAdmin)'''

class localityDescriptionAdmin(admin.ModelAdmin):
    list_display = ('Id', 'MSSubClass', 'MSZoning', 'LotFrontage', 'LotArea', 'Street', 'Alley', 'LotShape', 'LandContour', 'Utilities', 'LotConfig', 'LandSlope', 'Neighborhood')
   
   
admin.site.register(localityDescription, localityDescriptionAdmin)
