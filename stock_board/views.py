from django.shortcuts import render
from .models import StockList
from django.views import generic
from django.views import View
from .forms import StockForm

class Stock_list(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = 'stock_board/stock_list.html'
        stock_list = StockList.objects.all()
        return render(request, template_name, {'stock_list' : stock_list})


def check_post(request):
    template_name = 'stock_board/stock_board_success.html'
    if request.method == "POST":
        form = StockForm(request.POST)
        if form.is_valid():
            stock = form.save(commit=False)
            stock.add_stock()
            message = "Stock 추가 완료"
            return render(request, template_name, {"message": message})
    else:
        template_name = 'stock_board/insert.html'
        form = StockForm
        return render(request, template_name, {"form" : form})
