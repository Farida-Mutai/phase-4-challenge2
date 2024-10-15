from app import app
from model import db, Episode, Guest, Appearance
from datetime import datetime

def seed_database():
    with app.app_context():
        
        # Clear existing data
        db.session.query(Appearance).delete()
        db.session.query(Guest).delete()
        db.session.query(Episode).delete()
        db.session.commit()

        # Create sample episode data
        episodes_data = [
            {"title": "Episode 1", "air_date": "2023-01-01"},
            {"title": "Episode 2", "air_date": "2023-01-02"},
            {"title": "Episode 3", "air_date": "2023-01-03"},
            {"title": "Episode 4", "air_date": "2023-01-04"},
            {"title": "Episode 5", "air_date": "2023-01-05"},
        ]

        guests_data = [
            {"name": "John Doe", "profession": "Actor"},
            {"name": "Jane Smith", "profession": "Musician"},
            {"name": "Bob Johnson", "profession": "Comedian"},
            {"name": "Alice Brown", "profession": "Author"},
            {"name": "Charlie Davis", "profession": "Director"}
        ]

        # Add episodes to the database
        episodes = []
        for episode_info in episodes_data:
            episode = Episode(
                title=episode_info['title'],
                air_date=datetime.strptime(episode_info['air_date'], '%Y-%m-%d').date()
            )
            db.session.add(episode)
            episodes.append(episode)
        
        db.session.commit()  # Commit to get the IDs of the episodes

        # Add guests to the database
        guests = []
        for guest_info in guests_data:
            guest = Guest(name=guest_info['name'], profession=guest_info['profession'])
            db.session.add(guest)
            guests.append(guest)

        db.session.commit()  # Commit to get the IDs of the guests

        # Add appearances to the database
        for i, guest in enumerate(guests):
            for episode in episodes:
                appearance = Appearance(
                    rating=round(2.5 + i * 0.5, 1),  # Just a random rating for the appearance
                    episode_id=episode.id,
                    guest_id=guest.id
                )
                db.session.add(appearance)
        
        db.session.commit()

        print("Database seeded successfully!")

if __name__ == '__main__':
    seed_database()
