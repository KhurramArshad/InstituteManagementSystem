from accounts.models import Profile
from datetime import datetime
#import pyttsx3
class Custom:
    def __init__(self, user_id):
        self.user_id = user_id

    def status_confirm(self):
        profile = Profile.objects.get(user=self.user_id)
        if profile.status == 'activated':
            return True
        else:
            return False

    def welcomeMsg(self):
        engine = pyttsx3.init()
        """VOICE"""
        voices = engine.getProperty('voices')  # getting details of current voice
        # engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
        engine.setProperty('voice', voices[1].id)  # changing index, changes voices. 1 for female
        """VOLUME"""
        volume = engine.getProperty('volume')  # getting to know current volume level (min=0 and max=1)
        # print(volume)  # printing current volume level
        engine.setProperty('volume', 1.0)  # setting up volume level  between 0 and 1
        """ RATE"""
        rate = engine.getProperty('rate')  # getting details of current speaking rate
        # print(rate)  # printing current voice rate
        engine.setProperty('rate', 160)  # setting up new voice rate

        engine.say("Welcome back have a nice day")
        engine.runAndWait()

    def compare_date(self):
        profile = Profile.objects.get(user=self.user_id)
        if str(datetime.today().strftime('%Y-%m-%d')) <= str(profile.endDate):
            return True
        else:
            profile.status = 'deactivated'
            profile.save()
            return False


class CalculatePayableReceivable:
    def __init__(self, payable_list, received_list):
        self.list_1 = payable_list
        self.list_2 = received_list
        
    def my_sum(self):
        total_payable = sum(self.list_1)
        total_received = sum(self.list_2)
        balance = total_payable - total_received
        return total_payable, total_received, balance


