DROP TABLE IF EXISTS ;
CREATE TABLE contact_info (
  Name TEXT NOT NULL,
  surname Text NOT NULL,
  Email varchar(55) UNIQUE NOT NULL PRIMARY KEY,
  cell_no  INT NOT NULL,
  subject TEXT NOT NULL,
  message TEXT NOT NULL
  );

SELECT * FROM contact_info;
