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
        self.register_entity_file('place1.entity')
        self.register_entity_file('place2.entity')
        
        my_setting = self.settings.get('my_setting')
    def handle_navigate_from(self, message):
        
        
        
        place1=message.data["place1"]
        place2=message.data["place2"]
        """
        url='https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins='+place1+'&destinations='+place2+'&key=AIzaSyBpfgcCEAI_cnJB2yAtT7xw2m2Ci-e6vc0'
        print(url)
        r = requests.get(url)
        
        json_output = r.json()
        #print(json_output)
        
        output=json_output['rows']
        
        elements = output[0]['elements']
        distance = elements[0]['distance']
        duration = elements[0]['duration']
        
        di=distance['text']
        du=duration['text']
        
        
        self.speak_dialog("navigation.to",{"distance":di})
        self.speak_dialog("time",{"duration":du}) """
        self.speak_dialog(place1)
        self.speak_dialog(place2)
        self.log.info("There are five types of log messages: "
                      "info, debug, warning, error, and exception.")
        
        
    def stop(self):
        pass
    
def create_skill():
    return NavigateSkill()
