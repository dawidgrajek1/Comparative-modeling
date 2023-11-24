from Bio import PDB, SeqIO
import requests

querySequence = SeqIO.read("startingSequence.fasta", "fasta")
apiUrl = r"https://blast.ncbi.nlm.nih.gov/Blast.cgi"
params = {
    "QUERY": querySequence.seq,
    "DATABASE": "pdbaa",
    "PROGRAM": "blastp",
    "FORMAT_TYPE": "JSON2",
}
response = requests.get(apiUrl, params)
