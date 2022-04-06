CREATE TABLE entries (
	entry_id int NOT NULL,
    start_date DATE NOT NULL,
    start_time TIME NOT NULL,
    distance int(5) NOT NULL,
    distance_freestyle int(5),
    distance_breast int(5),
    duration int(4),
    comment TEXT,
    PRIMARY KEY(entry_id)
)