
def getoptions(j):
    text_file = open("txtfiles/options.txt", "r")
    lines = text_file.readlines()
    
    c=1
    d=4*(j-1)+1
    
    for line in lines:
        
        if c in range(d,d+4):
            return lines[c-1][:-1],lines[c][:-1],lines[c+1][:-1],lines[c+2][:-1]
        
               
        c+=1
def questions(j):
    text_file=open("txtfiles/questions.txt","r")
    lines=text_file.readlines()
    c=0
    for line in lines:
        if c==j:
                        return lines[j-1][:-1]
        c+=1
def writescores(username,score):
    text_file=open("txtfiles/scores.txt","a")
    
    text_file.write(username)
    score=str (score)
    text_file.write("\n")
    text_file.write(score)
    text_file.write("\n")

def getscore(j):
    text_file=open("txtfiles/scores.txt","r")
    lines=text_file.readlines()
    c=0
    d=2*(j-1)+1
    count=0
    for line in lines:
        count+=1
    for line in lines:
        if c in range(d,d+2):
            return lines[c-1][:-1],lines[c][:-1],count
        c+=1
print getscore(1)
print getscore(2)
