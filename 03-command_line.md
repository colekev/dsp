# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

cat - show the contents of a file in terminal
grep - search for text in file
find - finding files
'|' - piping from one command to another on the same line
pwd - print working directory
cd .. - move directory up one level 
man - bring up the manuel for a command in terminal
locate - search for filename or contents of a file
sort - sort the contents of a file
cut - cut part of a file

---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

'ls' list directory contents
'ls -a' include directory entries whose names begin with a dot
'ls -l' list in long format
'ls -lh' list in long format with unit suffixes
'ls -t' list and sort by time modified
'ls -Glp' long format list with colorized output enabled and slashes after directory names

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

'ls -R' list subdirectories
'ls -d' displays only directories
'ls -m' displays names as a comma-separated list
'ls -1' displays each entry on one line
'ls -g' displays the long format listing excluding owner name

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

'xargs' adds arguments to complete a command, the executes the resulting command. 

'ls | xargs -n 3 echo' is adding the arguments to display in three column to the 'ls' command

 

