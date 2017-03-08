# Small-Python-apps

### 1. Block facebook in working hours

We access the host file of system and add the desired websites in it to block those sites in working hours and then again unblock the websites after working hours

We convert the .py file to .pyw file to run it in background

To run it as soon as the computer starts we add it in Task Scheduler for windows:

1. Open Task Scheduler

2. Create Task

3. Check the run this highest privileges box and select window configuration 

4. Go to trigers -> New -> At startup

5. Go to actions -> New -> Start a program -> Browse: point to program script

6. Now go to conditions -> uncheck the power options

7. Our script is stacked in the task scheduler

8. Select your newly created task and click on Run

9. and our website blocker is running

### 2. Build a website wit flask

To install flask:

<code>pip install flask</code>

Run the script1.py and check the http://localhost:5000/ in your browser.

and http://localhost:5000/about/ to see the about page

Flask detects the changes in file and restarts the web app so you don't need to run it everytime just save the script

Create templates folder in current directory and save your html file templates.

To deploy our project online we need to intall virtualenv to run the required lib like flask and run python etc

<code>pip install virtualenv</code>

Create a virtual environment to get all the libs and other required files to deploy the site online

Place all the files in one folder and same level folder using cmd <code>python -m venv virtual</code>

Now we need to install the flask in our virtual python environment so open the virtual folder's python file and install flask via pip

Add the required files and push to live serve in my case I uploaded it on herko with cmd

### 3. WebCam montion detection record time

This program records the time for an object moving in front of webcam. opencv provides alot a cool image processing features and using it We implement this program