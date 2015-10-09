import socket
class SocketIPCConnection(object):
  """
  Socket connection object, returned by IPC factory clas. Subclasses will be
  specific to the connection target
  """
  def __init__(self, socket, message_object_class):
    """
    Construct a new 'SocketIPCConnection' object.

    :param socket: An open socket to the remote host
    :return: returns nothing
    """
    self._socket = socket
    self._message_object_class = message_object_class

  def is_open(self):
    """
    Check whether the socket is still open.

    :return: a boolean indicating whether the socket is open
    """
    return self._socket != None

  def close(self):
    """
    Close an open socket.

    :return: returns nothing
    """
    self._socket.close()
    self._socket = None

  def read_next(self):
    """
    Read the next element in the socket.

    This is a blocking call.

    :return: the next element in the stream
    """

    #TODO: implement
    return None

  def read_front(self):
    """
    Read the latest element in the socket.

    If an element is partially-written, then this function will block.

    :return: the element at the head of the stream
    """

    #TODO: implmenet
    return None

  def write(message_object):
    """
    Write an element to the socket.

    :param message_object: A data structure for transmission
    :return: returns nothing
    """
    #TODO: implement
    return None
