"""
Module Name: hello_world.py
Description: Hello World for Python
Author: Nick Munoz
Created: 12/5/24
"""

import json
import sys
import os

def load_json_data(file_path="students.json"):
    """
    Read json file and retrieve json data

    Args: 
    filename (str): Path to the json file

    Returns:
    json_data (dict): Dictionary that contains json data
    """
    json_data = None

    # check if file path exists
    if not os.path.exists(file_path):
        print(f"Error: {filepath} does not exist.")
        raise FileNotFoundError
        sys.exit(1)
    
    # try to read file
    try:
        with open(file_path, "r") as file:
            # save data from file
            json_data = json.load(file)
    except json.JSONDecodeError as e:
        print(f"Error: {filepath} contains invalid JSON.")
        raise e
        sys.exit(1)
    
    return json_data


def greet_users(json_data):
    """
    Print a greeting message to the student(s)

    Args:
    json_data (dict): Dictionary that contains json data         
    """
    # get list of students from json data
    student_list = json_data['students']

    # message that will be printed to console
    out_message = f"Hello, {student_list[0]['name']}"

    # number of students
    num_students = len(student_list)

    # iterate over the indexes for student_list up to second to last one
    for ind in range(1,num_students - 1):
        # take original string and concatenate student name
        if 'Partner' not in student_list[ind]['name']:
            out_message = out_message + ', ' + student_list[ind]['name']

    # add last student name
    if 'Partner' not in student_list[-1]['name']:
        out_message = out_message + ', and ' + student_list[-1]['name'] + '!\n'
    else:
        out_message = out_message + '!\n'

    # show greeting message
    print(out_message)
    print("Welcome to Python!")


def main():
    # read json data file
    student_data = load_json_data()
    # greet user(s)
    greet_users(student_data)


if __name__ == "__main__":
    main()