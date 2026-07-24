class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        chars = {c:[] for w in words for c in w} # making the graph for topological sort
        visited = {} # keeping track of 3 states, does not exist, true for in current path and false for visited but not in current path
        res = [] # keeps track of the result

        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1] #geting both words
            minlen = min(len(w1), len(w2))
            if(len(w1)>len(w2) and w1[:minlen]==w2[:minlen]): # if the first 2 words have the same prefix and the 1st word is longer return nothing as it says in the text
                return ""
            for i in range(minlen):
                if(w1[i] != w2[i]): #the first differing character is the lexigraphical order therefore append this to the character in w1 as this character in word 1 is greater than that same index of character in word 2
                    chars[w1[i]].append(w2[i])
                    break #break as only need to look at the first differnce
        
        def dfs(c):
            if(c in visited): # if the character has been visited then it has already been traversed, however we are looking at 2 states here
                return visited[c] # has the character been visited before then false but if is also in the current path then true and this means we hava a cycle so therefore the lanaguage is invalid
            visited[c] = True # originally will be in the path so set the visited to true to indicate this

            for nei in chars[c]: # looping through all the neighbors as one does in dfs
                if(dfs(nei)): # this will happen in the instance that there is cycle therfore the character has been visited before an in the path so return true, otherwise do nothing
                    return True
            visited[c] = False #once all neighbors have been traversed one should now set this to false indicating it has been visited but is now no longer in the current path
            res.append(c) # this is a post order traversal to get the correct order of characters in reverse

        for c in chars.keys(): # can start from anywhere so loop thorugh all possible characters as also could have a completely disconnected graph
            if(dfs(c)): # if a cycle exist will return true and therefore returns the empty string
                return ""
        
        return "".join(res[::-1]) #reverse the result as the original result was given in reverse order


        