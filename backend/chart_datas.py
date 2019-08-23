from django.db.models import Count
from django.core.serializers.json import DjangoJSONEncoder
from json import dumps
import pandas as pd
from backend.models import User, Team, TeamMember, Author, Batch, RegistryEntity, Entry, Schema


def get_team(team_name):
	team_object = Team.objects.get(name=team_name)
	team_users = User.objects.filter(id__in=[x.user_id for x in TeamMember.objects.filter(team_id=team_object.id)])
	team_user_ids = [x.id for x in team_users]
	return team_users


def total_reg_ents_bar(team_name):
	team_users = get_team(team_name)
	team_user_ids = [x.id for x in team_users]
	reo_counts = RegistryEntity.objects.filter(creator_id__in=team_user_ids).values("schema_id").annotate(
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


def total_eln_ents_bar(team_name):
	team_users = get_team(team_name)
	team_user_ids = [x.id for x in team_users]
	entries = Author.objects.filter(user_id__in=team_user_ids).values("user_id").annotate(Count('user_id')).order_by('user_id__count')
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


def reg_ents_per_user_line(team_name):
	team_users = get_team(team_name)
	team_user_ids = [x.id for x in team_users]
	reos = RegistryEntity.objects.filter(creator_id__in=team_user_ids).values('created_at', 'schema_id')
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


def eln_mods_per_user_line(team_name):
	team_users = get_team(team_name)
	datasets = []
	for cled_user in team_users:
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


def cell_line_health(team_name):
	"""
	3 datasets about cell lines
		1 cell lines per person 'Cell Line'= 'ts_PEyIKstK'
		1 designs per person 'Cell Line Design' = 'ts_zMfX4a2T'
		3 batches per person (should be >= than cell lines 'Cell Line Batch' = 'batsch_XbY4s84i'
	:param team_name:
	:return:
	"""

	team_users = get_team(team_name)
	team_user_ids = [x.id for x in team_users]
	cl_per_person = pd.DataFrame(RegistryEntity.objects.filter(schema_id='ts_PEyIKstK', creator_id__in=team_user_ids).values('creator_id').annotate(Count('creator_id'))).set_index('creator_id').rename(columns={'creator_id__count': 'cl'})
	cld_per_person = pd.DataFrame(RegistryEntity.objects.filter(schema_id='ts_zMfX4a2T', creator_id__in=team_user_ids).values('creator_id').annotate(Count('creator_id'))).set_index('creator_id').rename(columns={'creator_id__count': 'cld'})
	clb_per_person = pd.DataFrame(Batch.objects.filter(schema_id='batsch_XbY4s84i', creator_id__in=team_user_ids).values('creator_id').annotate(Count('creator_id'))).set_index('creator_id').rename(columns={'creator_id__count': 'clb'})
	df = pd.concat([cl_per_person, cld_per_person, clb_per_person], axis=1, sort=True).fillna(0)

	data = dumps(
		{
			'labels': list(df.index.map({x.id: x.name for x in team_users})),
			'datasets': [
				{
					'label': 'cell line',
					'data': df['cl'].to_list(),
					'borderWidth': 3
				},
				{
					'label': 'cell line design',
					'data': df['cld'].to_list(),
					'borderWidth': 3
				},
				{
					'label': 'cell line batch',
					'data': df['clb'].to_list(),
					'borderWidth': 3
				},
			]}, cls=DjangoJSONEncoder)
	options = dumps({'scales': {'yAxes': [{'ticks': {'max': 200, 'beginAtZero': True}}]}}, cls=DjangoJSONEncoder)
	return {'kind': 'bar', 'data': data, 'options': options}


def plasmid_health(team_name):
	"""
	3 datasets about plasmids
		1 plasmids per person  'Plasmid' 'ts_tF400h5Z'
		2 batches per person	'Plasmid Batch'  'batsch_bkooLwF9'
		3 glycerol stock per person	 , Strain'  'ts_ldSnOj6A'
	:param team_name:
	:return:
	"""

	team_users = get_team(team_name)
	team_user_ids = [x.id for x in team_users]
	pl_per_person = pd.DataFrame(RegistryEntity.objects.filter(schema_id='ts_tF400h5Z', creator_id__in=team_user_ids).values('creator_id').annotate(Count('creator_id'))).set_index('creator_id').rename(columns={'creator_id__count': 'pl'})
	plb_per_person = pd.DataFrame(Batch.objects.filter(schema_id='batsch_bkooLwF9', creator_id__in=team_user_ids).values('creator_id').annotate(Count('creator_id'))).set_index('creator_id').rename(columns={'creator_id__count': 'plb'})
	str_per_person = pd.DataFrame(RegistryEntity.objects.filter(schema_id='ts_ldSnOj6A', creator_id__in=team_user_ids).values('creator_id').annotate(Count('creator_id'))).set_index('creator_id').rename(columns={'creator_id__count': 'strain'})
	df = pd.concat([pl_per_person, plb_per_person, str_per_person], axis=1, sort=True).fillna(0)

	data = dumps(
		{
			'labels': list(df.index.map({x.id: x.name for x in team_users})),
			'datasets': [
				{
					'label': 'Plasmid',
					'data': df['pl'].to_list(),
					'borderWidth': 3
				},
				{
					'label': 'Plasmid Batch',
					'data': df['plb'].to_list(),
					'borderWidth': 3
				},
				{
					'label': 'Glycerol stock',
					'data': df['strain'].to_list(),
					'borderWidth': 3
				},
			]}, cls=DjangoJSONEncoder)
	options = dumps({'scales': {'yAxes': [{'ticks': {'max': 50, 'beginAtZero': True}}]}}, cls=DjangoJSONEncoder)
	return {'kind': 'bar', 'data': data, 'options': options}
