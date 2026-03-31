/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(0);
        ListNode head = dummy;
        int carry = 0;
        while (l1 != null || l2 !=null || carry > 0) {
            int res = carry;
            if  (l1 != null && l2 != null) {
                res += l1.val + l2.val;
            } else if (l1 == null && l2 != null) {
                res += l2.val;
            } else if (l1 !=null && l2 == null) {
                res += l1.val;
            }

            carry = 0;

            System.out.println("Res pre-carry: " + res);
            if (res >= 10) {
                carry = 1;
                res = res - 10;
            }
            System.out.println("Adding result: " + res);
            dummy.next = new ListNode(res);
            dummy = dummy.next;
            if (l1 != null) l1 = l1.next;
            if (l2 != null) l2 = l2.next;

            
        }
        return head.next;
    }
}
