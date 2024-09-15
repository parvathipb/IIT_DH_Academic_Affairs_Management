import psycopg2

conn = psycopg2.connect(database='iitdhdb', host="localhost", user="postgres", password="123456", port=5432)

try:
    mycursor = conn.cursor()
    student_id = input("Enter the student ID: ")

    # Get a list of sections the student has taken, along with the associated courses
    query = f"SELECT t.section, c.credits FROM Takes t JOIN Section s ON t.section = s.s_id JOIN Course c ON s.c_id = c.c_id WHERE t.student = {student_id}"
    mycursor.execute(query)
    sections = mycursor.fetchall()

    if not sections:
        print(f"Student {student_id} has not taken any sections.")
    else:
        print(f"Sections taken by Student {student_id}:")
        for section, credits in sections:
            print(f"Section ID: {section}, Credits: {credits}")

    # Prompt for the section to delete
    section_to_delete = int(input("Enter the section ID to delete: "))

    section_found = False  # Initialize a flag to track whether the section was found

    for section, credits in sections:
        if section == section_to_delete:
            section_found = True
            break  # Exit the loop if the section is found

    if section_found:
        # Delete the specified section from Takes
        delete_query = f"DELETE FROM Takes WHERE student = {student_id} AND section = {section_to_delete}"
        mycursor.execute(delete_query)
        conn.commit()
        print(f"Section ID {section_to_delete} deleted for Student {student_id}.")

        # Calculate updated credits with credits subtracted for the section to delete
        updated_credits = sum(credits if section != section_to_delete else 0 for section, credits in sections)

        update_credits_query = "UPDATE Student SET tot_credits = %s WHERE student_id = %s"
        mycursor.execute(update_credits_query, (updated_credits, student_id))

        conn.commit()
        print(f"Student's total credits updated to {updated_credits}.")

    else:
        print(f"Section ID {section_to_delete} not found in the student's sections.")

except (Exception, psycopg2.Error) as error:
    if conn:
        conn.rollback()
    print(f"Error: {error}")

finally:
    if conn:
        mycursor.close()
        conn.close()
