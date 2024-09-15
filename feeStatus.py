import psycopg2

# Database connection parameters
db_params = {
    'dbname': 'iitdhdb',
    'user': 'postgres',
    'password': '123456',
    'host': 'localhost',
    'port': '5432'
}

def find_fee_payments():
    try:
        # Connect to the database
        conn = psycopg2.connect(**db_params)
        cur = conn.cursor()

        # SQL query to retrieve fee payment records
        query = """
        SELECT student_id, fee_status
        FROM student;
        """
        cur.execute(query)
        fee_payments = cur.fetchall()

        if fee_payments:
            print("Fee Payment Records:")
            for payment in fee_payments:
                student_id, fee_status = payment
                print(f"Student ID: {student_id}, Fee Status: {fee_status}")
        else:
            print("No fee payment records found.")

        # Close the cursor and connection
        cur.close()
        conn.close()

    except psycopg2.Error as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    find_fee_payments()

