###Late Show API***

This is a simple API for managing episodes, guests, and their appearances on a show, built with Flask, Flask-SQLAlchemy, and Flask-RESTful. It includes functionality to retrieve episodes and guests, and create appearances, along with database seeding to pre-populate sample data.

####Features

Fetch all episodes and specific episodes by ID
Fetch all guests
Create guest appearances on episodes with rating validation
Supports relational data fetching between episodes, guests, and appearances
Implements cascading deletes and validation checks



Configure the Database:

Open app.py and configure your SQLALCHEMY_DATABASE_URI to use SQLite (or any other database if needed):

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lateshow.db'


Initialize the database:

flask db init
flask db migrate
flask db upgrade


Run the Flask server:

python app.py



####Database Models

The models for this API are structured as follows:

**Episode: Represents a TV episode with an air date and episode number.
**Guest: Represents a guest who appears on various episodes.
**Appearance: Represents the relationship between an episode and a guest, including the rating of the guest's appearance on the episode.


###Relationships
An Episode has many Guests through Appearance.
A Guest has many Episodes through Appearance.
An Appearance belongs to both an Episode and a Guest.


###Validations
Appearance Model

rating: Must be between 1 and 5 (inclusive). If the rating is outside this range, the request to create a new appearance will fail with validation errors.

###contacts
Incase of any issue,compliment on where i can improve reach me out on my email address farida.mutai@student.moringaschool.com
You can pull your changes in my github reachable repository https://github.com/Farida-Mutai/phase-4-challenge2

