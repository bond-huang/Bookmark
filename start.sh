#!/bin/bash
git config user.name "huang"
git config user.email "huang19891023@163.com"
git config --global core.quotepath false

nohup waitress-serve --call 'nav:create_app' > nohup.log 2>&1 &
if [ $? -ne 0 ];then
    exit 1
fi
cd ./dist
git init
sleep 5
git add .
git commit -m "Update gh-pages"
git push -f --force --quiet "https://${GH_TOKEN}@${GH_REF}" master:gh-pages

