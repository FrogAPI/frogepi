create table apikey(
    id integer primary key,
    hashing varchar(64),
    UNIQUE (hashing) ON CONFLICT IGNORE
);