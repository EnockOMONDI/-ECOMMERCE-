from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            cart.clear()
        return render(request, 'orders/order/created.html', {
            'order': order,
            'local_css_urls': ["css3/easy-responsive-tabs.css",
                            "css3/material-kit.min1036.css",
                            "css3/demo.css",
                            "css3/vertical-nav.css"],
             'local_js_urls': [ "core/jquery.min.js",
                           "core/popper.min.js",
                           "core/bootstrap-material-design.min.js",
                           "js3/vertical-nav.js",
                           "js3/material-kit.min1036.js",
                           "js3/demo.js",
                           "js3/buttons.js",
                           "js3/modernizr.js",                         
                           "js3/bootstrap.min.js",                           
                           "js3/plugins/moment.min.js ",
                           "js3/plugins/bootstrap-datetimepicker.js",
                           "js3/plugins/jquery.flexisel.js",
                           "js3/plugins/jquery.sharrre.js",
                           "js3/plugins/nouislider.min.js",
                           "js3/plugins/bootstrap-selectpicker.js",
                           "js3/plugins/bootstrap-tagsinput.js",
                           "js3/plugins/jasny-bootstrap.min.js"],
    })
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {
        
        'form': form,
        'local_css_urls': ["css3/easy-responsive-tabs.css",
                            "css3/material-kit.min1036.css",
                            "css3/demo.css",
                            "css3/vertical-nav.css"],
        'local_js_urls': [ "core/jquery.min.js",
                           "core/popper.min.js",
                           "core/bootstrap-material-design.min.js",
                           "js3/vertical-nav.js",
                           "js3/material-kit.min1036.js",
                           "js3/demo.js",
                           "js3/buttons.js",
                           "js3/modernizr.js",                         
                           "js3/bootstrap.min.js",                           
                           "js3/plugins/moment.min.js ",
                           "js3/plugins/bootstrap-datetimepicker.js",
                           "js3/plugins/jquery.flexisel.js",
                           "js3/plugins/jquery.sharrre.js",
                           "js3/plugins/nouislider.min.js",
                           "js3/plugins/bootstrap-selectpicker.js",
                           "js3/plugins/bootstrap-tagsinput.js",
                           "js3/plugins/jasny-bootstrap.min.js"],
    })
