import subprocess

def unsafe_run(user_input):
    subprocess.run(f"echo {user_input}", shell=True)
    
def safe_run(user_input):
    subprocess.run(["echo", user_input])
    
# EXPLANATION

# In the first function, unsafe_run, the line shell=True means that whatever is in the string
# will be passed to the shell. The shell looks at the string as a set of commands, meaning that special
# characters like ;, |, &&, are treated as commands and not text. So if a hacker injected a payload like 
# `; rm -rf /` into the user_input variable, the first function reads it as "run echo" ; "run  rm -rf /".
# This is called a shell injection vulnerability, and it's a very easy way for hackers to get access to 
# sensitive information or cause serious damage to a system.

# In the second function, safe_run, the shell is completely bypassed. No commands are being sent from the
# function directly to the shell. Instead, the function tells the operating system to launch the executable file
# named echo, then pass this next argument straight into that program. The operating system is not looking for special
# characters like the first function was, it is treating everything as a string of text. So if a hacker were to try and run
#  `; rm -rf /`, the echo program would simply print the text on the screen exactly as it was typed, no secondary commands.