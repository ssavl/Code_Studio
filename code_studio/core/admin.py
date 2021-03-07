from django.contrib import admin
from .models import *
from django.shortcuts import redirect
# from reversion.admin import VersionAdmin




class MyCore(admin.ModelAdmin):

    Model = HomePage




    def response_add(self, request, obj, post_url_continue=None):
        return redirect('/admin')


    def response_change(self, request, obj):
        if '_save' in request.POST:
            return redirect('/admin')
        if '_continue' in request.POST:
            return redirect(f'/admin/core/homepage/{obj.id}/change/')


    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False





admin.site.register(HomePage, MyCore)
