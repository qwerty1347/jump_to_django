from django import template


register = template.Library()


@register.filter
def descending_index(page_obj, counter0):
    total_count = page_obj.paginator.count
    per_page = page_obj.paginator.per_page
    current_page = page_obj.number

    return total_count - ((current_page - 1) * per_page + counter0)