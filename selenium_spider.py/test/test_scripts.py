
class Test_script:
    def __init__(self):
        
        self.script_animation_one()
    
    
    def script_animation_one(self):
        import time
        import sys
        
        animation = ("|/-\\")

        for i in range(100):
            time.sleep(0.1)
            sys.stdout.write("\r" + animation[i % len(animation)])
            sys.stdout.flush()
        print ("End!")
    
        
try:
     Test_script()
except:
    pass