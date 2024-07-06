# Outlook-Email-Collector

This script assists you in exporting all email addresses with which you have communicated.

## Prerequisites
- All emails must be downloaded and ready for offline access. If you have default settings like availability for the last year, then you can only export the last year. Ensure you have downloaded all emails from the exchange before you proceed.

## Steps
1. Extract your inbox as a CSV file (you can change the mapping and export only from, to, cc, bcc fields).
2. Save your inbox as `1.csv` and outbox as `2.csv`.
   - The script is currently defined for 2 files, but you can repeat the process if you have more folders.
3. Run the script using the command `python3 ./outlook.py`. It will scan the entire file and provide you with a list of emails.

Congratulations, you have successfully exported all emails that you have sent or received.

Good Luck, Have Fun! 
