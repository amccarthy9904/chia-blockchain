import os
from pathlib import Path
import shutil

class Prepper:
    
    plot = None
    farm = None
    dirs = {}
    trash_dir = "/media/lron/plot1/.Trash-1000"
    
    def __init__(self, plot, farm):
        self.plot = plot
        self.farm = farm
        
    def prep(self):
        root = Path("/media/lron/plot1/p1." + self.plot)
        tst1 = Path(str(root) +  "/p1." + self.plot + "t1")
        tst2 = Path(str(root) +  "/p1." + self.plot + "t2")
        farm = Path("/media/lron/farm1/f" + self.farm + "." + self.plot)
        
        self.dirs = {"r" : root, "t1" : tst1, "t2" : tst2, "f": farm}
        try:
            self.clean(True)
        except:
            pass
        
        os.mkdir(root)
        os.mkdir(tst1)
        os.mkdir(tst2)
        os.mkdir(farm)
        return self.dirs
        
        
    def clean(self, clean_farm = False):
        
        shutil.rmtree(self.dirs["r"])
        if clean_farm:
            shutil.rmtree(self.dirs["f"])
        try:
            shutil.rmtree(self.trash_dir)
        except:
            pass