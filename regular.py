import re
def detect_word_pattern(pattern,text):
    matches=re.findall(pattern,text)
    if matches:
        print("word patterns detected")
        for i in matches:
            print(i)
    else:
        print("no word pattern detected")
sample_inputs=[("[0-9]+","my date of birth is 30 august 2002"),
               ("[a-z A-Z]+","detecting word patterns"),
               ("[A-Z] [a-z]+","Shivani"),
               ("[a e i o u A E I O U]+","natural"),
               ("[0-9]{2}-[0-9]{2}-[0-9]{4}","11-01-2024"),
               ("[a-z][0-9]+@[a-z]+.com","sivani@gmail.com")]
for p,t in sample_inputs:
    print("pattern",p)
    print("text",t)
detect_word_pattern(p,t)
