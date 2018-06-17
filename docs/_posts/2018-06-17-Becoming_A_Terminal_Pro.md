---
layout: post
title:  "Becoming a Terminal Pro - Part 1"
date:   2018-06-11
excerpt: "Masterclass"
image: "../proatterminal.png"
---
### The Basics
Using the terminal properly can make your life a lot easier and your analysis a lot quicker if you know what you are doing. The terminal of Linux and Max machines runs the Bourne-again shell called Bash. Bash is your way to communicate with your computer directly and can save you a good deal of programming if you know what to say to your computer. To learn how to speak to a computer it is helpful to understand the basics of how a computer works. 

Bash is a shell language which is like a specific kind of programming language that wraps around the computers kernel like a shell. The kernel is what sits at the hear of every computer. The kernel controls all the hardware that sits in your computer and tells all the different hardware components what to do. Linux for example is not an operating system like windows it actually is a kernel. The operating system sits on top of the kernel and provides a user interface. So when we do something on the user interface it translates our actions to the kernel which then communicates to the actual physical parts of the machine. 

Speaking of which, what are the important parts of your computer? The three main compartments to understand how programming works is a central processing unit (CPU), the random access memory (RAM) and the harddrive. Imagine your computer to be a study room where you're trying to work. The disk would be a file cabinet where you store all your documents for long term use. The Ram would be the desk where you take your documents to be able to work on them. You who provides all the work, you are the CPU. That is why a good cpu is very important because it is the most crucial to how powerful your machine is. Of course a stellar CPU can't process a lot of documents without a big desk to work on them all or a file cabinet ot store them. Now if you are working on these documents you could do this with either one hand or two hands to speed up things. The hands here are like CPU cores. The more CPU cores you have, the more task you can do parallely. Nowadays good work machines can typically have up to 16 cores which means you can technically run 16 tasks separately. CPU cores have become so fast individually that DELL invented a way in which you can pretend to have two cores in one, meaning that even an individual core can handle two tasks at one because it is so powerful. This is called hyper-threading and can drastically speed things up.

So now that we have covered some of the theory of how a computer works I want you to see it in action. A program that you can install and operates like a command central for your computer is htop. Htop is the way to figure out what is going on where and why does the computer crash. If you haven't instaleld htop do so now by typing 

```
sudo apt-get install htop
```
when you open htop it can be quite overwhelming at first but let us start at the top.

<p style="text-align:center;"> <img class="center" width="800" src="{{ "../htop_1.png" | absolute_url }}" alt="" /> </p>

This is where htop shows you how busy each core is in percentage. You will notice my computer shows 8 cores here, which is actually not true it is 4 virtual cores running on 2 physical cores. If htop shows here that everything is close to 100% you will have serious difficulties operating your computer because you are giving it more things to process than it can.

<p style="text-align:center;"> <img class="center" width="800" src="{{ "../htop_2.png" | absolute_url }}" alt="" /> </p>

Just below you can see the computers memory on the upper left side. If this bar is close to full you are putting more things on your desk than you can fit, which will again make your computer unresponsive. When a computer completely fills up his memory there is essentially no way out but pulling the plug. That is exactly why Swap was invented, which you can see right below. Swap is basicallly part of your harddrive (the file cabinet in the metaphor) pretending to be ram. It is a lot slower than ram because the harddrive can not read and write as quickly as ram. When your ram fills up the computer wil lstart putting things into swap, which will severely slow things down, but at least it will not completely crash your computer.

<p style="text-align:center;"> <img class="center" width="800" src="{{ "../htop_4.png" | absolute_url }}" alt="" /> </p>


On the right hand side of the top of htop you can see how many task you currently have open. This will seem like a lot but most are not active. In my case only 2 are actively runnning. Right below you will find the Load average which is a very important number to take into account. The load average tells you how many cores you are using on average (first number is averaged over one minute second number is averaged over 5 minutes and third number is averaged over 15 minutes). If your load average is equal to or higher than number of cores that show up at the top of the screen you are asking too much of your computer and you should consider killing some tasks. An optimum for handling a lot of work while still acttively using your computer is a load average of 2 or 3 lower than the number of virtual cores. Just below the uptime will tell you how long your computer has been switched on.

<p style="text-align:center;"> <img class="center" width="800" src="{{ "../htop_3.png" | absolute_url }}" alt="" /> </p>

So if your computer is having trouble this is where it came from. This is the list of processes whereing the culprit sits that is hurting your computer. The difficult thing is finding out who specifically is causing problems. So if your system is slowly grinding to a halt you need to figure out why in the top section of the screen. It's mostly either to ram filling up or cores being overused. When you press F6 you can sort the list of process by it's core and memory usage and kill the most demanding one. You kill a process by pressing F9 and then sending signals to the process. There are two main ones for stopping a process: SIGTERM and SIGKILL. SIGTERM is asking the process nicely to finish up and close down whereas SIGKILL just pulls the plug and ends the process. One should always use the former before resorting to the latter. 

So now we understand the command center we can focus on the most powerful tools that are provided in bash

### The Basic Bash Toolkit

This section I will structure a little bit to make it more easily digestible. We are going to walk through and explain some of the most important built in commands of bash ranging from more basic to more complex tasks. I will also handpick some of the most useful command flags, which are the extra options you can specify introduced with a hyphen. 

Some of the commands i will describe can be chained together which is called piping in programming. Piping will take the output from one command and use it as an input for another command without you having to do that manually. \| is called the pype sympol and separates different commands in a chain like so:

```
(command_1) | (command_2) 
```

Similarily you can pipe the output of a program into a text file by using the > sign like so 

```
(command_1) | (command_2) > (output)
```

Be careful with what output file you specify as the firs action of the > sign is to empty that file. If you want to append to the end of a file use the sign twice like so >>.

A number of the commands you will find are impossible to execute and produce an error message along the lines of permission denied. A lot of the security and hence the reliance of programming on linux is due to the use of a super user system. The message you are receiving denotes that you are not a member of the eluded super user group, which to you will make things a lot more difficult. Overall however, keeping super user privilegesto the more experiences users makes linux a good programming playground. Essentially, if you are not a super user linux will keep you from doing things which could damage the system. Commands that could possibly do so are preceded by a sudo which means super user do. If you can not execute a sudo command with your normal user name and password there is no way around asking the administrator of your system to grant you super user rights or find another way to solve your problems.

Having introduced some of the basic concepts of the bash toolkit, here are some of the tools that you can use:

* **man** - Man stands for manual and is the starting point of any command line list, because you can use it to get a lot of information about any commandi in bash. If you do not know what a command is doing just type in man followed by the command and you will be suprised of how much you can gather from here. If man doesn't work most programs have the -h or --help option to give a description about what the programs do'

* **ls** - ls lists all the files in the directory you're in which is quite basic. You can get a lot more info with ls -lhtr, which lists all files with human readable (h) file sizes (l) in reverse (r) chronological (t) order. This way you can always stay on top what was most recently created

* **cd** - changes directories into whatever you specify after. If you do not specify anything it will take you back to your home directory, which can also be noted as ~. Two dots get you back a directory

* **pwd** - Gives you the full path of what directory you are in

* **rm** - Removes whatever you give it to. Especially dangerous when you use it with globbing, which is when you use special characters that stand in for multiple different characters. The star (\*) is one of the most useful here which extends to any character or number of characters. For example \*.txt would give you all files ending in .txt. As powerful as it is, it is alos very dangerous. Rm \* will irretrievably remove every single file in the current directory. Directories need to be removed with -r which means recursive. Always handle rm with care.

* **touch** - Creates a file with a name that you can specify after the touch command.

* **mkdir** - Similar to touch but creates a directory

* **cp** - Copies the first argument after into the location of the second item after the command. -v which means verbose is quite helpful as it tells you more about what it is doing at the moment. However if cp fails you would need to restart it from scratch and for big folders that can be very annoying. I reccommend rsync instead, which is essentially the same but will synchronise two folders instead of just copying files. If rsync fails you can restart it and it will pick up where it left off. -u is also a useful option for both cp and rsync which only copies files which are newer than versions of the file in the new destination.

* **mv** - Moves files from whatever you specify first to whatever you specify seconf. Be careful not to overwrite important files.

* **ln** - Ln is somewhat of a more sophisticated version of the copy command. Instead of copying the file it will put a sign into the folder which points to the location of the original file. This way you can access and modify files without duplicating them, which safes a lot of time and space. This is called a softlink which is produced with the -s flag. When a softlink is deleted, the original file will be untouched making it also very safe to use.

* **df** - Stands for disk free and will tell you how much space is used on your disk. It will also lit different partitions which is the way in which we partmentalise computer disks. Partitions are different drawers on the file cabinet that is your disk. Your whole disk could only be one partition or split into many different partitions. Making, removing or resizing partitions is a potentially very dangerous operation which should be kept to more experienced users. A useful flag here as in many other programs is the -h which will translate raw bytesizes into a more human readable byte, kilobyte, megabyte, gigabyte notation. If any of the percentages are very close to 100% and you are actively using that partition or drive, you will soon run into a space issue which you should prevent by removing big files.

* **du** - Is the abbreviation of disk usage and the way to find big files on your system. Going recursively into every downstream folder, du will tell you the size of every folder and file on the way. Again a useful flag is -h which will make the output more digestible. You can sort this list by piping it into sort -n which will give you a sorted list of files in order of their size.

* **find** - Does exactly what it promises it finds files. After noting which directory you want to look at staight after the find command you need to specify your searching criteria. You can use globbing like we introduced in the rm command. For example find . -name "\*.fa" will find every fasta file withing every file and subfolder of the current directory (denoted by the dot). Find will return a list of the paths of every file it found. If you want to use another command on the files you found you can do so straight away by using the -exec flag. This flag has a special syntax where {} is the placeholde of the files you found and the line end of the command has to be noted by \;. For example find . -name "\*.fa" -exec mafft {} \; will run the alignment program mafft on every fasta file it finds (see last weeks report for an intro to mafft).

* **watch** - Exectutes any command you give it repeatedly in two second intervals. If you want to change the time interval you can use -n to tell watch how many seconds it should wait between execution. With -d you can tell watch to highlight differences in output between the last iteration of the command. For example by typing watch -n 60 -d ls you can watch in real time what files are created in a folder with changes being highlighted. This can be very useful if you are executing programs which generate a lot of different files as output. 

This is the first set of useful tools which come shipped with bash and I highly encourage you to play with them pipe them into different other programs and see what they do. There are limitless combinations of how you can stick different commands together to make them do really complicated tasks. This is only the first part of a two part masterclass dedicated to the bash terminal. Next week we will talk about text related programs like grep and sed which are some of the most useful commands in bioinformatics 
I can image.



