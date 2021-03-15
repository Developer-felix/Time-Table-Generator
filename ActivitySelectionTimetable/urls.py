
from django.contrib import admin
from django.urls import path, include
import ActivitySelectionTimetable.settings
admin.site.site_header = "Timetable generator"

urlpatterns = [
    path('admin/', admin.site.urls),
   #main app
    path('', include('timetableapp.urls')),


]
