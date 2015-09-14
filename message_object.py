import json
class MessageObject(object):
    """
    Class representing an IPC message
    """
    def __init__(self):
        """
        Construct a new MessageObject object.

        :return:
        """
    def encode(self):
        """
        Create an encoded version of self
        :return: Returns encoded self
        """
        return json.dumps(self.__dict__)

class VehicleState(MessageObject):
    """
    Encodable UAV craft state information
    """
    #TODO: implment
    pass

class RadioState(MessageObject):
    """
    Encodable Doppler Radio signal state information
    """
    #TODO: implement
    pass

class LogEvent(MessageObject):
    """
    Encodable information for recording to system log
    """
    #TODO: implement
    pass

class BeliefUpdateSquare(MessageObject):
    """
    Encodable belief state for an area
    """
    def __init__(self, lat_min, lat_max, lon_min, lon_max, confidence):
        """
        Creates a new 'BeliefUpdateSquare' object

        :param lat_min: The minimum latitude of the grid
        :param lat_max: The maximum latitude of the grid
        :param lon_min: The minimum longitude of the grid
        :param lon_max: The maximum longitude of the grid
        :param confidence: The confidence of a signal source being in the   
            square
        :return: returns nothing
        """
        self.lat_min = lat_min
        self.lat_max = lat_max
        self.lon_min = lon_min
        self.lon_max = lon_max
        self.confidence = confidence

class BeliefUpdate(MessageObject):
    """
    Encodable change in belief state
    """
    def __init__(self, belief_squares):
        """
        Creates a new instance of object.

        :param belief_squares: An array of belief square objects
        :return: returns nothing
        """
    def encode(self):
        """
        Returns an encoded version of self
        """
        #TODO: implement

class BeliefGridRequest(MessageObject):
    """
    Message requesting a belief grid
    Forces a BeliefUpdate to be sent for the specified area, with
        the maximum specified resolution
    """
    def __init__(self, lat_min, lat_max, lon_min, lon_max, num_squares):
        """
        Creates a new 'BeliefGridRequest' object

        :param lat_min: The minimum latitude of the grid
        :param lat_max: The maximum latitude of the grid
        :param lon_min: The minimum longitude of the grid
        :param lon_max: The maximum longitude of the grid
        :param num_square: The number of grid squares to create
        :return: returns nothing
        """
        self.lat_min = lat_min
        self.lat_max = lat_max
        self.lon_min = lon_min
        self.lon_max = lon_max
        self.num_squares = num_squares
