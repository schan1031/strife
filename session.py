import os
import time

class Session:
    def __init__(self, user_id):
        self.user_id = user_id
        self.lock = False

    def handle_input(self):
        if self.lock:
            print('locked')
        else:
            print('handling')
            self.lock = True

    def clear_lock(self):
        self.lock = False