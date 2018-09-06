tasks=[
	#
	# Each TASK runs git pull, then executes one or more BUILDS
	# 
	{ 
		# Where to run git pull
		"git_pull_dir":"/root/armdev/bus_pirate_ng/source",
		# This task builds one firmware (NG1)
		"builds":[{ 
			"hardware":"NG1", # Info field. Passed with result for backend reference. Depends on your implementation
			"firmware":"8",	# Info field. Passed with result for backend reference. Depends on your implementation
			"work_dir":"/root/armdev/bus_pirate_ng/source", # Where to execute make command
			"make_command":"make bin",	# make command for this build
			"output_dir":"/root/armdev/bus_pirate_ng/source", # Where to find the compiled firmware
			"output_file":"buspirateNG.bin",	# Name of the firmware output file
			"api_url":"http://", # Where to POST the JSON as a file, your backend
			"api_key":"key" # Info field. Passed with result for backend reference. Depends on your implementation
		}]
	},
	{ 
		# Where to run git pull
		"git_pull_dir":"/root/picdev/Bus_Pirate",
		# This task builds three firmware versions (3/4/5)
		"builds":[{
			"hardware":"3",	# Info field
			"firmware":"8",	# Info field
			"work_dir":"/root/picdev/Bus_Pirate/Firmware/busPirate3X.X",
			"make_command":"make",
			"output_dir":"/root/picdev/Bus_Pirate/Firmware/busPirate3X.X/dist/default/production",
			"output_file":"busPirate3X.X.production.hex",
			"api_url":"http://",
			"api_key":"key" # Info field
		},
		{ 
			"hardware":"4", # Info field
			"firmware":"8",	# Info field
			"work_dir":"/root/picdev/Bus_Pirate/Firmware/busPirate4X.X",
			"make_command":"make",	
			"output_dir":"/root/picdev/Bus_Pirate/Firmware/busPirate4X.X/dist/default/production",
			"output_file":"busPirate4X.X.production.hex",
			"api_url":"http://",
			"api_key":"key" # Info field
		},
		{ 
			"hardware":"5",	# Info field
			"firmware":"8",	# Info field
			"work_dir":"/root/picdev/Bus_Pirate/Firmware/busPirate5X.X",
			"make_command":"make",	
			"output_dir":"/root/picdev/Bus_Pirate/Firmware/busPirate5X.X/dist/default/production",
			"output_file":"busPirate5X.X.production.hex",
			"api_url":"http://",
			"api_key":"key"	# Info field
		}]
	}
]