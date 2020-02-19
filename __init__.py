from mycroft import MycroftSkill, intent_file_handler


class Makertest(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('makertest.intent')
    def handle_makertest(self, message):
        self.speak_dialog('makertest')


def create_skill():
    return Makertest()

