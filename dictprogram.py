import pickle
f=open("meaning.txt",'r')
lines= f.read()
lines= lines.split('\n')
dict={}
var=raw_input("enter a word"+'\n')
print("you entered "+var)
for line in lines:
        word= line.split(" ")
        dict[word[0]]=word[1:]
if var in dict:
        print(dict[var])
else:
        var1=raw_input("please enter the synonym ")
        dict[var]=var1
        f= open("meaning.txt",'ab')
        f.write("\n"+var+":")
        pickle.dump(dict[var],f)
        print(var,":",dict[var])
f.close()


