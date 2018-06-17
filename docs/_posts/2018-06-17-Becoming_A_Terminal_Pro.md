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

<p style="text-align:center;"> <img class="center" height="50" src="{{ "../htop_1.png" | absolute_url }}" alt="" /> </p>

This is where htop shows you how busy each core is in percentage. You will notice my computer shows 8 cores here, which is actually not true it is 4 virtual cores running on 2 physical cores. If htop shows here that everything is close to 100% you will have serious difficulties operating your computer because you are giving it more things to process than it can.

<p style="text-align:center;"> <img class="center" height="50" src="{{ "../htop_2.png" | absolute_url }}" alt="" /> </p>

Just below you can see the computers memory on the upper left side. If this bar is close to full you are putting more things on your desk than you can fit, which will again make your computer unresponsive. When a computer completely fills up his memory there is essentially no way out but pulling the plug. That is exactly why Swap was invented, which you can see right below. Swap is basicallly part of your harddrive (the file cabinet in the metaphor) pretending to be ram. It is a lot slower than ram because the harddrive can not read and write as quickly as ram. When your ram fills up the computer wil lstart putting things into swap, which will severely slow things down, but at least it will not completely crash your computer.

<p style="text-align:center;"> <img class="center" height="50" src="{{ "../htop_4.png" | absolute_url }}" alt="" /> </p>


On the right hand side of the top of htop you can see how many task you currently have open. This will seem like a lot but most are not active. In my case only 2 are actively runnning. Right below you will find the Load average which is a very important number to take into account. The load average tells you how many cores you are using on average (first number is averaged over one minute second number is averaged over 5 minutes and third number is averaged over 15 minutes). If your load average is equal to or higher than number of cores that show up at the top of the screen you are asking too much of your computer and you should consider killing some tasks. An optimum for handling a lot of work while still acttively using your computer is a load average of 2 or 3 lower than the number of virtual cores. Just below the uptime will tell you how long your computer has been switched on.

<p style="text-align:center;"> <img class="center" height="300" src="{{ "../htop_3.png" | absolute_url }}" alt="" /> </p>

So if your computer is having trouble this is where it came from. This is the list of processes whereing the culprit sits that is hurting your computer. The difficult thing is finding out who specifically is causing problems. So if your system is slowly grinding to a halt you need to figure out why in the top section of the screen. It's mostly either to ram filling up or cores being overused. When you press F6 you can sort the list of process by it's core and memory usage and kill the most demanding one. You kill a process by pressing F9 and then sending signals to the process. There are two main ones for stopping a process: SIGTERM and SIGKILL. SIGTERM is asking the process nicely to finish up and close down whereas SIGKILL just pulls the plug and ends the process. One should always use the former before resorting to the latter. 

So now we understand the command center we can focus on the most powerful tools that are provided in bash

### The Bash Toolkit

This section I will structure a little bit to make it more easily digestible. We are going to walk through and explain some of the most important built in commands of bash ranging from more basic to more complex tasks. I will also handpick some of the most useful command flags, which are the extra options you can specify introduced with a hyphen.

#####man
Man stands for manual and is the starting point of any command line list, because you can use it to get a lot of information about any commandi in bash. If you do not know what a command is doing just type in man followed by the command and you will be suprised of how much you can gather from here.
