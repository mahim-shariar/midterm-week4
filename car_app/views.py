from django.shortcuts import render,redirect
from .models import CarModel
from .models import Order
from django.views.generic import DetailView
from . import forms
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.


@method_decorator(login_required, name='dispatch')
class DetailCarView(DetailView):
    model = CarModel
    pk_url_kwarg = 'id'
    template_name = 'car_details.html'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        car = self.object
        comment_form = forms.CommentsForm(data=request.POST)

        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = car
            new_comment.save()
            return redirect('car_details', id=car.id)
        else:
            return self.render_to_response(self.get_context_data(comment_form=comment_form))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.object
        comments = car.comments.all()
        comment_form = forms.CommentsForm()

        context['car'] = car
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context