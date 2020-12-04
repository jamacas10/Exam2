Jebel Macias - Exam 2
Question Minimum Falling Path Sum:
a.	To solve this problem recursively, I broke the problem down into all the possible minimum values that can be produced. I iterate through each index in the array, and determine the minimum value between the current index, current index + index above, current index + index above and behind, and the current index + index above and in front.  
b.	I stored the minimum value provided in each iteration in a 2d array that is the same size as the given array. Future iterations can then determine the minimum value of the sum of the current index + previous minimum value.

Question Palindromic Substrings:
a.	To solve this problem recursively, you must chunk the string into substrings and check if these substrings are palindromes. I had a plan to iterate through the string, and what I would then do is store the current character alone and also append it to characters that had been previously stored, allowing me to create a list of substring. As I would append the current character, I would then check if this substring were palindrome, and if this were true, I would increment a counter. 
b.	I would store all the possible substrings in an array, and store the current counter in a single variable of type int. As I iterate through the given string, the array would grow by one, and every substring in the array would have a character concatenated. Then if the substring is palindrome the counter is incremented by 1.  

Question Maximum Pair of Chains:
a.	For this problem I came up with a similar approach to how I solved palindromic substrings question. I broke the problem down, by checking what pairs could be created during each iteration. Then once the pairs were determined, I could then find which one of the possible chains had the max number of pairs.
b.	Like palindromic strings, I would store the paths in an array. However, a significant difference, was that I was not storing the entirety of the possible paths, but the last path that would continue the chain. I created a Pair node that contained the last path, and the current count of the chain. Furthermore, if the last path of a chain was changed, I would check if the count was greater than the current maximum, and if it was I would set the current maximum to count of the chain.

Question Arithmetic Slices:
a.	To solve this problem recursively, I broke the problem down by checking 3 consecutive sequences and incrementing a counter if consecutive arithmetic sequences are found. The consecutive counter resets when there is no consecutive sequence. Another counter is used to keep track of the consecutive sequences greater than 3.
b.	I stored the consecutive sequences greater than 3 in an integer data type, and then increment the arithmetic counts by the number of consecutive sequences. 

Question Partition K:
a.	To solve this problem recursively, I decided to first determine all the possible sums of the given number, and the possible numbers of the numbers before it. I did this to get all the possible for sums for the given number. I would then check if the 2 numbers were both a perfect square and if this condition were true then the least possible number of perfect squares would be 2. If neither were perfect squares these numbers would be skipped. However, if one of the numbers was not perfect, I would perform the same set of conditions on the non-perfect, by checking all the numbers that summed up to it. I could then use a counter to check how many sums are being added. 
b.	I stored all the possible sums in a dictionary as pair values, and the keys would be the number that all the pairs summed up to. I would store the counter in an integer data type. 

	
