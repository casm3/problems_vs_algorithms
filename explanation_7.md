# HTTPRouter using a Trie

The same implementation of Trie from previous problem was used here.

So the same complexity applies (O(1) to insert and find) and O(n) to any method that makes uses of the split_path method, since we just create a list of as much as needed directories into that given path.
