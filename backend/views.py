from django.views.generic import TemplateView
from backend.chart_datas import total_reg_ents_bar, total_eln_ents_bar, reg_ents_per_user_line


class ChartView(TemplateView):
	template_name = "index.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['context_charts'] = {
			'total_reg_ents_bar': total_reg_ents_bar(),
			'total_eln_ents_bar': total_eln_ents_bar(),
			'reg_ents_per_user_line': reg_ents_per_user_line()
		}
		return context
