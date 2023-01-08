
codons = ["ATG", "TAA", "TAG", "TGA"]
stop_codons = ["TAA", "TAG", "TGA"]
start_codon = "ATG"


#complementary sequence
def complementarity(sequence):
    compl = sequence.replace("A", "t").replace("C", "g").replace("T", "a").replace("G", "c")
    seq = compl.upper()
    complement = seq[::-1]
    print("The complementary sequence reversed is: ", complement)
    complementary_ORF_finder(complement)
    return complement

#checking the length of the detected ORFs
def ORF_quality_control(final_sequence):
    if len(final_sequence) > 6:
        return "True"
    return "None"

#detection of ORFs in the complementary sequence
def complementary_ORF_finder(complement):
    ORF_seq = start_finder(complement)

    if ORF_seq == "None":
        print("There are no start codons in your sequence! No ORF can be found.\n")
        print("Scanning of DNA sequence is done!")
        return

    final_sequence, remaining_sequence = stop_finder(ORF_seq)

    if final_sequence == "None":
        print("There are start codons but no stop codons in your sequence. No ORFs can be found.\n")
        print("Scanning of DNA sequence is done!")
        return
    
    ORF_quality_control(final_sequence)

    if ORF_quality_control(final_sequence) == "None":
        print("Detected ORF consists only of start and stop codon and is considered is too small.\n")
        return

    if ORF_quality_control(final_sequence) == "True":
        print("Several codons are detected between the start and stop codons; the detected sequence could in fact be a real ORF.\n")
        print("Continuing to search for other ORFs.\n")
    
    complementary_ORF_finder(remaining_sequence)  

    if len(remaining_sequence) == 0:
        print("Scanning of DNA sequence is done!")
    
#questioning of user if they want to detect ORFs in the complementary sequence   
def next_step(sequence):
    print("\nDNA is double stranded. Would you like to proceed with ORF detection in the complementary sequence?")
    answer = input("Please enter yes or no: \n")
    if answer == "yes":
        new_seq = input("Please enter your sequence again.\n")
        print("Proceeding with ORF detection in the complementery sequence.\n")
        complementarity(new_seq)
        return new_seq

    elif answer == "no":
        print("ORF detection in complementary sequence was blocked. The program is done running.\n")
 
#detection of ORFs in the inserted sequences
def ORF_finder(sequence):
    sequence = sequence.upper()

    ORF_seq = start_finder(sequence)

    if ORF_seq == "None":
        print("There are no start codons in your sequence! No ORF can be found.\n")
        print("Scanning of DNA sequence is done!")
        next_step(sequence)
        return

    final_sequence, remaining_sequence = stop_finder(ORF_seq)

    if final_sequence == "None":
        print("There are start codons but no stop codons in your sequence. No ORFs can be found.\n")
        print("Scanning of DNA sequence is done!")
        next_step(sequence)
        return
    
    ORF_quality_control(final_sequence)

    if ORF_quality_control(final_sequence) == "None":
        print("Detected ORF consists only of start and stop codon and is considered is too small. Proceeding with the rest of the sequence.\n")
        ORF_finder(remaining_sequence)  
        return 

    if ORF_quality_control(final_sequence) == "True":
        print("Several codons are detected between the start and stop codons; the detected sequence could in fact be a real ORF.\n")
        print("Continuing to search for other ORFs.\n")
    
    ORF_finder(remaining_sequence)  

    if len(remaining_sequence) == 0:
        print("Scanning of DNA sequence is done!")
        next_step(sequence)
        

#detection of start codons "ATG" in the inserted sequence
def start_finder(sequence):
    for x in range (0, len(sequence), 1):
        if start_codon in sequence[x:x+3]:
            ORF_seq = sequence[x:]
            start_position = abs(x)
            print("Start codon found at posistion", start_position, "of the currently scanned sequence. The remaining sequence is: ", ORF_seq)
            return ORF_seq
    return "None"

#detection of stop codons in the sequence
def stop_finder(ORF_seq):
    for x in range (0, len(ORF_seq), 3):
        if any(s in ORF_seq[x:x+3] for s in stop_codons):
            final_sequence = ORF_seq[:x+3]
            remaining_sequence = ORF_seq[x+3:]
            stop_position = abs(x+1)
            print("Stop codon found", stop_position, "nucleotides away from the start codon. The ORF sequence is: ", final_sequence)
            return final_sequence, remaining_sequence
    return "None", "None"

#code starts here
def main():
    sequence = input("\nThis is an ORF-detecting program for DNA sequences.\nPlease type your sequence below.\n")
    if "T" in sequence:
        print("Your sequence is in fact a DNA sequence. Proceeding with ORF finding.\n")
        ORF_finder(sequence)
    
    if "U" in sequence:
        print("Your sequence is an RNA sequence NOT a DNA sequence. This program can't detect ORFs in RNA sequences.\n")
        return  

if __name__ == "__main__":
    main()




 