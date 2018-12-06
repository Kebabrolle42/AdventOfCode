x=0
with open('puzzle1input.txt','r+') as f1, open('puzzle1output.txt', 'r+') as f2:
        for line in f1:
                x = x + int(line)
                f2.write(str(x) +  " ")                   

f1.close

