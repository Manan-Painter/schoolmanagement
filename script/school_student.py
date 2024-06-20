import xmlrpc.client

url = "http://hspl:8080/"
db = "12062024"
username = "admin"
password = "admin"

common = xmlrpc.client.ServerProxy("{}/xmlrpc/2/common".format(url))
uid = common.authenticate(db, username, password, {})
models = xmlrpc.client.ServerProxy("{}/xmlrpc/2/object".format(url))
try:
    # contact = models.execute_kw(db,
    #     uid,
    #     password, 'res.partner', 'unlink', [[5]])
    # print ("====contact_db_14===",contact)
    #
    # school_student = models.execute_kw(
    #     db,
    #     uid,
    #     password, "school.student", "unlink", [{
    #         "name" : "aadarsh",
    #         "school_standard" : 11,
    #     }]
    # )
    # print ("=school_student=",school_student)

    models.execute_kw(db, uid, password, 'school.student', 'unlink', [[7]])
    # check if the deleted record is still in the database
    models.execute_kw(db, uid, password, 'school.student', 'search', [[['id', '=', 2]]])

except Exception as e:
    print(e)