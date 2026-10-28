#!/usr/bin/python3

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: template is not a string")
        return

    if not isinstance(attendees, list):
        print("Error: attendees is not a list")
        return

    for attendee in attendees:
        if not isinstance(attendee, dict):
            print("Error: attendee is not a dict")
            return

    if template == "":
        print("Template is empty, no output files generated.")
        return
    if attendees == []:
        print("No data provided, no output files generated.")
        return
