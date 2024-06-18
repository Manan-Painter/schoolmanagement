import xmlrpc.client

url = "http://hspl:8080/"
db = "12062024"
username = "admin"
password = "admin"

common = xmlrpc.client.ServerProxy("{}/xmlrpc/2/common".format(url))
uid = common.authenticate(db, username, password, {})
models = xmlrpc.client.ServerProxy("{}/xmlrpc/2/object".format(url))
try:
    contact = models.execute_kw(db,
        uid,
        password, 'res.partner', 'search', [[['is_company', '=', True]]])
    print ("====contact_db_14===",contact)

    school_student = models.execute_kw(
        db,
        uid,
        password, "school.student", "create", [{
            "name" : "Mihir",
            "school_standard" : 11,
        }]
    )
    print ("=school_student=",school_student)

except Exception as e:
    print(e)