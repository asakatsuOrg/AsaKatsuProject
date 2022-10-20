def numUniqueEmails(emails):
    # !Solution 1
    # res = []
    # for email in emails:
    #     email = email.split("@")    # split into local and domain name
    #     local = email[0].replace(".", "") # period

    #     # plus
    #     local = local.split("+")[0]
    #     finalEmail = local + "@" + email[-1]
    #     if finalEmail not in res:
    #         res.append(finalEmail)

    # !Solution 2
    res = set()
    for email in emails:
        local, domain = email.split("@")
        local = "".join(local.split('+')[0].split('.'))
        email = local +'@' + domain
        res.add(email)

    return len(res)

# email = "alice.z@leetcode.com"
# email = email.replace(".", "")
# print(email)

emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
# emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
print(numUniqueEmails(emails))