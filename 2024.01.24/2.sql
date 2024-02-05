drop database if exists mus_library;
create database mus_library;
use mus_library;

create table genres (
    id tinyint unsigned primary key auto_increment,
    title varchar(32) not null unique
);

create table singers (
    id smallint unsigned primary key auto_increment,
    name varchar(64) not null unique
);

create table publishers (
    id tinyint unsigned primary key auto_increment,
    title varchar(64) not null unique,
    country varchar(32) not null
);
 
create table collections (
    id smallint unsigned primary key auto_increment,
    dt_release date not null,
    publisher_id tinyint unsigned not null
        references publishers (id)
        on update cascade
        on delete restrict
);

create table songs ( 
    id int unsigned primary key auto_increment, 
    title varchar(32) not null, 
    singer_id smallint unsigned not null references singers (id), 
    genre_id tinyint unsigned not null references genres (id), 
    duration time not null 
);

create table collection_song (
    collection_id smallint unsigned not null
    references collections (id),
    song_id int unsigned not null
    references songs (id),
    primary key (collection_id, song_id)
);
