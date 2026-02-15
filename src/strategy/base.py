from abc import ABC, abstractmethod

class BaseStrategy(ABC):
    @abstractmethod
    def generate_signal(self, df_low_tf, df_high_tf):
        pass
