from django.template import Library
from dev1C.models import *

register = Library()


@register.simple_tag()
def get_all_content(block_id):
    contents = Content.objects.filter(block=block_id)
    return contents


@register.simple_tag()
def get_list(text: Content):
    return text.content.split('\n')


@register.inclusion_tag('dev1C/table.html')
def show_table(table: Content):
    data = table.content.split('\n')
    data = [row.split(',') for row in data]
    head = data[0]
    rows = data[1:]
    return {'content': table,
            'head': head,
            'rows': rows}