from atexit import register
from django import template


register = template.Library()

@register.filter(name = "isexistincart")
def isexistincart(product,cart):
    keys = cart.keys()

    for id in keys:
        if int(id) == product.id:
            return True
    return False
@register.filter(name = "cartquant")
def cartquant(product,cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return cart.get(id)
    return False
@register.filter(name="totalprice")
def totalprice(product,cart):
    return product.price * cartquant(product,cart)
@register.filter(name ="totalsum")
def totalsum(product,cart):
    sum = 0
    for p in product:
        sum += totalprice(p,cart)
    return sum
@register.filter(name="multiplyprice")
def multiplyprice(num1,num2):
    return num1*num2



