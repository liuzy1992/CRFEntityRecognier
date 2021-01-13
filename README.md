# CRFEntityRecognier
**CRFEntityRecognier** uses CRF model to do named entity recognization (NER) in preprocessed texts.

## Requirement
python3    
pandas  
sklearn  
sklearn_crfsuite  
scipy  
joblib  

## Usage
```shell
./CRFEntityRecognier.sh <-i infile>
                        [-n n_jobs]
                        [-o outdir]
```
**-i**: filename of raw input text. Input text shoud be in TSV format with 4 colomns as follows:  
&nbsp;&nbsp;&nbsp;&nbsp;Sent_ID  Word  Pos  Tag  
**-n**: number of threads to use. Default=1  
**-o**: directory to save trained model. Default=./model  

## Example
Use following command to test:
```shell
./CRFEntityRecognier.sh -i testdata/test.tsv
```
