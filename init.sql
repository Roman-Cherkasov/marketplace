-- CREATE DATABASE marketplace;
CREATE SCHEMA IF NOT EXISTS main;
-- CREATE TABLE IF NOT EXISTS main.users (id BIGINT PRIMARY KEY NOT NULL,
CREATE TABLE IF NOT EXISTS main.users (id SERIAL PRIMARY KEY NOT NULL,
                                login TEXT NOT NULL,
                                password TEXT NOT NULL);
-- CREATE TABLE IF NOT EXISTS main.content (id BIGINT PRIMARY KEY NOT NULL,
CREATE TABLE IF NOT EXISTS main.content (id SERIAL PRIMARY KEY NOT NULL,
                                name TEXT NOT NULL,
                                category INT NOT NULL,
                                description TEXT);                       
-- CREATE TABLE IF NOT EXISTS main.subscriptions (user_id BIGINT REFERENCES main.users(id) NOT NULL,
CREATE TABLE IF NOT EXISTS main.subscriptions (user_id SERIAL REFERENCES main.users(id) NOT NULL,
                            -- content_id BIGINT REFERENCES main.content(id) NOT NULL);
                                content_id SERIAL REFERENCES main.content(id) NOT NULL);