from category.models import Category


def menu_links(request):
    """
    A custom context processor. Context processors are available from every template in the project.
    Needs to be registered in settings.py
    """

    links = Category.objects.all()

    return dict(links=links)
