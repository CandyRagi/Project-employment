class Solution(object):
    def deleteDuplicates(self,head):
        prev=head
        if head:
            next=head.next
        else:
            return head

        while prev and next:
            if(prev.val==next.val):
                prev.next=prev.next.next
                next=next.next
            else:
                prev=prev.next
                next=next.next

        return head
