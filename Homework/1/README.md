### MAPCP2019U - Introduction to Computer Programming (Summer 2019)    

**Name:** Niyousha Davachi  
**UTA EID:** 1001135833  
**Email:** <niyousha.davachi@mavs.uta.edu>  
**Department:** [Department of Physics](https://www.uta.edu/physics/)  
**University:** The University of Texas at Arlington  
**Level:** graduate  
**MAPCP-Class Title:** Student  
**Course Webpage:** [Our Course Page](https://www.cdslab.org/MAPCP2019U/)  
**Photo:** Will add soon.  

### Description of the project’s content

This repository contains my homework, quizzes, and virtually every effort that I have made for [MAPCP2019U class](https://www.cdslab.org/MAPCP2019U/). The structure of the project is the following:

* **[Homework](https://github.com/ni26/MAPCP2019U/tree/master/Homework):**    
    This directory contains all my homework submissions, each of which is a folder properly named with homework number, containing the homework submission.  
    <br>
* **[Quiz](https://github.com/ni26/MAPCP2019U/tree/master/Quiz):**  
    This directory contains all my quiz submissions, each of which is a folder properly named with quiz number, containing the quiz submission.  
    <br>
* **[Exam](the exam hyperlink should take the reader to the exams folder)
This directory contains all my exam submissions, each of which is a folder properly named with exam name or number, containing the exam submission.

For questions and troubleshooting, please contact:  

Niyousha Davachi  
niyousha.davachi@mavs.uta.edu

>I have not failed. I’ve just found 10,000 ways that won’t work.  
>[Thomas A. Edison](https://en.wikipedia.org/wiki/Thomas_Edison)

### Homework 1 Answers

**E)**   
No. The test.txt doesn't exist in branch 2. We only made the changes to branch 1. So, I think that is why.

**G)**   
The error was $ git checkout test1.  
```bash
error: The following untracked working tree files would be overwritten by checkout:
        Homework/1/test.txt
Please move or remove them before you switch branches.
Aborting
```
And it was fixed after pushing the changes to test2 branchi.

(I) My current working directory is master/Homework/1/, and what I see is the README.md file and the test.tx file. The test.tx file is the one that says "creating this file for the test1 branch".

(J) The error is CONFLICT (add/add): Merge conflict in Homework/1/test.txt
Auto-merging Homework/1/test.txt
Automatic merge failed; fix conflicts and then commit the result.
The reason it happens is that we have test.txt in both branches; both test1 and test2. So this makes git confused.

(K) I do not get any errors when checking out test2. I don't know why!

(L) When doing git stauts, it says everything is clear. It doesn't show any errors.

(O) When trying to delete branch test1 while on branch test2, this is the error I get:
error: The branch 'test1' is not fully merged.
If you are sure you want to delete it, run 'git branch -D test1'.

(P) Whwn I am in branch master, it easily deleted branch test1 from there. 
This is the message I got:
error: The branch 'test1' is not fully merged.
If you are sure you want to delete it, run 'git branch -D test1'.
In addition, when I do git branch, this is the message I get:
* master
  test2
So, looks like branch test1 is indeed deleted.

(Q) I think it is becasue when we are on branch test2 and try to delete branch test1, these two are not the same (i.e. not merged). But, when we are in branch master, and we try to dlete branch test1 from there, it easily does it because these two are merged and master is already updated by test1.

(R) The error I got is the following:
$ git branch -d test2
error: Cannot delete branch 'test2' checked out at 'C:/Users/Ni/Desktop/Git/MAPCP2019U'

(S) After deleting branch test2, and doing git branch, this is what I get:
$ git branch
* master

