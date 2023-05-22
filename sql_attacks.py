"""
File: sql_attacks.py
Authors: CSE453 Group 4
Purpose: To demonstrate the ability to harden code against attacks.
"""

# Write a function to accept two strings (username and a password) and return 
# a single string (SQL)
def query(username, password):
    pass


# Generate a set of cases (one for each member of your team) that represent 
# valid input where the username and the password consist of letters, numbers, 
# and underscores. This function will return member valid test cases.
def valid_tests():
    pass


# Create a function that feeds these test cases through the query function 
# and displays the resulting query
def valid_tests(valid_tests):

    # loop through valid test cases, print output
    pass


# Generate test cases (again, each team member should generate one test case) 
# that demonstrate a tautology attack. This function will return member valid 
# test cases.
def tautology_tests():
    pass


# Create a function that feeds these tautology test cases through the query 
# function and displays the output.
def test_tautology(tautology_tests):

    # loop through tautology test cases, print output
    pass


# Generate test cases (again, each team member should generate one test case) 
# that demonstrate a union query attack. This function will return member union 
# attack test cases.
def union_tests():
    pass 


# Create a function that feeds these union query test cases through the query 
# function and displays the output 
def test_union(union_tests):

    # loop through union test cases, print output
    pass


# Generate test cases (again, each team member should generate one test case) 
# that demonstrate an additional statement attack. This function will return 
# member additional statement attack test cases.
def additional_statement_tests():
    pass 


# Create a function that feeds these additional statement query test cases 
# through the additional statement function and displays the output 
def test_additional_statement(additional_statement_test):

    # loop through additional statement test cases, print output
    pass


# Generate test cases (again, each team member should generate one test case) 
# that demonstrate a comment attack. This function will return member comment
# attack test cases.
def comment_tests():
    pass 


# Create a function that feeds these comment test cases through the query 
# function and displays the output 
def test_comments(comment_test):

    # loop through comment test cases, print output
    pass


# Create a function to provide a weak mitigation against all four attacks. 
# This function accepts the input as a parameter (or two!) and returns the 
# sanitized input.
def weak_mitigation(username, password):
    pass


# Create a function to provide a strong mitigation against all command 
# injection attacks. This function accepts the input as a parameter (or two!) 
# and returns the sanitized input.
def strong_mitigation(username, password):
    pass


# main function
def main():
    pass


# if run directly, run main function
if __name__ == "__main__":
    main()