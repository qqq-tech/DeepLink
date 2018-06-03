class AdapterBaseClass:
    def __init__(self):
        raise NotImplementedError()

    def __del__(self):
        raise NotImplementedError()

    def conn(self,dbname):
        raise NotImplementedError()

    def close(self):
        raise NotImplementedError()

    def select(self,sql,data):
        pass

    def update(self,sql,data):
        pass

    def delete(self,sql,data):
        pass

    def create(self, sql, data):
        pass

    def insert(self, sql, data):
        pass
