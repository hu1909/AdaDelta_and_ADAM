import numpy as np 

class EMA:
    def __init__(self, beta=None, bias_correction=True):
        self.beta = beta
        self.bias_correction = bias_correction
        self.t = 0
        self.ema = None

    
    
    def calculate(self, new_value):
        self.t += 1
        if self.ema is None:
            self.ema= new_value
        else:
            self.ema = self.beta * new_value + (1 - self.beta) * self.ema
        
        if self.bias_correction:
            bias_ema = self.ema / (1 - (1 - self.beta) ** self.t)
            return bias_ema
        else:
            return self.ema_value
    
    def get_current_value(self):
        if self.bias_correction:
            return self.ema / (1 - (1 - self.beta) ** self.t)
        else:
            return self.ema
        