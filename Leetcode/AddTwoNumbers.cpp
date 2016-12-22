/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) 
    {
        bool carry = false;
        int temp = 0;
        ListNode* result = new ListNode(-1);
        // ListNode* result; For some reason it goes to L2;
        ListNode* rtemp = result;
        while(l1 != NULL && l2 != NULL)
        {
            std::cout << l1->val << "  " << l2->val << std::endl;
            temp = l1->val + l2->val;
            std::cout << "before if: " << temp << std::endl;
            if(carry)
            {
                temp++;
                carry = false;
            }
            std::cout << "After 1 if " << temp << std::endl;
            if(temp > 9)
            {
                carry = true;
                temp -= 10;
            }
            std::cout << "After 2 if " << temp << std::endl;
            rtemp->next = new ListNode(temp);
            rtemp = rtemp->next; 
            l1 = l1->next;
            l2 = l2->next;
        }
        
        return result->next;
    }
};
