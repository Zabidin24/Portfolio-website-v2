from sqlalchemy import create_engine, text
import mysql.connector
from mysql.connector.cursor import MySQLCursor


db_connection_string="mysql+pymysql://4cui1k5b88f03u1z2bwp:pscale_pw_AdiCfWfpwSeatb0oPIzeaTyVYsq04nlzzySxOSqp8KR@aws.connect.psdb.cloud/portfolio?charset=utf8mb4"

engine = create_engine(db_connection_string,
  connect_args={
        "ssl": {
            "ssl-ca": "/etc/ssl/cert.pem"
        }
    })
with engine.connect() as conn:result=conn.execute(text("select * from exp"))
print("type(result):",type(result))
result_all=result.all()
print("type(result all):",type(result_all))
first_result=result_all[0]
print("type(first_result:",type(first_result))



def Convert(lst):
 res_dct = map(lambda i: (lst[i], lst[i+1]), range(len(lst)-1)[::10])
 return dict(res_dct)
print("type(first_result_dict:",type(Convert(result_all)))
print(Convert(result_all[2]))