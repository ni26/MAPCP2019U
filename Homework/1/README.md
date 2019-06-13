## Beginning of the README file’s content  

### MAPCP2019U - Introduction to Computer Programming (Summer 2019)  

Name: <first name> <last name>
UTA EID: <your UTA EID>
Email: <your email>
Department: Department of Physics
University: The University of Texas at Arlington
Level: graduate - <Freshman (1st year) / Sophomore (2nd year) / Junior (3rd year) / Senior (4th year) / Dinosaur (5th year and above) >
MAPCP-Class Title: Student
Course Webpage: https://www.cdslab.org/MAPCP2019U/
Photo:

### Description of the project’s content
This repository contains my homework, quizzes, and virtually every effort that I have made for MAPCP2019U class. The structure of the project is the following:

homework: (the homework hyperlink should take the reader to the homework folder)
This directory contains all my homework submissions, each of which is a folder properly named with homework number, containing the homework submission.

quiz: (the quiz hyperlink should take the reader to the quizzes folder)
This directory contains all my quiz submissions, each of which is a folder properly named with quiz number, containing the quiz submission.

exam: (the exam hyperlink should take the reader to the exams folder)
This directory contains all my exam submissions, each of which is a folder properly named with exam name or number, containing the exam submission.

For questions and troubleshooting, please contact:

<your name>
<your email>
<any other contact or signature information that you would like to add>

I have not failed. I’ve just found 10,000 ways that won’t work.
Thomas A. Edison

# End of the README file’s content

E) No. The test.txt doesn't exist in branch 2. We only made the changes to branch 1. So, I think that is why.

G) The error was $ git checkout test1
error: The following untracked working tree files would be overwritten by checkout:
        Homework/1/test.txt
Please move or remove them before you switch branches.
Aborting
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
