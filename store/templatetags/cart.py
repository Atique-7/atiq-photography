from django import template

register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(productInfo, cart):
   keys = cart.keys()
   for id in keys:
      if int(id) == productInfo.id:
         return True
   return False


@register.filter(name='total_cart')
def total_cart(products):
   sum = 0;
   for item in products:
      sum += item.price
   return sum

@register.filter(name='empty_cart')
def empty_cart(cart):
   value = True
   if not cart:
      value = False
   return value