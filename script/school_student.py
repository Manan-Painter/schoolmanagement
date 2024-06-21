import xmlrpc.client

url = "http://hspl:8080/"
db = "12062024"
username = "admin"
password = "admin"

# Authenticate with the server
common = xmlrpc.client.ServerProxy("{}/xmlrpc/2/common".format(url))
uid = common.authenticate(db, username, password, {})
models = xmlrpc.client.ServerProxy("{}/xmlrpc/2/object".format(url))

try:
    # Corrected write operation to update student record with id=1
    student_id = 1
    models.execute_kw(db, uid, password, 'school.student', 'write', [[1], {'name': "sanket"}])
    print(f"Updated student with id {student_id}")

    # Check if the record is updated by reading the student record with id=1
    student_data = models.execute_kw(db, uid, password, 'school.student', 'read', [[1]])
    print(f"Student data: {student_data}")

except Exception as e:
    print(e)
