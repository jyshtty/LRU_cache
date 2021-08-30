class LRUCache:
    
    ##### STEP 1: Initialization of the LRUCache class
    # We will have 2 dictionaries for this implementation
    # Use of each of them is provided below
    
    def __init__(self, capacity: int):
        self.capacity = capacity        # Store the capacity of the cache
        self.cache = {}                 # The actual cache as dictionary
        self.timestamp = {}             # A dictionary to store the recency of usage of various keys in the cache
    
    
    
    ##### STEP 2: This is used to get the element from the Cache. Basically it checks if the 'key' exists 
    # and returns -1 if it does not. If the key exists, it updates the 'timestamp' dictionary with a timestamp
    # saying that a particular 'key' was used
    
    def get(self, key: int) -> int:
        if self.cache.get(key,-1)!=-1:
            self.timestamp[key] = datetime.datetime.now()  # 'timestamp' dictionary is updated for the key with the current time
        
        return self.cache.get(key,-1) # Value is returned. If no value exists that -1 is returned
        
    
    ##### STEP 3: This is used to put value into the cache. It works on 3 conditions:
    # 1. It checks if the key exists. If yes, it replaces it and updates the timestamp dictionary for that key
    
    # 2. If no key exists and the number of keys in the dictionary 'cache' is less than capacity value, 
    # it just adds the new key:value pair and adds 'key' to timestamp as it was the latest one that was used
    
    # 3. If number of keys in cache = capacity value, it finds the oldest key that was used using the timestamp
    # dictionary and pops it out. The oldest key would be the one with the oldest timestamp value as we always
    # update timestamp dictionary with latest time everytime a key is used.

    def put(self, key: int, value: int) -> None:
        
        # Getting the value for the 'key'
        keycheck = self.get(key)
        
        ## First condition of STEP 3
        if keycheck!=-1:
            self.cache[key]=value
            self.timestamp[key] = datetime.datetime.now()
            
        ## Second condition of STEP 3
        elif keycheck==-1 and len(list(self.cache.keys()))<self.capacity:
            self.cache[key]=value
            self.timestamp[key] = datetime.datetime.now()
        
        ## Third Condition of STEP 3
        elif keycheck==-1 and len(list(self.cache.keys()))==self.capacity:
            
            ## NOTE: The oldestkey formula can be replaced by the following:
            # min(self.timestamp.keys(), key = lambda x: self.timestamp.get(x)), But for some reason leetcode
            # takes more time for this and times out. so, I used the one below. 
            oldestkey = min(self.timestamp, key=self.timestamp.get)
            self.cache.pop(oldestkey)
            self.timestamp.pop(oldestkey)
            self.cache[key] = value
            self.timestamp[key] = datetime.datetime.now()
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
