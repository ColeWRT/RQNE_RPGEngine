class Node:
    # Initializes a node for a simple graph
    # Gives each node a string ID and a set of neigbors
    # Dictionary adjacency list is not necessary since edges will be unweighted
    # Set gives O(1) time complexity for adding, removing and parsing neighbors
    def __init__(self, node_id: str, neighbors : set = {}):
        self.node_id = node_id
        self.neighbors = neighbors

    def get_id(self):
        return self.node_id

    def get_neighbors(self):
        return self.neighbors

class MapNode(Node):
    # Expands on basic Node class to include location name and room properties
    def __init__(self, room_id: str, neighbors : set = {}, location_name: str = "Empty Room", properties: dict = {}):
        super().__init__(room_id, neighbors)
        self.name = location_name
        self.properties = properties

    # Helper functions
    def get_name(self): # Get readable name of the location
        return self.name

    def get_description(self): # Get readable description of the location
        return self.properties["description"]

    def get_property(self, property_name: str): # Get the value of a specific property of the location, if it exists
        return self.properties.get(property_name, None)

    def set_property(self, property_name: str, property_value): # Set the value of a specific property of the location, if it exists
        if property_name in self.properties.keys():
            self.properties[property_name] = property_value
            return property_value
        return None

    def get_item(self, item_name: str): # Pull an item from the location's inventory, if it exists
        if item_name in self.properties.get("items", {}):
            self.properties["items"].remove(item_name)
            return item_name
        return None

class QuestNode(Node):
    # Expands on basic Node class to include quest name and quest completion status
    def __init__(self, quest_id: str, successors : set = {}, quest_visible : bool = False, quest_complete :bool = False, quest_name: str = "Empty Quest"):
        super().__init__(quest_id, successors)
        self.quest_visible = quest_visible
        self.quest_complete = quest_complete
        self.quest_name = quest_name

    # Helper functions
    def get_name(self): # Get readable name of the quest
        return self.quest_name

    def get_status(self): # Get the completion status of the quest
        return self.quest_complete

    def complete_quest(self): # Mark the quest as complete
        self.quest_complete = True

    def calculate_visibility(self, completed_quests : set = {}): # Determine if a quest should be marked as visible
        for quest in self.neighbors:
            if quest not in completed_quests:
                self.quest_visible = False
                return
        self.quest_visible = True
        
    def check_visibility(self): # Check if the quest is visible to the player
        return self.quest_visible

class MapGraph:
    pass
    # can read from a json file to create a graph of MapNodes

class QuestGraph:
    pass
    # can read from a json file to create a graph of QuestNodes
