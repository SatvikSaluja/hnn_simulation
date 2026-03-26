from pathlib import Path
from hnn_core import jones_2009_model, simulate_dipole
from hnn_integrity import HNNIntegrityValidator

BASE_DIR=Path(__file__).parent
REPORT_DIR=BASE_DIR/"gsoc_reports"
REPORT_DIR.mkdir(exist_ok=True)

def run_simulation():
    print("Initializing Jones 2009 Model...")
    net=jones_2009_model()
    
 
 
    weights={'L2_pyramidal':0.01,'L5_pyramidal':0.01}
    net.add_evoked_drive('evdist',mu=50,sigma=2,numspikes=1,
                         weights_ampa=weights,location='distal')

    print("Executing simulation...")
    dpls=simulate_dipole(net,tstop=100.0,n_trials=1)
    
    validator=HNNIntegrityValidator(net,dpls[0])
    validator.check_config_integrity()
    validator.check_peak_latency()
    validator.report()
    
    
    validator.plot_results(REPORT_DIR/"regression_test_output.png")
    print(f"Audit plot saved to {REPORT_DIR}")

if __name__=="__main__":
    run_simulation()