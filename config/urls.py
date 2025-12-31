# kurslar_app/urls.py  (yoki sizning app nomingiz o‘rniga)
from django.urls import path
from django.contrib import admin
from course import views
from course.views import *
#     Branch_menu,
#     Branch_create,
#     Branch_update,
#     Branch_deletion,
#
#     Burning_menu,
#     Burning_create,
#     Burning_update,
#     Burning_deletion,
#
#     Infaration_menu,
#     Infaration_create,
#     Infaration_update,
#     Infaration_deletion,
#     testing,
# )
urlpatterns = [
    path('admin/', admin.site.urls),

    # ====================== Branch ======================

    path('branch/', Branch_menu.as_view(), name='branch_list'),
    path('branch/create/', Branch_create.as_view(), name='branch_create'),
    path('branch/<int:pk>/update/', Branch_update.as_view(), name='branch_update'),
    path('branch/<int:pk>/delete/', Branch_deletion.as_view(), name='branch_delete'),

    # ====================== Burning ======================

    path('burning/', Burning_menu.as_view(), name='burning_list'),
    path('burning/create/', Burning_create.as_view(), name='burning_create'),
    path('burning/<int:pk>/update/', Burning_update.as_view(), name='burning_update'),
    path('burning/<int:pk>/delete/', Burning_deletion.as_view(), name='burning_delete'),

    # ====================== Infaration ======================

    path('infaration/', Infaration_menu.as_view(), name='infaration_list'),
    path('infaration/create/', Infaration_create.as_view(), name='infaration_create'),
    path('infaration/<int:pk>/update/', Infaration_update.as_view(), name='infaration_update'),
    path('infaration/<int:pk>/delete/', Infaration_deletion.as_view(), name='infaration_delete'),

    #========================filter===============================

    path('backend_filter/', views.backend_filter, name='backend'),
    path('frontend_filter/',views.frontend_filter, name='frontend'),
]
