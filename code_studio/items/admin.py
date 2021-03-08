from django.contrib import admin
from .models import Item, Point
from django.utils.html import format_html
# from django.core.urlresolvers import reverse


class PointInline(admin.TabularInline):
    model = Point


class AccountAdmin(admin.ModelAdmin):


    Model = Item

    actions = ['mark_down', 'mark_up']

    def mark_down(self):
        pass

    def mark_up(self):
        pass

    mark_up.short_description = 'марк ап'
    mark_down.short_description = 'марк даун'

    inlines = [PointInline, ]
    fieldsets = (
        ('Основные данные', {
            'fields': ('name', 'slug')
        }),
        ('Дополнительные данные', {
            'fields': ('keywords_page', 'description_page', 'title_tag', 'img', 'created_at', 'title', 'title2',
                       'title3')
        }),
    )


    def change_button(self, obj):
        return format_html(f'<a class="btn" style="background-color: #4CAF50; border: none; color: white; '
                           f'padding: 7px 20px; text-align: center; text-decoration: none; display: inline-block; '
                           f'font-size: 14px; margin: 4px 2px; cursor: pointer;"  '
                           f'href="/admin/items/item/{obj.id}/change/">Изменить</a>')


    def delete_button(self, obj):
        return format_html(f'<a class="btn" style="background-color: #f44336; border: none; color: white; '
                           f'padding: 7px 20px; text-align: center; text-decoration: none; display: inline-block; '
                           f'font-size: 14px; margin: 4px 2px; cursor: pointer;"  '
                           f'href="/admin/items/item/{obj.id}/delete/">Удалить</a>')


    def point_button(self, obj):
        return format_html(f'<a class="btn" style="background-color: #008CBA; border: none; color: white; '
                           f'padding: 7px 20px; text-align: center; text-decoration: none; display: inline-block; '
                           f'font-size: 14px; margin: 4px 2px; cursor: pointer;"  '
                           f'href="/admin/items/point/add/">Добавить пункты</a>')

    list_display = ('name', '__str__', 'created_at', 'change_button', 'delete_button', 'point_button')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']


class MyPoint(admin.ModelAdmin):
    list_display = ['text', 'item', 'title_num']


admin.site.register(Item, AccountAdmin)
admin.site.register(Point, MyPoint)


