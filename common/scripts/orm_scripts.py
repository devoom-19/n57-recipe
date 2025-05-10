<<<<<<< HEAD
from blogs.models import BlogCategoryModel, Category, Product
from decimal import Decimal
from django.db.models import Q
=======
from blogs.models import BlogCategoryModel
>>>>>>> 031e4426d2755a8cbeb24e504ca6808c015cc87a


def run():
    # cat1 = BlogCategoryModel.objects.create(title='Query added to blog')
    # cat1 = BlogCategoryModel(title='Query added to blog')
    # cat1.save()
    # print(cat1)

<<<<<<< HEAD
=======

>>>>>>> 031e4426d2755a8cbeb24e504ca6808c015cc87a
    #BlogCategoryModel.objects.filter(id=1).delete()


    #BlogCategoryModel.objects.filter(id=1).update(title="nomini o'zgartirish")
<<<<<<< HEAD
    #cat = BlogCategoryModel.objects.get(id=1)
    #cat.title = "nomini o'zgartirish"
    #cat.save()


    'select * from blog_category'
    #cat = BlogCategoryModel.objects.all()
    #print(cat)


    'select from blog_category'
    #cat = BlogCategoryModel.objects.values('title')
    #print(cat)


    """
    __gt >
    __gte >=
    __lt <
    __lte <=
    __isnull
    """


    'select * from BlogCategory where id = > 1 and id <= 100'
    #cats = BlogCategoryModel.objects.filter(id__gte=1, id__lte=100)
    #print(cats)


    'select * from BlogCategory where id = > 1 or id <= 100'
    #cat = BlogCategoryModel.objects.filter(Q(id__gte=1) | Q(id__lte=3))
    #print(cat)





    #                           EXERCISE

    #c1 = Category.objects.create(name='Drinks', description='Soda')
    #c2 = Category.objects.create(name='Tech', description='Electric cars')
    c3 = Category.objects.create(name='Plant', description='Flower')


    #Product.objects.create(name='Coca Cola', price=5, category=c1, in_stock=True)
    Product.objects.create(name='Pion', price=100, category=c3, in_stock=True)
    #Product.objects.create(name='Zeekr', price=50000, category=c2, in_stock=False)
    #Product.objects.create(name='Nesquik', price=3, category=c1, in_stock=False)
    #Product.objects.create(name='Siren', price=20, category=c3, in_stock=False)
    #Product.objects.create(name='Tesla', price=40, category=c2, in_stock=True)


    #drinks_products = Product.objects.filter(category__name="Drinks")


    #product = Product.objects.filter(name="Pion").first()
    #product.price *= Decimal (1.10)
    #product.save()

    Category.objects.all().delete()

=======
    cat = BlogCategoryModel.objects.get(id=1)
    cat.title = "nomini o'zgartirish"
    cat.save()
>>>>>>> 031e4426d2755a8cbeb24e504ca6808c015cc87a
