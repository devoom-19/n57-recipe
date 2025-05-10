from django.contrib.auth.models import User
from django.db import models

from common.models import BaseModel


class BlogCategoryModel(BaseModel):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Blog category'
        verbose_name_plural = 'Blog categories'


class BlogTagModel(BaseModel):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Blog tag'
        verbose_name_plural = 'Blog tags'


class BlogModel(BaseModel):
    title = models.CharField(max_length=128)
    image1 = models.ImageField(upload_to='blogs')
    image2 = models.ImageField(upload_to='blogs')
    short_description = models.CharField(max_length=255)
    long_description = models.TextField()

    categories = models.ManyToManyField(BlogCategoryModel, related_name='blogs')
    tags = models.ManyToManyField(BlogTagModel, related_name='blogs')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Blog tag'
        verbose_name_plural = 'Blog tags'


class BlogCommentModel(BaseModel):
    comment = models.CharField(max_length=128)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_comment')
    blog = models.ForeignKey(BlogModel, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.comment

    class Meta:
        verbose_name = 'Blog comment'
        verbose_name_plural = 'Blog comments'


class BlogLikeModel(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_like')
    blog = models.ForeignKey(BlogModel, on_delete=models.CASCADE, related_name='likes')

    def __str__(self):
        return f'{self.user.get_full_name()} liked to {self.blog}'

    class Meta:
        verbose_name = 'Blog tag'
        verbose_name_plural = 'Blog tags'
<<<<<<< HEAD












class Category(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()


    def __str__(self):
        return self.name

    def __repr__(self):
        return f'Category: {self.name}'


    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(BaseModel):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product')
    in_stock = models.BooleanField(default=False)


    def __str__(self):
        return self.name

    def __repr__(self):
        return f'Product: {self.name}, Price: {self.price}'

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
=======
>>>>>>> 031e4426d2755a8cbeb24e504ca6808c015cc87a
