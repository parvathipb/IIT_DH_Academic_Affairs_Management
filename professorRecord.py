import psycopg2

# Database connection parameters
db_params = {
    'dbname': 'iitdhdb',
    'user': 'postgres',
    'password': '123456',
    'host': 'localhost',
    'port': '5432'
}

def retrieve_professor_details(pid):
    try:
        # Connect to the database
        conn = psycopg2.connect(**db_params)
        cur = conn.cursor()

        # SQL query to retrieve professor details by pid
        query = """
        SELECT pid, fname, lname, gender, email, phone_no, salary, special_status, d_id
        FROM professor
        WHERE pid = %s;
        """
        cur.execute(query, (pid,))
        professor_data = cur.fetchone()

        if professor_data:
            print("Professor Details:")
            print(f"Professor ID: {professor_data[0]}")
            print(f"First Name: {professor_data[1]}")
            print(f"Last Name: {professor_data[2]}")
            print(f"Gender: {professor_data[3]}")
            print(f"Email: {professor_data[4]}")
            print(f"Phone Number: {professor_data[5]}")
            print(f"Salary: {professor_data[6]}")
            print(f"Special Status: {professor_data[7]}")
            print(f"Department ID: {professor_data[8]}")
        else:
            print(f"No professor found with Professor ID {pid}")

        # Close the cursor and connection
        cur.close()
        conn.close()

    except psycopg2.Error as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    pid = input("Enter Professor ID: ")
    retrieve_professor_details(pid)

