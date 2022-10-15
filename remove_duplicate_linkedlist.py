from check_linkedlist_is_sorted import Node,SingleList

class sList(SingleList):

    def removeDuplicate(self):
        prev = self.head
        current = prev.next
        if self.checkIfSorted():
            while current:
                if prev.data == current.data:
                    temp = current
                    prev.next = current.next 
                    current = current.next 
                    temp = None
                else:
                    prev = current
                    current = current.next   

            return         



if __name__ == "__main__":
    llist = sList()
    llist.Append(10)
    llist.Append(10)
    llist.Append(20)
    llist.Append(20)
    llist.Append(22)
    llist.Append(31)
    llist.Append(31)
    llist.displayList()
    # print(llist.checkIfSorted())
    llist.removeDuplicate()
    llist.displayList()