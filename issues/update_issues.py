from transparency import settings
from github import Github
from issues import models as im


g = Github(settings.GITHUB_USER, settings.GITHUB_PASSWORD)

for i in g.get_user().get_repo('purubemalves').get_issues():
    if im.Issue.objects.get(number=i.number):
        existing_issue = im.Issue.objects.get(number=i.number)
        existing_issue.number = i.number
        existing_issue.title = i.title
        existing_issue.body = i.body
        existing_issue.is_closed = bool(i.closed_by)
        existing_issue.creation_date = i.created_at
        existing_issue.save()
    else:
        new_issue = im.Issue(
            number=i.number,
            title=i.title,
            body=i.body,
            is_closed=bool(i.closed_by),
            creation_date=i.created_at,
        )
        new_issue.save()

# TODO: save this info to a txt file (2017/03/02)
# new_file = open(settings.GITHUB_LOCALFILE, 'w')
# new_file.write(g.get_repo(settings.GITHUB_REPOSITORY).raw_data)
# new_file.close()
