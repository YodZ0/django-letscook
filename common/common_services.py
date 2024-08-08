def only_decorator(func: callable):
    def only_wrapper(objects, only=(), *args, **kwargs):
        return func(objects, *args, **kwargs).only(*only)

    return only_wrapper


def order_by_decorator(func: callable):
    def order_by_wrapper(objects, order_by=(), *args, **kwargs):
        return func(objects, *args, **kwargs).order_by(*order_by)

    return order_by_wrapper


def prefetch_related_decorator(func: callable):
    def prefetch_related_wrapper(objects, prefetch_related=(), *args, **kwargs):
        return func(objects, *args, **kwargs).prefetch_related(*prefetch_related)

    return prefetch_related_wrapper


@only_decorator
@order_by_decorator
@prefetch_related_decorator
def all_objects(objects, **kwargs):
    return objects.all(**kwargs)


@only_decorator
@order_by_decorator
@prefetch_related_decorator
def filter_objects(objects, **kwargs):
    return objects.filter(**kwargs)


def get_object(objects, **kwargs):
    return objects.get(**kwargs)


def create_object(objects, **kwargs):
    return objects.create(**kwargs)


def save_object(obj):
    return obj.save()


def delete_object(obj):
    return obj.delete()
