import time
import threading

class IA_class(threading.Thread):

    def __init__(self,list_action):
        self.list_action = list_action
        self.current_action = -1
        self.START = False
        self.STOP = False

    def start(self):
        """lance ma liste d'action"""
        self.START = True
        self.STOP = False

    def stop(self):
        """ Arrete ma liste d'action """ 
        self.list_action.stop()
        self.STOP = True
    
    

    def add_action(self,action):
        """ ajoute une action"""
        self.list_action.append(action)

    
    def select_action(self,indice):
        """ selectionne une action par indice """
        if indice < 0 or indice >= len(self.list_action):
            return 

        self.list_action[indice].start()

    def run(self):
        """ méthode abstraite qui exécute ma liste_d'action"""
        pass




