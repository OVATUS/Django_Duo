from django import template

register = template.Library()

@register.filter(name="as_widget")
def as_widget(field, css):
    """ใส่ class ของ Tailwind ให้ field ของฟอร์ม"""
    return field.as_widget(attrs={
        "class": css
    })
