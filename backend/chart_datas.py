from django.db.models import Count
from django.core.serializers.json import DjangoJSONEncoder
from json import dumps
import pandas as pd
from backend.models import User, Team, TeamMember, Author, Batch, BatchSchema, RegistryEntity, EntitySchema, Entry, \
	Schema, Field, FieldDefinition, SchemaField

cled_team = Team.objects.get(name="CHO Cell Line Engineering & Design")
cled_users = User.objects.filter(id__in=[x.user_id for x in TeamMember.objects.filter(team_id=cled_team.id)])
cled_user_ids = [x.id for x in cled_users]


def total_reg_ents_bar():
	reo_counts = RegistryEntity.objects.filter(creator_id__in=cled_user_ids).values("schema_id").annotate(
		Count('schema_id')).order_by('schema_id__count')
	labels = [Schema.objects.get(id=x['schema_id']).name for x in reo_counts]
	data = [x['schema_id__count'] for x in reo_counts]
	data = dumps(
		{
			'labels': labels,
			'datasets': [{
				'label': '# registered entities',
				'data': data,
				'borderWidth': 3
			}]}, cls=DjangoJSONEncoder)
	options = dumps({'scales': {'yAxes': [{'ticks': {'beginAtZero': True}}]}}, cls=DjangoJSONEncoder)
	return {'kind': 'bar', 'data': data, 'options': options}


def total_eln_ents_bar():
	entries = Author.objects.filter(user_id__in=cled_user_ids).values("user_id").annotate(Count('user_id')).order_by('user_id__count')
	labels = [User.objects.get(id=x['user_id']).name for x in entries]
	data = [x['user_id__count'] for x in entries]
	data = dumps(
		{
			'labels': labels,
			'datasets': [{
				'label': '# eln entries',
				'data': data,
				'borderWidth': 3
			}]})
	options = dumps({'scales': {'yAxes': [{'ticks': {'beginAtZero': True}}]}})
	return {'kind': 'bar', 'data': data, 'options': options}


def reg_ents_per_user_line():
	reos = RegistryEntity.objects.filter(creator_id__in=cled_user_ids).values('created_at', 'schema_id')
	df = pd.DataFrame(reos)
	datasets = []
	for sid in df.schema_id.unique():
		sidata = df.query('schema_id == @sid').set_index('created_at') \
			.resample('M').apply({'schema_id': 'count'}).reset_index() \
			.rename(columns={'created_at': 't', 'schema_id': 'y'}).to_dict('records')
		real_name = Schema.objects.get(id=sid).name
		datasets.append({'label': real_name, 'data': sidata})

	data = dumps({'datasets': datasets}, cls=DjangoJSONEncoder)
	options = dumps({
		'scales': {
			'yAxes': [{
				'ticks': {'max': 200}
			}],
			'xAxes': [{
				'type': 'time',
				'time': {
					'unit': 'month'
				}
			}]
		}
	}, cls=DjangoJSONEncoder)
	return {'kind': 'line', 'data': data, 'options': options}


def eln_mods_per_user_line():
	datasets = []
	for cled_user in cled_users:
		entry_id_list = Author.objects.filter(user_id=cled_user.id).values("entry_id")
		entries = Entry.objects.filter(id__in=entry_id_list)
		entry_mod_data = pd.DataFrame(entries.values('modified_at')).set_index('modified_at', drop=False).resample('M').apply({'modified_at': 'count'}).rename(columns={'modified_at': 'y'}).reset_index().rename(columns={'modified_at': 't'}).to_dict('records')
		datasets.append({'label': cled_user.name, 'data': entry_mod_data, 'hidden': True})

	data = dumps({'datasets': datasets}, cls=DjangoJSONEncoder)
	options = dumps({
		'title': {
			'display': True,
			'text': "ELN modifications per month (click names to show)"
		},
		'scales': {
			'xAxes': [{
				'type': 'time',
				'time': {
					'min': pd.Timestamp("2018-10-01T01"),
					'unit': 'month'
				}
			}]
		}
	}, cls=DjangoJSONEncoder)
	return {'kind': 'line', 'data': data, 'options': options}


def cell_line_health():
	# 3 datasets about cell lines
	# 	1 cell lines per person 'Cell Line'= 'ts_PEyIKstK'
	#	2 designs per person 'Cell Line Design' = 'ts_zMfX4a2T'
	#	3 batches per person (should be >= than cell lines 'Cell Line Batch' = 'batsch_XbY4s84i'
	cl_per_person = RegistryEntity.objects.filter(schema_id='ts_PEyIKstK', creator_id__in=cled_user_ids).values('creator_id').annotate(Count('creator_id'))
	cld_per_person = RegistryEntity.objects.filter(schema_id='ts_zMfX4a2T', creator_id__in=cled_user_ids).values('creator_id').annotate(Count('creator_id'))
	clb_per_person = Batch.objects.filter(schema_id='batsch_XbY4s84i', creator_id__in=cled_user_ids).values('creator_id').annotate(Count('creator_id'))
	data = dumps(
		{
			'labels': labels,
			'datasets': [{
				'label': '# eln entries',
				'data': data,
				'borderWidth': 3
			}]})


def very_last():
	# 3 datasets about plasmids
	# 	1 plasmids per person
	#	2 batches per person
	#	3 glycerol stock per person
	pass
