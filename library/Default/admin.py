from django.contrib import admin

from .models import main_cat,category,author,book,status,details,contact,slider,testimonials
# Register your models here.


admin.site.register(main_cat)
admin.site.register(category)
admin.site.register(author)
admin.site.register(book)
admin.site.register(status)
admin.site.register(details)
admin.site.register(contact)
admin.site.register(slider)
admin.site.register(testimonials)

