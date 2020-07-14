Two meatures to access csvfile：pandas/Csv https://blog.csdn.net/ninnyyan/article/details/80763301

In csv, csv.reader() func is used
The iter f have modes: a+/a w+/w r+/r

read and write the same file, a+/w+ can be used.
while both can read NOTHING in csv.reader, some blog says the pointer is set on the bottem, but using f.seek() func it can't be solved.

DONT'T KNOW WHY

another solution:using two files seems properit
https://stackoverflow.com/questions/34699944/using-r-mode-to-read-and-write-into-the-same-file

As for the PANDAS, didn't figure it out
