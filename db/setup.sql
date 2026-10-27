DROP TABLE IF EXISTS Rsvps;
DROP TABLE IF EXISTS Events;
DROP TABLE IF EXISTS Venues;
DROP TABLE IF EXISTS Users;

CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    name VARCHAR(255) NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE Venues (
    venue_id SERIAL PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL,
    address TEXT,
    capacity INT
);

CREATE TABLE Events (
    event_id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description VARCHAR(255),
    starts_at TIMESTAMPTZ NOT NULL,
    ends_at TIMESTAMPTZ NOT NULL,
    organiser_id INT REFERENCES Users(user_id),
    venue_id INT REFERENCES Venues(venue_id),
    created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE Rsvps (
    rsvp_id SERIAL PRIMARY KEY,
    attendee_id INT NOT NULL REFERENCES Users(user_id),
    event_id INT NOT NULL REFERENCES Events(event_id),
    created_at TIMESTAMPTZ DEFAULT NOW()
);