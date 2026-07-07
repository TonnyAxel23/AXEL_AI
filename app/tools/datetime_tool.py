from datetime import datetime


class DateTimeTool:

    @staticmethod
    def current_time():

        return datetime.now().strftime("%I:%M %p")


    @staticmethod
    def current_date():

        return datetime.now().strftime("%d %B %Y")