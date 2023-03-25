from datetime import datetime

def myFun(msg, dt=None):
    if not dt: #not 0,1 / null
        dt=datetime.utcnow()
        print('{0}:{1}'.format(dt,msg))
        
    
    
myFun("textmsg_3")