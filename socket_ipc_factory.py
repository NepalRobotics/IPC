import sys, socket, os
from socket_ipc_connection import SocketIPCConnection
from endpoints import EndpointType

class SocketIPCFactory(object):
  """
  Generates connections to remote programs.
  """
  _preamble = "HACF"

  def get_connection(self, endpoint):
    """
    Generate a socket connection object

    Args:
      endpoint: the connection type
    :return: a connection object
    """
    #Open socket
    if endpoint.endpoint_type == EndpointType.unix_socket_host:
      socket = self.listen_client(endpoint.address)
    elif endpoint.endpoint_type == EndpointType.unix_socket_client:
      socket = self.connect_server(endpoint.address)
    else:
      raise TypeError
    
    #Encapsulate socket
    return SocketIPCConnection(socket, endpoint.message_class)

  def listen_client(self, address):
    """
    Listen for a client to connect to the address
    
    Args:
      address: the unix domain socket address to bind to
    Returns:
      A bound socket connected to client
    """
    #Create socket
    uds = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    
    #Bind socket
    uds.bind(address)

    uds.listen(1)

    #Wait for valid connection
    while True:
      connection, remote_address = uds.accept()

      #Test connected client
      try:
        data = connection.recv(len(self._preamble))
        if data == self._preamble:
          #Success
          uds.close()
          return connection
      except Exception as e:
        pass
  
  def connect_server(self, address):
    """
    Connect to a listening server

    Args:
      address: the unix domain socket address to bind to
    Returns:
      A bound socket connected to server
    """
    #Create socket
    uds = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

    #Connect to server
    uds.connect(address)

    #Write preamble
    uds.sendall(self._preamble)

    return uds
