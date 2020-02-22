from django.shortcuts import render, get_object_or_404
from .models import Category, Product, SubCategory, MiniCategory
from cart.forms import CartAddProductForm
from django.contrib.auth.decorators import login_required
from .forms import NewsLetterForm

# @login_required(login_url='/accounts/login/')
def product_list(request,category_slug=None,):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products,
  
    }

    return render(request, 'shop/product/list.html',   context = {
        'category': category,
        'categories': categories,
        'products': products,  
        'tab': 'shop',
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





def subcategory_list(request, category_slug=None,subcategory_slug=None,minicategory_slug=None):
    category = None
    subcategory = None
    minicategory = None
    categories = Category.objects.all()
    subcategories = SubCategory.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        subcategories = SubCategory.objects.filter(category=category,available=True)

    context = {
        'category': category,
        'categories': categories,
        'subcategories': subcategories,
        'subcategory': SubCategory,
    }
    return render(request, 'shop/product/sublist.html', context)

def minicategory_list(request, subcategory_slug=None):
    subcategory = None
    subcategories = SubCategory.objects.all()
    minicategories = MiniCategory.objects.filter(available=True)
    if subcategory_slug:
        subcategory = get_object_or_404(SubCategory, slug=subcategory_slug)
        minicategories = MiniCategory.objects.filter(subcategory=subcategory,available=True)

    context = {
        'subcategories': subcategories,
        'Subcategory': SubCategory,
        'minicategories': minicategories,
        'minicategory': MiniCategory,
    }
    return render(request, 'shop/product/minilist.html', context)

# @login_required(login_url='/accounts/login/')
# def product_detail(request, id, slug):
#     product = get_object_or_404(Product, id=id, slug=slug, available=True)
#     cart_product_form = CartAddProductForm()
#     context = {
#         'product': product,
#         'cart_product_form': cart_product_form
#     }
#     return render(request, 'shop/product/detail.html', context)
def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form
    }
    return render(request, 'shop/product/detail.html',
     context = {
        'product': product,
        'cart_product_form': cart_product_form,
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


# homepage view

def home(request, category_slug=None,subcategory_slug=None,minicategory_slug=None):
    category = None
    subcategory = None
    minicategory = None
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()
    minicategories = MiniCategory.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        subcategories = SubCategory.objects.filter(category=category)

    # if subcategory_slug:
    #     subcategory = get_object_or_404(SubCategory, slug=subcategory_slug)
    #     minicategories = MiniCategory.objects.filter(available=True)


    context = {
        'category': category,
        'categories': categories,
        'products': products,
        'subcategories': subcategories,
        'minicategories ': minicategories ,
        'subcategory': subcategory,
        'minicategory': minicategory,
    }
    
    return render(request, 'shop/homepage/page/home.html',   context = {
        'category': category,
        'categories': categories,
        'products': products,
        'subcategories': subcategories,
        'minicategories': minicategories ,
        'subcategory': subcategory,
        'minicategory': minicategory ,
  
        'tab': 'shop',
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

 


def log(request):
  return render(request, 'shop/product/login2.html',{
        'tab': 'registration',
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



def vendorrequest(request):
  return render(request, 'shop/homepage/page/vendorrequest.html',{
        'tab': 'vendor',
        'local_css_urls': ["css3/easy-responsive-tabs.css",
                            "css3/material-kit.min1036.css",
                            "css3/demo.css",
                            "css3/vertical-nav.css"],
        'local_js_urls': ["js3/vertical-nav.js",
                          "js3/material-kit.min1036.js",
                           "js3/demo.js",
                           "js3/buttons.js",
                           "js3/modernizr.js",
                          
                           "js3/jquery.min.js",
                           "js3/bootstrap.min.js", 
                           "core/jquery.min.js",
                           "core/popper.min.js",
                           "core/bootstrap-material-design.min.js",
                           "js3/plugins/moment.min.js ",
                           "js3/plugins/bootstrap-datetimepicker.js",
                           "js3/plugins/jquery.flexisel.js",
                           "js3/plugins/jquery.sharrre.js",
                           "js3/plugins/nouislider.min.js",
                           "js3/plugins/bootstrap-selectpicker.js",
                           "js3/plugins/bootstrap-tagsinput.js",
                           "js3/plugins/jasny-bootstrap.min.js"],
    })

def Vendorfaqs(request):
  return render(request, 'shop/homepage/page/vendorfaqs.html',{
        'tab': 'Vendorfaqs',
        'local_css_urls': ["css3/easy-responsive-tabs.css",
                            "css3/material-kit.min1036.css",
                            "css3/demo.css",
                            "css3/vertical-nav.css"],
        'local_js_urls': ["js3/vertical-nav.js",
                          "js3/material-kit.min1036.js",
                           "js3/demo.js",
                           "js3/buttons.js",
                           "js3/modernizr.js",
                          
                           "js3/jquery.min.js",
                           "js3/bootstrap.min.js", 
                           "core/jquery.min.js",
                           "core/popper.min.js",
                           "core/bootstrap-material-design.min.js",
                           "js3/plugins/moment.min.js ",
                           "js3/plugins/bootstrap-datetimepicker.js",
                           "js3/plugins/jquery.flexisel.js",
                           "js3/plugins/jquery.sharrre.js",
                           "js3/plugins/nouislider.min.js",
                           "js3/plugins/bootstrap-selectpicker.js",
                           "js3/plugins/bootstrap-tagsinput.js",
                           "js3/plugins/jasny-bootstrap.min.js"],
    })


def homeaccesories(request):
  return render(request, 'shop/product/homeaccesories.html')

def decorbeauty(request):
  return render(request, 'shop/product/decorbeauty.html')

def about(request):
  return render(request, 'shop/product/about.html',{
             'tab': 'Vendorfaqs',
        'local_css_urls': ["css3/easy-responsive-tabs.css",
                            "css3/material-kit.min1036.css",
                            "css3/demo.css",
                            "css3/vertical-nav.css"],
        'local_js_urls': ["js3/vertical-nav.js",
                          "js3/material-kit.min1036.js",
                           "js3/demo.js",
                           "js3/buttons.js",
                           "js3/modernizr.js",
                          
                           "js3/jquery.min.js",
                           "js3/bootstrap.min.js", 
                           "core/jquery.min.js",
                           "core/popper.min.js",
                           "core/bootstrap-material-design.min.js",
                           "js3/plugins/moment.min.js ",
                           "js3/plugins/bootstrap-datetimepicker.js",
                           "js3/plugins/jquery.flexisel.js",
                           "js3/plugins/jquery.sharrre.js",
                           "js3/plugins/nouislider.min.js",
                           "js3/plugins/bootstrap-selectpicker.js",
                           "js3/plugins/bootstrap-tagsinput.js",
                           "js3/plugins/jasny-bootstrap.min.js"],
    })


def mens(request):
  return render(request, 'shop/product/mens.html')

def contact(request):
  return render(request, 'shop/product/contact.html',{
       'tab': 'registration',
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



def womens(request):
   return render(request, 'shop/product/womens.html')


