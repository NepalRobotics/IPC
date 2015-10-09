import message_object

class EndpointType(object):
    """
    Indicates what type of endpoint we are connecting to
    """
    unix_socket_host = 0
    unix_socket_client = 1

class Endpoint(object):
  """
  Represents a connection to bind to
  """
  address = None
  endpoint_type = None
  message_class = None

class _RadioAndBelief(Endpoint):
  """
  Superclass for radio-belief system IPC
  """
  address = "/tmp/radio_belief"
  message_class = message_object.RadioState

class BeliefFromRadio(_RadioAndBelief):
  """
  Called by Radio to get to Belief
  """
  endpoint_type = EndpointType.unix_socket_host

class RadioFromBelief(_RadioAndBelief):
  """
  Called by Belief process to get to Radio process
  """
  endpoint_type = EndpointType.unix_socket_client
