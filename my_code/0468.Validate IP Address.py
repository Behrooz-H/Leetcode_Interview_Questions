"""
Given a string queryIP, return "IPv4" if IP is a valid IPv4 address, "IPv6" if IP is a valid IPv6 address or "Neither" if IP is not a correct IP of any type.

A valid IPv4 address is an IP in the form "x1.x2.x3.x4" where 0 <= xi <= 255 and xi cannot contain leading zeros.
For example, "192.168.1.1" and "192.168.1.0" are valid IPv4 addresses while "192.168.01.1", "192.168.1.00", and "192.168@1.1" are invalid IPv4 addresses.

A valid IPv6 address is an IP in the form "x1:x2:x3:x4:x5:x6:x7:x8" where:

1 <= xi.length <= 4
xi is a hexadecimal string which may contain digits, lowercase English letter ('a' to 'f') and upper-case English letters ('A' to 'F').
Leading zeros are allowed in xi.
For example, "2001:0db8:85a3:0000:0000:8a2e:0370:7334" and "2001:db8:85a3:0:0:8A2E:0370:7334" are valid IPv6 addresses,
 while "2001:0db8:85a3::8A2E:037j:7334" and "02001:0db8:85a3:0000:0000:8a2e:0370:7334" are invalid IPv6 addresses.
"""

class Solution:
    def validateIPv4(self, IP):
        nums = IP.split(".")
        for x in nums:
            # Validate integer in range (0, 255):
            # 1. length of chunk is between 1 and 3
            if len(x) == 0 or len(x) > 3:
                return "Neither"
            # 2. no extra leading zeros
            if x[0] == "0" and len(x) != 1:
                return "Neither"
            # 3. only digits are allowed
            if not x.isdigit():
                return "Neither"
            # 4. less than or equal to 255
            if int(x) > 255:
                return "Neither"
        return "IPv4"

    def validateIPv6(self, IP):
        nums = IP.split(":")
        hexdigits = "0123456789abcdefABCDEF"
        for x in nums:
            # Validate hexadecimal in range (0, 2**16):
            # 1. at least one and not more than 4 hexsigits in one chunk
            if len(x) == 0 or len(x) > 4:
                return "Neither"
            # 2. only hexdigits are allowed: 0-9, a-f, A-F
            for ch in x:
                if ch not in hexdigits:
                    return "Neither"
        return "IPv6"

    def validIPAddress(self, IP):
        if IP.count(".") == 3:
            return self.validateIPv4(IP)
        elif IP.count(":") == 7:
            return self.validateIPv6(IP)
        else:
            return "Neither"



"""
Time complexity: O(N) because to count number of dots requires to
parse the entire input string.

Space complexity: O(1)."""