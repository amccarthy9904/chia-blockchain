
from logging import root
from pathlib import Path
from tests.clvm.test_puzzles import T1
from chia.plotting.create_plots import create_plots

class Plotter:
    
    k = None
    b = None
    f = None
    t1 = None
    t2 = None
    start_dir = "/home/lron/repos/chia-blockchain"
    script_loc = "/home/lron/repos/chia_script/plot.sh"
    
    def __init__(self, k, b, f, t1, t2):
        self.k = k
        self.b = b
        self.f = f
        self.t1 = t1
        self.t2 = t2
         
    def start(self):
        
        vars = [self.k, self.b, self.f, self.t1, self.t2]
        for v in vars:
            print (v, end = '\t')
        
        class Params(object):
            def __init__(self):
                self.size = vars[0]
                self.num = 1
                self.buffer = vars[1]
                self.num_threads = 2
                self.buckets = 128
                self.stripe_size = 65536
                self.alt_fingerprint = None
                self.pool_contract_address = None
                self.farmer_public_key = None
                self.pool_public_key = None
                self.final_dir = vars[2]
                self.tmp_dir = vars[3]
                self.tmp2_dir = vars[4]
                self.plotid = None
                self.memo = None
                self.nobitfield = False
                self.exclude_final_dir = False
        root_path = Path("/home/lron/.chia/mainnet")
        create_plots(Params(), root_path)
        
        