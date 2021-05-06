
class SequenceLengthPlugin:
    def input(self, filename):
       self.fasta = open(filename, 'r')

    def run(self):
        pass

    def output(self, filename):
       lineno = 1
       totallen = 0
       numseq = 0
       for line in self.fasta:
           if (lineno % 2 == 0):
               line = line.strip()
               totallen += len(line)
               numseq += 1
           lineno += 1
       outfile = open(filename, 'w')
       outfile.write("AVERAGE LENGTH: "+str(float(totallen)/numseq)+"\n")
       outfile.write("NUMBER OF SEQUENCES: "+str(numseq)+"\n")
