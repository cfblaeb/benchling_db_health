from django.urls import path
from django.views.generic import TemplateView
from backend.chart_datas import total_reg_ents_bar, total_eln_ents_bar


# this need to change...otherwise I think it will only retrieve data when the server starts and then never update it...
urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html", extra_context={
        'context_charts': {
            'total_reg_ents_bar': total_reg_ents_bar(),  
            'total_eln_ents_bar': total_eln_ents_bar()
        }
    }))
]
