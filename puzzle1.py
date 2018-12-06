x=0

f2 = open('puzzle1output.txt', 'r+')
f3 = open('puzzle1output2.txt', 'r+')
with open('puzzle1input.txt','r+') as f1, open('puzzle1output.txt', 'r+') as f2, open('puzzle1output2.txt', 'r+') as f3:
        for line in f1:
                x = x + int(line)
                f2.write(str(x) +  " ")
                for line in f2:
                        for line in f2:
                                if line == line:
                                        f3.write(f2.readline())                    

f1.close
f2.close
f3.close
