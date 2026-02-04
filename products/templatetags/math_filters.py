from django import template

register = template.Library()


@register.filter(name="mul")
def mul(value, arg):
    """
    Multiply two numbers safely in templates.
    Usage: {{ price|mul:rate }}
    """
    try:
        return float(value) * float(arg)
    except (TypeError, ValueError):
        return 0


@register.filter(name="div")
def div(value, arg):
    """
    Divide two numbers safely in templates.
    Usage: {{ price|div:rate }}
    """
    try:
        return float(value) / float(arg)
    except (TypeError, ValueError, ZeroDivisionError):
        return 0


@register.filter(name="add")
def add(value, arg):
    """
    Add two numbers safely.
    """
    try:
        return float(value) + float(arg)
    except (TypeError, ValueError):
        return value


@register.filter(name="sub")
def sub(value, arg):
    """
    Subtract two numbers safely.
    """
    try:
        return float(value) - float(arg)
    except (TypeError, ValueError):
        return value
