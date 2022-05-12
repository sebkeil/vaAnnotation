
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import AnnotationBox
import random


def index(response):
    return render(response, "main/index.html", {})

def annotate_view(response):
    if response.method == "POST":
        # NOTE: implement AL query here to get new id
        possible_ids = [a.id for a in list(AnnotationBox.objects.filter(is_annotated=False))]
        new_id = random.choice(possible_ids)
        return HttpResponseRedirect(f"/annotate/{new_id}")

    return render(response, "main/annotate.html", {})

def sentence_view(response, id):
    annotation_box = AnnotationBox.objects.get(id=id)

    if response.method == "POST":
        annotation_box.valence = response.POST.get("valenceSlider")
        annotation_box.arousal = response.POST.get("arousalSlider")
        is_miscellaneous = response.POST.get("is_miscellaneous")
        annotation_box.is_miscellaneous = False if is_miscellaneous == None else True
        annotation_box.is_annotated = True
        annotation_box.save()

        # NOTE: implement AL query here to get new id
        possible_ids = [a.id for a in AnnotationBox.objects.filter(is_annotated=False)]

        if len(possible_ids):
            new_id = random.choice(possible_ids)
            # toDO: add another attribute is_chosen that is activated here immediately, to avoid double annotations
            return HttpResponseRedirect(f"/annotate/{new_id}")

        else:
            return HttpResponse(response, "<h1> congrats! You have labeled all the data! </h1>")

    total_annotated = len(AnnotationBox.objects.filter(is_annotated=True))
    total = len(AnnotationBox.objects.all())

    context = {"sentence": annotation_box.sentence,
               "id": annotation_box.id,
               'total_annotated': total_annotated,
                'total': total,
               }

    return render(response, "main/sentence_view.html", context)

def guideline_view(response):
    return render(response, "main/guideline.html", {})

