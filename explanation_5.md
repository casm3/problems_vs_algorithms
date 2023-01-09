# Autocomplete with Tries

The Trie problem was also well explored by this section.

And the only additional method here was the suffixes.

## TrieNode class

The children that represents the TrieNode will be a hashmap data structure that will have another dictionaries/hashmaps representing other nodes inside it. The overall space complexity will be O(n*k), where n is for the nodes that can point to k other nodes.

The insert method has O(1) time complexity due the fact that we are dealing with a hashmap as basis. A new TrieNode might be created but in the same object so no additional space evaluation needs to be added.

The suffixes method requires **O(nk)** to loop through all nodes. Also we create and extend an suffix list that contains all the given suffixes and will be returned by the method. This list may have **O(g)** space complexity, a list of g-size strings.

## Trie class

A Trie contains TrieNodes with O(n*k) space complexity, and applies to all other methods.

The insert method is O(n) in time complexity, and depends on the word size that we need to loop through all characters. We also check the TrieNode here, but only a reference to the same instantiated previously, so O(1) operation.

The find method is O(1) in time complexity and O(1) in the attributions.
