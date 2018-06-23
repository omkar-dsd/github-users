import datetime
from .models import *
from django.contrib import admin
from django.db.models import Count


class UserAdmin(admin.ModelAdmin):
    '''To provide a proper display of user information in Admin panel'''

    list_display = ('login', 'user_thumbnail', 'name',
                    'email', 'company', 'location')
    search_fields = ('login', 'name', 'email', 'company', 'location')


admin.site.register(User, UserAdmin)


@admin.register(RequestSummary)
class SummaryAdmin(admin.ModelAdmin):
    '''Connects to the Summary Section in Admin Panel'''

    change_list_template = 'admin/request_summary_change_list.html'

    def changelist_view(self, request, extra_context=None):
        '''Template handler for summary view'''
        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )

        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response

        # Generate required dates for filter
        today = datetime.date.today()
        week = today - datetime.timedelta(days=7)
        string_date = datetime.datetime.strftime(today, '%Y%m%d')
        dom = int(string_date[-2:])
        month = datetime.date.today() - datetime.timedelta(days=dom)
        summary_list = []

        # Generating response summart list
        summary_list.append({'timestamp': 'Today', 'user_count': qs.filter(created_at__gt=today).count(
        ), 'request_count': Request.objects.filter(created_at__gt=today).count()})
        summary_list.append({'timestamp': 'Week', 'user_count': qs.filter(created_at__gt=week).count(
        ), 'request_count': Request.objects.filter(created_at__gt=week).count()})
        summary_list.append({'timestamp': 'Month', 'user_count': qs.filter(created_at__gt=month).count(
        ), 'request_count': Request.objects.filter(created_at__gt=month).count()})
        response.context_data['summary'] = summary_list

        return response
