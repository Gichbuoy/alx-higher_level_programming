### Test-driven development (TDD) 
- is a software development practice that emphasizes writing tests before writing the actual code. TDD follows a cycle of writing a failing test, writing the minimum amount of code to make the test pass, and then refactoring the code to improve its design while keeping the tests passing. The goal of TDD is to ensure that the code is thoroughly tested and meets the desired specifications.

- In Python, you can practice test-driven development using various testing frameworks such as unittest, pytest, and doctest. Here's a general outline of how to approach test-driven development in Python:

* Write a Test: Begin by writing a test that specifies the desired behavior of the code. Tests in Python are typically written as functions using an appropriate testing framework. Define test cases that cover different scenarios and expected outcomes.

* Run the Test: Execute the test(s) to verify that they fail. This step ensures that the tests are valid and accurately reflect the desired behavior.

* Write the Code: Implement the code necessary to pass the test. Start with the minimum amount of code needed to satisfy the test cases.

* Run the Test Again: Execute the tests to check if they pass. The goal is to have all the test cases pass without any failures.
	- The tests should now pass since the code has been implemented to fulfill the desired behavior.

* Refactor and Repeat: Refactor the code to improve its design, readability, and performance while ensuring that the tests continue to pass. The tests act as a safety net, providing confidence that the changes made during refactoring haven't introduced any regressions.

* Repeat the Cycle: Continue the cycle of writing tests, implementing code, running tests, and refactoring until the desired functionality is achieved, and the code is well-tested and maintainable.



# Types of Tests

## Functional Testing
- This is a type of black-box testing that is based on the specifications of the software that is to be tested. The application is tested by providing input and then the results are examined that need to conform to the functionality it was intended for. Functional testing of a software is conducted on a complete, integrated system to evaluate the system’s compliance with its specified requirements.

- There are five steps that are involved while testing an application for functionality:

* The determination of the functionality that the intended application is meant to perform.
* The creation of test data based on the specifications of the application.
* The output based on the test data and the specifications of the application.
* The writing of test scenarios and the execution of test cases.
* The comparison of actual and expected results based on the executed test cases.

- An effective testing practice will see the above steps applied to the testing policies of every organization and hence it will make sure that the organization maintains the strictest of standards when it comes to software quality.


## Unit Testing
- This type of testing is performed by developers before the setup is handed over to the testing team to formally execute the test cases. Unit testing is performed by the respective developers on the individual units of source code assigned areas. The developers use test data that is different from the test data of the quality assurance team.

- The goal of unit testing is to isolate each part of the program and show that individual parts are correct in terms of requirements and functionality.

- Limitations of Unit Testing:

* Testing cannot catch each and every bug in an application. It is impossible to evaluate every execution path in every software application. The same is the case with unit testing.
* There is a limit to the number of scenarios and test data that a developer can use to verify a source code. After having exhausted all the options, there is no choice but to stop unit testing and merge the code segment with other units.

## Integration Testing
- Integration testing is defined as the testing of combined parts of an application to determine if they function correctly. Integration testing can be done in two ways: Bottom-up integration testing and Top-down integration testing.
* Bottom-up integration: This testing begins with unit testing, followed by tests of progressively higher-level combinations of units called modules or builds.
* Top-down integration: In this testing, the highest-level modules are tested first and progressively, lower-level modules are tested thereafter.

- In a comprehensive software development environment, bottom-up testing is usually done first, followed by top-down testing. The process concludes with multiple tests of the complete application, preferably in scenarios designed to mimic actual situations.

## System Testing
- System testing tests the system as a whole. Once all the components are integrated, the application as a whole is tested rigorously to see that it meets the specified Quality Standards. This type of testing is performed by a specialized testing team.

- System testing is important because of the following reasons:

* System testing is the first step in the Software Development Life Cycle, where the application is tested as a whole.
* The application is tested thoroughly to verify that it meets the functional and technical specifications.
* The application is tested in an environment that is very close to the production environment where the application will be deployed.
* System testing enables us to test, verify, and validate both the business requirements as well as the application architecture.


## Regression Testing
- Whenever a change in a software application is made, it is quite possible that other areas within the application have been affected by this change. Regression testing is performed to verify that a fixed bug hasn’t resulted in another functionality or business rule violation. The intent of regression testing is to ensure that a change, such as a bug fix should not result in another fault being uncovered in the application.

- Regression testing is important because of the following reasons:

* Minimize the gaps in testing when an application with changes made has to be tested.
* Testing the new changes to verify that the changes made did not affect any other area of the application.
* Mitigates risks when regression testing is performed on the application.
* Test coverage is increased without compromising timelines.
* Increase speed to market the product.

## Acceptance Testing
- This is arguably the most important type of testing, as it is conducted by the Quality Assurance Team who will gauge whether the application meets the intended specifications and satisfies the client’s requirement. The QA team will have a set of pre-written scenarios and test cases that will be used to test the application.

- More ideas will be shared about the application and more tests can be performed on it to gauge its accuracy and the reasons why the project was initiated. Acceptance tests are not only intended to point out simple spelling mistakes, cosmetic errors, or interface gaps, but also to point out any bugs in the application that will result in system crashes or major errors in the application.

- By performing acceptance tests on an application, the testing team will deduce how the application will perform in production. There are also legal and contractual requirements for acceptance of the system.

## Alpha Testing
- This test is the first stage of testing and will be performed amongst the teams (developer and QA teams). Unit testing, integration testing and system testing when combined together is known as alpha testing. During this phase, the following aspects will be tested in the application:

* Spelling Mistakes
* Broken Links
* Cloudy Directions
* The Application will be tested on machines with the lowest specification to test loading times and any latency problems.

## Beta Testing
- This test is performed after alpha testing has been successfully performed. In beta testing, a sample of the intended audience tests the application. Beta testing is also known as pre-release testing. Beta test versions of software are ideally distributed to a wide audience on the Web, partly to give the program a “real-world” test and partly to provide a preview of the next release. In this phase, the audience will be testing the following:

* Users will install, run the application and send their feedback to the project team.
* Typographical errors, confusing application flow, and even crashes.
* Getting the feedback, the project team can fix the problems before releasing the software to the actual users.
* The more issues you fix that solve real user problems, the higher the quality of your application will be.
* Having a higher-quality application when you release it to the general public will increase customer satisfaction.


## Non-Functional Testing
- This section is based upon testing an application from its non-functional attributes. Non-functional testing involves testing a software from the requirements which are nonfunctional in nature but important such as performance, security, user interface, etc.

- Some of the important and commonly used non-functional testing types are discussed below.

## Performance Testing
- It is mostly used to identify any bottlenecks or performance issues rather than finding bugs in a software. There are different causes that contribute in lowering the performance of a software:

* Network delay
* Client-side processing
* Database transaction processing
* Load balancing between servers
* Data rendering
- Performance testing is considered as one of the important and mandatory testing type in terms of the following aspects:

* Speed (i.e. Response Time, data rendering and accessing)
* Capacity
* Stability
* Scalability
- Performance testing can be either qualitative or quantitative and can be divided into different sub-types such as Load testing and Stress testing.

## Load Testing
- It is a process of testing the behavior of a software by applying maximum load in terms of software accessing and manipulating large input data. It can be done at both normal and peak load conditions. This type of testing identifies the maximum capacity of software and its behavior at peak time.

- Most of the time, load testing is performed with the help of automated tools such as Load Runner, AppLoader, IBM Rational Performance Tester, Apache JMeter, Silk Performer, Visual Studio Load Test, etc.

- Virtual users (VUsers) are defined in the automated testing tool and the script is executed to verify the load testing for the software. The number of users can be increased or decreased concurrently or incrementally based upon the requirements.

## Stress Testing
- Stress testing includes testing the behavior of a software under abnormal conditions. For example, it may include taking away some resources or applying a load beyond the actual load limit.

- The aim of stress testing is to test the software by applying the load to the system and taking over the resources used by the software to identify the breaking point. This testing can be performed by testing different scenarios such as:

* Shutdown or restart of network ports randomly
* Turning the database on or off
* Running different processes that consume resources such as CPU, memory, server, etc.

## Usability Testing
- Usability testing is a black-box technique and is used to identify any error(s) and improvements in the software by observing the users through their usage and operation.

- According to Nielsen, usability can be defined in terms of five factors, i.e. efficiency of use, learn-ability, memory-ability, errors/safety, and satisfaction. According to him, the usability of a product will be good and the system is usable if it possesses the above factors.

- Nigel Bevan and Macleod considered that usability is the quality requirement that can be measured as the outcome of interactions with a computer system. This requirement can be fulfilled and the end-user will be satisfied if the intended goals are achieved effectively with the use of proper resources.

- Molich in 2000 stated that a user-friendly system should fulfill the following five goals, i.e., easy to Learn, easy to remember, efficient to use, satisfactory to use, and easy to understand.

- In addition to the different definitions of usability, there are some standards and quality models and methods that define usability in the form of attributes and sub-attributes such as ISO-9126, ISO-9241-11, ISO-13407, and IEEE std.610.12, etc.


## UI vs Usability Testing
- UI testing involves testing the Graphical User Interface of the Software. UI testing ensures that the GUI functions according to the requirements and tested in terms of color, alignment, size, and other properties.

- On the other hand, usability testing ensures a good and user-friendly GUI that can be easily handled. UI testing can be considered as a sub-part of usability testing.

## Security Testing
- Security testing involves testing a software in order to identify any flaws and gaps from security and vulnerability point of view. Listed below are the main aspects that security testing should ensure:

* Confidentiality
* Integrity
* Authentication
* Availability
* Authorization
* Non-repudiation
* Software is secure against known and unknown vulnerabilities
* Software data is secure
* Software is according to all security regulations
* Input checking and validation
* SQL insertion attacks
* Injection flaws
* Session management issues
* Cross-site scripting attacks
* Buffer overflows vulnerabilities
* Directory traversal attacks


## Portability Testing
- Portability testing includes testing a software with the aim to ensure its reusability and that it can be moved from another software as well. Following are the strategies that can be used for portability testing:

* Transferring an installed software from one computer to another.
* Building executable (.exe) to run the software on different platforms.
- Portability testing can be considered as one of the sub-parts of system testing, as this testing type includes overall testing of a software with respect to its usage over different environments. Computer hardware, operating systems, and browsers are the major focus of portability testing. Some of the pre-conditions for portability testing are as follows:

* Software should be designed and coded, keeping in mind the portability requirements.
* Unit testing has been performed on the associated components.
* Integration testing has been performed.
* Test environment has been established.

## Test Plan
- A test plan outlines the strategy that will be used to test an application, the resources that will be used, the test environment in which testing will be performed, and the limitations of the testing and the schedule of testing activities. Typically the Quality Assurance Team Lead will be responsible for writing a Test Plan.

- A test plan includes the following:

* Introduction to the Test Plan document
* Assumptions while testing the application
* List of test cases included in testing the application
* List of features to be tested
* What sort of approach to use while testing the software
* List of deliverables that need to be tested
* The resources allocated for testing the application
* Any risks involved during the testing process
* A schedule of tasks and milestones to be achieved

## Test Scenario
- It is a one line statement that notifies what area in the application will be tested. Test scenarios are used to ensure that all process flows are tested from end to end. A particular area of an application can have as little as one test scenario to a few hundred scenarios depending on the magnitude and complexity of the application.

- The terms ‘test scenario’ and ‘test cases’ are used interchangeably, however a test scenario has several steps, whereas a test case has a single step. Viewed from this perspective, test scenarios are test cases, but they include several test cases and the sequence that they should be executed. Apart from this, each test is dependent on the output from the previous test.

## Test Case
- Test cases involve a set of steps, conditions, and inputs that can be used while performing testing tasks. The main intent of this activity is to ensure whether a software passes or fails in terms of its functionality and other aspects. There are many types of test cases such as functional, negative, error, logical test cases, physical test cases, UI test cases, etc.

- Furthermore, test cases are written to keep track of the testing coverage of a software. Generally, there are no formal templates that can be used during test case writing. However, the following components are always available and included in every test case:

* Test case ID
* Product module
* Product version
* Revision history
* Purpose
* Assumptions
* Pre-conditions
* Steps
* Expected outcome
* Actual outcome
* Post-conditions
- Many test cases can be derived from a single test scenario. In addition, sometimes multiple test cases are written for a single software which are collectively known as test suites.


