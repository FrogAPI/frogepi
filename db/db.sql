create table quote(
    id integer primary key,
    auteur varchar(50),
    quote varchar(500),
    UNIQUE (auteur) ON CONFLICT IGNORE
);