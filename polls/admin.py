from django.contrib import admin

# Register your models here.
from .models import Question,Choice

admin.site.site_header = "Samuel's Appplication"
admin.site.site_title = "Samuel's Appplication Admin Area"
admin.site.index_title = "Welcome to my Application"

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 4

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None,{'fields':['question_text']}),
                 ("Date Information",{'fields':['pub_date'],'classes':['collapse']}),]
    inlines = [ChoiceInLine]

admin.site.register(Question,QuestionAdmin)
# admin.site.register(Question)
# admin.site.register(Choice)