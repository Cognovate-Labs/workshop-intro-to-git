"""
Module Name: hello_world.py
Description: Tests for Hello World
Author: Nick Munoz
Created: 12/5/24
"""

import pytest
import json
import os
from hello_world import load_json_data, greet_users

# helper function
def student_info_valid(invalid_students,students,field):
    status = True
    # iterate over students indexes
    for student_ind in range(len(students)):
        # if valid student name
        if invalid_students[student_ind]['name'] != students[student_ind]['name']:
            # check if github username was entered
            if invalid_students[student_ind][field] == students[student_ind][field]:
                status = False
    
    return status


@pytest.fixture
def JSON_FILEPATH():
    return 'students.json'


@pytest.fixture
def invalid_json_data(JSON_FILEPATH):
    """Fixture for invalid JSON data."""
    # initial json file that was given to students
    return {
        "workshop"         : 1,
        "students": [
            {
            "name" : "Partner 1",
            "github_username" : "",
            "email" : "",
            "os"    : "Windows | MAC | Linux",
            "total_effort_hours" : 0
            },
            {
            "name" : "Partner 2",
            "github_username" : "",
            "email" : "",
            "os"    : "Windows | MAC | Linux",
            "total_effort_hours" : 0
            },
            {
            "name" : "Partner 3",
            "github_username" : "",
            "email" : "",
            "os"    : "Windows | MAC | Linux",
            "total_effort_hours" : 0
            }
        ]
    }


@pytest.fixture
def submitted_json_data(JSON_FILEPATH):
    # check if file path exists
    assert os.path.exists(JSON_FILEPATH), f"Error: {JSON_FILEPATH} does not exist."

    json_data = None

    # try reading json data
    try:
        with open(JSON_FILEPATH, "r") as file:
            json_data = json.load(file)
        assert isinstance(json_data, dict), "Error: JSON data is not a dictionary."
    except json.JSONDecodeError as e:
        pytest.fail(f"Error: {JSON_FILEPATH} contains invalid JSON.")
    
    return json_data


def test_json_file_exists(JSON_FILEPATH):
    # check if file path exists
    assert os.path.exists(JSON_FILEPATH), f"Error: {JSON_FILEPATH} does not exist."


def test_json_file_is_valid(JSON_FILEPATH):
    # check if file path exists
    assert os.path.exists(JSON_FILEPATH), f"Error: {JSON_FILEPATH} does not exist."

    json_data = None

    # try reading json data
    try:
        with open(JSON_FILEPATH, "r") as file:
            json_data = json.load(file)
        assert isinstance(json_data, dict), "Error: JSON data is not a dictionary."
    except json.JSONDecodeError as e:
        pytest.fail(f"Error: {JSON_FILEPATH} contains invalid JSON.")


def test_correct_workshop(invalid_json_data, submitted_json_data):
    assert invalid_json_data['workshop'] == submitted_json_data['workshop'], "Error: Wrong workshop value in JSON"


def test_students_names_are_entered(invalid_json_data, submitted_json_data):
    invalid_students = invalid_json_data['students']
    students = submitted_json_data['students']

    # at least one students valid name was entered
    assert invalid_students[0]['name'] != students[0]['name'], "Error: Student 1 name hasn't been entered"


def test_students_have_github_usernames(invalid_json_data, submitted_json_data):
    invalid_students = invalid_json_data['students']
    students = submitted_json_data['students']

    # at least one students valid name was entered
    assert invalid_students[0]['name'] != students[0]['name'], "Error: Student 1 name hasn't been entered"

    # check if github usernames are added
    assert True == student_info_valid(invalid_students,students,'github_username'), "Error: Student github username wasn't listed"


def test_students_have_emails(invalid_json_data, submitted_json_data):
    invalid_students = invalid_json_data['students']
    students = submitted_json_data['students']

    # at least one students valid name was entered
    assert invalid_students[0]['name'] != students[0]['name'], "Error: Student 1 name hasn't been entered"

    # check if emails are added
    assert True == student_info_valid(invalid_students,students,'email'), "Error: Student email wasn't listed"


def test_students_have_os(invalid_json_data, submitted_json_data):
    invalid_students = invalid_json_data['students']
    students = submitted_json_data['students']

    # at least one students valid name was entered
    assert invalid_students[0]['name'] != students[0]['name'], "Error: Student 1 name hasn't been entered"

    # check if OS are added
    assert True == student_info_valid(invalid_students,students,'os'), "Error: Student OS wasn't listed"


def test_students_have_total_effort_hours(invalid_json_data, submitted_json_data):
    invalid_students = invalid_json_data['students']
    students = submitted_json_data['students']

    # at least one students valid name was entered
    assert invalid_students[0]['name'] != students[0]['name'], "Error: Student 1 name hasn't been entered"

    # check if total effort hours was added
    assert True == student_info_valid(invalid_students,students,'total_effort_hours'), "Error: Student total effort hours wasn't listed"