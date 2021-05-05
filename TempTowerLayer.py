# -*- coding: utf-8 -*-

import json
import re

from ..Script import Script


class TempTowerLayer(Script):
    def __init__(self):
        super().__init__()

    def getSettingDataString(self):
        return json.dumps({
            'name': 'Temp Tower Layer',
            'key': 'TempTowerLayer',
            'metadata': {},
            'version': 2,
            'settings': {
                'debug_output': {
                    'label': 'Debug Output',
                    'description': 'Set true for debug output enabled',
                    'type': 'bool',
                    'default_value': True
                },
                'start_temperature': {
                    'label': 'Start Temperature',
                    'description': 'Initial nozzle temperature',
                    'unit': '°C',
                    'type': 'int',
                    'default_value': 190
                },
                'layer_increment': {
                    'label': 'Layer Increment',
                    'description': (
                        'Adjust temperature each time layer number'
                        'changes by this much'
                    ),
                    'unit': 'layer',
                    'type': 'int',
                    'default_value': 50
                },
                'temperature_increment': {
                    'label': 'Temperature Increment',
                    'description': (
                        'Increase temperature by this much with each layer increment. '
                        'Use negative values for towers that become gradually cooler.'
                    ),
                    'unit': '°C',
                    'type': 'int',
                    'default_value': 5
                },
                'start_layer': {
                    'label': 'Start Layer ',
                    'description': (
                        'Start the temperature tower at this Layer.'
                    ),
                    'unit': 'layer',
                    'type': 'int',
                    'default_value': 5
                }
            }
        })

    def execute(self, data):
        start_temp = self.getSettingValueByKey('start_temperature')
        layer_inc = self.getSettingValueByKey('layer_increment')
        temp_inc = self.getSettingValueByKey('temperature_increment')
        start_layer = self.getSettingValueByKey('start_layer')
        debug_output = self.getSettingValueByKey('debug_output')

        # Set initial state
        current_temp = 0
        extra_layer = 0
        max_layer = 0

		"""
        for i, layer in enumerate(data):
            lines = layer.split('\n')
            for j, line in enumerate(lines):
                if line.startswith(";LAYER_COUNT:"):
                    max_layer = line
                    max_layer = max_layer.split(":")[1]
                if line.startswith(";LAYER:"):
                    current_layer = line
                    current_layer = current_layer.split(":")[1]

                if current_layer >= final_layer:
                    if debug_output:
                        lines[j] += '\n;Final Layer %d is reached, no temp increase at the end' % current_layer
                elif current_layer < start_layer:
                    if debug_output:
                        lines[j] += '\n;Layer %d is below minimum' % current_layer
                elif current_layer == start_layer:
                    current_temp = start_temp
                    if debug_output:
                        lines[j] += '\n;Start Layer %d reached' % current_layer
                elif current_layer > start_layer:
                    if debug_output:
                        lines[j] += '\n;Layer %d reached' % current_layer
                        extra_layer += 1
                    if extra_layer == layer_inc:
                        extra_layer = 0
                        new_temp = current_temp + temp_inc
                        if debug_output:
                            lines[j] += '\n;Target Layer %d reached' % current_layer
                            lines[j] += '\n;Calculated temp is %d' % new_temp
                else:
                    if debug_output:
                        lines[j] += '\n;Something wrong'

                if new_temp != current_temp:
                    current_temp = new_temp
                    lines[j] += '\n;TYPE:CUSTOM\nM104 S%d' % new_temp

            data[i] = '\n'.join(lines)
		"""
			
		for i, line in enumerate(data):
		
			
		
			lines = [line]
      
			if line.startswith(";LAYER_COUNT:"):
				max_layer = line
				max_layer = max_layer.split(":")[1]
				
			if line.startswith(";LAYER:"):
				current_layer = line
				current_layer = current_layer.split(":")[1]

			if current_layer >= final_layer:
				if debug_output:
					lines[j] += '\n;Final Layer %d is reached, no temp increase at the end' % current_layer
			elif current_layer < start_layer:
				if debug_output:
					lines[j] += '\n;Layer %d is below minimum' % current_layer
			elif current_layer == start_layer:
				current_temp = start_temp
				if debug_output:
					lines[j] += '\n;Start Layer %d reached' % current_layer
			elif current_layer > start_layer:
				if debug_output:
					lines[j] += '\n;Layer %d reached' % current_layer
					extra_layer += 1
				if extra_layer == layer_inc:
					extra_layer = 0
					new_temp = current_temp + temp_inc
					if debug_output:
						lines[j] += '\n;Target Layer %d reached' % current_layer
						lines[j] += '\n;Calculated temp is %d' % new_temp
			else:
				if debug_output:
					lines[j] += '\n;Something wrong'

			if new_temp != current_temp:
				current_temp = new_temp
				lines[j] += '\n;TYPE:CUSTOM\nM104 S%d' % new_temp

            data[i] = '\n'.join(lines)
			
        return data
