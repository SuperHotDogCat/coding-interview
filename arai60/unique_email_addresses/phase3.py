class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        for email in emails:
            local_name, domain_name = email.rsplit("@", maxsplit = 1)
            local_name = local_name.replace(".", "")
            local_name = local_name.split("+")[0]
            unique_emails.add(f"{local_name}@{domain_name}")
        return len(unique_emails)
