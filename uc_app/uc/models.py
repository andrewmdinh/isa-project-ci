from django.db import models
from django.core.validators import *

    # user_rating_stars = models.IntegerField()
    # ############
    # # FAVORITES
    # ############
    # favorite = models.ManyToManyField(Item)
    # ############
    # # BALANCE
    # # stores seller earning (can transfer to bank later) & promotion credit
    # ############
    # balance = models.DecimalField(default=0.00, max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])


class User(models.Model):
    first_name = models.CharField(max_length=30)

    last_name = models.CharField(max_length=30)

    username = models.CharField(max_length = 40, unique=True)   # django automatically create iD as primary key

    password = models.CharField(max_length=100)


class Item(models.Model):
    item_name = models.CharField(max_length=100)

    item_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])

    date_created = models.DateTimeField(auto_now_add=True)

    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="seller")  # 1 item have 1 seller

    buyer = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name="buyer")  # 1 item has 1 seller

    brand = models.CharField(max_length=100)
    #
    # item_rating_stars = models.IntegerField()
    #
    description = models.TextField(blank=True)
    image_url = models.URLField(max_length=1000)
    ITEM_SIZES = (
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
    ('OS', 'One Size'),
    ('Other', 'Other'))
    item_size = models.CharField(max_length = 15, choices=ITEM_SIZES)

    ITEM_TYPES = (
     	('Top', 'Top'),
    	('Bottom', 'Bottom'),
        ('Dress', 'Dress'),
        ('Footwear', 'Footwear'),
        ('Accessory', 'Accessory'),
    	('Other', 'Other')
    )
    item_type = models.CharField(max_length= 15, choices = ITEM_TYPES)


class Authenticator(models.Model):
    authenticator = models.CharField(primary_key=True, max_length=100)

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    date_created = models.DateTimeField(auto_now_add=True)
