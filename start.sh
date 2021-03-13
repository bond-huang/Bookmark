#!/bin/bash
nohup waitress-serve --call 'nav:create_app' > nohup.log 2>&1 &
