
## https://codechalleng.es/bites/89/

us_state_abbrev = {'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ',
                   'Arkansas': 'AR', 'California': 'CA', 'Colorado': 'CO',
                   'Connecticut': 'CT', 'Delaware': 'DE', 'Florida': 'FL',
                   'Georgia': 'GA', 'Hawaii': 'HI', 'Idaho': 'ID',
                   'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA',
                   'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA',
                   'Maine': 'ME', 'Maryland': 'MD', 'Massachusetts': 'MA',
                   'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS',
                   'Missouri': 'MO', 'Montana': 'MT', 'Nebraska': 'NE',
                   'Nevada': 'NV', 'New Hampshire': 'NH', 'New Jersey': 'NJ',
                   'New Mexico': 'NM', 'New York': 'NY',
                   'North Carolina': 'NC', 'North Dakota': 'ND',
                   'Ohio': 'OH', 'Oklahoma': 'OK', 'Oregon': 'OR',
                   'Pennsylvania': 'PA', 'Rhode Island': 'RI',
                   'South Carolina': 'SC', 'South Dakota': 'SD',
                   'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT',
                   'Vermont': 'VT', 'Virginia': 'VA', 'Washington': 'WA',
                   'West Virginia': 'WV', 'Wisconsin': 'WI', 'Wyoming': 'WY'}

states = ['Oklahoma', 'Kansas', 'North Carolina', 'Georgia', 'Oregon',
          'Mississippi', 'Minnesota', 'Colorado', 'Alabama',
          'Massachusetts', 'Arizona', 'Connecticut', 'Montana',
          'West Virginia', 'Nebraska', 'New York', 'Nevada', 'Idaho',
          'New Jersey', 'Missouri', 'South Carolina', 'Pennsylvania',
          'Rhode Island', 'New Mexico', 'Alaska', 'New Hampshire',
          'Tennessee', 'Washington', 'Indiana', 'Hawaii', 'Kentucky',
          'Virginia', 'Ohio', 'Wisconsin', 'Maryland', 'Florida',
          'Utah', 'Maine', 'California', 'Vermont', 'Arkansas', 'Wyoming',
          'Louisiana', 'North Dakota', 'South Dakota', 'Texas',
          'Illinois', 'Iowa', 'Michigan', 'Delaware']

NOT_FOUND = 'N/A'


def get_every_nth_state(n=10):
    """Return a list with every nth item (default 10th item)
       of states (takeaway: lists keep order)"""
    nth_list = []
    for count, state in enumerate(states, 1):
        if count % n == 0:
            nth_list.append(state)
            print(state)
    return nth_list
    pass


def get_state_abbrev(abbrev):
    """Look up a state abbreviation by full name in
       us_state_abbrev, if not found return NOT_FOUND
       (takeaway: dicts are great for lookups)"""
    match = None
    for k, v in us_state_abbrev.items():
        if k == abbrev:
            match = True
            print(v)
            return v
    if match == None:
        print(NOT_FOUND)
        return NOT_FOUND
    pass


def get_longest_state(data):
    """Takes dict or list and determines the longest state name
       (takeaways: use a dict method to get all keys, use sorted)"""
    for k in sorted(data, key=len, reverse=True):
        print(k)
        return k
    pass


def combine_state_names_and_abbreviations():
    """Return a new list with the first 10 abbreviations from the
       us_state_abbrev dict ordered values and the last 10 states from
       the states list (takeaways: use another dict method to get all
       values and use sorted, list slicing and list concatenation)"""
    new_lst = []
    for v in sorted(us_state_abbrev.values()):
        new_lst.append(v)
    new_lst = new_lst[:10]
    ord_state = sorted(states)
    for state in sorted(ord_state[-10:]):
        new_lst.append(state)
    print(new_lst)
    return new_lst
    pass


get_every_nth_state()
get_state_abbrev("Calrnia")
get_longest_state(states)
combine_state_names_and_abbreviations()

