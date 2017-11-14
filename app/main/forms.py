# encoding=utf8
import sys

reload(sys)
sys.setdefaultencoding('utf8')

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField,SubmitField, SelectMultipleField, TextAreaField, widgets
from wtforms.validators import DataRequired
from app.static.survey.survey import survey


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


class EditSurveyForm(FlaskForm):
    answer_tuples = {}
    categories = survey.keys()
    for category in categories:
        questions = survey[category]
        for question in questions:
            answer_tuples[question] = [(answer, answer) for answer in survey[category][question]]

    community_profile = survey["Community Profile"]
    technology = survey["Technology"]
    work = survey["Work"]
    cleveland = survey["Cleveland"]

    gender = SelectField('Gender', choices=community_profile["Gender"])
    ethnicity = SelectField('Ethnicity', choices=community_profile["Ethnicity"])
    highest_educational_attainment = SelectField('Highest Educational Attainment', choices=community_profile["Highest Educational Attainment"])
    undergraduate_major = SelectField('Undergraduate Major', choices=community_profile["Undergraduate Major"])
    how_you_learned_to_code = MultiCheckboxField('How You Learned to Code', choices=community_profile["How You Learned to Code"])
    primary_programming_languages_used_at_work = MultiCheckboxField('Primary Programming Languages Used at Work', choices=technology["Primary Programming Languages Used at Work"])
    primary_database_technologies_used_at_work = MultiCheckboxField('Primary Database Technologies Used at Work', choices=technology["Primary Database Technologies Used at Work"])
    primary_platforms_used_at_work = MultiCheckboxField('Primary Platforms Used at Work', choices=technology["Primary Platforms Used at Work"])
    primary_development_environments_used_at_work = MultiCheckboxField('Primary Development Environments Used at Work', choices=technology["Primary Development Environments Used at Work"])
    primary_version_control_systems_used_at_work = MultiCheckboxField('Primary Version Control Systems Used at Work', choices=technology["Primary Version Control Systems Used at Work"])
    tech_roles = MultiCheckboxField('Tech Role', choices=work["Tech Roles"])
    years_of_professional_experience = SelectField('Years of Professional Experience', choices=work["Years of Professional Experience"], coerce=int)
    total_compensation = SelectField('Annual Amount Earned From all Tech Activities Combined', choices=work["Total Compensation"])
    satisfaction_with_compensation = SelectField('Satisfaction with Compensation', choices=work["Satisfaction with Compensation"], coerce=int)
    what_you_value_most_in_compensation = MultiCheckboxField("What You Value Most in Compensation", choices=work["What You Value Most in Compensation"])
    how_many_days_per_week_you_work_from_home = SelectField("How Many Days Per Week You Work From Home", choices=work["How Many Days Per Week You Work From Home"], coerce=int)
    company_size = SelectField('Company Size', choices=work["Company Size"])
    total_hours_worked_per_week = SelectField('Total Hours Worked Per Week', choices=work["Total Hours Worked Per Week"], coerce=int)
    job_satisfaction = SelectField('Job Satisfaction', choices=work["Job Satisfaction"], coerce=int)
    a_customer_calls_late_friday_evening = SelectField('A Customer Calls Late Friday Evening', choices=work["A Customer Calls Late Friday Evening"])
    work_life_balance = SelectField('Work Life Balance', choices=work["Work Life Balance"], coerce=int)
    how_you_found_your_current_job = MultiCheckboxField('How You Found Your Current Job', choices=work["How You Found Your Current Job"])
    most_annoying_work_issue = MultiCheckboxField('Most Annoying Work Issue', choices=work["Most Annoying Work Issue"])
    favorite_office_perk = MultiCheckboxField('Favorite Office Perk', choices=work["Favorite Office Perk"])
    what_keeps_you_in_cleveland = MultiCheckboxField('What Keeps You in Cleveland', choices=cleveland["What Keeps You in Cleveland"])
    favorite_cleveland_pro_sports_team = SelectField('Favorite Cleveland Pro Sports Team', choices=cleveland["Favorite Cleveland Pro Sports Team"])
    favorite_cleveland_hangout_area = SelectField('Favorite Cleveland Hangout Area', choices=cleveland["Favorite Cleveland Hangout Area"])
    favorite_cleveland_activity = SelectField('Favorite Cleveland Activity', choices=cleveland["Favorite Cleveland Activity"])
    feedback = TextAreaField('Please provide feedback for the survey')
    submit = SubmitField('Submit')
