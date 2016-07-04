class DriveController(object):
    def __init__(self):
        pass
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        ''' Should be over-written by adapter if necessary to clean up connection 
            for instance
        '''
        pass

    def move_forward(self):
        ''' implemented specifically for hardware setup through adaptors '''
        raise NotImplementedError('move_forward method is expected to be overwritten')
    
    def move_backward(self):
        raise NotImplementedError('move_backward is expected to be overwritten')
    
    def move_right(self):
        raise NotImplementedError('move_right is expected to be overwritten')
        
    def move_left(self):
        raise NotImplementedError('move_left is expected to be implemented')
    
    def stop(self):
        raise NotImplementedError('stop is expected to be implemented')