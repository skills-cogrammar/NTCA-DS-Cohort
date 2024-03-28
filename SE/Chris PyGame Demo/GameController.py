import pygame

class GameController:
    def __init__(self):
        # Initialize a dictionary to hold key mappings to actions
        self.key_action_mapping = {}
        
    def register_action(self, key, action):
        """Associates a keyboard key with an action."""
        self.key_action_mapping[key] = action
    
    def remap_action(self, old_key, new_key):
        """Remaps an action from one key to another."""
        if old_key in self.key_action_mapping:
            self.key_action_mapping[new_key] = self.key_action_mapping.pop(old_key)
    
    def handle_keys(self, keys, clock_tick):
        """Handles PyGame events based on current key mappings."""
        for key in self.key_action_mapping:
            # returns True or False if the key is currently held down
            if keys[key]:
                action = self.key_action_mapping[key]
                action(clock_tick)  # Call the action function

