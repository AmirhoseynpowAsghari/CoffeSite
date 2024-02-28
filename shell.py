from User.models import UserModel, UserProfile
from Product.models import Product, Like
from django.contrib.auth import get_user_model


User = get_user_model()

users = User.objects.all()

for user in users:
	print(user.email)


# I can delete a user with delete method

# Create a Product instance
product = Product.objects.create(
    name='Example Product',
    description='This is an example description.',
    price=10.99,
    likes=5,
    reviews_count=3,
    average_rating=4.5
)

# Print the product's name
print(product.name)

# Create a Like instance
like = Like.objects.create(
    user=User.objects.get(email='admin@admin.com'),  # Provide the ID of the user who liked the product
    product=product,
    like_status=True
)

# Print the like status
print(like.like_status)