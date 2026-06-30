# SECTION 4 DOCUMENTATION

## HOW TO SET UP THE CRON JOB

In task 2, we set up a Cron job to automatically run task 1's file, monitor.py, every minute. 

To set up a Cron job, you must first run `crontab -e` in your command line. This will open up a text file in nano for you to edit.

The format of the Cron job is as follows: `* * * * * /path/to/.venv/bin/python3 -u /path/to/section4/task1/monitor.py >> /path/to/section4/task2/heartbeat.log`.

The five asterisks tell the system how often to run the job. From left to right, they represent minute, hour, day, month, and day of week. All five asterisks means the job executes every single minute of every day. 

The next lines define what program to run and where the output goes. The path to Python3 ensures that the script can find the correct environment executable. 

-u is important in insuring that the output and errors are unbuffered, meaning they are written to the file immediately instead of waiting.

The last two lines are the paths of the Python script to execute and the path to the file where the output should be saved. In this case, it's monitor.py and heartbeat.log respectively.

If done correctly, once saving the file the log should immediately begin to populate with data, and will continue to do so every minute. 

## TASK 3 CONCEPT QUESTION

In the task 3 file site_checker.py, I used a synchronous loop to run through each option of the URL list. For small lists, like the one used there, that works perfectly well. The issue arises when there is a large number of items to be looped through.

A synchronous loop goes one by one. It will take the first item in the list, do whatever the program needs of it, and moves onto the next. It's an inefficient way to get through the data, even if everything goes smoothly. But say there's a broken link or data. The loop does not move onto the next item until the broken one is dealt with, meaning it could be minutes, hours, or even days of waiting for this one item to be resolved before the rest of the code can run. 

This issue can be fixed through an asynchronous loop. Using the python library asyncio, we can take a large group of data and run it as a concurrent loop (everything runs at once) with asyncio.gather(). This will allow the system to continue processing the data, even if there is one element taking longer than the others.

It is important to note that running a large amount of tasks via asyncio.gather() has the potential to crash your machine. In this case, you should define asyncio.Semaphore() to tell the machine how many tasks it can run at the exact same time.