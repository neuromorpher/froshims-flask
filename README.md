# my-froshims 

A small Flask app derived from CS50s Flask lecture

### What I did differently 
 - Used the sqlite3 module in place of CS50s provided SQL libary with my own connect_db helper
 - Opened a separate database connection for each request to circumvent Flask's multithreading

### To Run (Windows) 
```
    python -m venv .venv 
    .venv\Scripts\activate.bat 
    pip install flask 
    flask run 
```
Then open http://localhost:5000 


