import psycopg2

# Database connection parameters
db_params = {
    'dbname': 'iitdhdb',
    'user': 'postgres',
    'password': '123456',
    'host': 'localhost',
    'port': '5432'
}

def find_courses_by_student(student_id):
    try:
        # Connect to the database
        conn = psycopg2.connect(**db_params)
        cur = conn.cursor()

        # SQL query to find courses selected by a student
        query = """
        SELECT c.c_id, c.c_name, d.d_name
        FROM student as s
        JOIN takes as t ON s.student_id = t.student
        JOIN section as sec ON t.section = sec.s_id
        JOIN course as c ON sec.c_id = c.c_id
        JOIN department as d ON c.d_id = d.d_id
        WHERE s.student_id = %s;
        """
        cur.execute(query, (student_id,))
        courses = cur.fetchall()

        if courses:
            print("Courses selected by Student:")
            for course in courses:
                c_id, c_name, d_name = course
                print(f"Course Number: {c_id}")
                print(f"Course Name: {c_name}")
                print(f"Department: {d_name}")
                print()

        else:
            print(f"No courses found for Student ID '{student_id}'")

        # Close the cursor and connection
        cur.close()
        conn.close()

    except psycopg2.Error as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    student_id = input("Enter Student ID: ")
    find_courses_by_student(student_id)
