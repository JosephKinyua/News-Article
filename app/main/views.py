from flask import render_template
from . import main
from ..requests import get_sources

@main.route('/')
def index():
    general_source = get_sources('general')
    business_source = get_sources('business')
    ent_source = get_sources('entertainment')
    health_source = get_sources('health')
    science_source = get_sources('science')
    sport_source = get_sources('sports')
    tech_source = get_sources('technology')
    
    return render_template('index.html', general = general_source, business= business_source, enterain = ent_source, health = health_source, science = science_source, sport = sport_source, tech = tech_source)

@main.route('/news/<id>')
def newsDetail(id):
    
    news = newsDetail(id)
    return render_template('news.html', news = news)