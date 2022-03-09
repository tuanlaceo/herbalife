from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator  # import lib cho pagination
from listings.choices import price_choices, bedroom_choices, state_choices
from .models import Listing

# Create your views here.
def index(request):
    #listings = Listing.objects.all()  # lay tat ca obkject trong Listings model
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)  # lay nhung object lan luot theo date va duoc check public
    paginator = Paginator(listings, 6)  # hien thi 6 san pham trong 1 page
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
    'listings': paged_listings
  }
    return render(request,'listings/listings.html', context)

def listing(request,listing_id):   # khi truy cap vao detail thi ta can them id cu the
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
    'listing': listing
  }
    return render(request,'listings/listing.html',context)

def search(request):
    queryset_list = Listing.objects.order_by('-list_date')
    # Keywords
    if 'keywords' in request.GET:
      keywords = request.GET['keywords']
      if keywords:
        queryset_list = queryset_list.filter(description__icontains=keywords)
    # City
    if 'city' in request.GET:
      city = request.GET['city']
      if city:
        queryset_list = queryset_list.filter(city__iexact=city)

    # State
    if 'state' in request.GET:
      state = request.GET['state']
      if state:
        queryset_list = queryset_list.filter(state__iexact=state)  #state__iexact : nghia la lay nhung can nha co so chinh xac ten tai state

    # Bedrooms
    if 'bedrooms' in request.GET:
      bedrooms = request.GET['bedrooms']
      if bedrooms:
        queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)  #bedrooms__lte : nghia la lay nhung can nha co so giuong ngu la max

    # Price
    if 'price' in request.GET:
      price = request.GET['price']
      if price:
        queryset_list = queryset_list.filter(price__lte=price)
    context = {
        
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listings': queryset_list,
        'values': request.GET,
    }
    return render(request,'listings/search.html',context)