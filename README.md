## Approximate String Alignments for CMPT353 Bioinformatics Assignment 2

This repository contains code for local alignment, global alignment, and global alignment with affine gaps. Local and global alignments take approximately 75 seconds to run on any two of the three .fasta files in the repository, and affine takes approximately two minutes to run. 

The scoring matrix used for the alignments rewards 3 for any matches, 2 for C-T or A-G pairs, and 0 for any other mismatches. The penalty for alignment with a gap is -1. For global alighment with affine gaps, the continuing of a opened gap is penalized for -0.01. The reason for the chosen scoring scheme is that both A and G have 2 ring bases and T and C have 1 ring bases. Mutation which preserves the ring numbers is more likely to happen than those that changes the ring number. Therefore while the exact matches are rewarded with score 3, the C-T and A-G pairs are rewarded with score of 2. Substitutions also make the strings more similar than insertions or deletions, so they are not awarded or penalized. Also, in real life, insertions or deletions (indels) occur more likely in a consecutive block in a single mutation event, so, while the penalty for opening a gap should be big, the penalty for continuing the gap should be small to reflect the true distribution of indels in gaps. 

To run the programs, use the .sh shell scripts with the desired arguments, including in order sequence 1, sequence 2, the scoring matrix, penality socre, and penalty for affine gaps if applicaple. For example, for local alignment, run the following commend in terminal: `./local.sh ypestis_modern.fasta test_medieval.fasta scoringMatrix.txt -1`. If report permission denied, run `chmod +x local.sh` first, then run the above line. 

The program will print out the alignment score. The lines for printing out the aligned sequences are commented out since they can be really long. If want the aligned sequences to be printed out, the two lines are in the traceback() function for all programs. 

The results are as follows:  
local alignment: yenterocolitica vs. medieval: 15809; ypestis vs. medieval: 20779  
global alignment: yenterocolitica vs. medieval: 15315; ypestis vs. medieval: 20778  
global with affine gaps: yenterocolitica vs. medieval: 16504.72; ypestis vs. medieval: 20777.98

Based on the results, ypestis is more closely related to the medieval bacterium. 
