"""
File: sql_attacks.py
Authors: CSE453 Group 4
Purpose: To demonstrate the ability to harden code against attacks.
"""

# Write a function to accept two strings (username and a password) and return 
# a single string (SQL)
def login(username, password):
    pass


# Generate a set of cases (one for each member of your team) that represent 
# valid input where the username and the password consist of letters, numbers, 
# and underscores.
def sql_tests():
    pass


# Create a function that feeds these test cases through the query function 
# and displays the resulting query
def test_sql_login(sql_test):
    pass


# Generate test cases (again, each team member should generate one test case) 
# that demonstrate a tautology attack
def tautology_tests():
    pass


# Create a function that feeds these tautology test cases through the query 
# function and displays the output.
def test_tautology(tautology_test):
    pass


# Generate test cases (again, each team member should generate one test case) 
# that demonstrate a union query attack
def union_tests():
    pass 


# Create a function that feeds these union query test cases through the query 
# function and displays the output 
def test_union(union_test):
    pass


# Generate test cases (again, each team member should generate one test case) 
# that demonstrate an additional statement attack
def additional_statement_tests():
    pass 


# Create a function that feeds these additional statement query test cases 
# through the additional statement function and displays the output 
def test_additional_statement(additional_statement_test):
    pass


# Generate test cases (again, each team member should generate one test case) 
# that demonstrate a comment attack
def comment_tests():
    pass 


# Create a function that feeds these comment test cases through the query 
# function and displays the output 
def test_comments(comment_test):
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