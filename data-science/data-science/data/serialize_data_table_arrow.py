
from metaflow import FlowSpec, step

class SerializeTable(FlowSpec):
    
    @step
    def start(self):
        self.next(self.end)
        
    @step
    def end(self):
        pass
    
if __name__ == "__main__":
    SerializeTable()
