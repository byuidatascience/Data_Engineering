## GalvanizeU-University of New Haven <br> Master of Science in Data Science <br> DSCI 6007: Distributed and Scalable Data Engineering <br>

### Logistics

__Lead Instructor:__ [Alessandro Gagliardi](mailto:alessandro@galvanize.com)  
__Assistant Instructor:__ [Conor Murphy](mailto:conor.murphy@galvanize.com)  

__Class Location:__ 44 Tehama St, 309 classroom, San Francisco, CA  
__Class Days/Times:__ Monday, Tuesday, Thursday, Friday 11am-1pm  
__Lab Days/Times:__ Monday, Tuesday, Thursday, Friday 2-3pm  
__Office Hours:__ Monday, Tuesday, Thursday, Friday 10-11am  

__Communication:__ [Slack Channel](https://gstudent.slack.com/archives/gu5_sf_de)

----

### Course Description

DSCI 6007: Distributed and Scalable Data Engineering will introduce you to working with distributed systems for efficiently collecting and analyzing large quantities of varied data.

#### Learning Objectives

By the end of the course, you should be able to:  
(_not a complete list_)

- Install and run a Linux virtual machine locally and in the cloud
- Utilize \*NIX command line tools to manipulate and analyze data
- Deploy and manipulate data and working code in the cloud
- Write complex SQL queries
- Design a database that conforms to the third normal form (3NF)
- Identify embarrassingly parallelizable tasks and parallelize them
- Describe and apply the MapReduce algorithm
- Describe and apply Spark's DataFrame abstraction
- Perform machine learning on a cluster
- Process data in pseudo-realtime
- Apply probabilistic data structures to handle high volume/velocity data
- *Build an end-to-end distributed data-pipeline*

#### Course Methodology: _What Not How_

Materials for this course will focus more on *what* needs to be accomplished, and less on *how* to accomplish it. That is, you will still need to know how to accomplish these goals, but you may be expected to be more self-reliant on finding and utilizing those materials yourself than you have been in the past. This course promotes *ideation*, or translating worldly problems into data problems. *The power of this tool cannot be underestimated for once we translate a worldly problem into a data problem we move into the realm of Moore's law and our impact becomes exponential.* This is a shift from having pre-made exercises common in data science curriculums to having to think critically about your motivating question and the end-to-end implementation of your pipeline.

Being able to teach yourself how to use a new technology is essential to your role as a data scientist. These tools evolve quickly and what is wired today will be tired tomorrow. It is not unknown for a tool to be deprecated in the course of a minimester. To the extent that we do provide instructions on "how", and do our best to keep the content of the course as up-to-date as possible, sometimes links will be dead, instructions will be out dated, and so on. You will have to rely on your colleagues and your ingenuity to figure out what to do.

### Required Books

None. Data Engineering is a new and evolving field, and there is no standard book that covers it completely and is current. We will post readings for each day.  They will be video tutorials, book chapters, and blog posts.  

### Optional Books

- [Agile Data Science 2.0](http://shop.oreilly.com/product/0636920051619.do) by Russell Jurney. This is the unofficial textbook for this course. It is still being written. (It is scheduled to be published just before finals week.) But you can get an early release ebook from O'Reilly. Jurney makes a few choices in his architecture which I would advise against, but overall, his stack is a lot like the one we will be developing. Jurney's book is fairly accessible. I may reference it throughout the course, though I will be sure to do so in a way that does not require you to actually own a copy yourself.
- [Big Data](https://www.manning.com/books/big-data) by Nathan Marz with James Warren. This was the original unofficial textbook for this course. The technologies used in this book were already out of date by the time it was published two years ago, but the overall strategy of the book has not changed. In fact, Jurney's architecture resembles Marz' in many ways. The most important chapters in this book are the first two which, conveniently, are available for free on the book's website.
- [Designing Data-Intensive Applications](http://shop.oreilly.com/product/0636920032175.do) by Martin Kleppmann. The other unofficial textbook for this course. This book takes a different approach than we will. While the two books above follow a path of building out a data pipeline from end to end, as we will in class, Kleppmann's book is organized more by topic: Replication, Partitioning, _etc._ I recommend it as a resource that will more likely be useful to you towards the end of this course and beyond as you go to take this material to your practicum site.

### Class Structure

This course is an "active" learning environment. You'll learn through doing. The focus will be applying concepts to data through programming.

Before class you will complete preparation materials (e.g., watch videos, read chapters, and complete workbooks). All preparation materials should be covered prior to the start of each class session. They are **always required** unless explicitly labeled as optional. These materials will be resource for factual knowledge. We will not be delivering traditional lectures. You are expected to be familiar with the basic concepts and technical jargon by the start of class.

In-class time is precious - We'll reserve it for discussion, presenting complex material, answering questions, and working on exercises.

Typical class structure:

- On Your Own (OYO) activity
- Review yesterday's lab
- RAT about previous material
- Discussion of today's topic
- Conceptual overview and techniques necessary to complete the lab
- Lab: Students work in pairs on the exercise

### Labs

Most days will include a module that will introduce a new topic. Each module includes a lab assignment. Most lab assignments will be paired programming assignments. Unless otherwise noted, lab assignments are due before the following class. (_i.e._ Tuesday's lab assignment is due Thursday at 9 a.m.) Some lab assignments may be submitted in the form of notebooks (Jupyter or Zeppelin) but most will be in the form of `.py` files. These files are expected to conform to [PEP 8](https://www.python.org/dev/peps/pep-0008/) standards. Adherence to these standards is a requirement of this course and failure to do so may affect your grade. Since many of you are new to programming, we will go easy on you at first, but by the second week, all of your code should follow these standards.

Following the first week, students will be called upon to present their own lab solutions for critique. Every student *must* present at least one lab during the term.

#### RAT

The Readiness Assessment Tests (RATs) are intended to test your understanding of the materials presented thus far in the course. This includes recent preparation material and items from previous classes. There are 3 parts: individual, small-group, and class

1. Each student will answered all the questions on the RAT individually.
2. Then the class will split into teams of 3-5. Each team will answer the same questions again, the goal is to reach consensus. This is an opportunity for peer-to-peer instruction which is often more effective than lectures!
3. Finally, the answers to the questions will be gone over by the class, hopefully resolving any final misunderstandings before proceeding with the exercises.

#### Pair programming

"Pairing" is where two programmers are working on the same code at the same time. It is a great way to improve as programmer and solve problems. One acts as the "driver", the other as the "navigator". The driver types and the navigator helps. For example, the navigator might name variables or look up documentation. Pairs will change every class.

### Project Presentations

Presentation are one way to demonstrate your learning, but more importantly it is practice for organizing and communicating your work and ideas. The presentations will function similar to code reviews in-front of your peers and instructors, who will function like Senior Developers. The purpose of students presenting work is two-fold:

All students will learn from all exercises, whether or not they had time to complete them in class.
Students will get to see alternative approaches to the exercises they did complete.

### Grades

| Item         | Weight |  
|:------------:|:------:|
| Mastery Tracker | 25% |  
| Labs          | 15% |
| Participation | 10% |  
| Final Project | 50% |

The expected grade for this class is a B+. Getting an A- or above requires completion of the Mastery Tracker, high level participation, and a stellar final project.

#### Mastery Tracking

Mastery Tracking is a tool to provide feedback student learning. Standards are the core-competencies of MSDS graduates - the knowledge, skills, and habits every student should possess by time they graduate. Standards are measurable, student-focused outcomes that state what students are expected to be able to do by the end of the course. Students who are below ‘mastery’ on a standard are expected to continue practicing said standard (with the instructor's guidance) until they reach mastery. What matters is that students eventually learn the material, not how many attempts it takes to get there. The Lead Instructor and Assistant Faculty are available to offer feedback and help guide everyone on their mastery journey.

Mastery Tracking uses a 4-point scale. Every student is expected to achieve 3 or above (Mastery) across all Standards by the end of the course. 1s and 2s indicate areas where students need further practice and/or interventions to reach mastery.

##### 4 pt Scale:

0 = Has not been covered  
1 = Falling far below mastery - Meeting none of the success criteria or has egregious errors  
2 = Approaching mastery - Meeting some of the success criteria  
3 = Mastery - Meeting all of the success criteria  
4 = Exceeding mastery - Truly exceeding expectations and demonstrating proficiency at a higher level of rigor  

#### Participation

You must also show up prepared. Each person is important to the dynamic of the class, and therefore students are required to participate in class activities.

#### Class Attendance

Attendance is mandatory. It is the responsibility of the student to attend all classes. If you have to miss class, due to sickness or other circumstances, please notify your instructor by Slack in advance. Supporting documents (doctor’s notes) should accompany absences due to sickness. Each excused absences beyond 2 or any unexcused absences will result in lowering your __overall course grade by ⅓ of an entire letter grade__ (A->A-, A->B+). It is at the instructor’s discretion to deny any absences or to allow students to make-up assignments, exams, etc. resulted from any absences.

### Course Requirements

#### Prerequisites

_None._

### Electronic Device Policy

Cell phones can be highly disruptive to the class environment. Please silence these devices. In the event of the need to use electronic devices during an person emergency, please step out of the classroom.

Laptops similarly must be closed during RATs and lecture. You are advised to take notes using pencil and paper. Research shows that this is better for retention and less likely to distract from the classroom experience.

### Late Assignments

All assignments are due before the following class. (_e.g._ Labs assigned on Tuesday are due Thursday morning.) Partial credit is available for labs turned in no more than 24 hours late. Beyond 24 hours, lab work may count towards the mastery tracker but will not be awarded credit of themselves.

### Academic Integrity

The University of New Haven is an academic community based on the principles of honesty, trust, fairness, respect, and responsibility. Academic integrity is a core University value which ensures respect for the academic reputation of the University, its students, faculty and staff, and the degrees it confers.

The University expects that all students will learn in an environment where they work independently in the pursuit of knowledge, conduct themselves in an honest and ethical manner and respect the intellectual work of others. Each member of the University community has a responsibility to be familiar with the definitions contained in, and adhere to, the Academic Integrity Policy. Violations of the Academic Integrity Policy include, but are not limited to:

- Cheating -- _i.e._ Don't read off of your neighbors exams
- Collusion -- Group work is encouraged except on evaluative exams. When working together (on exercises, etc.), acknowledgment of collaboration is required.
- Plagiarism -- Reusing code presented in labs and lectures is expected, but copying someone else's solution to a problem is a form of plagiarism (even if you change the formatting or variable names).
- Facilitating academic dishonesty

Students who are dishonest in any class assignment or exam will receive an "F" in this course. More information regarding UNH’s official academic integrity policies are outlined in [here](http://www.newhaven.edu/334887.pdf).

### Schedule

See [README](README.md) for updated schedule.
