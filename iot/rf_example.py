#!/usr/bin/python3.7

__author__ =  "oguzhanlarca"
__email__ =   "cu.oguzhan@gmail.com"
__status__ =  "Development"
__date__ =    "Late Updated: 2019-09-21"

from rtlsdr import RtlSdr

sdr = RtlSdr()

# configure device
sdr.sample_rate = 2.048e6  # Hz
sdr.center_freq = 70e6     # Hz
sdr.freq_correction = 60   # PPM
sdr.gain = 'auto'

print(sdr.read_samples(512))
