"""
  创造节点类
"""
class Node:
    def __init__(self,val,next=None):
        self.next=next
        self.val=val
class Linklist:
    def __init__(self):
        self.head=None
    def init_list(self,data):
        self.head=Node(None)
        p=self.head
        for i in data:
            p.next=Node(i)
            p=p.next
    def show(self):
        p=self.head.next
        while p !=None:
            print(p.val,end=" ")
            p=p.next
        print()


if __name__=="__main__":
    link=Linklist()

    l=[1,2,3,4,5]
    link.init_list(l)
    link.show()