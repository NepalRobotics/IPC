import sys, socket, os
from socket_ipc_connection import SocketIPCConnection
from endpoints import EndpointType

"""
Generates connections to remote programs.
"""
_preamble = "HACF"

def get_connection(endpoint):
  """
  Generate a socket connection object

  Args:
    endpoint: the connection type
  Returns: 
    A connection object
  """
  #Open socket
  if endpoint.endpoint_type == EndpointType.unix_socket_host:
    socket = listen_client(endpoint.address)
  elif endpoint.endpoint_type == EndpointType.unix_socket_client:
    socket = connect_server(endpoint.address)
  else:
    raise TypeError
  
  #Encapsulate socket
  return SocketIPCConnection(socket, endpoint.message_class)

def listen_client(address):
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
      data = connection.recv(len(_preamble))
      if data == _preamble:
        #Success
        uds.close()
        return connection
    except Exception as e:
      pass

def connect_server(address):
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
  uds.sendall(_preamble)

  return uds
