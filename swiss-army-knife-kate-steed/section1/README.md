# SECTION 1 DOCUMENTATION

## Section 1 Summary:

Section 1 was all about getting our personal machines ready for script writing! Each task focused on a single part or tool of script writing that we will need to be familiar with in order to successfully pass this class, including:

- Working with the terminal *(Task 1)*
- Writing our first basic script *(Task 2)*
- Creating SSH keys *(Task 3)*
- Creating virtual environments *(Task 4)*
- Changing file permissions *(Task 5)*
- Writing Requirement Files *(Task 6)*
- Creating aliases and profiles *(Task 7)*
- Creating Sentinels *(Task 8)*
- Creating global scripts through $PATH *(Task 9)*

This README.md document will outline what I think are some of the most important concepts of the Section 1 assignment.

## Sentinel Script: What is it & How to Run it

A Sentinel is a Python script that acts like a standalone system command. It does not have a .py extension, but if done correctly, should have a line of code to tell the OS what to use to run the file. In this case, the OS will use Python.

This Sentinel is coded to search for a specific directory, then give a success or failure message depending on what it finds. There are two ways to run this Sentinel, and both should give the same results.

### Method 1: Run through Task 8

- In terminal, type `cd ~/PATH-TO/CS3030-Labs/swiss-army-knife-kate-steed/section1/task8`, replacing PATH-TO with your actual path. 
- From within the `/task8` folder, type `./sentinel` to run the script.
- This sentinel is coded to look for the `/task8` directory, and since the `/task8` folder obviously exists (you're already inside it!), there will be a SUCCESS message displayed on the terminal.

### Method 2: Run Globally

** There are additional steps required to run scripts globally on your personal machine. See the **Global Setup** section below before attempting Method 2 **
- In Task 9, we set up the Sentinel script to run globally by updating the $PATH variable. This means that the Sentinel script can be run from anywhere.
- Simply type `sentinel` in the terminal from any folder.
- This method will also display a SUCCESS message on the terminal.
- This is because my specific Sentinel script is searching for a variable attached to the following line: `os.path.dirname(os.path.abspath(__file__))`. This tells the Sentinel to find the folder that the script is in, regardless on where it was launched from. Since the script is checking for `/task8`, and the script is in `/task8`, terminal will show SUCCESS regardless of what directory the user is currently in.

### Global Setup
To run scripts globally, there are some additional steps that need to be taken. This tutorial will walk you through how to globally run the Sentinel script from Task 8.
- Create a new folder in the home directory (~) called bin. If bin already exists, skip this step.
- Copy the Sentinel script into the bin folder: `cp ~/PATH-TO/CS3030-Labs/swiss-army-knife-kate-steed/section1/task8/sentinel ~/bin/`, replacing PATH-TO with your actual path.
- Type `nano ~/.bashrc` or `nano ~/.zshrc` for Windows/Linux and Apple devices respectively, and add the following line to the bottom of the page: `export PATH="$PATH:$HOME/bin"`
- Restart your terminal. If done correctly, **Method 2: Run Globally** should now function as intended. If not, redo the step above (pay attention to spelling!)

## Three Most Useful Shell Commands
Having mastery over the Shell is necessary for several career paths within the Technology industry. As someone still practicing with the Shell, these are the three most useful commands that I used throughout Section 1.
- **mkdir**: This command allows users to create new directories from within the command line. It can be used to create one new folder: `mkdir task1`, or can be used to make several folders in one command: `mkdir task1 task2 task3`. It is much faster to create folders and files using mkdir over using file explorer, as the latter only allows for one folder/file to be created at a time.
-  **chmod**: In the first few tasks of Section 1, I kept getting an error on my shell saying that I didn't have permission to move or edit the files/folders I had created. After many Google searches, I learned that there were permissions automatically assigned upon creation that were preventing me (a non-root user) from doing what I needed to do. The chmod command is used to edit the read, write, and execute permissions on files and folders.
-  **cd/ls**: Technically two commands, but I used them both so often and together that they both made the list. These two commands let me quickly navigate to a folder and see what's in it. The cd command allows uses to move in-between directories. They can move within their current directory, `cd .`, back into a previous directory, `cd ..`, into their home directory, `cd ~`, or into any folder connected to the directory, `cd ./folder-name`. The ls command allows users to see what files and folders are within their current directory. For example, from within `/task1`, if I type `ls` into the terminal, I should see `files_in_folder.py`.

## .venv Setup and Requirements.txt

### What is .venv?

.venv is a Python module used to create virtual environments. It creates a separate directory with it's own executable and site-packages, allowing users to install libraries specific to a project without affecting global Python installations or other projects. In layman's terms, it's like a Python shoebox stored within the larger Python closet. The items inside are contained by the shoebox and separate from any other clutter within the closet.

### How to Run .venv
- Make sure Python 3 is already installed. To install, run `sudo apt install python3-pip` in the terminal.
- In terminal, run `python3 -m venv .venv`
- To activate it, type `source .venv/bin/activate` for Linux and Apple systems, or `source .venv/Scripts/activate` or `.\.venv\Scripts\activate` for Windows.
- You will know your virtual environment is active when your terminal prompt shows (.venv) at the beginning of the line.

### What is a Dependency List?

Every developer is going to have a different selection of libraries installed on their machines, and we cannot assume that they will already have the libraries we require to run our program. To get around this, we create Dependency Lists. This files will tell other developers exactly what they need to have installed to get the correct functionality out of our program. 

### Where is Section 1's Dependency List?

It's in Task 6! The file is called `requirements.txt`. If you open it up in a text editor, you will see it has a list of 5 items and some numbers. This is the library name and version we used when creating this project. Developers can use this list to install the exact libraries we used, down to the exact version type. This is important data when it comes to recreating our same environment, as some libraries may receive updates after our project is created. This tells other developers that we know our project works with this version and we recommend using it, as we cannot make any guarantees about subsequent versions.