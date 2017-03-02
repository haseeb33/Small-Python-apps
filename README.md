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