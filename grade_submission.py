import psycopg2

conn = psycopg2.connect(database='iitdhdb',
                        host="localhost",
                        user="postgres",
                        password="123456",
                        port=5432) 
                        


try:
   
    mycursor = conn.cursor()
    professor_id = int(input("Enter your professor ID: "))
    conn.autocommit = False
    mycursor.execute("SELECT pid FROM professor WHERE pid = %s", (professor_id,))
    existing_prof = mycursor.fetchone()
    if existing_prof:
        query = f"""
         SELECT s.s_id, s.semester, s.c_id, c.c_name, s.faculty
         FROM section AS s
         INNER JOIN course AS c ON s.c_id = c.c_id
         WHERE s.faculty = {professor_id}
          """

        mycursor.execute(query)
        sections = mycursor.fetchall()
        if not sections:
            print("You don't teach any sections.")
        else:
            print("Sections you teach:")
            for section in sections:
                s_id, semester, c_id, c_name, faculty = section
                print(f"Section ID: {s_id}, Semester: {semester}, Course: {c_name}")

    # Allow the professor to enter grades
            section_id = int(input("Enter the section ID for which you want to submit grades: "))
            grades = []

            while True:
                student_id = int(input("Enter student ID (0 to exit): "))
                if student_id == 0:
                    break

                grade = int(input("Enter grade (0-10): "))
                if (grade >10):
                    print("Grade invalid")
                    break
                grades.append((student_id, grade, section_id))

    # Insert grades into the Takes table
            # if grades:
            #     query = "INSERT OR REPLACE INTO Takes (student, grade, section) VALUES (?, ?, ?)"
            #     mycursor.executemany(query, grades)
            #     conn.commit()
            #     print("Grades submitted successfully.")
            # else:
            #     print("No grades were submitted.")
# Insert grades into the Takes table
                if grades:
                    for student_id, grade, section_id in grades:
        # Check if the record already exists
                        mycursor.execute("SELECT student FROM Takes WHERE student = %s AND section = %s", (student_id, section_id))
                        existing_record = mycursor.fetchone()
        
                    if existing_record:
            # Update the existing record
                        update_query = "UPDATE Takes SET grade = %s WHERE student = %s AND section = %s"
                        mycursor.execute(update_query, (grade, student_id, section_id))
                        conn.commit()
                    else:
            # Insert a new record
                        insert_query = "INSERT INTO Takes (student, grade, section) VALUES (%s, %s, %s)"
                        mycursor.execute(insert_query, (student_id, grade, section_id))

                        conn.commit()
                        print("Grades submitted successfully.")
                else:
                    print("No grades were submitted.")

    else:
        print("No professor found")
# Close the database connection
except (Exception, psycopg2.Error) as error:
    if conn:
        conn.rollback()
    print(f"Error: {error}")

finally:
    if conn:
        mycursor.close()
        conn.close()



