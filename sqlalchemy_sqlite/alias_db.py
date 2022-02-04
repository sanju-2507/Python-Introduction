
from sqlalchemy.sql import alias, select

st = students.alias("a")
s = select([st]).where(st.c.id > 2)
conn.execute(s).fetchall()