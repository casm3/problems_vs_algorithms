from collections import defaultdict


# A RouteTrieNode will be similar to our autocomplete TrieNode...
# with one additional element, a handler.
class RouteTrieNode:
    def __init__(self):
        # Initialize the node with children as before, plus a handler
        self.children = defaultdict(RouteTrieNode)
        self.handler = None

    def insert(self, url: str):
        # Insert the node as before
        if url not in self.children:
            self.children[url] = RouteTrieNode()


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler):
        # Initialize the trie with an root node and a handler,
        # this is the root path or home page node
        self.root = RouteTrieNode()
        self.handler = handler

    def insert(self, urls: list[str], handler):
        # Similar to our previous example you will want to
        # recursively add nodes
        # Make sure you assign the handler to only
        # the leaf (deepest) node of this path
        current_node = self.root

        for url in urls:
            current_node.insert(url)
            current_node = current_node.children[url]
        current_node.handler = handler

    def find(self, urls: str):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current_node = self.root

        for url in urls:
            if url not in current_node.children:
                return
            current_node = current_node.children[url]

        return current_node.handler


# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, handler, not_found_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page
        # not found responses as well!
        self.route_trie = RouteTrie(handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        urls = self.split_path(path)
        self.route_trie.insert(urls, handler)

    def lookup(self, path: str):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        urls = self.split_path(path)

        if not urls:
            return self.route_trie.handler

        return (
            self.route_trie.find(urls)
            if self.route_trie.find(urls)
            else self.not_found_handler
        )

    def split_path(self, path: str):
        # you need to split the path into parts for
        # both the add_handler and lookup functions,
        # so it should be placed in a function here
        return [part for part in path.split("/") if part]


# Here are some test cases and expected outputs
# you can use to test your implementation

# create the router and add a route
# remove the 'not found handler' if you did not implement this
router = Router("root handler", "not found handler")
# add a route
router.add_handler("/home/about", "about handler")

# some lookups with the expected output
# should print 'root handler'
print(router.lookup("/"))
# should print 'not found handler' or None if you did not implement one
print(router.lookup("/home"))
# should print 'about handler'
print(router.lookup("/home/about"))
# should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/"))
# should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about/me"))
