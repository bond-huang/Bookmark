#!/bin/bash
git config user.name "${M_NAME}"
git config user.email "${M_EMAIL}"
git config --global core.quotepath false

nohup waitress-serve --call 'nav:create_app' > nohup.log 2>&1 &
if [ $? -ne 0 ];then
    exit 1
fi
git init
git checkout --orphan gh-pages
git status
sleep 5
git add .
git commit -m "Update gh-pages"
git remote add origin git@github.com:bond-huang/navigator.git
git push -f --force --quiet "https://${GH_TOKEN}@${GH_REF}" main:gh-pages

