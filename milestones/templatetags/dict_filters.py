from django import template

register = template.Library()  # we're creating a new Library instance where we will register our custom template filters

@register.filter  # this decorator is registering our function as a filter
def get_item(dictionary, key):  # this function takes a dictionary and a key as input
    return dictionary.get(key)  # it returns the value of the dictionary at the specified key
