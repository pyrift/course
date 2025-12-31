# views.py
from .serializers import BranchSerializer, InfarationSerializer, BurningSerializer
from .models import Branch, Infaration, Burning
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework import generics
from django.template import loader
from django.http import HttpResponse

# =========================================================================
# Branch bo'limi
class Branch_menu(generics.ListAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    permission_classes = [AllowAny]  # hammaga ochiq (yoki IsAuthenticated qo'ying)

class Branch_update(generics.UpdateAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    permission_classes = [IsAdminUser]  # faqat admin o'zgartira oladi

class Branch_deletion(generics.DestroyAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    permission_classes = [IsAdminUser]

class Branch_create(generics.CreateAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    permission_classes = [IsAdminUser]

# ======================================================================
# Burning bo'limi
class Burning_menu(generics.ListAPIView):
    queryset = Burning.objects.all()
    serializer_class = BurningSerializer
    permission_classes = [AllowAny]  # hammaga ko'rish uchun

class Burning_update(generics.UpdateAPIView):
    queryset = Burning.objects.all()
    serializer_class = BurningSerializer
    permission_classes = [IsAdminUser]

class Burning_deletion(generics.DestroyAPIView):
    queryset = Burning.objects.all()
    serializer_class = BurningSerializer
    permission_classes = [IsAdminUser]

class Burning_create(generics.CreateAPIView):
    queryset = Burning.objects.all()
    serializer_class = BurningSerializer
    permission_classes = [IsAdminUser]

# ======================================================================

class Infaration_menu(generics.ListAPIView):
    queryset = Infaration.objects.all()
    serializer_class = InfarationSerializer

class Infaration_update(generics.UpdateAPIView):
    queryset = Infaration.objects.all()
    serializer_class = InfarationSerializer

class Infaration_deletion(generics.DestroyAPIView):
    queryset = Infaration.objects.all()
    serializer_class = InfarationSerializer

class Infaration_create(generics.CreateAPIView):
    queryset = Infaration.objects.all()
    serializer_class = InfarationSerializer
#==============================filter================================================

#
# def testing(request):
#     # Masalan, branch_name = "IT" bo'lganlarni olish:
#     mydata = Branch.objects.filter(branch_name='frontned').values()
#
#     template = loader.get_template('template.html')
#     context = {
#         'mymembers': mydata,  # nomi 'mymembers' bo'lishi shart emas, istalgan
#     }
#     return HttpResponse(template.render(context, request))
def backend_filter(request):
    # 'backend' branchini tanlagan Infaration obyektlarini olish
    mydata = Infaration.objects.filter(direction__burning='backend')

    template = loader.get_template('template.html')
    context = {
        'mymembers': mydata,  # hozir bu Infaration obyektlari
    }
    return HttpResponse(template.render(context, request))

def frontend_filter(request):
    # 'backend' branchini tanlagan Infaration obyektlarini olish
    mydata = Infaration.objects.filter(direction__burning='frontend')

    template = loader.get_template('template.html')
    context = {
        'mymembers': mydata,  # hozir bu Infaration obyektlari
    }
    return HttpResponse(template.render(context, request))