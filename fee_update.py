import psycopg2

conn = psycopg2.connect(database='iitdhdb',
                        host="localhost",
                        user="postgres",
                        password="123456",
                        port=5432) 
                        


try:
   
    mycursor = conn.cursor()
    student_id = input("Enter the student ID: ")

    # Check if the student exists

    mycursor.execute("SELECT student_id, fee_status, category FROM student WHERE student_id = %s;", (student_id,))
    student = mycursor.fetchone()
    


    #query = "SELECT student_id, fee_status, category FROM student WHERE student_id = %s"
    #mycursor.execute(query, (student_id,))
    #student = mycursor.fetchone()

    if student:
        student_id, current_fee_status, category_id = student
        print(f"Current Fee Status for student {student_id}: {current_fee_status}")
	
    # Calculate the total fees for the student based on category
        mycursor.execute( "SELECT tution_fees FROM category WHERE category_id = %s",(category_id,))
        
        category_fees = mycursor.fetchone()

        if category_fees:
            category_fee = category_fees[0]
            print(f"Total Fees for student in Category {category_id}: {category_fee}")

        # Prompt for a new fee status
            new_fee_status = input("Enter new fee status (P for Paid, U for Pending): ").strip().upper()
            if new_fee_status in ('P', 'U'):
            # Update the fee status in the database
                mycursor.execute("UPDATE student SET fee_status = %s WHERE student_id = %s",(new_fee_status,student_id,))
                
                conn.commit()
                print(f"Fee Status for Student {student_id} updated to {new_fee_status}")
            else:
                print("Invalid fee status. Use 'P' for Paid or 'U' for Pending.")
        else:
            print("Category fees not found for this student's category.")
    else:
        print(f"student with ID {student_id} not found.")

except (Exception, psycopg2.Error) as error:
    if conn:
        conn.rollback()
    print(f"Error: {error}")

finally:
    if conn:
        mycursor.close()
        conn.close()



