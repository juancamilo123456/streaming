from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/post_list.html', {})

def about(request):
    return render(request, 'blog/about.html', {})

def contact(request):
    return render(request, 'blog/contact.html', {})

def shop_single(request):
    return render(request, 'blog/shop-single.html', {})

def shop(request):
    return render(request, 'blog/shop.html', {})



