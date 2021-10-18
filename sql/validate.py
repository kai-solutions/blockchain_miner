#!/usr/bin/env python
import snowflake.connector
import os

# Gets the version
ctx = snowflake.connector.connect(
    user=os.environ['USER'],
    password=os.environ['SNOWFLAKE_PASS'],
    account='KB33487.us-east-2.aws'
    )
cs = ctx.cursor()
try:
    cs.execute("SELECT current_version()")
    one_row = cs.fetchone()
    print(one_row[0])
finally:
    cs.close()
ctx.close()