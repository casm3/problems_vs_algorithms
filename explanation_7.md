# HTTPRouter using a Trie

The same implementation of Trie from previous problem was used here.

## RouteTrieNode class

The children that represents the RouteTrieNode will be a hashmap data structure that will have another dictionaries/hashmaps representing other nodes inside it. The overall space complexity will be O(n*k), where n is for the nodes that can point to k other nodes.

The insert method has O(1) time complexity due the fact that we are dealing with a hashmap as basis. A new RouteTrieNode might be created but in the same object so no additional space evaluation needs to be added.

## RouteTrie class

The insert method has O(n) time complexity due the fact that we are dealing with a list of strings.

The find method is also O(n) in time complexity. Same list of strings must be traversed.

Both insert and find method we may refer to the object, so no more than O(1) space complexity.

## Router

In both add_handler and lookup methods we create the urls list by using the split_path method, so add_handler and lookup are both O(n) in space complexity and O(n) in time complexity since they use the find method from RouteTrie class.

Finally the split_path method is O(n) in time complexity, we take a lot of time to split a bigger string to be returned by the method. Since we are dealing direct with the return here we do not need any additional variable so O(1) in space complexity.
