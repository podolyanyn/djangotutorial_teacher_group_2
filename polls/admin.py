from django.contrib import admin

from .models import Question, Choice



# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None, {"fields": ["question_text"]}),
#         ("Date information", {"fields": ["pub_date"]}),
#     ]
#
# admin.site.register(Question, QuestionAdmin)


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0


class QuestionAdmin(admin.ModelAdmin):
    list_display = ["question_text", "pub_date", "was_published_recently"]
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]
    inlines = [ChoiceInline]
    search_fields = ["question_text"]


admin.site.register(Question, QuestionAdmin)

# admin.site.register(Question)

admin.site.register(Choice)


