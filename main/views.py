
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import AnnotationBox
import random
import numpy as np
import datetime
from django.utils import timezone

def index(response):
    return render(response, "main/index.html", {})

def annotate_view(response):
    if response.method == "POST":

        # draft the highest ranked instance that is not annotated and not drafted
        new_choice = AnnotationBox.objects.filter(is_drafted=False).order_by('rank_idx')[0]
        new_choice.is_drafted = True

        # set the draft (limit) time 2 minutes into the future
        new_choice.draft_time = timezone.now()
        new_choice.save()

        return HttpResponseRedirect(f"/annotate/{new_choice.id}")

    return render(response, "main/annotate.html", {})

def sentence_view(response, id):
    annotation_box = AnnotationBox.objects.get(id=id)

    MINUTES = 5         # how many minutes one has to label before sentence becomes invalid

    if response.method == "POST":
        if annotation_box.draft_time + timezone.timedelta(minutes=1) > timezone.now():
            annotation_box.valence = response.POST.get("valenceSlider")
            annotation_box.arousal = response.POST.get("arousalSlider")
            is_miscellaneous = response.POST.get("is_miscellaneous")
            annotation_box.is_miscellaneous = False if is_miscellaneous == None else True
            annotation_box.is_annotated = True
            annotation_box.save()

            new_choice = AnnotationBox.objects.filter(is_drafted=False).order_by('rank_idx')[0]
            new_choice.is_drafted = True
            new_choice.draft_time = timezone.now() #+ datetime.timedelta(minutes=2)
            new_choice.save()
            return HttpResponseRedirect(f"/annotate/{new_choice.id}")

        else:
            annotation_box.draft_time = None
            annotation_box.is_drafted = False
            annotation_box.save()

            return HttpResponseRedirect("/timeout")

    total_annotated = len(AnnotationBox.objects.filter(is_annotated=True))
    total = len(AnnotationBox.objects.all())

    context = {"sentence": annotation_box.sentence,
               "id": annotation_box.id,
               'total_annotated': total_annotated,
                'total': total,
               'rank_idx': annotation_box.rank_idx,
               }

    return render(response, "main/sentence_view.html", context)

def guideline_view(response):
    return render(response, "main/guideline.html", {})

def timeout_view(response):
    if response.method == "POST":
        return HttpResponseRedirect("/annotate")
    return render(response, "main/timeout.html", {})