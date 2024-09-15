CREATE TABLE category(
 category_id INT NOT NULL PRIMARY KEY,
 category_name VARCHAR(30),
 tution_fees INT,
 scholarship_applicable CHAR(1)
);
 
CREATE TABLE department(
 d_id INT NOT NULL PRIMARY KEY,
 d_name VARCHAR(40),
 building VARCHAR(20)
);

CREATE TABLE professor(
 pid INT NOT NULL PRIMARY KEY,
 fname VARCHAR(100),
 lname VARCHAR(100),
 gender CHAR(1),
 email VARCHAR(40),
 phone_no VARCHAR(10),
 salary INT,
 special_status VARCHAR(20),
 d_id INT NOT NULL REFERENCES department(d_id)
);

CREATE TABLE hod(
 hod INT NOT NULL REFERENCES professor(pid),
 d_id INT NOT NULL REFERENCES department(d_id)
);

CREATE TABLE course(
 c_id INT NOT NULL PRIMARY KEY,
 c_name VARCHAR(50),
 credits INT,
 d_id INT NOT NULL REFERENCES department(d_id)
);

CREATE TABLE prerequisite (
    courseID INT NOT NULL REFERENCES course(c_id),
    prerequisiteID INT REFERENCES course(c_id)
);

CREATE TABLE classroom(
    r_id INT NOT NULL,
    building VARCHAR(20) NOT NULL,
    capacity INT,
    CONSTRAINT classroom_pk PRIMARY KEY (r_id),
    CONSTRAINT unique_classroom UNIQUE (r_id, building)
);

CREATE TABLE timeslot(
 t_id INT NOT NULL PRIMARY KEY,
 s_time VARCHAR(10),
 e_time VARCHAR(10),
 t_day VARCHAR(10)
);

CREATE TABLE section(
 s_id INT NOT NULL PRIMARY KEY,
 semester VARCHAR(10),
 c_year INT,
 c_id INT NOT NULL REFERENCES course(c_id),
 faculty INT NOT NULL REFERENCES professor(pid),
 class_time INT NOT NULL REFERENCES timeslot(t_id),
 class_room INT NOT NULL,
 class_building VARCHAR(20) NOT NULL,
 -- Add the foreign key constraints
 CONSTRAINT section_classroom_fk FOREIGN KEY (class_room, class_building) REFERENCES classroom(r_id, building)
);

CREATE TABLE student(
        student_id INT NOT NULL PRIMARY KEY,
        fname VARCHAR(100),
 	lname VARCHAR(100),
	gender CHAR(1),
        email VARCHAR(40),
        phone_no VARCHAR(10),
        batch INT,
        semester VARCHAR(10),
	year INT,
        program varchar(10),
        dob varchar(10),
        fee_status CHAR(1),
        home_address VARCHAR(100),
	tot_credits INT,
        category INT NOT NULL REFERENCES category(category_id),
	faculty_advisor INT NOT NULL REFERENCES professor(pid),
        department INT NOT NULL REFERENCES department(d_id)
);

CREATE TABLE exam(
 exam_date VARCHAR(10) NOT NULL,
 exam_weightage VARCHAR(3),
 exam_type VARCHAR(10),
 class_time INT NOT NULL REFERENCES timeslot(t_id),
 section INT NOT NULL REFERENCES section(s_id),
 class_room INT NOT NULL,
 class_building VARCHAR(20) NOT NULL,
 CONSTRAINT section_classroom_fk FOREIGN KEY (class_room, class_building) REFERENCES classroom(r_id, building),
 faculty_incharge INT NOT NULL REFERENCES professor(pid)
);

CREATE TABLE research_projects(
 project_title VARCHAR(100),
 credits INT,
 semester VARCHAR(10),
 stipend INT,
 students INT NOT NULL REFERENCES student(student_id),
 faculty INT NOT NULL REFERENCES professor(pid)
);

CREATE TABlE takes(
    grade INT,
    attendance_percentage FLOAT,
    section INT NOT NULL REFERENCES section(s_id),
    student INT NOT NULL REFERENCES student(student_id) 
);
