from django.contrib import admin
from issues import models as im


class IssueAdmin(admin.ModelAdmin):
    list_filter = ('milestone', 'submitter', 'labels')
    list_display = ['number', 'title', 'is_closed', 'creation_date']


class MilestoneAdmin(admin.ModelAdmin):
    list_filter = ('is_open', 'target_date')
    list_display = ['name', 'is_open', 'target_date', 'last_updated']


admin.site.register(im.Issue, IssueAdmin)
admin.site.register(im.Milestone, MilestoneAdmin)
