from collections import defaultdict


# Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        # Initialize this node in the Trie
        self.is_word: bool = False
        self.children: dict = defaultdict(TrieNode)

    def insert(self, char):
        # Add a child node in this Trie
        if char not in self.children:
            self.children[char] = TrieNode()

    def suffixes(self, suffix=""):
        # Recursive function that collects the suffix for
        # all complete words below this point
        suffix_list: list = []

        if self.is_word and suffix:
            suffix_list.append(suffix)

        if not self.children:
            return suffix_list

        for char in self.children:
            suffix_list += self.children[char].suffixes(suffix + char)
        return suffix_list


class Trie:
    def __init__(self):
        # Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        # Add a word to the Trie
        current_node = self.root

        for char in word:
            current_node.insert(char)
            current_node = current_node.children[char]

        current_node.is_word = True

    def find(self, prefix):
        # Find the Trie node that represents this prefix
        current_node = self.root

        if not prefix:
            return False

        for char in prefix:
            if char not in current_node.children:
                return False

            current_node = current_node.children[char]

        return current_node


MyTrie = Trie()
wordList = [
    "ant",
    "anthology",
    "antagonist",
    "antonym",
    "fun",
    "function",
    "factory",
    "trie",
    "trigger",
    "trigonometry",
    "tripod",
]
for word in wordList:
    MyTrie.insert(word)


MyTrie = Trie()
wordList = ["the", "a", "there", "answer", "any", "by", "their"]
for word in wordList:
    MyTrie.insert(word)


def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            return '\n'.join(prefixNode.suffixes())
        else:
            return prefix + " not found" if prefix else "not found"
    else:
        return ''


print(f(prefix='t'))
print('----------------------')
print(f(prefix='a'))
print('----------------------')
print(f(prefix='b'))
print('----------------------')
print(f(prefix=''))
print('----------------------')
print(f(prefix=None))
print('----------------------')
