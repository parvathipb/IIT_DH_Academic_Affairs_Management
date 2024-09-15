import psycopg2

# Database connection parameters
db_params = {
    'dbname': 'iitdhdb',
    'user': 'postgres',
    'password': '123456',
    'host': 'localhost',
    'port': '5432'
}

def find_department_by_name(d_name):
    try:
        # Connect to the database
        conn = psycopg2.connect(**db_params)
        cur = conn.cursor()

        # SQL query to find a department by name
        query = """
        SELECT d_id, d_name, building
        FROM department
        WHERE d_name = %s;
        """
        cur.execute(query, (d_name,))
        department = cur.fetchone()

        if department:
            print("Department Information:")
            d_id, d_name, building = department
            print(f"Department ID: {d_id}")
            print(f"Name: {d_name}")
            print(f"Building: {building}")
        else:
            print(f"No department found with the name '{d_name}'")

        # Close the cursor and connection
        cur.close()
        conn.close()

    except psycopg2.Error as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    d_name = input("Enter the department name: ")
    find_department_by_name(d_name)

