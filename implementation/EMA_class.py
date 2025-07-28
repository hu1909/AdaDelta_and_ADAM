import numpy as np 

class EMA:
    def __init__(self, alpha=None, window=None, bias_correction=True):

        if alpha is not None and window is not None:
            raise ValueError("Specify either alpha or window, not both")
        
        if alpha is not None:
            if not 0 < alpha <= 1:
                raise ValueError("Alpha must be between 0 and 1")
            self.alpha = alpha
        elif window is not None:
            if window <= 0:
                raise ValueError("Window must be positive")
            self.alpha = 2.0 / (window + 1)
        else:
            raise ValueError("Must specify either alpha or window")
        
        self.bias_correction = bias_correction
        self.t = 0
        self.ema_value = None

    
    
    def calculate(self, new_value):
        self.t += 1
        if self.ema_value is None:
            self.ema_value = new_value
        else:
            self.ema_value = self.alpha * new_value + (1 - self.alpha) * self.ema_value
        
        if self.bias_correction:
            bias_corrected_ema = self.ema_value / (1 - (1 - self.alpha) ** self.t)
            return bias_corrected_ema
        else:
            return self.ema_value
    
    def get_current_value(self):
        if self.ema_value is None:
            return None
        if self.bias_correction:
            return self.ema_value / (1 - (1 - self.alpha) ** self.t)
        else:
            return self.ema_value