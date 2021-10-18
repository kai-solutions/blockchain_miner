#!/bin/bash

my_activate() {

    source venv/bin/activate
    export SNOWFLAKE_PASS=$(pass SNOWFLAKE/ACCOUNT)
    export AWS_ACCESS_KEY_ID=$(pass AWS/AWS_ACCESS_KEY)
    export AWS_SECRET_ACCESS_KEY=$(pass AWS/AWS_SECRET_KEY)
    echo "Finished!"
}




