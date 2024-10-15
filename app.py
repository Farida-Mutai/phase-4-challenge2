from flask import Flask, request, make_response, jsonify
from flask_migrate import Migrate
from flask_restful import Api, Resource
from models import db, Episode, Guest, Appearance

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lateshow.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

#Define the homepage.
@app.route('/')
def home():
    return make_response("""
    <h1>Welcome to the Late Show </h1>
    
    """, 200)

class Episodes(Resource):
    #retrive all episodes in the database and return them as a json response.
    def get(self):
        episodes = [episode.to_dict() for episode in Episode.query.all()]
        return make_response(jsonify(episodes), 200)

class EpisodeById(Resource):
    #retrieve a specific episode by id from the database and return it as a json response.
    def get(self, id):
        episode = Episode.query.get(id)
        if episode:
            episode_dict = episode.to_dict()
            episode_dict['appearances'] = [appearance.to_dict() for appearance in episode.appearances]
            return make_response(jsonify(episode_dict), 200)
        else:
            return make_response(jsonify({"error": "Episode not found"}), 404)

class Guests(Resource):
    #retrive all guests in the database and return them as a json response.
    def get(self):
        guests = [guest.to_dict() for guest in Guest.query.all()]
        return make_response(jsonify(guests), 200)

class Appearances(Resource):
    #add a new appearance to the database and return the new appearance as a json response.
    def post(self):
        try:
            data = request.get_json()
            new_appearance = Appearance(
                rating=data['rating'],
                episode_id=data['episode_id'],
                guest_id=data['guest_id']
            )
            db.session.add(new_appearance)
            db.session.commit()
            return make_response(jsonify(new_appearance.to_dict()), 201)
        except Exception as e:
            return make_response(jsonify({"errors": [str(e)]}), 400)

#define the endpoints and their corresponding resources.
api.add_resource(Episodes, '/episodes' )
api.add_resource(EpisodeById, '/episodes/<int:id>')
api.add_resource(Guests, '/guests')
api.add_resource(Appearances, '/appearances')

if __name__ == '__main__':
    app.run(port=5555, debug=True)