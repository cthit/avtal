CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE event (
    id uuid,
    hubbit DATE,
    bookit DATE,
)