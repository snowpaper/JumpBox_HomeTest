# Recursive function to check if a String is palindrome
def reverse(s):
	# return reverse string
	return s[::-1]

def isPalindrome(s):
	# to change it the string is similar case
	s = s.lower()
	# length of s
	l = len(s)

	# In case of even
	if (l % 2) == 0:
		rev = reverse(s)
		if (s == rev):
			return True
		else:
			return False

	# In case of odd
	else:
		str1 = s[0:l//2]
		str2 = reverse(s[l//2+1:])
		if (str1 == str2):
			return True
		else:
			return False

def checkPalindrome(s):
	for str in s:
		if isPalindrome(str):
			print(str," : Palindrome")
		else:
			print(str," : This is not Palindrome")

if __name__ == "__main__":
# uncomment below to show output of Palindrome list.
#	str = ["Anna", "civic", "kayak", "level", "madam", "mom", "noon", "racecar", "radar", "redder", "refer", "repaper", "rotator", "12321", "15651"]
#	checkPalindrome(str)
# Input string to find it is PalinDrome or not.
	str = input("\nInput String : ").split()
	checkPalindrome(str)
