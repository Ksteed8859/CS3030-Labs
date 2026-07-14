# SECTION 5 DOCUMENTATION

## Security & Robustness Checklist

### 1. Enforce Virtual Environments:
 A good rule of thumb is to only allow your script access to what it needs to run, and nothing more. One way to achieve this is to ensure the script runs in an isolated container, such as a venv. This way, the script has limited access to the host's system. It also allows for necessary dependencies to be installed only where the script is, and not system-wide.

 ### 2. Mask Environment Variables:
 Environmental Variables are anything that needs to be kept confidential. Think API Keys, Database Credentials, and System Settings. In the event that an unauthorized individual gets ahold of your code, you want to mitigate how many secrets they will gain access to. To do this, store any sensitive data within a .env file (which is also listed in the .gitignore). When pulling these variables into code, mask them, so even as they are being used it is impossible to tell what it says.  

 ### 3. Order Exception Catching
 Have your error catching systems be specifically labeled and ordered so that specific or expected errors are caught first. For example, if your script cannot find a file it needs, there should be a specific error along the lines of FileNotFound. As files being moved or deleted is a common occurrence, having a specific error relating to that saves you time on troubleshooting. For non-specific errors, a general "catch-all" error message will suffice.

 ### 4. Validate & Sanitize Inputs
 All incoming data or user inputs should be treated as untrusted. There are a large number of cyber-attacks that function by injecting malicious code or data into a script, such as shell injections, so validating and sanitizing inputs prevent that data from causing damage to the system. Avoid string formatting (f"{input}), use the built-in html module, or implement regular expressions to insure the data being entered matches what you want.

 ### 5. Enable Cohesive Logging
 Every critical action should be logged in a clear and cohesive way. In Task 2, we set up a log that clearly defines the type of warning, the time, and the message detailing what the warning is for. There should also be logs for things like file modifications or system log on's, so that you are always aware of what is going on in your system. 


 ## Technical Reflection

I think out of all of the modules we have completed in this class, Section 4 was my most difficult. Section 4 was our section on Automation and Admin, but it was also the first section where we worked "beyond" our code, so to speak. 

Up until then, our code was confined more or less to our own machines. We were doing things like creating logs to monitor our system health, designing scripts that automatically deleted .tmp and .log files, or reading files that we created on our local machines.

Module 4 was the first time we expanded our scripts beyond our personal machines, and made them interact with the web or other applications. In Task 3, we had our script ping URLs out on the world wide web and capture the status code. Or in Task 4, we used Webhooks to automatically send messages to third-party applications like Discord or Slack. 

It's a crucial skill to understand how our scripts can interact with the creations of other people, as it's unrealistic to believe that we will be the only person responsible for anything our script might need. But it also adds another layer of complexity. For example, in Task 4, not only did we need to understand our code and what were were making, but we also had to have a basic understanding of the third-party application and how it's Webhook needed to tie into our work. It required more research on my end. Not only did I need to learn how to write my own code, but I also needed to learn how to implement the connection from Discord, and I needed to keep in mind how to do it securely, as this could potentially open up a vulnerability that someone could exploit.