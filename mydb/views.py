from django.views.generic import ListView
# Create your views here.
from .models import Db
class HomePageView(ListView):
    model=Db
    template_name='home.html'