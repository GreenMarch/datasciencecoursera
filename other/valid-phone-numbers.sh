# Read from the file file.txt and output all valid phone numbers to stdout.
# Using grep:
# Runtime: 4 ms, faster than 55.93% of Bash online submissions for Valid Phone Numbers.
# Memory Usage: 3.1 MB, less than 57.14% of Bash online submissions for Valid Phone Numbers.
# grep -P '^(\d{3}-|\(\d{3}\) )\d{3}-\d{4}$' file.txt

# Using sed:
# Runtime: 0 ms, faster than 100.00% of Bash online submissions for Valid Phone Numbers.
# Memory Usage: 3.1 MB, less than 96.43% of Bash online submissions for Valid Phone Numbers.
# sed -n -r '/^([0-9]{3}-|\([0-9]{3}\) )[0-9]{3}-[0-9]{4}$/p' file.txt

# Using awk:
# Runtime: 0 ms, faster than 100.00% of Bash online submissions for Valid Phone Numbers.
# Memory Usage: 3.4 MB, less than 7.14% of Bash online submissions for Valid Phone Numbers.
# awk '/^([0-9]{3}-|\([0-9]{3}\) )[0-9]{3}-[0-9]{4}$/' file.txt

"""
193. Valid Phone Numbers
Easy

115

300

Favorite

Share
Given a text file file.txt that contains list of phone numbers (one per line), write a one liner bash script to print all valid phone numbers.

You may assume that a valid phone number must appear in one of the following two formats: (xxx) xxx-xxxx or xxx-xxx-xxxx. (x means a digit)

You may also assume each line in the text file must not contain leading or trailing white spaces.

Example:

Assume that file.txt has the following content:

987-123-4567
123 456 7890
(123) 456-7890
Your script should output the following valid phone numbers:

987-123-4567
(123) 456-7890
"""
