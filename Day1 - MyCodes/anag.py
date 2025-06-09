import collections

s = "silent"
l = "listen"

if len(s) == len(l):
    for i in s:
        if s.count(i) == l.count(i):
            print("it's an anagram")


else:
    print("not anagram")