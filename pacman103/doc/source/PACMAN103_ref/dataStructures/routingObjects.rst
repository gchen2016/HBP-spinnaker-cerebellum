
Routing Objects
---------------

Routing objects are used to capture the chosen path that is taken by messages
(spikes, temperature values, etc) that pass between cores.

Each subedge represents a path between two computing task, one a producer and
one a consumer of information. These tasks have been allocated to cores by the
*mapper* process and it is the task of the *router* process to select the
route taken from producer to consumer, travelling chip to chip and thereby
generating the *Routing* object.

.. _Routing:

Routing
=======

A *Routing* object is created for each subedge and consists of an ordered list
of *RoutingEntry* objects. Each such *RoutingEntry* therefore refers to one step
on the path, containing information on the specific router it has been assign to
and the key and mask fields for the entry in that router's table.

=================== ===================
  Field                   Value
=================== ===================
  Defined in           lib/lib_map
  Class name           Routing
  Generated by         Router
  Used by              Routing Table Generator
=================== ===================

An instance of the *Routing* class has the following child elements:

=================== ======================== ========================= 
  Element                 Type               Notes
=================== ======================== ========================= 
  subedge           Ref. to subedge          This is the subedge being routed
  routing_entries   List (type RoutingEntry) Order list making up the route
=================== ======================== ========================= 

.. _RoutingEntry:

RoutingEntry 
============

The *Routing* object contains an ordered list of *RouteEntry* objects, which 
are described next.

=================== ===================
  Field                   Value
=================== ===================
  Defined in           lib/lib_map
  Class name           RoutingEntry
  Generated by         Router
  Used by              Routing Table Generator
=================== ===================

An instance of the *RoutingEntry* class has the following child elements:

=================== =========================== ========================= 
  Element                 Type                  Notes
=================== =========================== ========================= 
  router             Ref. to the assigned       With one router per chip
                     router                     this is equivalent to a chip assignment
  key                Routing key for the        Stored in the routing table
                     parent subedge             on the chosen chip
  mask               Required mask for correct  Stored in the routing table
                     routing                    on the chosen chip
  route              ?? Note sure what this
                     does ??
=================== =========================== ========================= 

