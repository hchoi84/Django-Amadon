from django.shortcuts import render
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request):
    total_ordered = 0
    for order in Order.objects.all():
        total_ordered += order.total_price

    context = {
        "quantity_from_form": Order.objects.last().quantity_ordered,
        "price_from_form": Order.objects.last().total_price,
        "total_charge": Order.objects.last().quantity_ordered * Order.objects.last().total_price,
        "total_ordered": total_ordered
    }

    return render(request, "store/checkout.html", context)

def purchase(request):
    quantity_from_form = int(request.POST["quantity"])
    price_from_form = Product.objects.get(id=request.POST["price"]).price
    total_charge = quantity_from_form * price_from_form
    print("Charging credit card...")
    Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
    return redirect("/checkout")