from django.db import models


CHOOSE_SIZE = (
    ("P", "pequeno"),
    ("M", "médio"),
    ("G", "grande"),
    ("GG", "gigante"),
    ("XG", "extra grande"),
)

# a= 350px h =400px
class Image(models.Model):
    image = models.ImageField(
        upload_to="imagens/%Y/%m/%d", width_field="400", height_field="250"
    )

    def __str__(self):
        return self.image

    class Meta:
        db_table = "image"
        verbose_name = "image"
        verbose_name_plural = "imagens"


class Product(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    value = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(verbose_name="descrição")
    id_image = models.ManyToManyField(
        "home.Image", verbose_name="image", db_column="id_imagens"
    )
    size = models.CharField(max_length=2, choices=CHOOSE_SIZE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Product"
        verbose_name = "Product"
        verbose_name_plural = "Products"


class Category(models.Model):
    name = models.CharField(max_length=255)
    id_product = models.ManyToManyField(
        "home.Product", verbose_name="product", db_column="id_product"
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Category"
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class cart(models.Model):

    id_user = models.ForeignKey(
        "accounts.User",
        verbose_name="Usuário",
        db_column="id_user",
        on_delete=models.CASCADE,
    )
    id_product = models.ManyToManyField(
        "home.Product", verbose_name="product", db_column="id_product"
    )

    def __str__(self):
        return self.id_user

    class Meta:
        db_table = "cart"
        verbose_name = "cart"
        verbose_name_plural = "carts"
