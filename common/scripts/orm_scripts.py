from blogs.models import BlogCategoryModel


def run():
    # cat1 = BlogCategoryModel.objects.create(title='Query added to blog')
    # cat1 = BlogCategoryModel(title='Query added to blog')
    # cat1.save()
    # print(cat1)


    #BlogCategoryModel.objects.filter(id=1).delete()


    #BlogCategoryModel.objects.filter(id=1).update(title="nomini o'zgartirish")
    cat = BlogCategoryModel.objects.get(id=1)
    cat.title = "nomini o'zgartirish"
    cat.save()
