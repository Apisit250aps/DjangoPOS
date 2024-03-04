from django.db import models

# Create your models here.


class ProductType(models.Model):
    code = models.CharField(max_length=4, unique=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ProductCategory(models.Model):
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    code = models.CharField(max_length=4, unique=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class AreaData(models.Model):
    code = models.CharField(max_length=4, unique=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ShoData(models.Model):
    code = models.CharField(max_length=8, unique=True)
    name = models.CharField(max_length=255)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    # Address
    contact = models.CharField(max_length=255)
    address = models.TextField()
    sub_district = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    province = models.CharField(max_length=255)
    zip = models.CharField(max_length=5)
    area = models.ForeignKey(AreaData, on_delete=models.CASCADE)
    # Contact
    tel = models.CharField(max_length=10, null=True)
    fax = models.CharField(max_length=10, null=True)
    email = models.EmailField()
    remark = models.TextField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ProductData(models.Model):
    code = models.CharField(max_length=8, unique=True)
    name = models.CharField(max_length=255)
    unit_cost = models.DecimalField(max_digits=10, decimal_places=2)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    description = models.TextField()
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    shop = models.ForeignKey(ShoData, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ProductDelete(models.Model):
    product = models.ForeignKey(ProductData, on_delete=models.CASCADE)
    del_unit = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.name


class CustomerData(models.Model):
    code = models.CharField(max_length=8, unique=True)
    name = models.CharField(max_length=255)

    address = models.TextField()
    sub_district = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    province = models.CharField(max_length=255)
    zip = models.CharField(max_length=5)

    tel = models.CharField(max_length=10, null=True)
    fax = models.CharField(max_length=10, null=True)
    email = models.EmailField()
    remark = models.TextField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class InputInvoice(models.Model):
    no = models.CharField(max_length=12, unique=True)
    shop = models.ForeignKey(ShoData, on_delete=models.CASCADE)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    remark = models.TextField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.no


class InputData(models.Model):
    invoice_no = models.ForeignKey(InputInvoice, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductData,  on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.product.name


class OutputInvoice(models.Model):
    no = models.CharField(max_length=12, unique=True)
    customer = models.ForeignKey(CustomerData, on_delete=models.CASCADE)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    remark = models.TextField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.no


class OutputData(models.Model):
    invoice_no = models.ForeignKey(OutputInvoice, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductData,  on_delete=models.CASCADE)
    quantity = models.IntegerField()
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.product.name
