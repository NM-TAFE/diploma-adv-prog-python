import logging

class UploadNotifier:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, fn):
        self.subscribers.append(fn)

    def notify(self, doc_name):
        for fn in self.subscribers:
            fn(doc_name)

def alert_admin(doc):
    logging.info(f"[ALERT] Admin notified: '{doc}' uploaded.")

def log_upload(doc):
    logging.info(f"[LOG] Document '{doc}' was uploaded.")