import psycopg2

conn = psycopg2.connect(database='iitdhdb',
                        host="localhost",
                        user="postgres",
                        password="123456",
                        port=5432) 
                        


try:
    mycursor = conn.cursor()
    student_id = input("Enter the student ID: ")
    conn.autocommit = False
    mycursor.execute("SELECT student_id FROM student WHERE student_id = %s", (student_id,))
    existing_student = mycursor.fetchone()

    if existing_student:
        mycursor.execute("""
            SELECT s.student_id, SUM(T.grade * C.credits) / SUM(C.credits) AS cpi
            FROM student AS s
            LEFT JOIN Takes AS T ON s.student_id = T.student
            LEFT JOIN section AS SEC ON T.section = SEC.s_id
            LEFT JOIN course AS C ON SEC.c_id = C.c_id
            WHERE s.student_id = %s
            GROUP BY s.student_id
        """, (student_id,))

        results = mycursor.fetchall()
        if results:
            print(f"CPI for student '{student_id}':")
            for student_id, cpi in results:
                print(f"CPI: {cpi:.2f}")
        else:
            print(f"Student with ID {student_id} not found.")
    else:
        print(f"Student with ID {student_id} not found.")
except (Exception, psycopg2.Error) as error:
    if conn:
        conn.rollback()
    # print(f"Error: {error}")

finally:
    if conn:
        mycursor.close()
        conn.close()
