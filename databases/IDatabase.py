from abc import ABC, abstractmethod

class IDatabase(ABC):

    @abstractmethod
    def create(self, sql, params=None):
        pass

    @abstractmethod
    def read(self, sql, params=None):
        pass

    @abstractmethod
    def update(self, sql, params=None):
        pass

    @abstractmethod
    def delete(self, sql, params=None):
        pass