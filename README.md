# Navigator
[![Build Status](https://travis-ci.org/bond-huang/navigator.svg?branch=main)](https://travis-ci.org/bond-huang/navigator)   
A simple web navigation tool.
## Description 
Function Description：
- Currently only add,edit and delete functions;
- The main category is sorted according to the order of addition;
- The sub category is sorted in alphabetical order;
- Hyperlinks are sorted according to the order in which they are added;
- The name can be repeated, but the hyperlink cannot,If link cannot be added, it means duplicate；

Needs to be initialized the database before use：
```sh
$ export FLASK_APP=nav
$ export FLASK_ENV=development
$ flask init-db
Initialized the database
```
## Example
Choose a main category：   
![main category](https://github.com/bond-huang/navigator/blob/main/home.png)

Add：   
![Add](add.png)

Edit：   
![Edit](edit.png)

Delete：   
![Delete](delete.png)

## Build documentation 
The build documentation on the following website:     
[https://ebook.big1000.com](https://ebook.big1000.com)

