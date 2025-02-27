from flask import Flask
from .views import main_views, voice_views, pose_views
from pyfiglet import Figlet

def initialize():
    f = Figlet(font='slant', width=200)
    ascii_art = f.renderText('Team PostProduction')
    print(ascii_art)

def create_app():
    app = Flask(__name__)

    initialize()

    app.register_blueprint(main_views.bp)
    app.register_blueprint(pose_views.bp)
    app.register_blueprint(voice_views.bp)

    return app