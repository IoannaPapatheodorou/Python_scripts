# Python_scripts-ORF-detector
 
ORF-detector in Python


This repository contains simple scripts in Python language. The scripts aim to perform certain molecular biology-related processes in biological data. This particular script aims to detect open reading frames (ORFs) in a DNA sequence. 


The steps of the script are the following:

1. The user is asked to provide a DNA sequence. If the sequence is an RNA sequence the user is notified that the script can't continue running.
	
2. Once the sequence is provided every position of the sequence is scanned for "ATG" nucleotides in order to determine a start codon posistion. 
One an "ATG" is found, the user is notified for the "ATG" position and the remaining sequence. If there are no start codons in the sequence the user is notified.
	
3. The sequence is scanned in a "triplet-step" in order to find any of the stop codons. If a stop codon is found the user is notified for the length of the ORF in nucleotides as well as the sequence of the ORF. If no stop codon is found the user is notified.
	
4. The program scans the rest of the sequence after the ORF is found, in order to determine more start and/or stop codons. The user is notified accordingly. This procedure is repeated for the whole sequence.
	
5. Once scanning of the sequence is done the user is asked if they would like to proceed to detect ORFs in the complementary strand. If the user andwers "yes" they will be asked to provide theis sequence again. If the answer is "no" the program will stop running and the user will be notified that all procedures are done. 
	
6. For ORF-detection in the complementary strand, first the complement of the initial sequence if found. Then the complementary sequence is reversed and processed similarly (please see steps 2 - 4). 
	
7. Once the ORF-detecting procedures for the complementary scan are done the user is notified that the program has finished running.
