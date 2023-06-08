from django.contrib import admin
from .models import User,Userprofile,Employee,Department,Author,Book,Person



# Register your models here.
admin.site.register(User),
admin.site.register(Userprofile),
admin.site.register(Employee),
admin.site.register(Department),
admin.site.register(Book),
admin.site.register(Author),
admin.site.register(Person)