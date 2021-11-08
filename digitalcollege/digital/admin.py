from django.contrib import admin
from digital import models

admin.site.register(models.StudentModel)
admin.site.register(models.DepartmentModel)
admin.site.register(models.YearModel)
admin.site.register(models.FacuiltyModel)
admin.site.register(models.OuNotesModel)

class PreviousAdmin(admin.ModelAdmin):
	prepopulated_field = {'slug':('paper_year','subject')}

admin.site.register(models.PreviousPapersModel,PreviousAdmin)
admin.site.register(models.GallaryModel)
admin.site.register(models.LibraryModel)
admin.site.register(models.TimeTableAndSyllabusModel)
admin.site.register(models.ResultModel)