import argparse
import mysql 

if __name__ == '__main__':

	"""
		--type=user --name=eduffield --address1= --address2= etc
	"""

    parser = argparse.ArgumentParser()
    
    #voting
    parser.add_argument('-v', '--vote-times')
    parser.add_argument('-w', '--vote-type')
    parser.add_argument('-o', '--vote-outcome')

    #governance objects
    parser.add_argument('-t', '--type')
    parser.add_argument('-c', '--create')
    parser.add_argument('-d', '--amend')
    parser.add_argument('-r', '--revision')
    parser.add_argument('-u', '--url')
    parser.add_argument('-n', '--name')

    #governance objects (users, groups, companies)
    parser.add_argument('-f', '--first_name')
    parser.add_argument('-l', '--last_name')
    parser.add_argument('-a', '--address1')
    parser.add_argument('-b', '--address2')
    parser.add_argument('-c', '--city')
    parser.add_argument('-s', '--state')
    parser.add_argument('-e', '--country')

    #governance objects (proposals, contracts)
    parser.add_argument('-p', '--priority')
    parser.add_argument('-m', '--months')

    #ownership
    parser.add_argument('-u', '--user_owner_id')
    parser.add_argument('-x', '--user_from_id')
    parser.add_argument('-y', '--user_to_id')
    parser.add_argument('-g', '--group_id')
    parser.add_argument('-c', '--company_id')

    parser.add_argument('-v', dest='verbose', action='store_true')
    args = parser.parse_args()
    # ... do something with args.output ...
    # ... do something with args.verbose ..

