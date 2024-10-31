from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionSubmitReport(Action):
    def name(self):
        return "action_submit_report"

    def run(self, dispatcher, tracker, domain):
        incident_type = tracker.get_slot('incident_type')
        device = tracker.get_slot('device')
        # Process the incident report...
        dispatcher.utter_message(text="Your report has been submitted. Our team will contact you shortly.")
        return []

# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

