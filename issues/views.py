from django.shortcuts import render
from issues import models as im


def protocolo(request):
    if request.method == 'GET':
        html_variables = {'values': {}}
        for i in im.Issue.objects.all():
            html_variables['values'][str(i.number)] = {
                'title': i.title,
                'body': i.body,
                'assignee': i.assignee,
                'is_closed': i.is_closed,
                'creation_date': i.creation_date,
                'milestone': i.milestone,
                'submitter': i.submitter,
                'labels': i.labels,
            }

        html_variables['issues'] = sorted(html_variables['values'].keys())
        return render(request, 'issues/protocolo.html', html_variables)
    else:
        return render(request, 'common/404.html')
