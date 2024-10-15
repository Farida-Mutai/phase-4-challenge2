from app import app
from models import db, Episode, Guest, Appearance

def seed_database():
    with app.app_context():
        # Clear existing data from the tables
        db.session.query(Appearance).delete()
        db.session.query(Guest).delete()
        db.session.query(Episode).delete()
        db.session.commit()

        # Episode data
        episodes_data = [
            {"date": "2023-01-01", "number": 1},
            {"date": "2023-01-02", "number": 2},
            {"date": "2023-01-03", "number": 3},
            {"date": "2023-01-04", "number": 4},
            {"date": "2023-01-05", "number": 5},
            {"date": "2023-01-06", "number": 6},
            {"date": "2023-01-07", "number": 7},
            {"date": "2023-01-08", "number": 8},
            {"date": "2023-01-09", "number": 9},
            {"date": "2023-01-10", "number": 10},  # Fixed duplicate date
        ]

        # Guest data
        guests_data = [
            {"name": "John Doe", "occupation": "Actor"},
            {"name": "Jane Smith", "occupation": "Musician"},
            {"name": "Bob Johnson", "occupation": "Comedian"},
            {"name": "Alice Brown", "occupation": "Author"},
            {"name": "Charlie Davis", "occupation": "Director"},
            {"name": "David Wilson", "occupation": "Writer"},
            {"name": "Emily Thompson", "occupation": "Producer"},
            {"name": "Michael Lee", "occupation": "Screenwriter"},
            {"name": "Sarah Johnson", "occupation": "Sound Designer"},
            {"name": "Jessica Smith", "occupation": "Makeup Artist"},
        ]

        # Seed Episodes
        episodes = []
        for episode_info in episodes_data:
            episode = Episode(date=episode_info['date'], number=episode_info['number'])
            db.session.add(episode)
            episodes.append(episode)

        db.session.commit()  # Commit after adding all episodes

        # Seed Guests
        guests = []
        for guest_info in guests_data:
            guest = Guest(name=guest_info['name'], occupation=guest_info['occupation'])
            db.session.add(guest)
            guests.append(guest)

        db.session.commit()  # Commit after adding all guests

        # Seed Appearances: each guest appears in multiple episodes
        for guest in guests:
            for episode in episodes:
                appearance = Appearance(
                    rating=3,  # Default rating
                    episode_id=episode.id,
                    guest_id=guest.id
                )
                db.session.add(appearance)

        db.session.commit()  # Final commit after adding appearances

        print("Database seeded successfully.")

if __name__ == '__main__':
    seed_database()
