#!/bin/bash
sleep 180s
TARGET_HOST="edge-router"
STATUS=$(curl -s -o /dev/null -w "%{http_code}" ${TARGET_HOST}) 
  if [ $STATUS -ne 200 ]; then
      echo "${TARGET_HOST} is not accessible"
      exit 1
  fi

  echo "Will run tests"
  python testing.py
  echo "done"
