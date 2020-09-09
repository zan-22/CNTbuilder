CNTbuilder

A python script that can be used to generate carbon nanotubes

How to use:

In interactive terminal, run the script and 

call CNTbuilder(geometry, n, length of tube, C-C bond length)

Geometry can either be "zigzag" or "armchair" (remember quotation marks)

n is an integer where n > 0

Length of tube is the length of the carbon nanotube in Ångstrøm

C-C bond length is the bond length between the carbon atoms in Ångstrøm.

Common C-C bond length is 1.42 Å

The output is written as an .xyz file which has to be present in the same

folder as this script. Currently the output file has to be named zan.xyz

It is recommended to use Avogadro to visualize the Carbon Nanotube or any

other molecular builder/visualizer that supports .xyz format

Script is currently not able to generate chiral nanotubes.

Example: CNTbuilder("armchair", 10, 10, 1.42), where n = 10 and length is 10Å
