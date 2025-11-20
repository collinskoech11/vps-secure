from django.contrib import admin
from .models import Profile, Request

class RequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'status')
    list_filter = ('status',)
    actions = ['approve_requests']

    def approve_requests(self, request, queryset):
        for req in queryset:
            user = req.user
            user.is_staff = True
            user.save()
            req.status = 'approved'
            req.save()
    approve_requests.short_description = 'Approve selected requests'

admin.site.register(Profile)
admin.site.register(Request, RequestAdmin)