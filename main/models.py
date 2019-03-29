from django.db import models
from Account.models import Account
from LoginHelper import LoginHelper
from CreateAccountHelper import CreateAccountHelper
# Create your models here.
class UI:
    """
    Here is where the string input from the command line is parsed. I currently have it set up so its
    checking the string in lower so that the commands wont be case sensitive. If you wish to add an additional
    command just add another "elif command[0].lower() == <commandName>" at the bottom. Make sure command
    returns a string.
    """

    def command(self, inStr):
        command = inStr.split(' ')

        if command[0].lower() == "login":
            login = LoginHelper()

            return login.login(command)

        elif command[0].lower() == "logout":

            logout = LoginHelper()
            return logout.logout()

        elif command[0].lower() == "createaccount":

            CA = CreateAccountHelper()
            return CA.createAccount(command)

        elif command[0].lower() == "createlab":
            """
            The code for creating a lab should go here. 
            """
            return command[0]
        elif command[0].lower() == "createcourse":
            """
            """
            return command[0]

        else:
            return command[0] + " is an unsupported command"

        return inStr


#class createCourse(models.model):
#    name = models.CharField(max_length=30)
#    number = models.CharField(max_length=3)
#    days = models.CharField(max_length=4)
#    start = models.CharField(max_length=4)
#    end = models.CharField(max_length=4)


