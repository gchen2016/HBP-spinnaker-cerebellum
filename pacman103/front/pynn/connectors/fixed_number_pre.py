from pacman103.front.common.randomDistributions import generateParameterArray
from pacman103.front.pynn.connectors.abstract_connector import AbstractConnector
from pacman103.front.common.synapse_row_info import SynapseRowInfo
from pacman103.front.common.synaptic_list import SynapticList

import numpy
import random

class FixedNumberPreConnector( AbstractConnector ):
    """
    Connects a fixed number of pre-synaptic neurons selected at randoom, 
    to all post-synaptic neurons

    :param `int` n_pre:
        number of random pre-synaptic neurons connected to output
    :param `bool` allow_self_connections:
        if the connector is used to connect a
        Population to itself, this flag determines whether a neuron is
        allowed to connect to itself, or only to other neurons in the
        Population.
    :param weights: 
        may either be a float, a !RandomDistribution object, a list/
        1D array with at least as many items as connections to be
        created. Units nA.
    :param delays: 
        If `None`, all synaptic delays will be set
        to the global minimum delay.
    :param `pyNN.Space` space: 
        a Space object, needed if you wish to specify distance-
        dependent weights or delays - not implemented
    """
    def __init__(self, n_pre, weights = 0.0, delays = 1,
                  allow_self_connections = True):
        """
        Creates a new FixedNumberPreConnector
        """
        self.n_pre = int(n_pre)
        self.weights = float(weights)
        self.delays = int(delays)
        self.allow_self_connections = allow_self_connections
        
    def generate_synapse_list(self, prevertex, postvertex, delay_scale, 
            synapse_type):
        id_lists = list()
        weight_lists = list()
        delay_lists = list()
        type_lists = list()
        for _ in range(0, prevertex.atoms):
            id_lists.append(list())
            weight_lists.append(list())
            delay_lists.append(list())
            type_lists.append(list())
        
        pre_synaptic_neurons = random.sample(range(0, prevertex.atoms), 
                self.n_pre)
 
        for pre_atom in pre_synaptic_neurons:
            present = numpy.ones(postvertex.atoms, dtype=numpy.uint32)
            n_present = postvertex.atoms
            
            id_lists[pre_atom] = numpy.where(present)[0]
            weight_lists[pre_atom] = generateParameterArray(self.weights,
                    n_present, present)
            delay_lists[pre_atom] = (generateParameterArray(self.delays,
                    n_present, present) * delay_scale)
            type_lists[pre_atom] = synapse_type
        
        connection_list = [SynapseRowInfo(id_lists[i], weight_lists[i], 
                delay_lists[i], type_lists[i])
                for i in range(0, prevertex.atoms)]
        
        return SynapticList(connection_list)
