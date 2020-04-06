import pyodbc

def read(cnxn):
    print("Read")
    cursor = cnxn.cursor()
    cursor.execute("SELECT * FROM user_reg")
    for row in cursor:
     print(row)

def create(cnxn):
    print("Create")
    cursor = cnxn.cursor()
    cursor.execute('''INSERT INTO user_reg (username, firstname, lastname, typeofuser, address1, phone1, dateofbirthday, dateofbirthmonth, dateofbirthyear, cityofbirth, countryofbirth, sex, maritialstatus)
                  VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,);''')

    cnxn.commit()
    read(cnxn)


def update(cnxn):
    print("Update")
    cursor = cnxn.cursor()
    cursor.execute('''UPDATE user_reg (username, firstname, lastname, typeofuser, address1, phone1, dateofbirthday, dateofbirthmonth, dateofbirthyear, cityofbirth, countryofbirth, sex, maritialstatus)
                  VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,);''')

    cnxn.commit()
    read(cnxn)


def delete(cnxn):
    print("Delete")
    cursor = cnxn.cursor()
    cursor.execute('''DELETE FROM user_reg (username, firstname, lastname, typeofuser, address1, phone1, dateofbirthday, dateofbirthmonth, dateofbirthyear, cityofbirth, countryofbirth, sex, maritialstatus)
                  VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,);''')

    cnxn.commit()
    read(cnxn)
    
server = 'DESKTOP-HGO4IUV'
database = 'Django'


cnxn = pyodbc.connect(
    'Driver={ODBC Driver 17 for SQL Server}; \
     Server=' + server + '; \
     Database=' + database +';\
     Trusted_Connection=yes;'
)


cursor = cnxn.cursor()


cnxn.commit()


cursor.execute('SELECT * FROM user_reg')

for row in cursor:
    print(row)
    


    
    
