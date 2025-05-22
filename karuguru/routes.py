from flask import Blueprint, render_template, send_from_directory
import os


main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def home():
    return render_template('home.html')

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/junior_secondary')
def junior_secondary():
    return render_template('junior_secondary.html')

@main.route('/boarding')
def boarding():
    return render_template('boarding.html')

@main.route('/admissions')
def admissions():
    return render_template('admissions.html')

@main.route('/bus_routes')
def bus_routes():
    return render_template('bus_routes.html')

@main.route('/school_uniform')
def school_uniform():
    return render_template('school_uniform.html')

@main.route('/contact')
def contact():
    return render_template('contact.html')

@main.route('/primary_school')
def primary_school():
    return render_template('primary_school.html')

@main.route('/upper_school')
def upper_school():
    return render_template('upper_school.html')

@main.route('/clubs')
def clubs():
    return render_template('clubs.html')

@main.route('/sports')
def sports():
    return render_template('sports.html')

@main.route('/download-fees-pdf')
def download_fees_pdf():
    # The PDF should be stored in the static/pdfs directory
    return send_from_directory('static/pdfs', 'school_fees.pdf', as_attachment=True)

