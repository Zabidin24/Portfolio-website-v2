from sqlalchemy import create_engine, text


db_connection_string="mysql+pymysql://4cui1k5b88f03u1z2bwp:pscale_pw_AdiCfWfpwSeatb0oPIzeaTyVYsq04nlzzySxOSqp8KR@aws.connect.psdb.cloud/portfolio?charset=utf8mb4"

engine = create_engine(db_connection_string,
  connect_args={
        "ssl": {
            "ssl-ca": "/etc/ssl/cert.pem"
        }
    })


with engine.connect() as conn:
  result=conn.execute(text("select * from exp"))
  result_all=result.all()
d1={k:"a" for k in result_all}
print (d1,type(d1))