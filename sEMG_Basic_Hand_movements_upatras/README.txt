Source:

Christos Sapsanis (csapsanisa€?@a€?gmail.com) and Anthony Tzes 
ANeMoS Lab 
School of Electrical and Computer Engineering 
University of Patras 

G. Georgoulas 
KIC Laboratory 
Department of Informatics and Telecommunications Technology, 
Technological Educational Institute of Epirus


Data Set Information:

Instrumentation: 
The data were collected at a sampling rate of 500 Hz, using as a programming kernel the National Instrumenta€?s (NI) Labview. The signals were band-pass filtered using a Butterworth Band Pass filter with low and high cutoff at 15Hz and 500Hz respectively and a notch filter at 50Hz to eliminate line interference artifacts. 
The hardware that was used was an NI analog/digital conversion card NI USB- 009, mounted on a PC. The signal was taken from two Differential EMG Sensors and the signals were transmitted to a 2-channel EMG system by Delsys Bagnolia?¡é Handheld EMG Systems. 

Protocol: 
The experiments consisted of freely and repeatedly grasping of different items, which were essential to conduct the hand movements. The speed and force were intentionally left to the subjecta€?s will. There were two forearm surface EMG electrodes Flexor Capri Ulnaris and Extensor Capri Radialis, Longus and Brevis) held in place by elastic bands and the reference electrode in the middle, in order to gather information about the muscle activation. 

The subjects were asked to perform repeatedly the following six movements, which can be considered as daily hand grasps: 
a) Spherical: for holding spherical tools 
b) Tip: for holding small tools 
c) Palmar: for grasping with palm facing the object 
d) Lateral: for holding thin, flat objects 
e) Cylindrical: for holding cylindrical tools 
f) Hook: for supporting a heavy load 

An illustrative photo is included in the data folder. 

Two different databases are included: 
1) 5 healthy subjects (two males and three females) of the same age approximately (20 to 22-year-old) conducted the six grasps for 30 times each. The measured time is 6 sec. There is a mat file available for every subject. 
2) 1 healthy subject (male, 22-year-old) conducted the six grasps for 100 times each for 3 consecutive days. The measured time is 5 sec. There is a mat file available for every day.


Attribute Information:

Data Format: 
The format of each mat file is the following: 
a€¡é The data per grasp and per channel are in separate table with an obvious naming. {Spherical --> (spher_ch1, spher_ch2), Tip --> (tip_ch1, tip_ch2), Palmar --> (palm_ch1, palm_ch2), Lateral --> (lat_ch1, lat_ch2), Cylindrical --> (cyl_ch1, cyl_ch2), Hook --> (hook_ch1, hook_ch2)} 
a€¡é Each row of these tables has the whole signal per trial. The signal value is measured in Voltage. 

In summary, in each subject, there will be a mat file with 12 matrixes, in which matrix there will be 30 (trials) rows and 3000 (points of the signal) columns for database 1 (or 100 rows and 2500 columns for database 2). 


Relevant Papers:

Since the data is signals in time domain, part of it can be used for classification using signal processing techniques and methods, such as Empirical Mode Decomposition (EMD). Moreover, suggested features for extraction can be Integrated Electromyogram (IEMG), Zero Crossing (ZC), Slope Sign Changes (SSC), Waveform Length (WL), Willison Amplitude (WAMP) etc. 

More information can be found in the following paper: 
a€¡é C. Sapsanis, G. Georgoulas, A. Tzes, a€?EMG based classification of basic hand movements based on time-frequency featuresa€? in 21th IEEE Mediterranean Conference on Control and Automation (MED 13), June 25 - 28, pp. 716 - 722, 2013.



Citation Request:

If you found useful these databases, please cite the following: 
For the database 1), 
a€¡é C. Sapsanis, G. Georgoulas, A. Tzes, D. Lymberopoulos, a€?Improving EMG based classification of basic hand movements using EMDa€? in 35th Annual International Conference of the IEEE Engineering in Medicine and Biology Society 13 (EMBC 13), July 3-7, pp. 5754 - 5757, 2013. 
For the database 2): 
a€¡é C. Sapsanis. 'Recognition of basic hand movements using electromyography'. 2013.

