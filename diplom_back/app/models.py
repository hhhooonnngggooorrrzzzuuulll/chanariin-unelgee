from django.db import models

# 1. Салбар (Branch)
class Branch(models.Model):
    name = models.CharField(max_length=255, verbose_name="Салбарын нэр")
    location = models.CharField(max_length=255, verbose_name="Салбарын байршил")

    def __str__(self):
        return self.name

# 2. Албан тушаал (Role)
class Role(models.Model):
    name = models.CharField(max_length=255, verbose_name="Албан тушаалын нэр", unique=True)

    def __str__(self):
        return self.name

# 3. Ажилтан (Worker)
class Worker(models.Model):
    first_name = models.CharField(max_length=255, verbose_name="Овог")
    last_name = models.CharField(max_length=255, verbose_name="Нэр")
    phone = models.CharField(max_length=20, verbose_name="Утасны дугаар")
    role = models.ForeignKey(Role, on_delete=models.CASCADE, verbose_name="Албан тушаал")
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, verbose_name="Салбар")

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

# 4. Үйлчилгээний төрөл (ServiceType)
class ServiceType(models.Model):
    name = models.CharField(max_length=255, verbose_name="Үйлчилгээний төрөл", unique=True)

    def __str__(self):
        return self.name

# 5. Үйлчилгээ (Service)
class Service(models.Model):
    name = models.CharField(max_length=255, verbose_name="Үйлчилгээний нэр")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Үнэ")
    duration = models.IntegerField(verbose_name="Үргэлжлэх хугацаа (минут)")
    service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE, verbose_name="Үйлчилгээний төрөл")

    def __str__(self):
        return self.name

# 6. Хэрэглэгч (Customer)
class Customer(models.Model):
    name = models.CharField(max_length=255, verbose_name="Хэрэглэгчийн нэр")
    phone = models.CharField(max_length=20, verbose_name="Утасны дугаар")
    email = models.EmailField(verbose_name="Цахим шуудан", unique=True)

    def __str__(self):
        return self.name

# 7. Цаг захиалга (TimeOrder)
class TimeOrder(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Хүлээгдэж буй'),
        ('confirmed', 'Баталгаажсан'),
        ('cancelled', 'Цуцлагдсан'),
    ]
    
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name="Хэрэглэгч")
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, verbose_name="Салбар")
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, verbose_name="Ажилтан")
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name="Үйлчилгээ")
    date = models.DateField(verbose_name="Огноо")
    time = models.TimeField(verbose_name="Цаг")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name="Төлөв")

    def __str__(self):
        return f"{self.customer.name} - {self.date} {self.time}"

# 8. Төлбөр (Payment)
class Payment(models.Model):
    PAYMENT_METHODS = [
        ('cash', 'Бэлэн'),
        ('card', 'Карт'),
        ('online', 'Онлайн'),
    ]

    time_order = models.ForeignKey(TimeOrder, on_delete=models.CASCADE, verbose_name="Цаг захиалга")
    payment_type = models.CharField(max_length=50, choices=PAYMENT_METHODS, verbose_name="Төлбөрийн төрөл")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Төлбөрийн дүн")
    payment_date = models.DateTimeField(auto_now_add=True, verbose_name="Төлбөрийн огноо")

    def __str__(self):
        return f"{self.time_order.customer.name} - {self.amount}₮"
