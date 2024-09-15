import psycopg2

# Function to connect to the PostgreSQL database
def connect_to_database():
    try:
        conn = psycopg2.connect(
            database='iitdhdb',
            host='localhost',
            user='postgres',
            password='123456',
            port=5432
        )
        return conn
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL:", error)
        return None

# Function to validate admin authentication
def admin_authenticate():
    admin_password = "acadadmin123"  # Replace with your admin password
    entered_password = input("Enter admin password: ")
    return entered_password == admin_password

# Function to add a new student
def add_student(conn, student_id, fname, lname, gender, email, phone_no, batch, program, dob, semester, year, tot_credits, fee_status, home_address, category, faculty_advisor, department):
    try:
        cursor = conn.cursor()

        # Check if the admin is authenticated
        if not admin_authenticate():
            print("Admin authentication failed. Access denied.")
            return

        # Check if the student already exists in the database
        cursor.execute("SELECT student_id FROM student WHERE student_id = %s", (student_id,))
        existing_student = cursor.fetchone()

        if existing_student:
            print("Output: Student ID already exists")
        else:
            # Insert the new student details into the student table
            cursor.execute(
                "INSERT INTO student (student_id, fname, lname, gender, email, phone_no, batch, program, dob, semester, year, tot_credits, fee_status, home_address, category, faculty_advisor, department) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (student_id, fname, lname, gender, email, phone_no, batch, program, dob, semester, year, tot_credits, fee_status, home_address, category, faculty_advisor, department)
            )

            conn.commit()
            print("Output: Student details inserted into the student table successfully")

        cursor.close()
    except (Exception, psycopg2.Error) as error:
        print("Error while adding a student:", error)

# Function to add a new department
def add_department(conn, d_id, d_name, building, hod):
    try:
        cursor = conn.cursor()

        # Check if the admin is authenticated
        if not admin_authenticate():
            print("Admin authentication failed. Access denied.")
            return

        # Check if the department already exists in the database
        cursor.execute("SELECT d_id FROM department WHERE d_id = %s", (d_id,))
        existing_department = cursor.fetchone()

        if existing_department:
            print("Output: Department ID already exists")
        else:
            # Insert the new department details into the department table
            cursor.execute(
                "INSERT INTO department (d_id, d_name, building) VALUES (%s, %s, %s)",
                (d_id, d_name, building)
            )
            if hod !=0:
                cursor.execute(
                    "INSERT INTO hod (d_id, hod) VALUES (%s, %s)",
                    (d_id, hod)
                )
            conn.commit()
            print("Output: Department details inserted into the department table successfully")

        cursor.close()
    except (Exception, psycopg2.Error) as error:
        print("Error while adding a department:", error)

# Function to add a new professor to a specific department
def add_professor(conn, pid, fname, lname, gender, email, phone_no, salary, special_status, d_id):
    try:
        cursor = conn.cursor()

        # Check if the admin is authenticated
        if not admin_authenticate():
            print("Admin authentication failed. Access denied.")
            return

        # Check if the department exists
        cursor.execute("SELECT pid FROM professor WHERE pid = %s", (pid,))
        existing_professor = cursor.fetchone()

        if existing_professor:
            print("Output: Professor ID already exists")
        else:
            # Insert the new professor details into the professor table
            cursor.execute(
                "INSERT INTO professor (pid, fname, lname, gender, email, phone_no, salary, special_status, d_id) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (pid, fname, lname, gender, email, phone_no, salary, special_status, d_id)
            )

            conn.commit()
            print("Output: Professor details inserted into the professor table successfully")

        cursor.close()
    except (Exception, psycopg2.Error) as error:
        print("Error while adding a professor:", error)

# Function to add a new course
def add_course(conn, c_id, c_name, credits, d_id):
    try:
        cursor = conn.cursor()

        # Check if the admin is authenticated
        if not admin_authenticate():
            print("Admin authentication failed. Access denied.")
            return

        # Check if the course already exists in the database
        cursor.execute("SELECT c_id FROM course WHERE c_id = %s", (c_id,))
        existing_course = cursor.fetchone()

        if existing_course:
            print("Output: Course ID already exists")
        else:
            # Insert the new course details into the course table
            cursor.execute(
                "INSERT INTO course (c_id, c_name, credits, d_id) VALUES (%s, %s, %s, %s)",
                (c_id, c_name, credits, d_id)
            )

            conn.commit()
            print("Output: Course details inserted into the course table successfully")

        #cursor.close()
    except (Exception, psycopg2.Error) as error:
        print("Error while adding a course:", error)

def add_prerequisite(conn, course_id, prereq_id):
    try:
        cursor = conn.cursor()

        # Check if the admin is authenticated
        if not admin_authenticate():
            print("Admin authentication failed. Access denied.")
            return

        # Check if the course and prerequisite exist in the database
        cursor.execute("SELECT c_id FROM course WHERE c_id = %s", (course_id,))
        existing_course = cursor.fetchone()

        cursor.execute("SELECT c_id FROM course WHERE c_id = %s", (prereq_id,))
        existing_prerequisite = cursor.fetchone()

        if not existing_course or not existing_prerequisite:
            print("Output: Course or prerequisite does not exist.")
        else:
            # Insert the new prerequisite details into the prerequisite table
            cursor.execute(
                "INSERT INTO prerequisite (courseid, prerequisiteid) VALUES (%s, %s)",
                (course_id, prereq_id)
            )

            conn.commit()
            print("Output: Prerequisite added successfully")

        cursor.close()
    except (Exception, psycopg2.Error) as error:
        print("Error while adding a prerequisite:", error)

def add_section(conn, s_id, semester, c_year, c_id, faculty, class_time, class_room, class_building):
    try:
        cursor = conn.cursor()

        # Check if the admin is authenticated
        if not admin_authenticate():
            print("Admin authentication failed. Access denied.")
            return

        # Check if the section already exists in the database
        cursor.execute("SELECT s_id FROM section WHERE s_id = %s", (s_id,))
        existing_section = cursor.fetchone()

        if existing_section:
            print("Output: Section ID already exists")
        else:
            # Insert the new section details into the section table
            cursor.execute(
                "INSERT INTO section (s_id, semester, c_year, c_id, faculty, class_time, class_room, class_building) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                (s_id, semester, c_year, c_id, faculty, class_time, class_room, class_building)
            )

            conn.commit()
            print("Output: Section details inserted into the section table successfully")

        cursor.close()
    except (Exception, psycopg2.Error) as error:
        print("Error while adding a section:", error)

# Function to enroll a student in a course
def enroll_student(conn, student_id, course_id):
    try:
        cursor = conn.cursor()

        # Check if the course prerequisites are met by the student
        cursor.execute("SELECT prerequisiteID FROM prerequisite WHERE courseID = %s", (course_id,))
        prerequisites = cursor.fetchall()

        if prerequisites:
            for prereq in prerequisites:
                prereq_id = prereq[0]
                # Check if the student has already taken the prerequisite course in any of the previously enrolled sections
                cursor.execute(
                    "SELECT * FROM takes WHERE student = %s AND section IN (SELECT section FROM takes WHERE student = %s) AND (select course_id from section= %s",
                    (student_id, student_id, prereq_id),
                )
                if not cursor.fetchone():
                    print("Output: Prerequisite not met. Student has not taken course", prereq_id)
                    return
        # Execute a SQL query to fetch the section_id based on the course_id
        section_id = cursor.execute("SELECT s_id FROM section WHERE c_id = %s", (course_id,))
        # Enroll the student in the course with attendance% and grade set to nil
        cursor.execute(
            "INSERT INTO takes (student, section, attendance_percentage, grade) VALUES (%s, %s, %s, NULL, NULL)",
            (student_id, section_id),
        )

        conn.commit()
        print("Output: Student enrolled in the course successfully, Section for the course is", section_id)

        # Update student's total credits
        cursor.execute(
            "UPDATE student SET tot_credits = tot_credits + (SELECT credits FROM course WHERE c_id = %s) WHERE student_id = %s",
            (course_id, student_id),
        )

        conn.commit()
        print("Output: Student's total credits updated")

        cursor.close()
    except (Exception, psycopg2.Error) as error:
        print("Error while enrolling a student:", error)


# Function to check if a student has completed a course
def check_course_completion(conn, student_id, course_id):
    try:
        cursor = conn.cursor()
        # Execute a SQL query to fetch the section_id based on the course_id
        section_id = cursor.execute("SELECT s_id FROM section WHERE c_id = %s", (course_id,))
        cursor.execute(
            "SELECT grade FROM takes WHERE student_id = %s AND section_id = %s",
            (student_id, course_id),
        )
        grade = cursor.fetchone()

        if grade and grade[0] is not None:
            print("Output: Course is completed with grade", grade[0])
        else:
            print("Output: Course is not completed")

        cursor.close()
    except (Exception, psycopg2.Error) as error:
        print("Error while checking course completion:", error)

# Main program
if __name__ == "__main__":
    conn = connect_to_database()

    if conn:
        while True:
            print("Choose an option:")
            print("1. Student Enroll")
            print("2. Department Addition")
            print("3. Professor Addition")
            print("4. Course Addition(with an option to add a prerequisite)")
            print("5. Exit")
            option = input("Enter your choice (1/2/3/4/5): ")

            if option == "1":
                # Add a new student
                student_id = input("Enter student ID: ")
                fname = input("Enter first name: ")
                lname = input("Enter last name: ")
                gender = input("Enter gender as Male(M), Female(F), Other(O): ")
                email = input("Enter email: ")
                phone_no = input("Enter phone number: ")
                batch = input("Enter joining year/batch: ")
                program = input("Enter program: ")
                dob = input("Enter date of birth in format yyyy-mm-dd: ")
                semester = input("Enter semester Spring/Autumn: ")
                year = input("Enter B.tech year: ")
                tot_credits = input("Enter total credits: ")
                fee_status = input("Enter fee status as P(if Paid) or U(if Unpaid): ")
                home_address = input("Enter home address: ")
                category = input("Enter category id: ")
                faculty_advisor = input("Enter faculty advisor id: ")
                department = input("Enter department id: ")

                add_student(conn, student_id, fname, lname, gender, email, phone_no, batch, program, dob, semester, year, tot_credits, fee_status, home_address, category, faculty_advisor, department)

            elif option == "2":
                # Add a new department
                d_id = input("Enter department ID: ")
                d_name = input("Enter department name: ")
                building = input("Enter building: ")
                hod = input("Enter HOD(type 0 if there is no hod): ")

                add_department(conn, d_id, d_name, building, hod)

            elif option == "3":
                # Add a new professor
                pid = input("Enter professor ID: ")
                fname = input("Enter first name: ")
                lname = input("Enter last name: ")
                gender = input("Enter gender as Male(M), Female(F), Other(O): ")
                email = input("Enter email: ")
                phone_no = input("Enter phone number: ")
                salary = input("Enter salary: ")
                special_status = input("Enter special status: ")
                d_id = input("Enter department ID: ")

                add_professor(conn, pid, fname, lname, gender, email, phone_no, salary, special_status, d_id)

            elif option == "4":
                # Add a new course
                c_id = input("Enter course ID: ")
                c_name = input("Enter course name: ")
                credits = input("Enter credits: ")
                d_id = input("Enter department ID: ")
                add_prereq = input("Do you want to add a prerequisite to this course? (Y/N): ").strip().lower()
                if add_prereq == "y":
                    prereq_id = input("Enter the prerequisite course ID: ")
                    add_course(conn, c_id, c_name, credits, d_id)
                    add_prerequisite(conn, c_id, prereq_id)
                else:
                    add_course(conn, c_id, c_name, credits, d_id)

            elif option == "5":
                # Exit the program
                print("Exiting the program.")
                break

            else:
                print("Invalid option. Please choose a valid option (1/2/3/4/5).")

        conn.close()
    else:
        print("Database connection failed. Please check your connection parameters.")

