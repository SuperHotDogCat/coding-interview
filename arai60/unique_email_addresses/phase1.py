# atoiににていると思いwhile文で問題文の条件を意識しつつ実装。だが, @が一つであるという条件から多分local部分とdomain部分に分けて実装した方が良かったのだなと思う
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        valid_emails = set()
        for email in emails:
            split_email_strings = []
            prev_cursor = 0
            cursor = 0
            while email[cursor] != "@":
                if email[cursor] == "+":
                    split_email_strings.append(email[prev_cursor:cursor])
                    while email[cursor] != "@":
                        cursor += 1
                    prev_cursor = cursor
                    break
                elif email[cursor] == ".":
                    split_email_strings.append(email[prev_cursor:cursor])
                    prev_cursor = cursor + 1
                cursor += 1
            split_email_strings.append(email[prev_cursor:cursor])
            split_email_strings.append(email[cursor:])
            valid_emails.add("".join(split_email_strings))

        return len(valid_emails)
