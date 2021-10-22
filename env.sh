#!/bin/bash

activate() {

    source venv/bin/activate
    export SNOWFLAKE_PASS=$(pass SNOWFLAKE/ACCOUNT)
    export AWS_ACCESS_KEY_ID=$(pass AWS/AWS_ACCESS_KEY)
    export AWS_SECRET_ACCESS_KEY=$(pass AWS/AWS_SECRET_KEY)

    cat  > .env << EOF
    AWS_ACCESS_KEY_ID=$(pass AWS/AWS_ACCESS_KEY)
    AWS_SECRET_ACCESS_KEY=$(pass AWS/AWS_SECRET_KEY)
EOF
    echo "Finished!"
}




