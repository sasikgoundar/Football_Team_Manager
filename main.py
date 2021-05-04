from tkinter import *
import sqlite3

conn = sqlite3.connect("football_teams_data.db")
cursor = conn.cursor()

def exot():
    exit(0)

#Create Table Agent
cursor.execute('CREATE TABLE AGENTS(NAME varchar(40),'
               'NATIONALITY VARCHAR(20),'
               'RATING NUMBER(2),'
               'PRIMARY KEY (NAME))')

#Create Table Clubs
cursor.execute('CREATE TABLE CLUBS (CLUB_ID number (2) NOT NULL, '
               'CLUB_NAME varchar (30) NOT NULL, '
               'CLUB_RATING number (2), '
               'CLUB_MANAGER varchar (30), '
               'CLUB_CHAIRMAN varchar (30), '
               'LEAGUE varchar (30), '
               'CLUB_TITLEs number (2), '
               'YEAr_FOUNDED number (4), '
               'PRIMARY KEY (CLUB_NAME))')

#Create Table Nationals
cursor.execute('CREATE TABLE NATIONALS(NATION varchar(20),'
               'MANAGER varchar(30),'
               'WORLD_CUP_WON number(2),'
               'RATING number(2),'
               'primary key (NATION))')

#Create Table Players
cursor.execute('CREATE TABLE PLAYERS(FIRST_NAME VARCHAR(20) NOT NULL,'
               'LAST_NAME VARCHAR(20),'
               'NATIONALITY VARCHAR(20),'
               'CLUB__NAME varchar(30),'
               'AGE NUMBER(2),YEARS_AT_CLUB NUMBER(2),'
               'AGENT_NAME VARCHAR(40),'
               'RATING NUMBER(2),'
               'POSITION VARCHAR(4),'
               'FOREIGN KEY(CLUB__NAME) REFERENCES CLUBS(CLUB_NAME),'
               'FOREIGN KEY(AGENT_NAME) REFERENCES AGENTS(NAME),'
               'FOREIGN KEY(NATIONALITY) REFERENCES NATIONALS(NATION))')