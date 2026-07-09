class ResponseGenerator:

    @staticmethod
    def success(message):

        return f"AXEL: {message}"

    @staticmethod
    def error(message):

        return f"AXEL: {message}"

    @staticmethod
    def unknown():

        return "AXEL: Sorry, I didn't understand that."
