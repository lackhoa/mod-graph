from graphviz import Digraph
import os

NUM = 123
NAME = 'mod_'+str(NUM)

mod = Digraph(NAME)
mod.background = 'black'
#Phase one: render the main mod using 'circo' engine
mod.node('0', style='filled')
for i in range(NUM):
    mod.edge(str(i), str((i+1) % NUM), color='blue')

#Save the result of the graphviz rendering command to the file 'mod.gv'
mod.engine='circo'
mod.format='gv'
mod.render(NAME)

#Phase One point Five: Do some processing to extract the positioned vertices and edges
with open(NAME+'.gv') as f:
    circo_src = f.read()
circo_src = circo_src.split('\n')
#You don't want the first and last line
circo_src = circo_src[1 : len(circo_src)-2]
#You don't want the semicolons
for i in range(len(circo_src)):
    circo_src[i] = circo_src[i].replace(';', '')

for item in circo_src:
    print(item)

#Phase Two: add the edges to the previous rendering
#Load it with the previous graph render result
mod.body = circo_src

#Add in the edges
for i in range(NUM):
    mod.edge(str(i), str((10*i) % NUM), color='yellow')

#Write the body to the file 'mod'
mod.render(NAME)

#Render using neato engine, had to call externally because
#we need the '-n' option to fix the layout determined by circo
os.system('neato -n '+NAME+' -Tpdf -O')
os.system('rm '+NAME)
os.system('rm '+NAME+'.gv')
