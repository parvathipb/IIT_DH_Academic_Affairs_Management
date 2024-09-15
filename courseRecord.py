import psycopg2

# Database connection parameters
db_params = {
    'dbname': 'iitdhdb',
    'user': 'postgres',
    'password': '123456',
    'host': 'localhost',
    'port': '5432'
}

def find_course_details_by_c_id(c_id):
    try:
        # Connect to the database
        conn = psycopg2.connect(**db_params)
        cur = conn.cursor()

        # SQL query to retrieve course details by c_id
        query = """
        SELECT c_id, c_name, credits, d_id
        FROM course
        WHERE c_id = %s;
        """
        cur.execute(query, (c_id,))
        course_data = cur.fetchone()

        if course_data:
            print("Course Details:")
            print(f"Course ID: {course_data[0]}")
            print(f"Course Name: {course_data[1]}")
            print(f"Credits: {course_data[2]}")
            print(f"Department ID: {course_data[3]}")
        else:
            print(f"No course found with Course ID {c_id}")

        # Close the cursor and connection
        cur.close()
        conn.close()

    except psycopg2.Error as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    c_id = input("Enter Course ID: ")
    find_course_details_by_c_id(c_id)

