Social Network Connectivity Problem
===================================
Given a social network containing n members and a log file containing m 
timestamps at which times pairs of members formed friendships, design an 
algorithm to determine the earliest time at which all members are connected 
(i.e., every member is a friend of a friend of a friend ... of a friend). 

Assume that the log file is sorted by timestamp and that friendship is an 
equivalence relation. The running time of your algorithm should be O(m*log(n)) 
or better and use extra space proportional to O(n).

Solution
---------
1. connect m[i].friend_1 with m[i].friend_2
2. update max_tree_size list which keeps track of the largest tree in the graph
3. if max_tree_size() equals n, then return m[0].time, else continue looping through m.

this algorithm takes m iterations at worst with log(n) work in each iteration, 
therefore O(m*log(n))