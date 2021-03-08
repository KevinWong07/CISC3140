## Kevin Wong
## CISC 3140
## Lab 4

### How 2 Linux

First. If you're reading this and are already using a Linux system, why are you here?  
Second. Follow the instructions at [this link](https://docs.microsoft.com/en-us/windows/wsl/install-win10) to download and install a Linux subsystem on your Windows computer. 

Now that you have downloaded and installed a Linux system, you will need to learn about what the basic commands are.  

| Commands | Description | Example Usage |  
| --- | --- | --- |  
| whoami | Displays current user profile | $ whoami |
| ls | List all files in current directory | $ ls |
| pwd | List directory user is currently in | $ pwd |
| mkdir | Creates a new directory | $ mkdir FolderName |
| rm | Removes file/directory | $ rm FileName |
| mv | Moves file/directory from one place to another | $ mv File1 Folder 2 |
| cp | Copies file to another | $ cp File1 File2 |
| cat | Views content of a file | $ cat File1 |

There are also default programs, also known as `apt packages` that will be installed when you're installing the system. Please run the following code to update the apt package list and ensure you're running everything on the most recent software patches.  
`$ sudo apt update && sudo apt upgrade -y`  

Here is a list of tools that are installed and most commonly used. 

| Programs | Description | Example Usage |  
| --- | --- | --- |  
| curl | Allows user to access a url | $ curl github.com |
| wget | Downloads files from provided url | $ wget https://github.com/Username/Repo/FileName |
| zip | Compresses files/directories into a file | $ zip  |
