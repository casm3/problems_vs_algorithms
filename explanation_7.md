# HTTPRouter using a Trie

The same implementation of Trie from previous problem was used here.

So the same complexity applies (O(1) to insert and find) and O(n) to any method that makes uses of the split_path method, since we just create a list of as much as needed directories into that given path.

The Space complexity for the Trie problem is O(n*k), where n is for the nodes that can point to k other nodes. This may surpass the O(m) for the urls list that is created by the split method.
