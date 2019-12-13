import requests
from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler



class NavigateSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        super().__init__()
        self.learning = True

    def initialize(self):
        self.register_intent_file('navigate.from.intent', self.handle_navigate_from)
        #self.register_intent_file('do.you.like.intent', self.handle_do_you_like)
        my_setting = self.settings.get('my_setting')
    def handle_navigate_from(self, message):
        
        
        
        place1=message.data.get('place1')
        place2=message.data.get('place2')
        url='https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins='+place1+'&destinations='+place2+'&key=AIzaSyBpfgcCEAI_cnJB2yAtT7xw2m2Ci-e6vc0'

        r = requests.get(url)
        
        json_output = r.json()
        #print(json_output)
        
        output=json_output['rows']
        
        elements = output['elements']
        distance = elements['distance']
        duration = elements['duration']
        
        di=distance[0]['text']
        du=duration[0]['text']
        
        self.log.info("There are five types of log messages: "
                      "info, debug, warning, error, and exception.")
        self.speak_dialog("navigation.to",{"distance":di})
        self.speak_dialog("time",{"duration":du})
        
    def stop(self):
        pass
    
def create_skill():
    return NavigateSkill()
