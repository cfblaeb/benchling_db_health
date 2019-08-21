from django.db.models import Count
from json import dumps
from backend.models import User, Team, TeamMember, Author, Batch, BatchSchema, RegistryEntity, EntitySchema, Entry, Schema, Field, FieldDefinition, SchemaField

cled_team = Team.objects.get(name="CHO Cell Line Engineering & Design")
cled_users = User.objects.filter(id__in=[x.user_id for x in TeamMember.objects.filter(team_id=cled_team.id)])
cled_user_ids = [x.id for x in cled_users]


def total_reg_ents_bar():
    reo_counts = RegistryEntity.objects.filter(creator_id__in=cled_user_ids).values("schema_id").annotate(Count('schema_id'))
    labels = [Schema.objects.get(id=x['schema_id']).name for x in reo_counts]
    data = [x['schema_id__count'] for x in reo_counts]
    data = dumps(
        {
            'labels': labels,
            'datasets': [{
                'label': '# registered entities',
                'data': data,
                'borderWidth': 1
            }]})
    options = dumps({'scales': {'yAxes': [{'ticks': {'beginAtZero': True}}]}})
    return {'kind': 'bar', 'data': data, 'options': options}


def total_eln_ents_bar():
    entries = Author.objects.filter(user_id__in=cled_user_ids).values("user_id").annotate(Count('user_id'))
    labels = [User.objects.get(id=x['user_id']).name for x in entries]
    data = [x['user_id__count'] for x in entries]
    data = dumps(
        {
            'labels': labels,
            'datasets': [{
                'label': '# eln entries',
                'data': data,
                'borderWidth': 1
            }]})
    options = dumps({'scales': {'yAxes': [{'ticks': {'beginAtZero': True}}]}})
    return {'kind': 'bar', 'data': data, 'options': options}
