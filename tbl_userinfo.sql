BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "tbl_userinfo" (
	"id"	INTEGER,
	"name"	TEXT,
	"HOD"	TEXT,
	"Department"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);
INSERT INTO "tbl_userinfo" VALUES (1,'John','Jack','EEE');
INSERT INTO "tbl_userinfo" VALUES (2,'James','Oliver','ME');
INSERT INTO "tbl_userinfo" VALUES (3,'Smith','Meera','ECE');
INSERT INTO "tbl_userinfo" VALUES (4,'Tina','Julia','IT');
INSERT INTO "tbl_userinfo" VALUES (5,'Holia','Julia','IT');
COMMIT;
