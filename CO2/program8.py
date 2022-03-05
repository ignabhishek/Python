#Accept a list of words and return length of longest word

word=input("Enter some words seperated by commas:")
word_lst=word.split(",")
longest=len(word_lst[1])
for i in word_lst:
    if len(i) > longest:
        longest=len(i)
print("Length of longest word in the list is:",longest)

# n = int(input("enter the no. of words:"))
# l=[]
# print("enter ",n," words")
# for i in range(n):
#     l.append(input())
# long = len(l[1])
# for i in l:
#     if len(i) > long:
#         long = len(i)
# print("Length of longest word in the list is:",long)     
