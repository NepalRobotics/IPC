import socket_ipc_factory, endpoints, threading, time, unittest

class TestIPCFactory(unittest.TestCase):
  
  def test_radio_belief(self):
    #TODO: add docstring comment
    class CompletedCount(object):
      def __init__(self):
        self.count = 0
        self._lock = threading.Lock()
      def incr(self):
        self._lock.acquire(True)
        self.count += 1
        self._lock.release()

    completed_count = CompletedCount()

    test_message = "TestMessage"

    def radio():
      factory = socket_ipc_factory
      connection = factory.get_connection(endpoints.BeliefFromRadio)
      connection._socket.send(test_message)
      connection.close()
      completed_count.incr()
  
    def belief():
      connection = socket_ipc_factory.get_connection(endpoints.RadioFromBelief())
      data = connection._socket.recv(len("TestMessage"))
      self.assertEqual(data, test_message, "Test message corrupted")
      connection.close()
      completed_count.incr()
  
    rad = threading.Thread(target=radio)
    bel = threading.Thread(target=belief)
  
    print "Starting threads"
    rad.start()
    time.sleep(1)
    bel.start()
    rad.join()
    bel.join()
    self.assertEqual(2, completed_count.count, "Not all threads completed properly")
    print "Done"
