# Our Subject class that communicates change
class EventNotifier:
    def __init__(self):
        self.subscribers = []

    # Record a list of the subscribers we need to inform
    def subscribe(self, function_passed):
        self.subscribers.append(function_passed)

    # When we are ready notify all the subscribers
    def notify(self, event):
        for function_passed in self.subscribers:
            function_passed(event)

# Observers (Listeners)
def log_event(event):
    print(f"Logging: {event}")

def send_alert(event):
    print(f"Alert: {event}")

notifier = EventNotifier()
notifier.subscribe(log_event)
notifier.subscribe(send_alert)

# The event itself
notifier.notify("File uploaded")