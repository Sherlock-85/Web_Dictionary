from abc import ABC, abstractmethod

class Page(ABC):
    # Abstract classes should not be initialized
    @abstractmethod
    def serve(self):
        pass