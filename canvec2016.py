"""
OGR2OSM translation for Canvec 2016 road network data.
See the metadata description at http://ftp.geogratis.gc.ca/pub/nrcan_rncan/vector/canvec/doc/CanVec_Catalogue_50K_Transport/SRDB_EXPL_ESSIM_50K_Transport-sd-en.html#div-1330009
"""

def roadClassLookup(roadclass_identifier):
	tags = {}
	if type(roadclass_identifier) is not int:
		print('not an int')
		return tags
	if roadclass_identifier == 20:
		# Not Identified
		# Unknown, not listed, not applicable or impossible to determine.
		tags['highway'] == 'road'
	elif roadclass_identifier == 307:
		# Alleyway-Lane
		# A low-speed thoroughfare dedicated to provide access to the rear of properties.
		tags['highway'] = 'service'
		tags['service'] = 'alley'
	elif roadclass_identifier == 308:
		# Arterial
		# A major thoroughfare with medium to large traffic capacity.
		tags['highway'] = 'primary'
	elif roadclass_identifier == 309:
		# Collector
		# A minor thoroughfare mainly used to access properties and to feed traffic with right of way.
		tags['highway'] = 'secondary'
	elif roadclass_identifier == 310:
		# Expressway-Highway
		# A high-speed thoroughfare with a combination of controlled access intersections at any grade.
		tags['highway'] = 'trunk'
	elif roadclass_identifier == 311:
		# Freeway
		# An unimpeded, high-speed controlled access thoroughfare for through traffic with typically no at-grade intersections, usually with no property access or direct access, and which is accessed by a ramp. Pedestrians are prohibited.
		tags['highway'] = 'motorway'
	elif roadclass_identifier == 312:
		# Local-Strata
		# A low-speed thoroughfare dedicated to provide access to properties with potential public restriction such as: trailer parks, First Nations, strata, private estates, seasonal residences.
		tags['highway'] = 'residential'
		tags['access'] = 'private'
	elif roadclass_identifier == 313:
		# Local-Street
		# A low-speed thoroughfare dedicated to provide full access to the front of properties.
		tags['highway'] = 'residential'
	elif roadclass_identifier == 314:
		# Local-Unknown	
		# A low-speed thoroughfare dedicated to provide access to the front of properties but for which the access regulations are unknown.
		tags['highway'] = 'residential'
		tags['fixme'] = 'access restrictions unknown' # IS THAT AN ACCEPTED VALUE FOR ACCESS?
	elif roadclass_identifier == 315:
		# Ramp
		# A system of interconnecting roadways providing for the controlled movement between two or more roadways.
		tags['highway'] = 'motorway_link' # THERE IS ONLY ONE RAMP CLASS IN CANVEC, THIS PROBABLY NEEDS CLEANUP AFTER
	elif roadclass_identifier == 316:
		# Rapid Transit
		# A thoroughfare restricted to public transit buses.
		tags['highway'] = 'unclassified'
		tags['access'] = 'no'
		tags['bus'] = 'yes'
	elif roadclass_identifier == 317:
		# Resource-Recreation Cart Track
		# Définition à venir
		tags['highway'] = 'raceway'
		tags['sport'] = 'karting'
	elif roadclass_identifier in [318, 319, 320]:
		# Resource-Recreation Dry Weather
		# Définition à venir
		tags['highway'] = 'raceway'
	elif roadclass_identifier == 312:
		# Service Lane
		# A stretch of road permitting vehicles to come to a stop along a freeway or highway. Scale, service lane, emergency lane, lookout, and rest area.
		tags['highway'] = 'service'
	else:
		tags['highway'] = 'unclassified'
	return tags


def filterTags(attrs):
	if not attrs: return

	tags = {}
	
	#Add the source
	tags.update({'source':'CANVEC2016'})
	if 'numlanes' in attrs:
		tags.update({'lanes': attrs['numlanes']}) 
	if 'rdsegnamen' in attrs:
		tags.update({'name': attrs.get('rdsegnamen')})
	if 'rdsefnamfr' in attrs: 	 
		tags.update({'name:fr': attrs.get('rdsegnamfr')})
	if 'rdcls' in attrs:
		tags.update(roadClassLookup(int(attrs.get('rdcls'))))  

	return tags
