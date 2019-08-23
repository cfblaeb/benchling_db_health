from django.views.generic import TemplateView
from backend.chart_datas import total_reg_ents_bar, total_eln_ents_bar, reg_ents_per_user_line, eln_mods_per_user_line, cell_line_health, plasmid_health


class ChartView(TemplateView):
	template_name = "index.html"
	team_name = None

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['context_charts'] = {
			'total_reg_ents_bar': total_reg_ents_bar(self.team_name),
			'total_eln_ents_bar': total_eln_ents_bar(self.team_name),
			'reg_ents_per_user_line': reg_ents_per_user_line(self.team_name),
			'eln_mods_per_user_line': eln_mods_per_user_line(self.team_name),
			'cell_line_health': cell_line_health(self.team_name),
			'plasmid_health': plasmid_health(self.team_name)
		}
		return context
