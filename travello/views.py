from django.shortcuts import render
from . models import Destination

# Create your views here.
def index(request):
      dest1 = Destination()
      dest1.name = "Off The Ground Off The Ground"
      dest1.price = 400
      dest1.img = 'services-1.jpg'
      dest1.desc = "Perfect for fresh ideas or young startups, this package will help get the business off the ground"


      dest2 = Destination()
      dest2.name = "Accelerated Growth"
      dest2.price = 800
      dest2.img = 'services-2.jpg'
      dest2.desc = "Use this service pack to give your company the necessary impulse to become an industry leader"



      dest3 = Destination()
      dest3.name = "Market Domination"
      dest3.price = 200
      dest3.img = 'services-3.jpg'
      dest3.desc = "You already are a reference point in your industry now you need to learn about acquisitions"
      
      dests = [dest1,dest2,dest3]
      
      return render(request, 'index.html',{'dests':dests})