# Author: Hunter M/Erika T.
# Date Updated: 4/19/19
# Description: This class connects to the MongoDB Atlas using admin logins.


from pymongo import MongoClient


def loginDatabase():
    # get admin login and connect to mongo
    adminUser = input('Enter your MongoDB Admin user name:')
    adminPass = input('Enter your MongoDB Admin password:')

    client = MongoClient("mongodb+srv://" + adminUser + ":" + adminPass + "@databaseproject-ry5nf.mongodb.net/test?ssl=true&ssl_cert_reqs=CERT_NONE")

    return client