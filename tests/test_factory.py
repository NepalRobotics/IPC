#!/usr/bin/python
import socket_ipc_factory, endpoints, threading, time, unittest

class TestIPCFactory(unittest.TestCase):
  
  def test_radio_belief(self):

    class CompletedCount(object):
      def __init__(self):
        self.count = 0
        self._lock = threading.Lock()
      def incr(self):
        self._lock.acquire(True)
        self.count += 1
        self._lock.release()

    completed_count = CompletedCount()

    def radio():
      print "Created radio"
      factory = socket_ipc_factory
      print "Created factory"
      connection = factory.get_connection(endpoints.BeliefFromRadio)
      print "Radio connected"
      connection._socket.send("TestMessage")
      connection.close()
      completed_count.incr()
  
    def belief():
      print "Created belief"
      connection = socket_ipc_factory.get_connection(endpoints.RadioFromBelief())
      print "Belief connected"
      data = connection._socket.recv(len("TestMessage"))
      print data
      connection.close()
      completed_count.incr()
  
    rad = threading.Thread(target=radio)
    bel = threading.Thread(target=belief)
  
    print "Starting threads"
    rad.start()
    bel.start()
    rad.join()
    bel.join()
    self.assertEqual(2, completed_count.count, "Not all threads completed properly")
