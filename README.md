## <div align="center">TravianHelper </div>

```
It is for the browser game, Travian Kingdoms.

What the program does?

- It builds for you
- It recruits for you
- It alerts you if you are under attack
- It sends farmlist for you

I am trying to improve python and webscraping, so I decided to write it in python.
```

### Requirements:

 - Python 3.8.0+
 - Modules in requirements.txt (Might be too much, will check it later)
 - Microsoft Edge browser

### How to run:

```
In root directory type:
python -m src.main
```
Tested on Lubuntu and Windows 10

### How to run tests:

You need credentials.json in order to run the tests successfully.
Important: File should be put in the root directory, and named "credentials.json"
It should be like this:
```
{
    "email": "write_your_travian_kingdoms_email_here",
    "password": "write_your_travian_kingdoms_password_here"
}
```
If you want to run only the application, you don't need to create the json file!
```
In root directory type:
pytest
```

### There are lots of function not implemented yet, it's still in WIP.
