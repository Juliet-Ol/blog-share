# Blog Share

## Application Link



## Description

Blog Share is an application where someone can register and log in. In the application one can be able to share a quote, read a quote and comment on it and even vote for the post. 

The app helps people share a quote that motivates them and in turn can motivate others

## Installations

Guide to install Blog Share
 
### Clone this repository

 git clone https://github.com/Juliet-Ol/blog-share

 - [Get into the cloned directory]

 cd blog_share

 - [Create and activate your virtual environment:]

 mkvirtualenv virtual

 - [Install dependancies within your active environment]

 ### Environment variables:

 Create a file called .env in the root folder

 (virtual)$ touch .env

 - [Add the following lines to the file as seen in config.py file]

SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', '').replace(
    'postgres://', 'postgresql://') or\
    'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False  
LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')

## Start the flask server

(Virtual)$ flask run

**Features and BDD**

Users can log in and access other quotes and also post a quote

**Technology Used**

Framework: Flask language Python

### Developed with

Structure: Bootstrap, HTML, Shell
Styles: CSS


### Author

Design and developed by: Juliet Oluoch


## License Copyright

Copyright (c) 2022 Juliet Oluoch

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.