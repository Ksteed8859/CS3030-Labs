# SECTION 2 DOCUMENTATION

## Section 2 Summary:

Section 2: The System Utility Toolkit was a set of labs designed to help us build tools that interact with the Operating System. We learned some of the common utilities and modules used in the industry, as well as safety practices to prevent hackers from taking advantage of our Operating System. The complete list of tasks completed are as follows:

- The Recursive Cleaner, using the pathlib module *(Task 1)*
- The Archive Architect, using the shutil module *(Task 2)*
- The System Reporter, using the subprocess module *(Task 3)*
- Professional CLI Design, using the argparse module *(Task 4)*
- The "Shell=True" Security Audit, securing the subprocess module *(Task 5)*

This README.md document will outline what I think are some of the most important concepts of the Section 2 assignment.

## Security Report Using `Shell=True`

Using `Shell=True` with invalidated user input leaves a developers system vulnerable to hijacking or serious damage. If a command is run with the `Shell=True` parameter, like it is in the first function of *Task 5*, the entire string is passed into the system shell and run like a set of commands. In that event, hackers could tack on an extra command to the user input using special characters to tell the shell to run a potentially dangerous command and cause a security breach, such as `echo hello ; cat /etc/passwd`.

## What is argparse and Why is it Important?

As most of us know by now, system administrators in the real world rely heavily on the command line. They use it for everything, as it is often the faster (or only) option when interacting with their systems. 

The argparse Python module allows system administration tools to accept arguments directly from the command line using flags, such as "--help" or "--ext". This way, the program doesn't need to stop and ask the user questions, it can just go!

So why do we need to know argparse for this class? After all, we're the once writing the function; we can tell it the answers it needs. Well, that's not always the case in the real world, and especially when working with scripting languages, the less human intervention, the better. With one command in the CLI, the program has all the information it needs. This is helpful in a great number of scenarios, such as automating a system to run a certain command without a human needing to be physically present to give the arguments.

## How to Avoid Shell Injection Vulnerabilities

As seen in Task 5, we have to be careful in the way we tell our programs to interact with the shell and operating system. Two words is all it takes to expose our systems to dangerous hackers: `shell=True`. So, what's the better way to handle this, and how is it different?

The issue with `shell=True` is that it is allowing our Python script to interact directly with the CLI. And the CLI pays special attention to special characters, such as ;, |, or &&. To the computer, our script is feeding it a command that it needs to execute, and each special character gives it another command to run. That means that if a hacker were to inject the following string into our program `echo hello ; cat /etc/passwd`, the CLI would see these as two commands and do as it's told, echo hello and print out the entire /etc/passwd file. Not good for security!

So what's the safer alternative? It may seem pretty obvious, but we really want to limit the amount of direct interaction our program has with the CLI. Go to Task 5 and look at the function safe_run. You can see that we are giving the subprocess.run function two parameters: "echo" and user_input. Notice the comma, these are two separate parameters as opposed to the unsafe_run function above. This distinction tells the program exactly how to process the user input in a way that does not give users direct access to the command line. The first parameter: "echo", is telling the operating system to launch the executable file called echo. Then, from within echo, input the user_data variable as a string. Since echo only does one thing, echo back whatever it's given, and the user_data has been fed directly to that file, nothing put in user_data is treated as a command. It is simply repeated back exactly as it was entered, making it impossible for hackers to inject malicious code into the command line.