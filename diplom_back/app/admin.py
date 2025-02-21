from django.contrib import admin
from .models import Branch, Worker, Service, Customer, TimeOrder, Payment,Role, ServiceType

admin.site.register(Branch)
admin.site.register(Worker)
admin.site.register(Service)
admin.site.register(Customer)
admin.site.register(TimeOrder)
admin.site.register(Payment)
admin.site.register(Role)
admin.site.register(ServiceType)