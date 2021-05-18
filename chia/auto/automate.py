from chia.auto.plotter import Plotter
from chia.auto.prepper import Prepper
import configparser
import threading
import time

def plot_thread():
    
    properties = "/home/lron/repos/chia-blockchain/chia/auto/properties.ini"
    config = configparser.ConfigParser(allow_no_value=True)
    config.read(properties)
    print(config.sections())

    prep = Prepper(config['Plot Params']['n'], config['Plot Params']['f'])
    dirs = prep.prep()
    
    print(dirs)
    
    plot = Plotter(config.getint('Plot Params', 'k'), config.getint('Plot Params', 'b'), dirs["f"], dirs["t1"], dirs["t2"])
    # iterate n and update properties.ini
    config.set('Plot Params', 'n', str(config.getint('Plot Params', 'n') + 1))
    with open(properties, 'w') as props:
        config.write(props)
        
    plot.start()
    prep.clean()

def status(thread1, thread2, thread3):
    print("STATUS")
    print(f"thread1 = {thread1.isAlive()}")
    print(f"thread2 = {thread2.isAlive()}")
    print(f"thread3 = {thread3.isAlive()}")

if __name__ == "__main__":
    
    plot_thread_1 = threading.Thread(target=plot_thread, daemon=True)
    plot_thread_2 = threading.Thread(target=plot_thread, daemon=True)
    plot_thread_3 = threading.Thread(target=plot_thread, daemon=True)
    
    plot_thread_1.start()
    # 2 hours
    time.sleep(7200)
    plot_thread_2.start()
    time.sleep(7200)
    plot_thread_3.start()
    
    while True:
        if not plot_thread_1.isAlive():
            plot_thread_1 = threading.Thread(target=plot_thread, daemon=True)
            plot_thread_1.start()
        if not plot_thread_2.isAlive():
            plot_thread_2 = threading.Thread(target=plot_thread, daemon=True)
            plot_thread_2.start()
        if not plot_thread_2.isAlive():
            plot_thread_2 = threading.Thread(target=plot_thread, daemon=True)
            plot_thread_2.start()
        time.sleep(60)
        status(plot_thread_1, plot_thread_2, plot_thread_3)
 
        
    # plot_thread()

