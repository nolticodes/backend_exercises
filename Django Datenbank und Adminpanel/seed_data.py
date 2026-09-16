from decimal import Decimal

from django.db import transaction
from sales.models import Bill, Customer, Order, Product, Producttype


with transaction.atomic():
    customer1 = Customer.objects.create(
        first_name="John",
        last_name="Doe",
        newsletter_abo=True,
        email_adress="john.doe@example.com",
        account=Decimal("100.00"),
    )

    customer2 = Customer.objects.create(
        first_name="Jane",
        last_name="Smith",
        newsletter_abo=False,
        email_adress="jane.smith@example.com",
        account=Decimal("200.00"),
    )

    customer3 = Customer.objects.create(
        first_name="Alice",
        last_name="Johnson",
        newsletter_abo=True,
        email_adress="alice.johnson@example.com",
        account=Decimal("300.00"),
    )

    product1 = Product.objects.create(
        name="Product A",
        price=Decimal("10.00"),
    )

    product2 = Product.objects.create(
        name="Product B",
        price=Decimal("20.00"),
    )

    product3 = Product.objects.create(
        name="Product C",
        price=Decimal("30.00"),
    )

    bill1 = Bill.objects.create(
        total_amount=Decimal("50.00"),
        is_paid=False,
    )

    bill2 = Bill.objects.create(
        total_amount=Decimal("100.00"),
        is_paid=True,
    )

    bill3 = Bill.objects.create(
        total_amount=Decimal("150.00"),
        is_paid=False,
    )

    order1 = Order.objects.create(
        customer=customer1,
        bill=bill1,
    )

    order2 = Order.objects.create(
        customer=customer2,
        bill=bill2,
    )

    order3 = Order.objects.create(
        customer=customer3,
        bill=bill3,
    )

    product_types = [
        (order1, product1, "Wood"),
        (order1, product2, "Iron"),
        (order2, product1, "Wood"),
        (order2, product3, "Plastic"),
        (order3, product1, "Wood"),
        (order3, product2, "Iron"),
        (order3, product3, "Plastic"),
    ]

    for order, product, type_name in product_types:
        Producttype.objects.create(
            order=order,
            product=product,
            type_name=type_name,
        )

print("Testdaten wurden erfolgreich erstellt.")