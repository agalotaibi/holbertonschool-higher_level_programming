import os

def generate_invitations(template, attendees):

    if not isinstance(template, str):
        print("Error: Template must be a string")
        return
    if not isinstance(attendees, list):
        print("Attendees must be a list")
        return
    if not template:
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return
    if not all(isinstance(item, dict) for item in attendees):
        print("Attendees must be a list of dictionaries")
        return


    for index, attendee in enumerate(attendees, start=1):

        invitation_text = template


        placeholders = ["name", "event_title", "event_date", "event_location"]

        for key in placeholders:

            value = attendee.get(key)

            value_str = str(value) if value is not None else "N/A"


            invitation_text = invitation_text.replace("{" + key + "}", value_str)


        output_filename = f"output_{index}.txt"

        try:
            with open(output_filename, "w") as output_file:
                output_file.write(invitation_text)
        except Exception as e:
            print(f"Error writing file {output_filename}: {e}")
