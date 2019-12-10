import random
import time


count_of_generation = 1000
board_dimention = 8
count_of_horses = 12
best_phenotip = 64
crossover_point = 3
iteration = 100


class Individual:
	def __init__(self):
		self.horses = []
		self.board = [[] for _ in range(board_dimention)]
		self.bitted_positions = [[] for _ in range(board_dimention)]
		for i in range(board_dimention):
			for j in range(board_dimention):
				self.board[i].append(0)
				self.bitted_positions[i].append(0)
		


	def create_first_population(self):
		self.set_random_horses()
		self.check_phenotip()
		self.create_horses_array()

	def rand_horse(self):
		self.a = random.randint(1, board_dimention - 2)
		self.b = random.randint(1, board_dimention - 2)
		if self.board[self.a][self.b] == 1:
			self.rand_horse()

	def check_bitted_positions(self, a, b):
		self.bitted_positions[a][b] = 1
		if (b != 1):
			self.bitted_positions[a - 1][b - 2] = 1
			self.bitted_positions[a + 1][b - 2] = 1
		if (a != 1):
			self.bitted_positions[a - 2][b - 1] = 1
			self.bitted_positions[a - 2][b + 1] = 1
		if (a != board_dimention - 2):
			self.bitted_positions[a + 2][b - 1] = 1
			self.bitted_positions[a + 2][b + 1] = 1
		if (b != board_dimention - 2):
			self.bitted_positions[a + 1][b + 2] = 1
			self.bitted_positions[a - 1][b + 2] = 1

	def set_random_horses(self):
		for i in range(count_of_horses):
			self.rand_horse()
			self.board[self.a][self.b] = 1
			self.check_bitted_positions(self.a, self.b)

	def create_horses_array(self):
		self.horses = []
		for i in range(board_dimention):
			for j in range(board_dimention):
				if self.board[i][j] == 1:
					self.horses.append([i, j])

	def check_phenotip(self):
		phenotip = 0
		for i in range(board_dimention):
			for j in range(board_dimention):
				phenotip += self.bitted_positions[i][j]
		self.phenotip = phenotip
		if phenotip == board_dimention**2:
			print(f'            *********************** ')
			print(f'\n\n\n\n            --------- DONE!-------- \n\n\n\n ')

			self.print_horses_board()
			self.print_phenotip_board()
			self.print_phenotip()
			print(f'\n{self.horses}\n')
			print(f'\n\n\n\n        ----****   array of average of generation phenotip:   ****----\n\n  {average_array}       ')
			exit()

	def print_phenotip(self):
		print(f"		phenotip = {self.phenotip}")

	def print_horses_board(self):
		print("\n        board:")
		for i in range(board_dimention):
			for j in range(board_dimention):
				print(self.board[i][j], end ='  ')
			print(' ')


	def print_phenotip_board(self):
		print("\n    bitted positions:  ")
		for i in range(board_dimention):
			for j in range(board_dimention):
				print(self.bitted_positions[i][j], end='  ')
			print(' ')



	def swap(self, some_board):

		crossover_point = random.randint(0, count_of_horses-1)
		print(f'_______________\n\na:     {self.horses}')
		print(f'phenotip:     {self.phenotip}')
		print(f'\n\nb:     {some_board.horses}')
		print(f'phenotip:     {some_board.phenotip}')
		# print(f'\na from 0 to cross:  {self.horses[0:crossover_point]}')
		print(f'\ncrossover point: {crossover_point}\n')
		
		for i in range(crossover_point, count_of_horses):

			if some_board.horses[i] in self.horses[0:i]:
				while True:
					self.horses[i][0] = random.randint(1, board_dimention-2)
					self.horses[i][1] = random.randint(1, board_dimention-2)
					if self.horses[i]  not in self.horses[0:i]:
						break
			else:
				self.horses[i] = some_board.horses[i]


		print(self.horses)
		self.update_boards()
		print(f"\n\n		phenotip = {self.phenotip}")




	def make_two_childs(self, some_board):

		crossover_point = random.randint(0, count_of_horses-1)
		# print(f'_______________\n\na:     {self.horses}')
		# print(f'phenotip:     {self.phenotip}')
		# print(f'\n\nb:     {some_board.horses}')
		# print(f'phenotip:     {some_board.phenotip}')
		# print(f'\na from 0 to cross:  {self.horses[0:crossover_point]}')
		# print(f'\ncrossover point: {crossover_point}\n')
		first_child = Individual()
		second_child = Individual()
		
		for i in range(crossover_point):
			first_child.horses.append(self.horses[i])
			second_child.horses.append(some_board.horses[i])


		for i in range(crossover_point, count_of_horses):
			if some_board.horses[i] in first_child.horses[0:i]:
				while True:
					new_rand_horse = [random.randint(1, board_dimention-2), random.randint(1, board_dimention-2)]
					if new_rand_horse not in first_child.horses[0:i]:
						first_child.horses.append(new_rand_horse)
						break
			else:
				first_child.horses.append(some_board.horses[i])

			if self.horses[i] in second_child.horses[0:i]:
				while True:
					new_rand_horse = [random.randint(1, board_dimention-2), random.randint(1, board_dimention-2)]
					if new_rand_horse not in second_child.horses[0:i]:
						second_child.horses.append(new_rand_horse)
						break
			else:
				second_child.horses.append(self.horses[i])
		
		childs_array.append(first_child)
		childs_array.append(second_child)
		# print(f'first child:     {first_child.horses}')
		first_child.update_boards()
		# print(f"\n		phenotip = {first_child.phenotip}")
		# print(f'second child:     {second_child.horses}')
		second_child.update_boards()
		# print(f"\n		phenotip = {second_child.phenotip}")




	def twice_crossingover(self, some_board):
		crossover_point = random.randint(1, count_of_horses - 8)
		crossover_point2 = random.randint(crossover_point+1, count_of_horses - 1)

		print(f'_______________\n\na:     {self.horses}')
		print(f'phenotip:     {self.phenotip}')
		print(f'\n\nb:     {some_board.horses}')
		print(f'phenotip:     {some_board.phenotip}')
		# print(f'\na from 0 to cross:  {self.horses[0:crossover_point]}')
		print(f'\ncrossover point: {crossover_point}')
		print(f'crossover point2: {crossover_point2}\n')


		for i in range(crossover_point, crossover_point2):
			new_item = some_board.horses[i]
			while new_item in self.horses[0:crossover_point]:
				new_item[0] = random.randint(1, board_dimention - 2)
				new_item[1] = random.randint(1, board_dimention - 2)
			self.horses[i] = new_item


		print(self.horses)
		self.update_boards()

		print(f"\n\n		phenotip = {self.phenotip}")
	

	def update_boards(self):
		self.clean_boards()
		for horse in self.horses:
			self.a = horse[0]
			self.b = horse[1]
			self.board[self.a][self.b] = 1
			self.check_bitted_positions(self.a, self.b)
		self.check_phenotip()
		self.create_horses_array()


	def clean_boards(self):
		for i in range(board_dimention):
			for j in range(board_dimention):
				self.board[i][j] = 0
				self.bitted_positions[i][j] = 0

#TODO: 
# add array horses
# add method to swap random horses genom
# ask about sort list of horses




def generation_phenotip(gen):
	gen_phenotip = 0
	for indiv in gen:
		gen_phenotip += indiv.phenotip
	gen_phenotip /= count_of_generation
	return gen_phenotip




generation_array = []
childs_array = []


for i in range(count_of_generation):
	generation_array.append(Individual())
	generation_array[i].create_first_population()

generation_array.sort( reverse = True, key = lambda elem: elem.phenotip)


	



# for indiv in generation_array:
# 	print('____________________________')
# 	print(indiv.horses)
# 	print(f"		phenotip = {indiv.phenotip}")

average_array = []
for j in range(iteration):
	

	print(f'\n\n\n\n                                     * * *')
	print(f'                        ...generating new generation... \n')
	print(f'                                   --- #{j+1} ---')

	for i in range(count_of_generation-1):
		generation_array[i].make_two_childs(generation_array[i+1])
	generation_array[count_of_generation-1].make_two_childs(generation_array[0])
	childs_array.sort( reverse = True, key = lambda elem: elem.phenotip)
	generation_array = childs_array[0:count_of_generation]


	average_array.append(generation_phenotip(generation_array))
	print(f'\n\n        ****     average of generation phenotip =  {average_array[j]}       ****')



	# print(f'\n\n\n\n\n                                 childs #{j+1}')
	# for indiv in childs_array:
	# 	# indiv.print_horses_board()
	# 	# indiv.print_phenotip_board()
	# 	print('____________________________________________________________')
	# 	print(indiv.horses)

	# 	indiv.print_phenotip()


	# print(f'\n\n\n\n\n\n                                 generation #{j+1}')
	# for indiv in generation_array:
	# 	# indiv.print_horses_board()
	# 	# indiv.print_phenotip_board()
	# 	print('____________________________________________________________')
	# 	print(indiv.horses)
	# 	indiv.print_phenotip()


	
	

print(f'\n\n\n\n        ----****   array of average of generation phenotip:   ****----\n\n  {average_array}       ')