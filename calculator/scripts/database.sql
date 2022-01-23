DROP TABLE user

CREATE TABLE user (
	id INTEGER PRIMARY KEY,
	username TEXT NOT NULL UNIQUE,
	email_address TEXT NOT NULL UNIQUE,
	password_hash TEXT NOT NULL ,
	budget INTEGER NOT NULL
);

DROP TABLE tracking_history

CREATE TABLE tracking_history (
	id INTEGER PRIMARY KEY,
	tracking_date TEXT NOT NULL,
	budget INTEGER,
	intake INTEGER,
	expenditure INTEGER,
	userid INTEGER NOT NULL,
	FOREIGN KEY (userid)
       REFERENCES user (id),
	UNIQUE(userid, tracking_date)
);

