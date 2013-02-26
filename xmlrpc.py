import xmlrpclib

username = 'admin' #the user
pwd = 'passme'      #the password of the user
dbname = 'campsia'    #the database
model='res.partner'

# Get the uid
sock_common = xmlrpclib.ServerProxy ('http://192.168.1.4:8069/xmlrpc/common')
uid = sock_common.login(dbname, username, pwd)

#replace localhost with the address of the server
sock = xmlrpclib.ServerProxy('http://192.168.1.4:8069/xmlrpc/object')
args = [('first_name', '=', 'Tony'),]
ids = sock.execute(dbname, uid, pwd, model, 'search', args)
# READ PARTNER DATA
fields = ['last_name','exam_reg_no',]

results = sock.execute(dbname, uid, pwd, model, 'read', ids, fields)
print results
