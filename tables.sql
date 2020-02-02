CREATE TABLE _USER(
    Id serial PRIMARY KEY,
    Username VARCHAR(50) UNIQUE NOT NULL,
    PIC bytea);
CREATE TABLE RUSER(
    Id INTEGER PRIMARY KEY,
    Email TEXT UNIQUE NOT NULL,
    Fname VARCHAR(50) ,
    Lname VARCHAR(50) ,
    Pass VARCHAR(50) NOT NULL,
    Gender CHAR(10),
    Bdate DATE,
    Bio VARCHAR(2000) ,
    Phone CHAR(20) UNIQUE,
    City VARCHAR(50),
    Country VARCHAR(50),
    CONSTRAINT RUSER_UID_FKEY FOREIGN KEY (Id)
    REFERENCES _USER(Id) MATCH SIMPLE
    ON UPDATE CASCADE ON DELETE RESTRICT);
CREATE TABLE GUSER(
    Id INTEGER PRIMARY KEY,
    CONSTRAINT GUSER_UID_FKEY FOREIGN KEY (Id)
    REFERENCES _USER(Id) MATCH SIMPLE
    ON UPDATE CASCADE ON DELETE CASCADE);
CREATE TABLE SMEDIA_RUSER(
    Id serial PRIMARY KEY,
    Smedia VARCHAR(20) NOT NULL,
    Link VARCHAR(200) NOT NULL,
    CONSTRAINT SMEDIA_RUSER_UID_FKEY FOREIGN KEY (Id)
    REFERENCES RUSER(Id) MATCH SIMPLE
    ON UPDATE CASCADE ON DELETE CASCADE);
CREATE TABLE AUTHOR(
    Id INTEGER PRIMARY KEY,
    Count_posts INT NOT NULL DEFAULT 0 ,
    CONSTRAINT AUTHOR_UID_FKEY FOREIGN KEY (Id)
    REFERENCES RUSER(Id) MATCH SIMPLE
    ON UPDATE CASCADE ON DELETE RESTRICT);
CREATE TABLE ADMIN(
    Id INTEGER PRIMARY KEY,
    CONSTRAINT ADMIN_U FOREIGN KEY (Id)
    REFERENCES RUSER(Id) MATCH SIMPLE
    ON DELETE RESTRICT);
CREATE TABLE POST(
    P_id serial PRIMARY KEY,
    Subject VARCHAR(100) UNIQUE NOT NULL,
    Date TIMESTAMPTZ NOT NULL,
    TYPE CHAR(20) NOT NULL);
CREATE TABLE POST_TAG(
    P_id serial,
    Tag VARCHAR(50),
    PRIMARY KEY(P_id, Tag),
CONSTRAINT POST_TAG_P_id_FKEY FOREIGN KEY (P_id)
REFERENCES POST(P_id) MATCH SIMPLE
ON UPDATE CASCADE ON DELETE CASCADE);
CREATE TABLE ARTICLE(
    P_id serial PRIMARY KEY,
    CONSTRAINT ARTICLE_P_id_FKEY FOREIGN KEY (P_id)
    REFERENCES POST(P_id) MATCH SIMPLE
    ON UPDATE CASCADE ON DELETE RESTRICT);
CREATE TABLE CONTENT(
    P_id serial,
    Seq_num INT,
    PRIMARY KEY(P_id, Seq_num),
    CONSTRAINT CONTENT_P_id_FKEY FOREIGN KEY (P_id)
    REFERENCES ARTICLE(P_id) MATCH SIMPLE
    ON UPDATE CASCADE ON DELETE CASCADE);
CREATE TABLE PICTURE(
    P_id serial,
    Seq_num INT,
    Caption VARCHAR(100),
    Picture_file BYTEA,
    PRIMARY KEY(P_id, Seq_num),
    CONSTRAINT PICTURE_P_id_Seq_num_FKEY FOREIGN KEY(P_id, Seq_num)
    REFERENCES CONTENT(P_id, Seq_num) MATCH SIMPLE 
    ON UPDATE CASCADE ON DELETE CASCADE);
CREATE TABLE VIDEO(
    P_id serial,
    Seq_num INT,
    Caption VARCHAR(100),
    Video_file VARCHAR(200),
    PRIMARY KEY(P_id, Seq_num),
    CONSTRAINT PICTURE_P_id_Seq_num_FKEY FOREIGN KEY(P_id, Seq_num)
    REFERENCES CONTENT(P_id, Seq_num) MATCH SIMPLE 
    ON UPDATE CASCADE ON DELETE CASCADE);
CREATE TABLE TEXT(
    P_id serial,
    Seq_num INT,
    PRIMARY KEY(P_id, Seq_num),
    CONSTRAINT PICTURE_P_id_Seq_num_FKEY FOREIGN KEY(P_id, Seq_num)
    REFERENCES CONTENT(P_id, Seq_num) MATCH SIMPLE 
    ON UPDATE CASCADE ON DELETE CASCADE);
CREATE TABLE TEXT_CONTENT(
    P_id serial,
    Seq_num INT,
    Script VARCHAR(10000) NOT NULL,
    Language VARCHAR(200) NOT NULL,
    PRIMARY KEY(P_id, Seq_num),
    CONSTRAINT PICTURE_P_id_Seq_num_FKEY FOREIGN KEY(P_id, Seq_num)
    REFERENCES CONTENT(P_id, Seq_num) MATCH SIMPLE 
    ON UPDATE CASCADE ON DELETE CASCADE);
CREATE TABLE VIDEO_POST(
    P_id serial PRIMARY KEY,
    Des VARCHAR(100) NOT NULL,
    Id serial Not NULL,
    Video_file VARCHAR(100) NOT NULL,
    CONSTRAINT VIDEO_POST_P_id_FKEY FOREIGN KEY (P_id)
    REFERENCES POST(P_id) MATCH SIMPLE 
    ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT VIDEO_POST_UID_FKEY FOREIGN KEY (Id)
    REFERENCES ADMIN(Id) MATCH SIMPLE
    ON UPDATE CASCADE ON DELETE CASCADE);
CREATE TABLE VIDEO_SUB(
    P_id serial PRIMARY KEY,
    Languge CHAR(20) NOT NULL,
    Sub_file VARCHAR(100) NOT NULL,
    CONSTRAINT VIDEO_SUB_P_id_FKEY FOREIGN KEY (P_id)
    REFERENCES Video_POST(P_id) MATCH SIMPLE 
    ON UPDATE CASCADE ON DELETE CASCADE);
CREATE TABLE QPOST(
    P_id serial PRIMARY KEY,
    Des VARCHAR(1000) NOT NULL,
    Id serial NOT NULL,
    CONSTRAINT QPOST_P_id_FKEY FOREIGN KEY (P_id)
    REFERENCES POST(P_id) MATCH SIMPLE 
    ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT QPOST_UID_FKEY FOREIGN KEY (Id)
    REFERENCES RUSER(Id) MATCH SIMPLE 
    ON UPDATE CASCADE ON DELETE NO ACTION);
CREATE TABLE ARTICLE_AUTHOR(
    P_id serial ,
    Id serial NOT NULL,
    PRIMARY KEY(P_id, Id),
    CONSTRAINT ARTICLE_AUTHOR_P_id_FKEY FOREIGN KEY (P_id)
    REFERENCES ARTICLE(P_id) MATCH SIMPLE 
    ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT ARTICLE_AUTHOR_UID_FKEY FOREIGN KEY (Id)
    REFERENCES AUTHOR(Id) MATCH SIMPLE 
    ON UPDATE CASCADE ON DELETE NO ACTION);
CREATE TABLE USER_VIEW(
    P_id serial ,
    Id serial NOT NULL,
    PRIMARY KEY(P_id, Id),
    CONSTRAINT USER_VIEW_P_id_FKEY FOREIGN KEY (P_id)
    REFERENCES POST(P_id) MATCH SIMPLE 
    ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT USER_VIEW_UID_FKEY FOREIGN KEY (Id)
    REFERENCES _USER(Id) MATCH SIMPLE 
    ON UPDATE CASCADE ON DELETE CASCADE);
CREATE TABLE USER_LIKE(
    P_id serial ,
    Id serial NOT NULL,
    PRIMARY KEY(P_id, Id),
    Like_Dislike CHAR(10) NOT NULL,
    CONSTRAINT USER_VIEW_P_id_FKEY FOREIGN KEY (P_id)
    REFERENCES POST(P_id) MATCH SIMPLE 
    ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT USER_VIEW_UID_FKEY FOREIGN KEY (Id)
    REFERENCES _USER(Id) MATCH SIMPLE 
    ON UPDATE CASCADE ON DELETE CASCADE);
CREATE TABLE COMMENT(
    P_id serial,
    Id serial,
    Seq_num INT,
    Count_replies INT NOT NULL DEFAULT 0,
    R_flag BOOLEAN NOT NULL,
    PRIMARY KEY(P_id, Id, Seq_num),
    CONSTRAINT COMMENT_P_id_FKEY FOREIGN KEY (P_id)
    REFERENCES POST(P_id) MATCH SIMPLE
    ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT COMMENT_UID_FKEY FOREIGN KEY (Id)
    REFERENCES _USER(Id) MATCH SIMPLE 
    ON UPDATE CASCADE ON DELETE CASCADE);
CREATE TABLE REPLAY(
    P_id serial,
    Id serial,
    Seq_num INT,
    CP_id serial NOT NULL ,
    CUID serial NOT NULL ,
    CSeq_num INT NOT NULL ,
    Count_replies INT NOT NULL DEFAULT 0,
    R_flag BOOLEAN NOT NULL,
    PRIMARY KEY(P_id, Id, Seq_num),
    CONSTRAINT REPLAY_P_id_UID_Seq_num_FKEY FOREIGN KEY(P_id, Id, Seq_num)
    REFERENCES COMMENT(P_id,Id,Seq_num) MATCH SIMPLE 
    ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT REPLAY_CP_id_CUID_CSeq_num_FKEY FOREIGN KEY(CP_id, CUID, CSeq_num)
    REFERENCES COMMENT(P_id,Id,Seq_num) MATCH SIMPLE 
    ON UPDATE CASCADE ON DELETE CASCADE);
CREATE VIEW V_USERS AS
    SELECT _user.id as id, email,fname,lname,pass,gender,bdate,pic,bio,ADMIN.id as ADMIN,
    AUTHOR.id as AUTHOR
    FROM _USER LEFT JOIN RUSER ON _USER.id=RUSER.id
    LEFT JOIN ADMIN ON ADMIN.id=_USER.id
    LEFT JOIN AUTHOR ON AUTHOR.id=_USER.id;






    



