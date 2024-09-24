# Student Lab Assignment

## Summary of the application

Application that manages student lab assignments for a discipline. The application will allow to:

* Manage students and assignments. The user can add, remove, update, and list both students and assignments.
* Give assignments to a student or a group of students. In case an assignment is given to a group of students, every student in the group will receive it. In case there are students who were previously given that assignment, it will not be assigned again.
* Grade student for a given assignment. When grading, the program must allow the user to select the assignment that is graded, from the student’s list of ungraded assignments. A student’s grade for a given assignment cannot be changed. Deleting a student removes their assignments. Deleting an assignment also removes all grades at that assignment.
* Create statistics:
  * All students who received a given assignment, ordered alphabetically.
  * All students who have the average grae below 5 at a lab.
* Generate random students/prolems
* Unlimited undo/redo functionality. Each step will undo/redo the previous operation performed by the user. Undo/redo operations must cascade and have a memory-efficient implementation (no superfluous list copying)

# What I learned

## Python and what makes a language diffrent

* Even though C/C++ are high level languages, Python made those languages look low level or at least more closer to assembly with syntax that was easier to understand for humans. Since all the code that we write will become assembly code
(because that's the only language machines understand), it made me realize what truly makes a high level programming language diffrent. Questions like "am I allowed to do this" or "what happens in he baground if I do this or that" are the
questions that matter and which make programming languages diffrent. Sure syntax is important but often you will forget parts of it if you don't program in that language for a while, another thing I learned is thinking in a more general code(pseudocode)
and than just use the syntax of the language you're programming in.

* So, Python is a language written in C++, highly efficient if you want to focus just on implementing your idea as fast as possible and don't care about the speed efficiency your program runs. It doesn't have a compiler, it has an interpreter that interprets
every line of code. In python everything is an object including numbers. 2 types of objects: mutable - their values can change, non - mutable - trying to change their value will create a new object with that value. Parameters are always transferred through
reference.

## How to write code

Thre were a lot of new principles that were introduced to me which I applied for the first time here:

* Test-driven development - I think the important thing here is to test your functions, no matter if you write the function and than write the test function or the other way around
  
* GRASP and Layered Arhitecture - The whole purpose of this project was to get used to this structure that companies used like having diffrent classes for different stuff:
   * Repositary - Abstract class. A way in which we remember the inputs for a student for example. Class mainly for the storage of multiple objects of the same entity.
   * Service - Class that will coordinate everything that happens with certain entities. Repositary being just the storage and Service a way to manage that storage.
 
     
    All of this helps us keep the cupling low (dependency between modules) and cohesion high (degree to which the elements inside a module belong together).
  
* The importance of comments - With time my perception of comments has changed. Now I think that functions need to have an appropiate name of what it does, and if it's not clear enough only then you should comment on what that function does and NOT HOW it
  does it(if the function does something complex that is really hard to understand just by reading the code, only than comments are appropiate to help the programmers understand faster what is happening inside the function). Comments about the type of a
  variable should be used if you can't tell the type by the name of a variable(for example a variable called "name" makes it pretty clear that we're talking about a string).
  
* Single Responsibility Principle - Probably the most useful principle that saves you time in the future. A function should do one and only one thing. If it does multiple, than those need to be separated into diffrent functions.

### BIG mistake

The application will let you grade students on a problem. Since a student can have multiple problems and a problem can be assigned to multiple students, that means we have a Many to Many relationship, which means we need a new class called Grade or something.
I didn't do that:). Instead I though that the logical solution was to make my repository for problems have a dictionary of dictionarys. Big mistake which makes the code very hard to understand sometimes and made writing the code for this program harder
that it should be, but at least I experimented with dictionary of dictionarys.

### Overall

This is definetly not my best work. I made a lot of mistakes while also learning a lot of cool stuff that I carried in my next project:https://github.com/pstefangabriel/Lab9
