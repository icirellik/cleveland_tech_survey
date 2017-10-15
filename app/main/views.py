from flask import render_template, redirect, url_for, abort, flash
from flask_login import login_required, current_user
from . import main
from .forms import EditProfileForm, EditProfileAdminForm, EditSurveyForm
from .. import db
from ..models import Role, User
from ..decorators import admin_required
from ..survey_questions_and_answers import survey_questions_and_answers, labels


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        abort(404)
    return render_template('user.html', user=user)


@main.route('/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.location = form.location.data
        current_user.about_me = form.about_me.data
        db.session.add(current_user)
        flash('Your profile has been updated.')
        return redirect(url_for('.user', username=current_user.username))
    form.name.data = current_user.name
    form.location.data = current_user.location
    form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', form=form)


@main.route('/edit-profile/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_profile_admin(id):
    user = User.query.get_or_404(id)
    form = EditProfileAdminForm(user=user)
    if form.validate_on_submit():
        user.email = form.email.data
        user.username = form.username.data
        user.confirmed = form.confirmed.data
        user.role = Role.query.get(form.role.data)
        user.name = form.name.data
        user.location = form.location.data
        user.about_me = form.about_me.data
        db.session.add(user)
        flash('The profile has been updated.')
        return redirect(url_for('.user', username=user.username))
    form.email.data = user.email
    form.username.data = user.username
    form.confirmed.data = user.confirmed
    form.role.data = user.role_id
    form.name.data = user.name
    form.location.data = user.location
    form.about_me.data = user.about_me
    return render_template('edit_profile.html', form=form, user=user)


@main.route('/survey/<username>')
def survey(username):
    user = User.query.filter_by(username=username).first()
    # jobs = user.jobs.split('|')
    # years_of_pro_exp = user.years_of_pro_exp
    # gender = user.gender
    # ethnicity = user.ethnicity
    #
    # answers = []
    # answers.append(user.jobs.split('|'))
    # answers.append([user.years_of_pro_exp])
    # answers.append([user.gender])
    # answers.append([user.ethnicity])
    #
    # labels = []
    # labels.append('Jobs')
    # labels.append('Years of Professional Experience')
    # labels.append('Gender')
    # labels.append('Ethnicity')
    #
    # questions_and_answers = zip(labels, answers)

    questions = survey_questions_and_answers.keys()

    if user is None:
        abort(404)
    # return render_template('survey.html', user=user, questions_and_answers=questions_and_answers)
    return render_template('survey.html', user=user, questions=questions, labels=labels)


@main.route('/edit-survey', methods=['GET', 'POST'])
@login_required
def edit_survey():
    form = EditSurveyForm()
    if form.validate_on_submit():
        current_user.jobs = '|'.join(form.jobs.data)
        current_user.years_of_pro_exp = form.years_of_pro_exp.data
        current_user.gender = form.gender.data
        current_user.ethnicity = form.ethnicity.data
        db.session.add(current_user)
        flash('Thanks for updating your survey responses!')
        return redirect(url_for('.survey', username=current_user.username))
    form.jobs.data = current_user.jobs
    form.years_of_pro_exp = current_user.years_of_pro_exp
    form.gender = current_user.gender
    form.ethnicity = current_user.ethnicity
    return render_template('edit_survey.html', form=form)


# TODO: add admin-edit-survey
