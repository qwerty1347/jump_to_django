from django.urls import reverse


def print_reverse(url: str):
    """
    url 이름을 전달받아 URL을 생성하는 함수

    Args:
        url (str): URL 이름

    Returns:
        str: 생성된 URL
    """
    print(reverse(url))