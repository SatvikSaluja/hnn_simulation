import numpy as np
import matplotlib.pyplot as plt

class HNNIntegrityValidator:
    def __init__(self,net,dpl):
        self.net=net
        self.dpl=dpl
        self.results={}

    def check_config_integrity(self):
        has_metadata=len(self.net.cell_types)>0
        has_times=len(self.net.cell_response.times)>0
        dt=self.net.cell_response.times[1]-self.net.cell_response.times[0]
        is_dt_valid=np.isclose(dt,0.125)
        self.results['config_ok']=has_metadata and has_times and is_dt_valid
        return self.results['config_ok']

    def check_peak_latency(self,window_start=50,window_end=80):
   

        times=self.dpl.times
        data=self.dpl.data['agg']

        peak_idx=np.argmax(np.abs(data))
        peak_time=times[peak_idx]
        

        is_latency_valid=window_start<peak_time<window_end
        self.results['latency_ok']=is_latency_valid
        return is_latency_valid,peak_time

    def plot_results(self,save_path):
        plt.figure(figsize=(10,5))
        plt.plot(self.dpl.times,self.dpl.data['agg'],color='black',label='Simulated Dipole')
       
        plt.axvspan(50,80,color='green',alpha=0.1,label='Expected Peak Window')
        plt.title("Automated Regression Test: Peak Latency Validation")
        plt.xlabel("Time (ms)")
        plt.ylabel("nAm")
        plt.legend()
        
        plt.grid(True,alpha=0.2)
        plt.savefig(save_path)
        plt.close()

    def report(self):
        print("--- HNN-Core System Audit ---")
        for test,passed in self.results.items():
            print(f"{test}: {'PASSED' if passed else 'FAILED'}")