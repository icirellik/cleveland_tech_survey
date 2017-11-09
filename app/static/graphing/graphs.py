import json
import plotly

from app.static.graphing import graph_tools
from app.static.graphing.graph_tools import COLORS as color
from app.static.survey.survey_questions_and_answers import survey_questions_and_answers


def gender_by_percent(pd_series):
    title = 'Gender by Percent'
    colors = color['cavaliers'].values() + ['#d3d3d3']
    return graph_tools.generate_pie_chart_percentage_dict(title=title, colors=colors, pd_series=pd_series)


def salary_for_years_of_exp(pd_series):
    title = 'Compensation for Years of Professional Experience'
    sal_exp = (pd_series.replace('[\$,)]', '', regex=True).replace('[(]', '-', regex=True).astype(float))
    x = sal_exp['annual_amount_earned_from_all_tech_activities_combined']
    y = sal_exp['years_of_professional_experience']
    mode = 'markers'
    xaxis_title = 'Total Compensation'
    yaxis_title = 'Years of Professional Experience'
    return graph_tools.generate_non_pie_chart_dict(title=title, x=x, y=y, mode=mode, xaxis_title=xaxis_title,
                                                   yaxis_title=yaxis_title, color=color['indians']['red'],
                                                   line_color=color['indians']['navy'])


def get_chart_ids_and_titles():
    return tuple((i, title) for i, title in enumerate(survey_questions_and_answers.keys()))


def get_title_and_df_key_from_tab_value(tab_value):
    title = tab_value.replace('"', '')
    df_key = tab_value.replace('"', '').lower().replace(' ', '_')
    return title, df_key


def get_graph_dict(title, pd_series, colors=None, suffix=None, yaxis_title=None):
    if colors:
        chart_dict = graph_tools.generate_pie_chart_percentage_dict(title=title, pd_series=pd_series, colors=colors, suffix=suffix)
    chart_dict = graph_tools.generate_horizontal_line_chart_dict(title=title, pd_series=pd_series, yaxis_title=yaxis_title)
    return json.dumps(chart_dict, cls=plotly.utils.PlotlyJSONEncoder)
