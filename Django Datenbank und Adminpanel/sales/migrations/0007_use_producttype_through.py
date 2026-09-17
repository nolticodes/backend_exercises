from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "sales",
            "0006_rename_email_adress_customer_email_address",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="products",
        ),
        migrations.AddField(
            model_name="order",
            name="products",
            field=models.ManyToManyField(
                through="sales.ProductType",
                to="sales.product",
            ),
        ),
    ]