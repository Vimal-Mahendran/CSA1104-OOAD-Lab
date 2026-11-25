class Conference:
    def __init__(self, title, date):
        self.title = title
        self.date = date
        self.sessions = []

    def add_session(self, session):
        self.sessions.append(session)


class Organizer:
    def __init__(self, organizer_id, name):
        self.organizer_id = organizer_id
        self.name = name

    def arrange_program(self, conference, program_details):
        print(f"Organizer {self.name} is arranging program for {conference.title}")


class CentralManagementSystem:
    def __init__(self, system_id):
        self.system_id = system_id
        self.members = []

    def register_member(self, member, role):
        self.members.append({"member": member, "role": role})
        print(f"Registered {member.name} with role: {role}")


class Participant:
    def __init__(self, participant_id, name, role):
        self.participant_id = participant_id
        self.name = name
        self.role = role

    def submit_presentation(self, presentation_title):
        print(f"{self.name} submitted presentation: {presentation_title}")


class Presentation:
    def __init__(self, presentation_id, title, presenter):
        self.presentation_id = presentation_id
        self.title = title
        self.presenter = presenter