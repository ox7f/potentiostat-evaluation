from config import CONFIG
from potentiostat import Potentiostat

"""
amplitude = data['volt_max']-data['volt_min']/2.0
offset = data['volt_max']+data['volt_min']/2.0
period_ms = int(1000*4*amplitude/data['volt_per_sec'])

print('amplitude:', amplitude)
print('offset:', offset)
print('period_ms:', period_ms)

calculated_data = {
    'quietValue' : 0.0,
    'quietTime'  : 0,
    'amplitude'  : amplitude,
    'offset'     : offset,
    'period'     : period_ms,
    'numCycles'  : data['num_cycle'],
    'shift'      : data['shift'],
}

_self.dev.set_curr_range('100uA') #str(data['curr_range'])+'µA')
_self.dev.set_sample_rate(data['sample_rate'])
_self.dev.set_param(_self.name, calculated_data)

t,volt,curr = _self.dev.run_test(display='pbar',filename=_self.datafile)
"""

port = 'COM3'       # Serial port for potentiostat device
datafile = 'data.txt'       # Output file for time, curr, volt data

test_name = 'cyclic'        # The name of the test to run
curr_range = '100uA'        # The name of the current range [-100uA, +100uA]
sample_rate = 100.0         # The number of samples/second to collect

volt_min = -0.1             # The minimum voltage in the waveform (V)
volt_max =  1.0             # The maximum voltage in the waveform (V)
volt_per_sec = 0.050        # The rate at which to transition from volt_min to volt_max (V/s)
num_cycles = 1              # The number of cycle in the waveform

# Convert parameters to amplitude, offset, period, phase shift for triangle waveform
amplitude = (volt_max - volt_min)/2.0            # Waveform peak amplitude (V) 
offset = (volt_max + volt_min)/2.0               # Waveform offset (V) 
period_ms = int(1000*4*amplitude/volt_per_sec)   # Waveform period in (ms)
shift = 0.0                                      # Waveform phase shift - expressed as [0,1] number
                                                # 0 = no phase shift, 0.5 = 180 deg phase shift, etc.

# Create dictionary of waveform parameters for cyclic voltammetry test
test_param = {
        'quietValue' : 0.0,
        'quietTime'  : 0,
        'amplitude'  : amplitude,
        'offset'     : offset,
        'period'     : period_ms,
        'numCycles'  : num_cycles,
        'shift'      : shift,
        }

# Create potentiostat object and set current range, sample rate and test parameters
dev = Potentiostat(port)     
dev.set_curr_range(curr_range)   
dev.set_sample_rate(sample_rate)
dev.set_param(test_name,test_param)
t,volt,curr = dev.run_test(test_name,display='pbar',filename=datafile)
print('potentiostat werte', [t, volt, curr])