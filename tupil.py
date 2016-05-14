import sys,io
import collections as col

Sale= col.namedtuple("Sale", "producitid cutomerid date quantity price")
Sale=(Sale(23,34,"2008-09-19",3,344),Sale(32,11,"2008-09-10",3,200))

sales = list(Sale)
print (sales)
#sales.append=(Sale(23,322,"2008-09-19",3,344))
#sales.append=(Sale(32,112,"2008-09-10",3,200))
total=0
for i in sales:
    total+= i.quantity * i.price
print(total)
