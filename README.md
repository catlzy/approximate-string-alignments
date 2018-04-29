# Approximate String Alignments

## Overview
This repository contains code for local alignment, global alignment, and global alignment with affine gaps. Local and global alignments take approximately 75 seconds to run on any two of the three .fasta files in the repository, and affine takes approximately two minutes to run. 

The .sh files are the shell scripts for the three alignments. The .py files are the python programs for the alignments. The scoringMatrix.txt is the current scoring matrix used to produce all results bellow. The .fasta files are three sequences being aligned. 

## Scoring Matrix
The scoring matrix used for the alignments rewards 3 for any matches, 2 for C-T or A-G pairs, and 0 for any other mismatches. The penalty for alignment with a gap is -1. For global alighment with affine gaps, the continuing of a opened gap is penalized for -0.01. The reason for the chosen scoring scheme is that both A and G have 2 ring bases and T and C have 1 ring bases. Mutation between amino acids with the same ring numbers is more likely to happen than those that with different ring numbers. Therefore while the exact matches are rewarded with score 3, the C-T and A-G pairs are rewarded with score of 2. Also, in real life, insertions or deletions (indels) occur more likely in a consecutive block in a single mutation event, so, while the penalty for opening a gap should be big, the penalty for continuing the gap should be small to reflect the true distribution of indels in gaps. Thus, in global alignment with affine gaps, opening a gap is penalized for -1 and continuing is penalized for -0.01. 

## To Run
To run the programs, use the .sh shell scripts in the command line with the desired arguments, including in order sequence 1, sequence 2, the scoring matrix, penality socre, and penalty for affine gaps (only include this argument when running `affin.sh`. For example, for local alignment, run the following commend in terminal: `./local.sh ypestis_modern.fasta test_medieval.fasta scoringMatrix.txt -1`. If report `permission denied`, run `chmod +x local.sh` first, then run the above line. 

## Output
The program will print out the alignment score. The lines for printing out the aligned sequences are commented out in the programs since they can be really long. If want the aligned sequences to be printed out, the two lines are at the end of the traceback() function for all programs. 

## Results
The results are as follows:  
local alignment: yenterocolitica vs. medieval: 15809; ypestis vs. medieval: 20779  
global alignment: yenterocolitica vs. medieval: 15315; ypestis vs. medieval: 20778  
global with affine gaps: yenterocolitica vs. medieval: 16504.72; ypestis vs. medieval: 20777.98

Based on the results, Y.pestis is more closely related to the medieval bacterium. 
