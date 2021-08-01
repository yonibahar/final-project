"""We have an existing dictionary that maps US states to their capitals.
1. Print the state capital of Idaho
2. Print all states.
3. Print all capitals.
4. Create a single string 'Alabama -> Montgomery, Alaska -> Juneau, ...'
5. Ensure the string you created in 4. is alphabetically sorted by state
7. Now we want to add the reverse look up, given the name of a capital what state
is it in?
Implement the function def get_state(capital): below so it returns the state.
GOTCHAS: What happens if two states have the same capital name, how do you
handle that?

"""
import sys

import pytest

STATES_CAPITALS = {
    'Alabama' : 'Montgomery',
    'Alaska' : 'Juneau',
    'Arizona' : 'Phoenix',
    'Arkansas': 'Little Rock',
    'California' : 'Sacramento',
    'Colorado' : 'Denver',
    'Connecticut' : 'Hartford',
    'Delaware' : 'Dover',
    'Florida' : 'Tallahassee',
    'Georgia' : 'Atlanta',
    'Hawaii' : 'Honolulu',
    'Idaho' : 'Boise',
    'Illinois' : 'Springfield',
    'Indiana' : 'Indianapolis',
    'Iowa' : 'Des Moines',
    'Kansas' : 'Topeka',
    'Kentucky' : 'Frankfort',
    'Louisiana' : 'Baton Rouge',
    'Maine' : 'Augusta',
    'Maryland' : 'Annapolis',
    'Massachusetts' : 'Boston',
    'Michigan' : 'Lansing',
    'Minnesota' : 'Saint Paul',
    'Mississippi' : 'Jackson',
    'Missouri' : 'Jefferson City',
    'Montana' : 'Helena',
    'Nebraska' : 'Lincoln',
    'Nevada' : 'Carson City',
    'New Hampshire' : 'Concord',
    'New Jersey' : 'Trenton',
    'New Mexico' : 'Santa Fe',
    'New York' : 'Albany',
    'North Carolina' : 'Raleigh',
    'North Dakota' : 'Bismarck',
    'Ohio' : 'Columbus',
    'Oklahoma' : 'Oklahoma City',
    'Oregon' : 'Salem',
    'Pennsylvania' : 'Harrisburg',
    'Rhode Island' : 'Providence',
    'South Carolina' : 'Columbia',
    'South Dakota' : 'Pierre',
    'Tennessee' : 'Nashville',
    'Texas' : 'Austin',
    'Utah' : 'Salt Lake City',
    'Vermont' : 'Montpelier',
    'Virginia' : 'Richmond',
    'Washington' : 'Olympia',
    'West Virginia' : 'Charleston',
    'Wisconsin' : 'Madison',
    'Wyoming' : 'Cheyenne',
}


def capital_of_Idaho():
    # Your code here
    return STATES_CAPITALS['Idaho']
print(capital_of_Idaho())

def all_states():
    # Your code here
   return STATES_CAPITALS.keys()
print(all_states())

def all_capitals():
    # Your code here
    return STATES_CAPITALS.values()
print(all_capitals())

def states_capitals_string():
    # Your code here
    single_string = ""
    for key,value in STATES_CAPITALS.items():
        single_string += key + " -> " + value + ", "
    return single_string[:-2]
print(states_capitals_string())

def test_sorted(single_string):
    dict1 = {}
    for state_pair in single_string.split(", "):
        members = state_pair.split(" -> ")
        dict1.update({members[0] : members[1]})
    states = list(dict1.keys())
    for index in range(len(states) -1 ):
        if states[index] < states[index + 1]:
            continue
        else:
            print("string is not sorted alfabeteclly")
            return
    print("string is sorted")

test_sorted(states_capitals_string())

def get_state(capital):
    states = []
    for key, value in STATES_CAPITALS.items():
        if capital == value:
            states.append(key)
    if len(states) == 0:
        return "not found"
    return states
print(get_state('Madison'))





def test_state_to_capital():
    assert 'Cheyenne' == STATES_CAPITALS['Wyoming']


def test_state_to_capital_unknown():
    with pytest.raises(KeyError):
        STATES_CAPITALS['']


def test_capital_to_state():
    assert 'Wyoming' == get_state('Cheyenne')


def test_capital_to_state_unknown():
    with pytest.raises(KeyError):
        get_state('')


# def main():
#     return pytest.main(__file__)


# if __name__ == '__main__':
#     sys.exit(main())
