class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        if len(emails) == 0:
            return 0

        from collections import defaultdict
        email_table = defaultdict(int)

        for email in emails:
            parts = email.split("@")
            parts[0] = parts[0].replace(".", '')
            if "+" in parts[0]:
                parts[0] = parts[0][0:parts[0].find("+")]
            email_table[tuple(parts)] += 1
        return len(email_table.keys())
