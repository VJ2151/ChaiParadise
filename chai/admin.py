from django.contrib import admin


# Register your models here.



from .models import ChaiVariety, ChaiReview

class ChaiReviewInline(admin.TabularInline):
    model = ChaiReview
    extra = 2

class ChaiVarietyAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date_added')
    inlines = [ChaiReviewInline]

admin.site.register(ChaiVariety, ChaiVarietyAdmin)