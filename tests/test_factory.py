#!/usr/bin/python
import socket_ipc_factory, endpoints, threading, time, unittest

class TestIPCFactory(unittest.TestCase):
  
  def test_radio_belief(self):

    completed_threads = 0
    completed_threads_lock = threading.Lock()

    def incr_completed():
      completed_threads_lock.acquire(blocking=True)
      completed_threads += 1
      completed_threads_lock.release()

    def radio():
      print "Created radio"
      factory = socket_ipc_factory
      print "Created factory"
      connection = factory.get_connection(endpoints.BeliefFromRadio)
      print "Radio connected"
      connection._socket.send("TestMessage")
      incr_completed()
  
    def belief():
      print "Created belief"
      connection = socket_ipc_factory.get_connection(endpoints.RadioFromBelief())
      print "Belief connected"
      data = connection._socket.recv(len("TestMessage"))
      print data
      incr_completed()
  
    rad = threading.Thread(target=radio)
    bel = threading.Thread(target=belief)
  
    print "Starting threads"
    rad.start()
    bel.start()
    rad.join()
    bel.join()
    self.assertEqual(2, completed_threads, "Not all threads completed properly")
