
#Create a blockchain from scratch 
# This is called SNAKECOIN (*_-)


import hashlib as hasher 
import datetime as date 
from menu import menu
 

class Block:
	def __init__(self,index,timestamp,data,previous_hash):
		self.index = index 
		self.timestamp = timestamp
		self.data = data
		self.previous_hash = previous_hash
		self.hash = self.hash_block() 

	def hash_block(self):
		sha = hasher.sha256()
		sha.update((str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)).encode('utf-8'))
		return sha.hexdigest()

def create_genesis_block():
		#manually construct a block with index zero
		return Block(0, date.datetime.now(), "Genesis Block" , "0")


def next_block(last_block):
		this_index = last_block.index +1 
		this_timestamp = date.datetime.now() 
		this_data = "Hey! I'm block" + str(this_index)
		this_hash = last_block.hash
		return Block(this_index, this_timestamp, this_data, this_hash)


menu()

#create the blockchain by connection all blocks together
blockchain = [create_genesis_block()]
previous_block = blockchain[0]

#how many blocks should we add to the chain
#after the genesis block(which is the first one)
	
num_of_blocks_to_add = 4

#add blocks using a for loop 
for i in range(0,num_of_blocks_to_add):
	block_to_add = next_block(previous_block)
	blockchain.append(block_to_add)
	previous_block = block_to_add

	#Print out the whole blockchain
	print()
	print("Block " + str(block_to_add.index) + " has been added successfully!!!" )
	print("Hash : {}\n".format(block_to_add.hash))
	print("Block data : " , block_to_add.data)
	if(block_to_add == create_genesis_block() ):
		print("No previous hash")
	else:
		print("Previous hash = ", block_to_add.previous_hash) 
	
	




