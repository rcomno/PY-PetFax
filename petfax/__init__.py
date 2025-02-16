from flask import Flask
#app factory
def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello():
        return 'Hello petfax!'

    #importing/registering the blue print
    from . import pet
    app.register_blueprint(pet.bp)
    
    return app