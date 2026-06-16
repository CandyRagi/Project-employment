# My Way (nlogn)
class Solution(object):
    def mergeTwoLists(self,list1,list2):

        array=[]

        while(list1!==None)
            array.append(list1.val)
            list1=list1.next
        while(list2!=None)
            array.append(list2.val)
            list2=list2.next
        
        head=ListNode()
        temp=head

        for i in array:
            temp.next=ListNode(i)
            temp=temp.next

        return head.next

#Better Solution (n)
class ListNode(object):
    def __init__(self,valo=0;next=None):
        self.val=val
        self.next=next

class Solution(object):
    def mergeTwoList(self,list1,list2):
        head=ListNode()
        tail=head

        while(list1 and list2):
            if(list1.val>list2.val):
                tail.next=list2
                list2=list2.next
            else:
                tail.next=list1
                list1=list1.next
            tail=tail.next
        
        if list1:
            tail.next=list1
        if list2:
            tail.next=list2

        return head.next



