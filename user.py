import csv
import sqlite3

# git config --global user.name "YourUserName"
# git config --global user.email "YourEmail"
# git init //to initialize git
# git status //to see the status 
# git add . //to add the all files from current director to git


# Creating the connection function to connect sqlite3 database
def create_connection():    
    try:
        conn=sqlite3.connect("users.sqlite3")
        return conn
    except Exception as e:
        print(e)

# Creating Options as a input String

INPUT_STRING="""
1. CREATE TABLE
2. DUMP users from csv INTO users TABLE
3. Add new user INTO user TABLE
4. QUERY all users from TABLE
5. QUERY user by id from TABLE
6. QUERy specified no. of records from TABLE
7. DELETE all users
8. DELETE user by id
9. UPDATE user
10. Press any key to EXIT

"""

# Create table 
def create_table(conn)    :
    CREATE_USERS_TABLE_QUERY="""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name CHAR(255) NOT NULL,
            last_name CHAR(255) NOT NULL,
            company_name CHAR(255) NOT NULL,
            address CHAR(255) NOT NULL,
            city CHAR(255) NOT NULL,
            county CHAR(255) NOT NULL,
            state CHAR(255) NOT NULL,
            zip REAL NOT NULL,
            phone1 CHAR(255) NOT NULL,
            phone2 CHAR(255),
            email CHAR(255) NOT NULL,
            web text
        );
    """
    cur = conn.cursor()
    cur.execute(CREATE_USERS_TABLE_QUERY)
    print("User table was created successfully.")

def read_csv():
    users=[]
    with open("sample_users.csv", "r") as f:
        data=csv.reader(f)
        for user in data:
            users.append(tuple(user))
    # return users #to get all data and append in list
    return users[1:] #getting data without header row

def insert_users(con, users):
    user_add_query="""
    INSERT into users
    (
        first_name,
        last_name,
        company_name,
        address,
        city,
        county,
        state,
        zip,
        phone1,
        phone2,
        email,
        web
    )
    values (?,?,?,?,?,?,?,?,?,?,?,?)
    
    """
    cur=con.cursor()
    cur.executemany(user_add_query, users)
    con.commit()
    print(f"{len(users)} users were imported successfully")

#used for all users for No, 4
# def select_user(conn):
#     cur=conn.cursor()
#     users=cur.execute("SELECT * FROM users")
#     for user in users:
#         print(user)

# to select specified number of users 
def select_user(conn, no_of_users=0):
    cur=conn.cursor()
    users=cur.execute("SELECT * FROM users")
    for i, user in enumerate(users):
        if no_of_users and no_of_users ==i:
            break
        print(user)

# select fuction by providing the user id 
def select_user_from_id(conn, user_id):
    cur=conn.cursor()
    users=cur.execute("SELECT * FROM users where id=?;",(user_id,)) # select the user by user id provided by user
    for user in users:
        print(user)
        
    #delete function for all user delete 
def delete_user(conn):
    cur=conn.cursor()
    cur.execute("DELETE from users;") # delete the users
    conn.commit()
    print("All users were deleted successfully.")
    
    # delete function by user id
def delete_user_by_id(conn, user_id):
    cur=conn.cursor()
    cur.execute("DELETE from users where id=?;", (user_id,)) # delete the user by providing user id
    conn.commit()
    #print("The selected user is deleted successfully.")
    print(f"User with id {user_id} was successfully deleted.")

# update function 
def update_user_by_id(conn, user_id, column_name, column_value):
    update_query=f"UPDATE users set {column_name}=? where id=?;"
    cur=conn.cursor()
    cur.execute(update_query,(column_value, user_id))
    conn.commit()
    print(
        f"{column_name} was updated with value {column_value} of user with id {user_id}"
    )
# Columns of the table to be inserted
COLUMNS=(
    "first_name",
    "last_name",
    "company_name",
    "address",
    "city",
    "county",
    "state",
    "zip",
    "phone1",
    "phone2",
    "email",
    "web",
)
            
def main(): # 
    conn=create_connection()
    user_input=input(INPUT_STRING)
    if user_input=="1":
        create_table(conn)
        
    elif user_input=="2":
        users=read_csv() #reading the csv file and assigning with user
        # print(users) #printing the users
        insert_users(conn, users)
        
    elif user_input=="3":
        user_data=[]
        for column in COLUMNS:
            column_value=input(f"Enter the value of {column}: ")
            user_data.append(column_value)
        insert_users(conn, (tuple(user_data),))
    
    elif user_input=="4":
        select_user(conn)
        
    elif user_input=="5":
        user_id=int(input("Enter the user id: ")) # asking the user for user id
        select_user_from_id(conn, user_id) 
        
    elif user_input=="6":
        no_of_users=input("Enter how many users you want do display? ")
        if no_of_users.isnumeric() and int(no_of_users)>0:
            select_user(conn, no_of_users=int(no_of_users))
    
    elif user_input=="7":
        delete_user(conn)
        
    elif user_input=="8":
        user_id=int(input("Enter the user id: "))
        delete_user_by_id(conn, user_id)
        
    elif user_input=="9":
        user_id=input("Enter the user id to update. ")
        if user_id.isnumeric():
            column_name=input(
                f"Enter the column you want to edit. Please make sure column is with in {COLUMNS}: "
                )
            if column_name in COLUMNS:
                column_value=input(f"Enter the value of {column_name}: ")
                update_user_by_id(conn, user_id, column_name, column_value)
            else:
                print("Column name is not found. ")
        else:
            print("Invalid user id")
            
    elif user_input=="10":
        print("Thank you for using the system.")
        exit()
        
    else:
        print("Invalid Input. Existing.....")
        
if __name__ =="__main__":
    main()
    
    
       