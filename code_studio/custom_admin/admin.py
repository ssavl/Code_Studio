from django.contrib.admin import AdminSite
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.conf.urls import url
from items.forms import ItemForm
from items.models import Item, Point


class MyAdminSite(AdminSite):

    def get_urls(self):
        additional_urls = [
            # url(r'^items/item/add/$', self.admin_view(self.my_view))
            url(r'^items/item/(?P<id>\d+)/change/$', self.admin_view(self.my_edit_view))
        ]
        return additional_urls + super().get_urls()


    def my_view(self, request):
        PointFormSet = inlineformset_factory(Item, Point, fields=('text',))
        item = ItemForm()
        formset = PointFormSet(instance=item)

        return render(request, 'admin/item_form.html', {'formset': formset})


    def my_edit_view(self, request, id):
        PointFormSet = inlineformset_factory(Item, Point, fields=('text', ))
        item = Item.objects.get(id=id)
        formset = PointFormSet(instance=item)

        return render(request, 'admin/item_form.html', {'formset': formset})


admin_site = MyAdminSite()
