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

So now that we have covered some of the theory of how a computer works I want you to see it in action. A program that you can install and operates like a command central for your computer is htop. If you haven't instaleld htop do so now by typing 

```
sudo apt-get install htop
```
when you open htop it can be quite overwhelming at first but let us start at the top.

<p style="text-align:center;"> <img class="center" height="600" src="{{ "../htop_1.png" | absolute_url }}" alt="" /> </p>




