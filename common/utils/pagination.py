from django.core.paginator import Paginator
from django.db.models.query import QuerySet


def get_paginated_queryset(
    list: QuerySet,
    page: int,
    size: int = 10,
    block_size: int = 5,
) -> dict:
    paginator = Paginator(list, size)
    page_obj = paginator.get_page(page)

    total_pages = paginator.num_pages
    current = page_obj.number

    current_block = (current - 1) // block_size
    start = current_block * block_size + 1
    end = min(start + block_size - 1, total_pages)

    return {
        'page_obj': page_obj,
        'page_range': range(start, end + 1),
        'total_pages': total_pages
    }
