#!/bin/bash
# 0.0.0.0:5000/catch_me request that makes server respond You got me! sent 
curl -sL 0.0.0.0:5000/catch_me_3 -X PUT -d "user_id=98" -H "Origin:School"
