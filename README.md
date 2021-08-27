# gitlab-autoadd

This is a script I wrote up in order to add large groups of people to groups on Gitlab since Gitlab doesn't currently supportmass user imports.

## Usage

The script should be run as follows:

`python3 main.py <accounts.csv>`

The `accounts.csv` file should contain one email address per line. Upon running the program, you will be asked for four inputs:

1. Enter the Gitlab URL - This defaults to https://gitlab.com, however users can change it to their organization's Gitlab
2. Enter the Gitlab Group - You can find this by browsing to your group's home page on Gitlab and looking at whatever comes after the final slash in the address bar
3. Enter Gitlab Access Level - This defines what permissions your users will have within the group. See https://docs.gitlab.com/ee/api/invitations.html#valid-access-levels for the different access levels. Note: please enter the number rather than the name. For example, if you wanted to give everyone Developer access, then you would enter `20`
4. Enter your Private Access Token - To generate one of these, go to Profile->Edit Profile->Access Tokens. Gitlab will instruct you on how to create this. Note, you need to ensure that `api` is selected as one of the available scopes. DO NOT SHARE THIS TOKEN WITH ANYONE.

The script will then loop through every email in the file and print SUCCESS if an invite could be sent, or FAIL if the user is already in the group or if you do not have access to make these changes.