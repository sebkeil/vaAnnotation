from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("annotate", views.annotate_view, name='annotate_view'),
    path("annotate/<int:id>", views.sentence_view, name='sentence_view'),
    path("guideline", views.guideline_view, name='guideline_view'),
    path("timeout", views.timeout_view, name='timeout_view')

]

