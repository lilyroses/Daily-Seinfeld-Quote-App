CREATE TABLE student (
    student_id  INTEGER PRIMARY KEY     NOT NULL,
    class_id    INTEGER NOT NULL,
    FOREIGN KEY(class_id)   REFERENCES class
);

