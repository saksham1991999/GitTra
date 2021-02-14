from comment_parser import comment_parser

f = open("comments.txt", "w", encoding="utf-8")

#the lines below extract comments from a python file called test.py

commentTextList = []

for each in comment_parser.extract_comments('test.py', mime='text/x-python'):
    commentTextList.append(each.text()+"\n")
    
print(commentTextList)

f.writelines(commentTextList)