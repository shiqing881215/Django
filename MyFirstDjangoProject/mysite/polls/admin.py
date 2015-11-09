#
# This is the major file to config admin page
#

from django.contrib import admin

from .models import Choice, Question

# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

# Custom option, put pub_date before question_text
class QuestionAdmin(admin.ModelAdmin):
    # Fields we want to display in the question detail page
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    # Columns we want to display in the question list
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    # Add search box
    search_fields = ['question_text']

# This will show the Question on the amdin page
admin.site.register(Question, QuestionAdmin)