The purpose of GalaGo is to help users manage and promote their events.
The application is designed to make it easy for organizers to create events and for attendees to find and participate
in events that interest them. With features such as event creation, event updates, event deletion, event listings,
and event details, users can easily manage their events and keep track of attendee participation.

I decided to use five models - Organizer, Event, Attendee, Category, and EventCategory.
These models represent the main entities in our system - organizers who create events, events that are created,
attendees who participate in the events, categories to which the events belong, and the relationship between events
and categories.

Once the data models were in place, I built the views and templates for the application. This involved creating
the necessary HTML templates and defining the various views that were required to create, update, delete and display events.
I also implemented forms for user input and validation.

Testing with the database was particularly important, especially with the integration of MySQL. I ran various tests to make sure that the data models were correctly defined and that the data was being stored and retrieved as expected.

Recently, I have added a new feature to the application - a system of login. This will allow organizers and attendees to have their own accounts.

To implement this feature, I added a new model called User, which represents the user accounts. I also created the necessary views and templates for user registration, login, and profile management. The authentication and authorization process was implemented using Django's built-in authentication system and access control mechanisms.

With this new feature, "GalaGo" has become a more comprehensive and user-friendly application for event management.


// NEW FOR CA3 //

I have added both manual and automated testing to ensure the quality and correctness of the application.

The testing methodology for the Organizer model in this application includes both manual and automatic tests. The automatic tests were implemented using the Django test framework and cover various aspects of the Organizer model, such as the correct labeling of its fields, the maximum length of its fields, and the correct string representation of the object. Additionally, both positive and negative tests were implemented to ensure that the model correctly handles valid and invalid data.

In terms of test coverage, the Organizer model tests cover the majority of the functionality of the model. However, further tests can be added in the future to ensure even better test coverage.

Furthermore, I have configured the system to use a configuration file for development and another file for testing. This allows for easy and efficient testing, as the test configuration file can be set up to use a separate database and other settings from the development configuration file. This separation of concerns ensures that the tests are conducted in an isolated environment and do not affect the development environment.

We can run the tests by using : py runtests.py test

