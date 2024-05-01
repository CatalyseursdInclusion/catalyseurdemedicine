# catalyseurdemedicine

First program - inside tika folder

This program takes in a jpeg image of pharmacy invoice, and it extracts the medication names from it.

To execute the code run following 

python3 extract_medicine_name [-i input filename] [-h]
or 
./extract_medicine_name [-i input filename] [-h]

where the input file name is in jpeg format.

As an example - 
python3 extract_medicine_name.py -i scan.jpeg
or 
./extract_medicine_name.py -i scan.jpeg

Ensure the jpg file is in the same directory as the code.




Second program - inside heartdisease folder

This program trains a RandomForest model on heart disease dataset from UC Irvine repository
Database url: https://archive.ics.uci.edu/dataset/45/heart+disease

The dataset was downloaded and only "processed.cleveland.data" was used for model training
There are 303 records with 14 columns including the target label
the header record was missing, so we added a header record so that we can have the column names in pandas

The "target" field refers to the presence of heart disease in the patient.  It is integer valued from 0
(no presence) to 4. Experiments with the Cleveland database have concentrated on simply attempting 
to distinguish presence (values 1,2,3,4) from absence (value 0) -- from heart-disease.names

We created two version of the dataset uci_heart_mod.csv is with multiclass target and 
uci_heart_mod_binary.csv is with binary target labels where we collapsed target label 1,2,3,4 into 1
