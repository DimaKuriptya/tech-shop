from django.template import Library


register = Library()

@register.simple_tag
def get_errors(form):
    errors = []
    for _, error in form.errors.items():
        errors.append(error)
    return errors
