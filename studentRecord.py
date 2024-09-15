import psycopg2

# Database connection parameters
db_params = {
    'dbname': 'iitdhdb',
    'user': 'postgres',
    'password': '123456',
    'host': 'localhost',
    'port': '5432'
}

def retrieve_student_details(student_id):
    try:
        # Connect to the database
        conn = psycopg2.connect(**db_params)
        cur = conn.cursor()

        # SQL query to retrieve student details by student_id
        query = """
        SELECT student_id, fname, lname, gender, email, phone_no, batch, semester, year, program, dob, fee_status, home_address, tot_credits, category, faculty_advisor, department
        FROM student
        WHERE student_id = %s;
        """
        cur.execute(query, (student_id,))
        student_data = cur.fetchone()

        if student_data:
            print("Student Details:")
            print(f"Student ID: {student_data[0]}")
            print(f"First Name: {student_data[1]}")
            print(f"Last Name: {student_data[2]}")
            print(f"Gender: {student_data[3]}")
            print(f"Email: {student_data[4]}")
            print(f"Phone Number: {student_data[5]}")
            print(f"Batch: {student_data[6]}")
            print(f"Semester: {student_data[7]}")
            print(f"Year: {student_data[8]}")
            print(f"Program: {student_data[9]}")
            print(f"Date of Birth: {student_data[10]}")
            print(f"Fee Status: {student_data[11]}")
            print(f"Home Address: {student_data[12]}")
            print(f"Total Credits: {student_data[13]}")
            print(f"Category: {student_data[14]}")
            print(f"Faculty Advisor: {student_data[15]}")
            print(f"Department: {student_data[16]}")
        else:
            print(f"No student found with Student ID {student_id}")

        # Close the cursor and connection
        cur.close()
        conn.close()

    except psycopg2.Error as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    student_id = input("Enter Student ID: ")
    retrieve_student_details(student_id)

