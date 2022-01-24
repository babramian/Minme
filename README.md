# Minme URL Shortener


***Languages/Frameworks used***
- Python
- Flask
- SQLAlchemy

RUN INSTRUCTIONS:
1) Clone this repository, make sure you remember what directory you've cloned it to

2) Open your terminal and go to the directory containing this program

3) Type 'flask db init', press Enter

4) Type 'flask db migrate', press Enter

5) Type 'flask db upgrade', press Enter

6) Your database is now initialized, run the program by typing 'flask run' and pressing enter

7) Go to your local host on your browser to use the program, if you're unsure of what this is, flask should tell you in the terminal

You can now use the program, type in a URL to convert it, the program will return a shortened URL, to use the shortened URL as of now you have to copy the six digits after the 'min.me/' and paste it after your local host url, like this 'localhost/123456' and you will be redirected to the original url!

##WORK IN PROGRESS

###Current objectives
- Push program onto a fully functioning website
- Get the shortened url to redirect through 'min.me'
