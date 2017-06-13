from django.contrib import admin

from .models import Board

class BoardAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,          {'fields' : ['title']}),
        ('contents',    {'fields' : ['contents']}),
        ('pub_date',    {'fields' : ['pub_date']}),
            ]
    
    def dave_model(self, request, obj, form, change):
        obj.author = request.user
        super(Board, self).save_model(request, obj, form, change)


# admin.site.register(Board, BoardAdmin)
admin.site.register(Board)
