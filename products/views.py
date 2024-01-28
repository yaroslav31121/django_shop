from django.shortcuts import render
from .models import Product, Comment
from .forms import CommentForm


def product_detail(request, product_id):
    product = Product.objects.get(pk=product_id)
    comments = Comment.objects.filter(product=product)


    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.product = product
            comment.save()
    else:
        form = CommentForm()

    return render(request, 'products/product_detail.html', {
        'product': product, 'comments': comments, 'form': form})
