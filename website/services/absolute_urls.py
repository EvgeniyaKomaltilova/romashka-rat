from django.urls import reverse


def get_rat_url(obj):
    return reverse('rat', kwargs={'rat_id': obj.id})


def get_litter_url(obj):
    return reverse('litter', kwargs={'litter_year': obj.year, 'litter_id': obj.id})
