from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.views.generic.edit import CreateView
from rest_framework import generics, filters, pagination
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import logout


from .forms import UserRegisterForm, OrganizationForm, EventForm
from .models import Organization, Event
from .serializers import OrganizationSerializer, EventSerializer



# class OrganizationCreateView(CreateView):
#     model = Organization
#     form_class = OrganizationNewForm
#     template_name = 'organizations.html'
#     success_url = '/'



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)


        if form.is_valid():
            form.save()
            messages.success(request, f'Создан аккаунт')
            return redirect('home')
    else:
        error_message = "Проверьте введённные данные и исправьте ошибки"
        form = UserRegisterForm()

    return render(request, 'register.html', {'form': form})

# def login(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         password = request.POST['password']
#         user = authenticate(request, email=email, password=password)
        
#         if user is not None:
#             login(request, user)
#             return redirect('home')  
#         else:
#             error_message = 'Неверный email или пароль.'
#             return render(request, 'login.html', {'error_message': error_message})

#     return render(request, 'login.html')

# def register(request):
    # if request.method == 'POST':
    #     form = UserCreationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('home')
    # else:
    #     form = UserCreationForm()
    # print({'form': form})
    # return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            form.user_cache.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, form.get_user())
            return redirect('home') 
    else:
        form = AuthenticationForm(request)

    return render(request, 'login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
    return render(request, 'logout.html')


@login_required
def home(request):
    user = request.user
    organizations = Organization.objects.all()
    events = Event.objects.filter(organizations__in=organizations)
    
    context = {
        'user': user,
        'organizations': organizations,
        'events': events
    }
    return render(request, 'home.html', context)


def organizations(request):
    organizations = Organization.objects.all()
    if request.method == 'POST':
        form = OrganizationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = OrganizationForm()
    return render(request, 'organizations.html', {'organizations': organizations, 'form': form})


def organization_profile(request, organization_id):
    organization = get_object_or_404(Organization, id=organization_id)
    context = {'organization': organization}
    return render(request, 'organization_profile.html', context)

def event_list(request):
    events = Event.objects.all()
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event-list')
    else:
        form = EventForm()
    return render(request, 'event_list.html', {'events': events, 'form': form})



def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('event-list')
    else:
        print(form)
        form = EventForm()
    return render(request, 'event_create.html', {'form': form})



def event_edit(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event-list')
    else:
        form = EventForm(instance=event)
    return render(request, 'events/event_edit.html', {'form': form, 'event': event})


class OrganizationCreateView(generics.CreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [IsAuthenticated]

class EventCreateView(generics.CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

class EventDetailView(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class EventListAPIView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['date']
    pagination_class = pagination.LimitOffsetPagination
