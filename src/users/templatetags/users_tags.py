from django.template import Library


register = Library()

@register.simple_tag
def get_user_errors(form):
    errors = []
    for _, value in form.errors.items():
        for error in value:
            errors.append(error)
    return errors
