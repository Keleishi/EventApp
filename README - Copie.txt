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