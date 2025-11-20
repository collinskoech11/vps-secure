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
            user.is_superuser = True
            user.save()
            req.status = 'approved'
            req.save()
    approve_requests.short_description = 'Approve selected requests and make superuser'

    def save_model(self, request, obj, form, change):
        if obj.status == 'approved':
            user = obj.user
            user.is_staff = True
            user.is_superuser = True
            user.save()
        super().save_model(request, obj, form, change)

admin.site.register(Profile)
admin.site.register(Request, RequestAdmin)
