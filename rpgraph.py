

class Node:
    # Initializes a node for a simple graph
    # Gives each node a string ID and a set of neigbors
    # Dictionary adjacency list is not necessary since edges will be unweighted
    # Set gives O(1) time complexity for adding, removing and parsing neighbors
    def __init__(self, node_id: str, neighbors : set = {}):
        self.node_id = node_id
        self.neighbors = neighbors

class MapNode(Node):
    # Expands on basic Node class to include location name and room properties
    def __init__(self, room_id: str, neighbors : set = {}, location_name: str = "Empty Room", properties: dict = {}):
        super().__init__(room_id, neighbors)
        self.name = location_name
        self.properties = properties

    # helper functions:
        # get_name()
        # get_description()
        # get_property(property_name)
        # set_property(property_name, property_value)
        # get_item(item_name)

class QuestNode(Node):
    # Expands on basic Node class to include quest name and quest completion status
    def __init__(self, quest_id: str, successors : set = {}, quest_visible : bool = False, quest_complete :bool = False, quest_name: str = "Empty Quest"):
        super().__init__(quest_id, successors)
        self.quest_visible = quest_visible
        self.quest_complete = quest_complete
        self.quest_name = quest_name

    # helper functions:
        # get_name()
        # get_status()
        # complete_quest()
        # check_visibility()
