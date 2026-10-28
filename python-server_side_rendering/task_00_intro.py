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

    for number, attendee in enumerate(attendees, 1):
        invitation = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            invitation = invitation.replace("{" + key + "}", value)

        filename = "output_" + str(number) + ".txt"
        with open(filename, "w") as file:
            file.write(invitation)
