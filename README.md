## Project architecture


![alt text](image.png)


Note: this is only a backend project


The API will allow users to register, browse events, RSVP, and manage their attendance. Organisers will be able to create and manage events, and view statistics about their audience.

## Database Setup

To reset or create your local PostgreSQL database using environment settings:

1. Customise your connection details inside `.env.development`.
2. Run the automated wrapper script from the project root:

```bash
./setup_db.sh
```

to make this executable run :

chmod +x setup_db.sh


## How to run db/setup.sql

sudo -u postgres psql -d postgres -f db/setup.sql
