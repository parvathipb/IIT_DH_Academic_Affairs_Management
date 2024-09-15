import psycopg2

# Database connection parameters
db_params = {
    'dbname': 'iitdhdb',
    'user': 'postgres',
    'password': '123456',
    'host': 'localhost',
    'port': '5432'
}

def find_project_by_faculty(faculty_name):
    try:
        # Connect to the database
        conn = psycopg2.connect(**db_params)
        cur = conn.cursor()

        # SQL query to find projects by faculty
        query = """
        SELECT project_title, credits, semester, stipend, students, faculty
        FROM research_projects
        WHERE faculty = %s;
        """
        cur.execute(query, (faculty_name,))
        projects = cur.fetchall()

        if projects:
            print("Projects by Faculty:")
            for project in projects:
                project_title, credits, semester, stipend, students, faculty = project
                print(f"Title: {project_title}")
                print(f"Credits: {credits}")
                print(f"Semester: {semester}")
                print(f"Stipend: {stipend}")
                print(f"Students: {students}")
                print(f"Faculty: {faculty}")
                print()

        else:
            print(f"No projects found for faculty '{faculty_name}'")

        # Close the cursor and connection
        cur.close()
        conn.close()

    except psycopg2.Error as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    faculty_name = input("Enter the faculty ID: ")
    find_project_by_faculty(faculty_name)

