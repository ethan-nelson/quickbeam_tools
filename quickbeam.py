# -*- coding: utf-8 -*-
# MIT License (c) 2015 Ethan Nelson 

def read(filename, **kwargs):
	"""
	A QuickBeam reader.

	Input
	-----
	filename: a QuickBeam hdf5 file

	Optional arguments
	------------------
	**kwargs: include only the variable of interest (tba)

	"""
	import numpy as np
	import struct

	ref = {}

	file = open(filename, 'rb')
	ref['filename'] = file.read(200)
	ref['title'] = file.read(100)
	ref['sensor'] = file.read(20)
	ref['freq'] = struct.unpack( "f", file.read(4) )[0]
	ref['year'] = struct.unpack( "hxx", file.read(4) )[0]
	ref['month'] = struct.unpack( "hxx", file.read(4) )[0]
	ref['day'] = struct.unpack( "hxx", file.read(4) )[0]
	ref['hour'] = struct.unpack( "hxx", file.read(4) )[0]
	ref['minute'] = struct.unpack( "hxx", file.read(4) )[0]
	ref['second'] = struct.unpack( "hxx", file.read(4) )[0]
	ref['nx'] = struct.unpack( "hxx", file.read(4) )[0]
	ref['ny'] = struct.unpack( "hxx", file.read(4) )[0]
	ref['deltax'] = struct.unpack( "f", file.read(4) )[0]
	ref['deltay'] = struct.unpack( "f", file.read(4) )[0]
	ref['nhgt'] = struct.unpack( "hxx", file.read(4) )[0]

	grid1d = ref['nhgt']
	grid2d = ref['ny'] * ref['nx']
	grid3d = ref['nhgt'] * ref['ny'] * ref['nx']

	shape1d = [ ref['nhgt'] ]
	shape2d = [ ref['ny'], ref['nx'] ]
	shape3d = [ ref['nhgt'], ref['ny'], ref['nx'] ]

	ref['hgt'] = np.reshape( \
				struct.unpack( str(grid1d)+"f", file.read(4*grid1d) ), \
				shape1d )
	ref['lat'] = np.reshape( \
				struct.unpack( str(grid2d)+"f", file.read(4*grid2d) ), \
				shape2d )
	ref['lon'] = np.reshape( \
				struct.unpack( str(grid2d)+"f", file.read(4*grid2d) ), \
				shape2d )
	ref['sfcrain'] = np.reshape( \
				struct.unpack( str(grid2d)+"f", file.read(4*grid2d) ), \
				shape2d )
	ref['tempk'] = np.reshape( \
				struct.unpack( str(grid3d)+"f", file.read(4*grid3d) ), \
				shape3d )
	ref['Z_eff'] = np.reshape( \
				struct.unpack( str(grid3d)+"f", file.read(4*grid3d) ), \
				shape3d )
	ref['Z_ray'] = np.reshape( \
				struct.unpack( str(grid3d)+"f", file.read(4*grid3d) ), \
				shape3d )
	ref['h_atten'] = np.reshape( \
				struct.unpack( str(grid3d)+"f", file.read(4*grid3d) ), \
				shape3d )
	ref['g_atten'] = np.reshape( \
				struct.unpack( str(grid3d)+"f", file.read(4*grid3d) ), \
				shape3d )
	ref['Z_cor'] = np.reshape( \
				struct.unpack( str(grid3d)+"f", file.read(4*grid3d) ), \
				shape3d )

	file.close()

	return ref
