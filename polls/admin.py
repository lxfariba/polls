from django.contrib import admin

from .models import Choice, Question


class ChoiceInline(admin.StackedInline):
	model = Choice
	extra = 3


class QuestionAdmin(admin.ModelAdmin):
	feildsets = [
	(None,             {'feilds':['question_text']}),
	('Dateinformation', {'feilds':['pub_date'], 'classes':['collapse']}),
	]
	inlines = [ChoiceInline]

	list_display = ('question_text','pub_date','was_published_recently')
	list_filter = ['pub_date']
	search_feilds = ['question_text']
	
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
