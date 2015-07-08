from django.contrib import admin
from .models import MonthlyPeriod, MonthlyTransaction


class MonthlyTransactionInline(admin.StackedInline):
    model = MonthlyTransaction
    extra = 0


class MonthlyPeriodAdmin(admin.ModelAdmin):
    inlines = (MonthlyTransactionInline, )


admin.site.register(MonthlyPeriod, MonthlyPeriodAdmin)