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
    head = data[0].split(',')
    rows = data[1:]
    values = list()
    for row in rows:
        if '[' in row and ']' in row:
            new_row = list()
            index = row.index('[')
            new_row.append(row[:index].split(',')[0])
            array = row[index:].replace('[', '').replace(']', '').replace("'", '')
            new_row.append(array)
            values.append(new_row)
        else:
            values.append(row.split(','))
    return {'content': table,
            'heads': head,
            'rows': values}


@register.simple_tag()
def get_list(content: Content):
    return content.content.split('\n')