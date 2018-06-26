---
layout: post
title:  "Becoming a Terminal Pro - Part 2"
date:   2018-06-24
excerpt: "Masterclass"
image: "/images/proatterminal.jpg"
---

# Becoming a Terminal Pro: Part 2

## The UNIX Philosophy

We have covered the theory of computers, shells and some fundamental Bash
commands previously (see
[here](https://dtc-coding-dojo.github.io/main//blog/Becoming_A_Terminal_Pro/)
for last week's reports). In this masterclass, we will present the anatomy of a
Bash command, shell scripting and text-based tools such as `grep`, `sed` and
`awk`.  Before we delve into the terminal, it is important to state some of the
fundamental principles of the **Unix Philosophy**, as all of the tools we will
discuss today were made with these principles in mind.

1. [Do one thing and do it
   well](https://en.wikipedia.org/wiki/Unix_philosophy#Do_One_Thing_and_Do_It_Well).
2. [Everything is a file](https://en.wikipedia.org/wiki/Everything_is_a_file).
3. [Plain text is the universal
   interface](https://en.wikipedia.org/wiki/Unix_philosophy).

Most of the command-line tools we will use today have a very narrow, but
well-defined function. The strength of Bash and other UNIX shells comes not
from the individual tools themselves, but from how they interact.  The
universal interface for these tools is plain text, as opposed to binary code.
This is because these tools were made for you, a *human being*, not for
computers, and it is generally easier for a human to read plain text than it is
to read binary code.  Throughout this report, we will revisit and clarify these
principles where relevant.

## The Simple Command

The simple command is a list of **tokens**, separated by spaces or tabs (or
**blanks**), where the first token is the command to be executed and the
remaining tokens are its arguments. For example:

```
$ echo This is a command
This is a command
```

The command `echo` outputs its arguments to the terminal. Even at this basic
level, there are some peculiarities in Bash that we need to explain.  First of
all, because the arguments are passed to the program as a list of tokens, and
not as the literal string that you use to invoke the command, it does not
matter how many spaces you enter in between arguments:

```
$ echo apples bananas
apples bananas
$ echo        apples       bananas
apples bananas
```

In this example, both commands receive the same argument list `['echo',
'apples', 'bananas']`, even though the spacing in the simple command was
different. Let's write our first shell script to illustrate this further. Using
your favorite text editor, write the following script and save it to a file
called `args.sh`.

```
#!/bin/bash

echo Program name: $0
echo Argument 1: $1
echo Argument 2: $2
```

The first line in this script uses the shebang notation to indicate that the
script is a Bash script. We will discuss this in more depth later.

In a Bash script, the argument list is accessible by the special variable `$N`,
where `N` is the Nth argument. The zeroth argument is a special argument that
holds the command that invoked script. For instance, if we execute this script
without any arguments, we get the following output.

```
$ chmod +x args.sh
$ ./args.sh
Program name: ./args.sh
Argument 1:
Argument 2:
```

It may seem odd that a program or script should learn its own name through the
argument list, should it not know that already? The fact is that the program
name is just the name of the file containing it, which is an arbitrary label
and not known to the program *a priori*. We can rename the file to `zebra.sh`
and it will behave in exactly the same way.

```
$ mv args.sh zebra.sh
$ ./zebra.sh
Program name: ./zebra.sh
Argument 1:
Argument 2:
```

As before, when invoking `args.sh` with additional arguments, Bash splits up
the simple command into individual tokens, separated by blanks, and places them
into the argument list before it is passed to the program or script.

```
$ ./args.sh apples bananas
Program name: ./args.sh
Argument 1: apples
Argument 2: bananas
```

### Escaping Characters

The fact that Bash splits up the simple command in this way may pose problem
when you want to include spaces or tabs in your arguments.  For instance,
perhaps you want to print the line `Wait for it...        Here it is!` with a
bunch of spaces in the middle. One way to achieve this is to use **escape** the
meaning of space as a separator by using a backslash (`\ `).  When preceding a
character with a non-quoted backlash, you tell Bash that you want the character
to be interpreted *literally* and not with the special significance that it may
have in Bash commands.

```
$ ./args.sh apples\ bananas
Program name: ./args.sh
Argument 1: apples bananas
Argument 2:
```

In this example, we escaped the space between `apples` and `bananas` so that
the space was interpreted literally instead of as a token separator. In Bash, a
token is a string that is considered a single unit, and may may contain spaces,
tabs or newlines. The argument list in this example contains two tokens:
`['./args.sh', 'apples bananas']`.

There is one exceptional character which the non-quoted backslash does not
escape: the newline.  Instead, if you enter a backslash, immediately followed
by `Enter`, it is used for **line continuation**, meaning that you split your
command over multiple lines.

```
$ ./args.sh apples\
> bananas
Program name: ./args.sh
Argument 1: applesbananas
Argument 2:
```

If you want to enter literal newline characters, you need to use quoting.

### Quoting

Another method to group words together into tokens is to use **quotations**,
which in Bash come in two different flavours: single quotes (`'`) and double
quotes (`"`). The main difference is that double quotes allow you to perform
variable and command substitution (discussed later in the report) in the quoted
region, while single quotes preserve the literal string sequence.

```
$ var=cucumber
$ echo "$var"
cucumber
$ echo '$var'
$var
```

Quotations are ubiquitous in Bash and it is generally advised to enclose
variable substitutions with double quotes
([link](https://www.tldp.org/LDP/abs/html/quotingvar.html)). This avoids some
subtle bugs, one of which we actually have made in `args.sh`.  Consider the
following command:

```
$ ./args.sh "apples    bananas"
Program name: ./args.sh
Argument 1: apples bananas
Argument 2:
```

We would expect the spaces between `apples` and `bananas` to be preserved in
the script, but they have collapsed into a single space. This is because we
have not enclosed the variable substitution `$1` in double quotes. Hence, when
our script prints the first argument, the Bash interprets the line as follows:

```
# Command
echo Argument 1: $1

# Variable substitution
echo Argument 1: apples    bananas

# Argument list to echo
['echo', 'Argument', '1:', 'apples', 'bananas']
```

Since parameter substitution occurs *before* token splitting, the spaces
between `apples` and `bananas` count as blanks, hence they are processed as
separate tokens by Bash. We modify our Bash script with double quotes to
correct this.

```
#!/bin/bash

echo "Program name: $0"
echo "Argument 1: $1"
echo "Argument 2: $2"
```

Now we get the desired behaviour because `Argument 1: apples    bananas` is
interpreted as a single token.

```
$ ./args.sh "apples    bananas"
Program name: ./args.sh
Argument 1: apples    bananas
Argument 2: 
```

Note that even the empty string can be a token.

```
$ ./args.sh "" cucumber
Program name: ./args.sh
Argument 1:
Argument 2: cucumber
```

In this example, the argument list is `['./args.sh', '', 'cucumber']`. For more
information regarding quoting, see the `QUOTING` section in the Bash manpage
(`man 1 bash`).

## Standard Output, Standard Error and File Redirection

So far, we have discussed the argument list, which is a type of input to a
command.  We now focus on the output of commands.  Commands are capable of
printing text to the terminal as an output. For instance:

```
$ touch file
$ ls file
file
```

Here, the `ls` command prints the text `file` to the terminal. As discussed in
the introduction, **everything is a file**, and that includes the terminal
output.  In UNIX, every file opened by a process is associated with a number
called the **file descriptor**.  By default, programs write to the reserved
file descriptor `1`, also known as the **standard output**, or **stdout**.
Without any redirections, the standard output is linked to a special "file"
that represents the terminal.  We can show this explicitly by examining the
directory `/proc/self/fd`, which is a virtual directory, provided by the Linux
operating system, that displays the file descriptors of the current process.

```
$ ls -l /proc/self/fd/1
lrwx------ 1 thomas thomas 64 Jun 23 19:26 /proc/self/fd/1 -> /dev/pts/0
```

In this case, stdout is linked to the device file `/dev/pts/0`. This is the
file that represents the terminal.  Thus, when `ls` writes to stdout, it
appears on the terminal.  The redirection operator `> some_file` that we saw in
last week's session sets file descriptor `1`, or stdout, to `some_file` instead
of `/dev/pts/0`.  We illustrate this as follows:

```
$ ls -l /proc/self/fd/1 > /tmp/some_file
$ cat /tmp/some_file
l-wx------ 1 thomas thomas 64 Jun 23 20:15 /proc/self/fd/1 -> /tmp/some_file
```

Instead of printing to the terminal, the stdout of `ls` was redirected to
`/tmp/some_file`.

To drive the point home that the terminal output is exposed by UNIX as a file,
open up a second terminal and write to the device file that corresponds to the
first terminal (in my case `/dev/pts/0`).

```
# Terminal 1
$ ls -l /proc/self/fd/1
lrwx------ 1 thomas thomas 64 Jun 23 19:26 /proc/self/fd/1 -> /dev/pts/0

# Terminal 2
$ echo apples > /dev/pts/0

# Terminal 1
$ apples
```

You can write text to `/dev/pts/0` as if it was a file! Trying to open it with
a text editor will fail however because it is not a "regular" file, but a
"device" file, which imposes some restrictions on the type of operations you
can perform on it.

### Standard Error

As you execute commands and redirect their stdout, you may notice that some
terminal output may still appear. This is especially the case when an error
occurs.

```
$ ls non_existent_file > output
ls: cannot access 'non_existent_file': No such file or directory
```

What is going on here? It turns out that Linux commands often write to another
standardised file descriptor; the **standard error** or **stderr**.  The
standard error corresponds to file descriptor `2` and is also linked to the
terminal by default. It is mostly used to print error or debugging messages
that are not part of the expected output of the command.

```
$ ls -l /proc/self/fd/1 /proc/self/fd/2
lrwx------ 1 thomas thomas 64 Jun 23 20:38 /proc/self/fd/1 -> /dev/pts/0
lrwx------ 1 thomas thomas 64 Jun 23 20:38 /proc/self/fd/2 -> /dev/pts/0
```

Therefore, every Linux program has two distinct streams of output, stdout and
stderr, that both refer to the terminal by default but can be redirected in
Bash. This is achieved by the generalised redirection operator `n> file`, where
`n` is the file descriptor. For example, in the following command we redirect
stdout to `output` and redirect stderr to `error_log`.

```
# Redirect stdout to output and stderr to error_log
$ ls existing_file non_existent_file > output 2> error_log
$ cat output
existing_file
$ cat error_log
ls: cannot access 'non_existent_file': No such file or directory
```

We can also use `1> output` instead of `> output`, but because stdout is the
*standard* output, the redirection `> output` without explicit file descriptor
defaults to `1> output`.

You may sometimes need to redirect both stdout and stderr to the same file.
This can be achieved by redirecting stderr to stdout by entering `2>&1`.

```
# Redirect stdout and stderr to output
$ ls existing_file non_existent_file > output 2>&1
$ cat output
ls: cannot access 'non_existent_file': No such file or directory
existing_file
```

Note that the order of redirection matters because if `2>&1` comes before `>
output`, stdout is still linked to the terminal when stderr copies the stdout
link.  If `2>&1` comes *after* `> output`, stderr will copy the link to
`output` from stdout.  Since redirecting stderr and stdout to a file together
is a common operation, Bash provides the notation `&> output`, which is
shorthand for `> output 2>&1`.

```
# Redirect stdout and stderr to output
$ ls existing_file non_existent_file &> output
$ cat output
ls: cannot access 'non_existent_file': No such file or directory
existing_file
```

All of the above is also valid for the append operator `>>` (see last week's
report).

### The Null Device

Everything in UNIX is a file, although some files are not "regular" files in
the sense that they do not correspond to an actual file on a disk. Rather, they
are special files that support certain file operations.  We have seen one
example of this with the device file `/dev/pts/0` that corresponds to a
terminal.  Another special file that is often useful is the **null device**.
Like the terminal file, you cannot open it in a text editor, but you can read
from it and write to it.

```
$ cat /dev/null
$ echo banana > /dev/null
```

When you read from `/dev/null`, it acts as an empty file and returns no data.
When you write to `/dev/null`, the operating system simply discards the data,
not saving it in main memory or on the disk. It is useful when you want
suppress either stdout or stderr. For this reason, it is also called the "bit
bucket" or the "black hole".

```
# Discard stderr
$ ls existing_file non_existent_file 2>/dev/null
existing_file
```

In UNIX, even the void itself is a file.

## Standard Input and Pipelines

Having discussed stdout and stderr, the two standardised output streams that
every Linux program has access to, we now turn to **standard input**, or stdin,
which is the standard input stream.  As with stdout and stderr, the standard
input is a file descriptor that is linked to the terminal by default.  The file
descriptor for stdin is `0`.

```
$ ls -l /proc/self/fd/0
lrwx------ 1 thomas thomas 64 Jun 23 21:20 /proc/self/fd/0 -> /dev/pts/0
```

Whenever you run a command that asks for your input on the terminal, the
command is actually reading from the stdin file, which is the terminal by
default.

```
$ touch file
$ rm -i file
rm: remove regular empty file 'file'? y
```

Some commands accept terminal input indefinitely. For instance, the command
`cat` without any arguments copies the input from stdin to stdout.

```
$ cat > file
apples
bananas
# Stop input with Ctrl-D
$ cat file
apples
bananas
```

In this case, you need to use `Ctrl-D` to indicate the end of the stdin file,
i.e.\ no more input is available.

Similar to the redirection of stdout and stderr, we can redirect stdin to read
from a file instead of the terminal input. Since we are opening a file for
*reading* from it instead of writing to it, we use the `< file` notation
(shorthand for `0< file`).  We can thus run the interactive command of before
in an alternative way by writing `y` to the file `input_file` and then
redirecting stdin to `input_file`.

```
$ echo y > input_file
$ cat input_file
y
$ touch file
$ rm -i file < input_file
rm: remove regular empty file 'file'? 
```

In this example, we have used `input_file` to store the stdout of `echo y`,
which is then used as the stdin of `rm -i file`.  The pattern of using one
command's stdout as the stdin of another command is so common that UNIX
developers created the pipe operator `|` to accomplish this directly without
having to store intermediate results.

```
$ touch file
$ echo y | rm -i file
rm: remove regular empty file 'file'? 
```

When you use a pipe operator, you connect the stdout of one command to the
stdin of another command by using a **pipe**.  A pipe is a special type of file
that you can read and write from, and whose output is the same as what has been
written to it.  Thus, the pipeline `cmd1 | cmd2` redirects the stdout of `cmd1`
to a pipe, and redirects the stdin of `cmd2` to the same pipe.  We show this
with the following command:

```
$ ls -l /proc/self/fd/1 | { cat; ls -l /proc/self/fd/0; }
l-wx------ 1 thomas thomas 64 Jun 23 21:59 /proc/self/fd/1 -> pipe:[425929]
lr-x------ 1 thomas thomas 64 Jun 23 21:59 /proc/self/fd/0 -> pipe:[425929]
```

The curly bracket notation here is used to group commands together, so that we
execute `cat` and `ls -l /proc/self/fd/0` together as a single command after
the pipeline.  In this grouping, `cat` is used to display the output from the
command before the pipe operator (which is `ls -l /proc/self/fd/1` and shows
the stdout redirection).  We will not delve deeper into commands grouping here,
as it is a rather advanced Bash feature.

In any case, the first line shows that the stdout of the command before the
pipe operator is linked to `pipe:[425929]` with write-only permissions (see
`l-wx`), while the second line shows that the stdin of the command after the
pipe operator is linked to the same pipe with read-only permissions (see
`lr-x`).

This brings us to one of the more amusing examples of pipelines.  Apparently,
some UNIX developers found it so cumbersome to repeatedly enter `y` in the
terminal when running interactive programs, that they developed an application
that just writes `y` to stdout in an infinite loop.

```
$ yes
y
y
y
...
```

You can press `Ctrl-C` to interrupt the command.

Thus, if you are running some interactive program and cannot be bothered to
press `y`, you can pipe the output of `yes` instead.

```
$ touch file
$ yes | rm -i file
rm: remove regular empty file 'file'? 
```

To pipe the stdout and stderr together, you need to redirect stdout to stdin
using `2>&1`.  Alternatively, you can use the notation `|&`, which is short for
`2>&1 |`.

```
$ ls -l existing_file non_existent_file 2>&1 | cat > file
$ cat file
ls: cannot access 'non_existing_file': No such file or directory
existing_file
$ ls -l existing_file non_existent_file |& cat > file
$ cat file
ls: cannot access 'non_existing_file': No such file or directory
existing_file
```

The reason why this works is because the pipe redirection of stdout takes
places *before* any redirections specified on the command-line using `n> file`.

## Summary of Standard Files and Pipelines

In UNIX, everything is a file, but not all files are regular files that can be
opened in a text editor.  Device files, such as the ones that correspond to the
terminal, are abstract files that do not contain "data" like a regular file
does, but they support the same write and read operations that regular files
do.  Similarly, pipes are a special type of file that acts as a conduit between
a process writing to it and a process reading from it.

Every file opened by a process is associated with a unique number to identify
it, the file descriptor.  The file descriptors `0`, `1` and `2` are
**reserved** file descriptors and correspond to **stdin**, **stdout** and
**stderr**, respectively.  By default, they are linked to the terminal device
file, meaning that stdin reads from the terminal, and stdout and stderr write
to the terminal.

![Default files for stdin, stdout and stderr.](default.png)

Using the redirection operator `n> file`, where `n` is the file descriptor, we
can associate different output files to stdout and stderr.  When `n` is
omitted, the redirection defaults to stdout (file descriptor 1).

![Redirect stdout to `output_file` (`cmd > output_file`).](redirect_stdout.png)

![Redirect stderr to `error_log` (`cmd 2> error_log`).](redirect_stderr.png)

Stdout and stderr can be redirected to the same file by redirecting stderr to
stdout after redirecting stdout, e.g.\ `cmd > output_file 2>&1`.  You can also
use the Bash shorthand `cmd &> output_file`, which has the same effect.

![Redirect stdout and stderr to `output_file` (`cmd &>
output_file`).](redirect_stdout_stderr.png)

Similarly, you can specify stdin to be linked to a regular file instead of the
terminal.  The redirection operator for input files is `n< file`.  When `n` is
omitted, the redirection defaults to stdin (file descriptor 0).

![Redirect stdin to `input_file` (`cmd < input_file`).](redirect_stdin.png)

You are allowed to perform as many redirections as you like in the same
command.

![Redirect stdin to `input_file`, stdout to `output_file` and stderr to
`error_log` (`cmd < input_file > output_file 2>
error_log`).](redirect_stdin_stdout_stderr.png)

When you pipe two commands, Bash first creates a pipe, which has a write-end
and a read-end.  The stdout of the first command is redirected to the write-end
of the pipe and the stdin of the second command is redirected to the read-end
of the pipe.  The pipe is a special type of file that copies its input to its
output.

![Pipe stdout of first command to stdin of second command (`cmd1 |
cmd2`).](pipe.png)

For more information, see the `REDIRECTION` section in the Bash manpage, as
well as the `Pipelines` subsection in the `SHELL GRAMMAR` section.

## Filters

When you pipe two commands, the stdout of the second command is, by default,
linked to the terminal.  However, you can repeat this process iteratively and
pipe the stdout of the second command into a third command, and so on.  This
led to the concept of **filter** programs.  These are programs that accept
stream of data in its stdin, perform some operations on it and output a
modified stream of data in its stdout.  UNIX pipelines are extremely useful
because it makes it easy to combine the functionality of multiple small filter
programs that "do one thing and do it well", to perform complex operations on
data.

### `grep`

One of the most well-known and useful filters is the `grep` command.  The
syntax for `grep` is `grep PATTERN [FILE]`, where `PATTERN` is a regular
expression and `FILE` is optional.  When given a file, `grep` prints only those
lines that match the regular expression somewhere on that line.

```
$ cat fruit
apple and banana
kiwi and banana
pear and orange
$ grep 'banana' fruit
apple and banana
kiwi and banana
```

Notice the use of single quotes to specify the pattern.  It is generally
recommended to use single quotes when you are specifying a regular expression,
because Bash and regular expressions have many "special" characters in common.
Hence, if you do not use single quotes, Bash may preprocess your argument and
provide a different pattern to `grep` than you intended to.

When you do not supply a file as an argument, `grep` reads from stdin.  You
could provide this by preceding it with `cat fruit |`, which will pipe the
contents of `fruit` into the stdin of `grep`, or by directly redirecting stdin
of `grep` to the file `fruit`.

```
$ cat fruit | grep 'banana'
apple and banana
kiwi and banana
$ grep 'banana' < fruit
apple and banana
kiwi and banana
```

Sometimes you need to print all the lines that match `PATTERN1` *or*
`PATTERN2`.  You can specify multiple patterns with the `-e` option (short for
`--regexp`).

```
$ cat fruit | grep -e 'kiwi' -e 'orange'
kiwi and banana
pear and orange
```

In another case you might have to print all the lines that match `PATTERN1`
*and* `PATTERN2`.  There is no builtin option in grep for that, but in typical
UNIX fashion, you can achieve it by simply applying `grep` to the data twice!

```
$ cat fruit | grep 'banana' | grep 'apple'
apple and banana
```

After the first `grep`, only the lines that match `banana` remain.  By applying
the second `grep`, you select from those line only those that match `apple`.
Hence, you end up with lines that match both patterns.

You can also negate the matching logic and print only those lines that do *not*
match your pattern using the `-v` option (short for `--invert-match`).

```
$ cat fruit | grep -v 'banana'
pear and orange
```

You can turn off case sensitivity using the option `-i` (short for
`--ignore-case`).

```
$ cat fruit_mixed_case
apple and BANANA
kiwi and Banana
pear and orange
$ cat fruit_mixed_case | grep -i 'banana'
apple and BANANA
kiwi and Banana
```

A common use case of `grep` is to search for certain keywords in text files.
Often you would want to see some context to the matching line, e.g.\ show a
number of lines before or after the matching line.  You can match a number of
lines *before* the match with the option `-B` (short for `--before-context`).

```
$ grep -B 1 'pear' fruit
kiwi and banana
pear and orange
```

Similarly, print a number of lines *after* the match with the option `-A` (short
for `--after-context`).

```
$ grep -A 1 'apple' fruit
apple and banana
kiwi and banana
```

Finally, you can print a number of lines before *and* after the match with the
option `-C` (short for `--context`).

```
$ grep -C 1 'kiwi' fruit
apple and banana
kiwi and banana
pear and orange
```

When searching through files, it may also be useful to print the line number
along with the match.  You can do this with the option `-n` (short for
`--line-number`).

```
$ grep -n 'pear' fruit
3:pear and orange
```

If you do not wish to print the whole line that matches your pattern, but only
the matching pattern.  Use the option `-o` (short for `--only-matching`).

```
$ grep -o 'banana' fruit
banana
banana
```

Combine this with `wc -l` to count the total number of matches in the file.

```
$ grep -o 'banana' fruit | wc -l
2
```

Finally, you can use `grep` to search a directory recursively.  With the option
`-r` (short for `--recursive`), `grep` looks through all the files in the
directory and all its subdirectories for matching lines.

```
$ ls
fruit
fruit_mixed_case
$ grep -i -r 'banana' .
./fruit:apple and banana
./fruit:kiwi and banana
./fruit_mixed_case:apple and BANANA
./fruit_mixed_case:kiwi and Banana
```

Here, I supplied the current directory `.` as the search directory.  More
information on `grep` can be found on its manpage (`man 1 grep`). For quick
reference, use the command `grep --help`.

### `sed`

The name `sed` stands for **stream editor**.  It is a powerful tool for editing
streams of data that actually has its own scripting language.  However, we will
use it here only for its original and main purpose, which is text substitution.

Like `grep`, `sed` is a program that processes its input line by line.  It is
called in a similar way to `grep`, but instead of supplying a pattern, you give
`sed` a substitution command of the form `s/pattern/replacement/options`.  For
example:

```
$ cat fruit
apple and banana
kiwi and banana
pear and orange
$ cat fruit | sed 's/and/or/'
apple or banana
kiwi or banana
pear or orange
```

You can omit `replacement` to delete the match from the data stream.

```
$ cat fruit | sed 's/and//'
apple  banana
kiwi  banana
pear  orange
```

Note that `sed` will output every line, regardless of whether there was a match
on the line or not (as opposed to `grep`).

```
$ cat fruit | sed 's/kiwi/pineapple/'
apple and banana
pineapple and banana
pear and orange
```

Also, the choice of delimiter is arbitrary, we can also call `sed` as follows:

```
$ cat fruit | sed 's;and;or;'
apple or banana
kiwi or banana
pear or orange
```

If you want to use the delimiter inside the pattern or replacement, you must
escape it using the backslash:

```
$ cat fruit | sed 's/and/and\/or/'
apple and/or banana
kiwi and/or banana
pear and/or orange
```

This example also shows why it is a good idea to enclose the substitution
command inside single quotes.  If it was not quoted, Bash would interpret the
backslash as an escape for character `/`, and the backslash would thus not
appear in the substitution command to sed.

By default, `sed` only substitutes the first match it encounters in every line.
With the option `g` (for global), you replace every matches.

```
$ cat fruit | sed 's/na/no/'
apple and banona
kiwi and banona
pear and orange
$ cat fruit | sed 's/na/no/g'
apple and banono
kiwi and banono
pear and orange
```

The option `i` sets case insensitivity:

```
$ cat fruit_mixed_case
apple and BANANA
kiwi and Banana
pear and orange
$ cat fruit_mixed_case | sed 's/banana/cantaloupe/i'
apple and cantaloupe
kiwi and cantaloupe
pear and orange
```

It is also possible to provide a file on the command-line, instead of reading
from stdin.

```
$ sed 's/and/or/' fruit
apple or banana
kiwi or banana
pear or orange
```

However, you should never redirect the stdout of `sed` to the file that you are
reading from.

```
$ sed 's/and/or/' fruit > fruit
$ cat fruit
# Fruit is an empty file!
```

This removes the contents of the `fruit` because Bash redirects stdout to
`fruit` *before* running the `sed` command.  When using the `> fruit`
redirection operator, the file contents are deleted before the command is
executed.  The solution is to either redirect stdout to a temporary file first
and then overwriting your original file with the temporary file, or to use the
option `-i` (short for `--in-place`).

```
$ sed -i 's/and/or/' fruit
$ cat fruit
apple or banana
kiwi or banana
pear or orange
```

### `tr`

The program `tr` (short for translate) is similar to `sed` in the sense that it
performs text substition.  However, the differences are that `sed` is
line-oriented and based on regular expressions, while `tr` is
character-oriented and does not use regular expressions.  Generally speaking,
`tr` is a more basic tool, but is very useful to convert characters on the fly.

The syntax for `tr` is `tr SET1 SET2`, where `SET1` and `SET2` are sets of
characters.  The action of `tr` is to replace every character in the input
stream that appears in `SET1` with the corresponding character in `SET2`.

```
$ cat fruit
apple and banana
kiwi and banana
pear and orange
$ cat fruit | tr 'aeio' 'AEIO'
ApplE And bAnAnA
kIwI And bAnAnA
pEAr And OrAngE
```

If `SET2` is shorter than `SET1`, the last character of `SET2` is repeated
until `SET2` has the same length as `SET`.  Hence the following two commands
are equivalent.

```
$ cat fruit | tr 'aeio' 'A_'
Appl_ And bAnAnA
k_w_ And bAnAnA
p_Ar And _rAng_
$ cat fruit | tr 'aeio' 'A___'
Appl_ And bAnAnA
k_w_ And bAnAnA
p_Ar And _rAng_
```

This is particularly useful when you need to replace a set of characters by a
single character.

```
$ cat fruit | tr 'aeio' '_'
_ppl_ _nd b_n_n_
k_w_ _nd b_n_n_
p__r _nd _r_ng_
```

It is possible to specify "special" characters in the character sets, such as
newlines and tabs.

```
$ cat fruit | tr '\n' ';'
apple and banana;kiwi and banana;pear and orange;
```

There are also predefined characters sets that are specified with the special
syntax `[:name:]`.

```
$ cat fruit | tr '[:alpha:]' '_'
_____ ___ ______
____ ___ ______
____ ___ ______
$ cat fruit | tr '[:lower:]' '[:upper:]'
APPLE AND BANANA
KIWI AND BANANA
PEAR AND ORANGE
```

For a list of these escaped characters and predefined character sets, see its
manpage (`man 1 tr`).

When given the option `-d` (short for `--delete`), the second character set is
ignored and all the characters in `SET1` are deleted from the input stream.
For instance, the following command replaces all spaces and newlines.

```
$ cat fruit | tr -d ' \n'
appleandbananakiwiandbananapearandorange
```

As opposed to `sed`, the tool `tr` only works on stdin and stdout; you cannot
specify files as an argument or edit files in-place.  Thus you have to redirect
stdout to store your results.

### `awk`

AWK is a programming language for processing text files. It was initially
developed by Alfred **A**ho, Peter **W**einberger and Brian **K**ernighan (the
name comes from their initials).  The syntax for `awk` is a similar to `sed`;
`awk COMMAND [FILE]`, where `COMMAND` is a command in the AWK language.  Like
`sed`, AWK is an programming language in itself with many features, but here we
focus only on its ability to reformat field-separated text files.

By default, `awk` processes the input stream line by line and separates each
line into **fields**.  The default separators are spaces and tabs (this is
similar to the token separator in Bash).  In every line, the Nth field is
referenced by `$N`.  We can use the `print` statement to print a certain field
to stdout. For example:

```
$ cat fruit
apple and banana
kiwi and banana
pear and orange
$ cat fruit | awk '{ print $1 }'
apple
kiwi
pear
$ cat fruit | awk '{ print $2 }'
and
and
and
$ cat fruit | awk '{ print $3 }'
banana
banana
orange
```

You can also include literal strings in print statements:

```
$ cat fruit | awk '{ print "I prefer " $1 " over " $3 }'
I prefer apple over banana
I prefer kiwi over banana
I prefer pear over orange
```

You can specify any delimiter using the option `-F` (short for
`--field-separator`).

```
$ cat fruit.csv
apple,banana
kiwi,banana
pear,orange
$ cat fruit.csv | awk -F , '{ print "I will trade " $1 " for " $2 }'
I will trade apple for banana
I will trade kiwi for banana
I will trade pear for orange
```

Using just the print statement and the `-F` option, `awk` is a powerful to
manipulate data files that are formatted in fields such as comma-separated
values files.

#### Example: Printing Users and Default Shells

We illustrate how the tools we have discussed so far can be used and combined
easily process text files.  The file `/etc/passwd` contains information on all
the user and system accounts on the machine, such as their name and default
shell.  You can view your `/etc/passwd` file by executing `cat /etc/passwd` and
you will notice that it is a text file with a rather difficult to read format.
Suppose we are interested in viewing the users that do not have `nologin` or
`false` as their default shell.  Moreover, we only want to know their name and
default shell.  We can easily extract this information and print it in a nice
format using the tools we just learned.

```
$ cat /etc/passwd | grep -v nologin | grep -v false | sed 's;/bin/;;' | \
> awk -F: '{ print "User " $1 " uses the " $7 " shell." }'
User root uses the bash shell.
User sync uses the sync shell.
User thomas uses the bash shell.
```

If you have troubles understanding this pipeline, you can always build up the
pipeline gradually to understand what each step does.  For example, compare the
output of `cat /etc/passwd` and `cat /etc/passwd | grep -v nologin` to
understand what `grep` does.  Once you understand that, add the next command in
the pipeline and repeat until you understand the entire pipeline.

### `tee`

When you are redirecting the stdout of a long-running program to a file using
`> file`, you may want to see the output of your program on the terminal as
well.  This is where the utility `tee` comes in handy.  When you use `tee FILE`
in a pipeline, it will copy its stdin to stdout, as well as `FILE`.

```
$ cat fruit | sed 's/and/or/' | tee fruit_or
apple or banana
kiwi or banana
pear or orange
$ cat fruit_or
apple or banana
kiwi or banana
pear or orange
```

Since `tee` does not modify the data stream, just copies it to a file, you can
insert `tee` at any place in the pipeline to store extract the data at any
point in the pipeline.

```
$ cat fruit | sed 's/and/or/' | tee fruit_or | \
> tr '[:lower:]' '[:upper:]' | tee fruit_or_upper
APPLE OR BANANA
KIWI OR BANANA
PEAR OR ORANGE
$ cat fruit_or
apple or banana
kiwi or banana
pear or orange
$ cat fruit_or_upper
APPLE OR BANANA
KIWI OR BANANA
PEAR OR ORANGE
```

The name `tee` is derived from its function, as it forms a "T" junction in the
pipeline, preserving the flow of data while also copying it out to an external
file.

### `sort` and `uniq`

`sort` is a UNIX utility that sorts the input stream line per line.

```
$ cat countries
England
Tunisia
Belgium
Panama
$ cat countries | sort
Belgium
England
Panama
Tunisia
```

The default ordering is lexicographic, i.e.\ the dictionary ordering.  Using
the option `-n` (short for `--numeric-sort`), you can sort by numeric value.

```
$ cat score_countries
6 England
0 Tunisia
6 Belgium
0 Panama
$ cat score_countries | sort -n
0 Panama
0 Tunisia
6 Belgium
6 England
```

By default, `sort` sorts in ascending order.  Reverse the order with the option
`-r` (short for `--reverse`).

```
$ cat score_countries | sort -n -r
6 England
6 Belgium
0 Tunisia
0 Panama
```

Use the `-h` (short for `--human-numeric-sort`) option to sort by human readable
numbers, such as those outputted by `du -h`.

```
$ du -s -h /usr /bin /home
6.1G    /usr
13M     /bin
283G    /home
$ du -s -h /usr /bin /home | sort -h
13M     /bin
6.1G    /usr
283G    /home
```

When you have a text file that with repeated lines, use a `sort` followed by
`uniq` to get the set of unique lines.

```
$ cat colleges
Linacre
Pembroke
Christ Church
Pembroke
Oriel
Linacre
Brasenose
$ cat colleges | sort | uniq
Brasenose
Christ Church
Linacre
Oriel
Pembroke
```

To count how many times each line occurs, use the option `-c` (short for
`--count`).

```
$ cat colleges | sort | uniq -c
      1 Brasenose
      1 Christ Church
      2 Linacre
      1 Oriel
      2 Pembroke
```

#### Example: Printing Most-Frequently Used Commands

You can use `sort` and `uniq` to show your most frequently used commands.  Try
out the following pipeline and analyze it like the previous example to
understand what it does.

```
$ history | awk '{ print $2 }' | sort | uniq -c | sort -h | tail -5
     37 grep
     40 man
     71 echo
    145 cat
    181 ls
```

## Command Substitution

The stdout of some Bash commands are sometimes useful in the arguments of other
commands.  For instance, the command `which` gives the absolute pathname of a
command's executable file.

```
$ which ls
/bin/ls
```

**Command substitution** allows you to reuse a command's stdout in another
command's argument.  When writing `cmd1 $(cmd2)`, Bash first executes `cmd2`
and places its stdout in the argument of `cmd1`.

```
$ cp $(which ls) ./ls_copy

# After command substitution
$ cp /bin/ls ./ls_copy
```

In older scripts, you may encounter an alternative notation for command
substitutions using backticks (``cmd1 `cmd2` ``).

```
$ cp `which ls` ./ls_copy

# After command substitution
$ cp /bin/ls ./ls_copy
```

However, the use of backticks is considered outdated and should be avoided as
it is not as flexible as using the `$(cmd)` notation.

#### Example: Convert Manpages to PDF Document

Perhaps you want to print out a manpage on paper or you just prefer the PDF
format over the manpage format.  The option `-w` (short for `--where`) prints
the location of the manpage source file instead of opening the manpage.

```
$ man -w 1 bash
/usr/share/man/man1/bash.1.gz
```

This is a `gzip`-compressed file, so to view it you need to the command `zcat`,
which performs the same function as `cat`, but decompresses the file first.
Run the following command to convert the manpage to a PDF file and analyze the
command to understand what the command substitution does.

```
$ zcat $(man -w 1 bash) | groff -man | ps2pdf - - > bash.man.pdf
```

## Shebang Notation

A script is a sequence of commands executed by an **interpreter**.  The
interpreter is an executable program like `bash`.  A Bash script is run by
passing its filename to the `bash` command.  Bash will then open the script and
execute its commands one by one.

```
$ cat script.sh
echo "Hello World!"
$ bash script.sh
Hello World!
```

When you treat the script as an executable file however, the operating system
needs to know what interpreter to use on the script file.  This is specified
with the **shebang notation** `#!/path/to/interpreter` and must be on the first
line of the script.  The special sequence of characters `#!` at the start of
the file tells the operating system that the file is a script.  Linux then
reads the absolute path to the interpreter that follows the shebang and
executes it, passing on the script file to the interpreter's arguments.

```
$ cat script.sh
#!/bin/bash
echo "Hello World!"
$ chmod +x script.sh
$ ./script.sh
Hello World!

# This is equivalent to
$ /bin/bash ./script.sh
Hello World!
```

You have to provide an absolute path because the interpreter is launched by the
operating system, which does not perform automatic executable lookup like Bash
does by searching the directories in `$PATH`.

Other scripting languages also specify their interpreter using the shebang
notation.

```
$ cat script.py
#!/usr/bin/python
print("Hello World!")
$ chmod +x script.py
$ ./script.py
Hello World!

# This is equivalent to
$ /usr/bin/python ./script.py
Hello World!
```

The location of the `python` interpreter may differ on your system.  As
mentioned earlier, you can use `which` to see the location of the executable
file (if the command is not a shell builtin, as we will see later).

```
$ which python
/usr/bin/python
```

The method of how the operating system executes scripts can be made explicit
using `/bin/echo` instead of an actual interpreter.

```
$ cat script.echo
#!/bin/echo
$ chmod +x script.echo
$ ./script.echo
./script.echo

# This is equivalent to
$ /bin/echo ./script.echo
./script.echo
```

### Running Scripts with `source`

When executing Bash scripts, you may encounter some unexpected behaviour,
particularly when it comes to variables.

```
$ cat var.sh
#!/bin/bash
echo "var: $var"
$ var=pear
$ ./var.sh
var: 
```

You would expect your variable assignments to persist inside the script, but
that is not the default behaviour.  Whenever you run an *external* command in
Bash, like `/bin/bash`, Bash runs it in a **child process** or **subshell**.
This child process does not have access to the local variables of the parent.
However, you can set a variable to be an **environment variable** with the
command `export`, which means that it will be inherited by all child processes.

```
$ export var
$ ./var.sh
var: pear
```

However, it does not work the other way around.  Environment variables are only
inherited unidirectionally from shell to subshell (or from parent process to
child process).  Thus, any environment variables defined in a script will not
be visible to the shell when it is run in a subshell.

```
$ cat export.sh
#!/bin/bash
child_var=cantaloupe
export child_var
$ ./export.sh
$ echo "child_var: $child_var"
child_var: 
```

This poses a problem when you write a script that is intended to modify the
current shell's environment.  Fortunately, there is a shell builtin command
`source` (or its synonym `.`) to run a script in the current shell environment.

```
$ cat source_example.sh
source_var=watermelon
$ source source_example.sh
$ echo "source_var: $source_var"
source_var: watermelon
```

The main difference between running a script using `/bin/bash` and `source` is
that the former command invokes the external program `/bin/bash` in a subshell,
while the latter command is a shell builtin that does not leave the current
shell environment.  You can check whether a command is an external program or a
shell builtin using the shell builtin `type NAME`, which displays information
on how Bash interprets the command `NAME`.

```
$ type bash
bash is /bin/bash
$ type source
source is a shell builtin
$ type type
type is a shell builtin
```

If the command is an external program, `type` will show its absolute path.
Note that the documentation for shell builtin commands is displayed using the
shell builtin `help`, and not `man`.

```
$ man source
No manual entry for source
$ help source
source: source filename [arguments]
    Execute commands from a file in the current shell.
    
    Read and execute commands from FILENAME in the current shell.  The
    entries in $PATH are used to find the directory containing FILENAME.
    If any ARGUMENTS are supplied, they become the positional parameters
    when FILENAME is executed.
    
    Exit Status:
    Returns the status of the last command executed in FILENAME; fails if
    FILENAME cannot be read.
```

Running `help` without any arguments displays a list of shell builtin commands.

## Resources for learning more

* `man 1 bash`
* `help`
* [Introduction to Linux on
  edX](https://www.edx.org/course/introduction-linux-linuxfoundationx-lfs101x-1)
