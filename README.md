#This repo is to explore using Unittest and Pytest.
# TDD and Unit Testing 
## Unittest and Pytest 

### TDD
What is it ?

How do you implement it ?

### Unit Testing 
what is it ? what are the benefits?

- Test Driven Development 
- Maintainable 
- Reduces Technical Debt 
- Know when you are done
- You have a sense of direction 

### Tools/ Frameworks for Python 

#### Unit Test
- Unittest comes with python (standard)

#### Pytests
- Pytests needs to be installed as a package, however it is pretty and clean and tests the same as unittest



## Specification for Airport
Use TDD to write some tests, then code the airport interface.

This file has the specification for the airport.
### Passengers
- as a user I can create a Passanger
- It can be created with name and passport number
- I can create 'Joana Thomson' with the Passport number 'B343123'
- I can create 'Birt Kuman' with the Passport number 'B13927'
- If I try to create a user with out a name or a passport number I get an error

### Plane
- As a User I can create a Plane with a plane number

### Flight_trip
- As a user I can create a flight with no specific information
- as a user I can add a plane
- as a User I can add a destination
- As a user I can add a origin
- As a user I can add a Passanger to the list of passangers
- Passanger list is a list of objct that are Passanger