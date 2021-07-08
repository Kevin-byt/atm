# atm

Run atm.py

This program simulates the functioning of an ATM machine

When the program starts, it gives the user 2 options:
1. Running as an admin
2. Running as an account holder (user)

1. Admin
- The user needs to login to the admin console through a password (Default password is 1234)
- The admin menu gives the user the following capabilities:
	1. Creating an account
	2. Deleting an account
	3. Viewing the accounts in the system
	4. Adding a user automatically (The user is already predefined). 
	
2. Account Holder (User)
- This logs in to a specific account
- It allows the user to do the following:
	1. Deposit funds into his accounts (Both USD and KES)
	2. Withdraw funds from his accounts (only if the balance is more than the withdrawal amount)
	3. Check his balances (Both USD and KES)
	4. Can change password
- The user's activities update the account balances based on the nature of the transaction