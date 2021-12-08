import sys, copy


immune = {}
infection = {}
with open('advent-input.txt') as f:
	a = f.readlines()

	is_immune = True
	is_infection = True
	id = 0
	for i in a:
		if "Immune System" in i:
			is_immune = True
		elif "Infection" in i:
			is_infection = True
			is_immune = False

		if "units each with" not in i:
			continue

		obj = {}
		line = i.strip().split(' units each with')
		num_units = int(line[0])
		line = line[1].split(' hit points ')
		hp = int(line[0])
		line = line[1]

		obj['weak'] = []
		obj['immune'] = []
		if line[0] == '(':
			parts = line.split(') ')
			line = parts[1]
			wk_im = parts[0].split('(')[1].split(';')

			wk = []
			im = []
			if len(wk_im) == 1:
				if "immune to" in wk_im[0]:
					im = wk_im[0]
				else:
					wk = wk_im[0]
			else:
				if "immune to" in wk_im[0]:
					im = wk_im[0]
					wk = wk_im[1]
				else:
					im = wk_im[1]
					wk = wk_im[0]

			if wk != []:
				wk = wk.split("weak to")[1].strip().split(',')
				wk = [i.strip() for i in wk]

			if im != []:
				im = im.split("immune to")[1].strip().split(',')
				im = [i.strip() for i in im]

			obj['weak'] = wk
			obj['immune'] = im

		line = line.split('with an attack that does ')[1].split(' damage at initiative ')
		damage = line[0].split(' ')
		damage_type = damage[1]
		damage = int(damage[0])
		initiative = int(line[1])

		obj['num_units'] = num_units
		obj['hp'] = hp
		obj['initiative'] = initiative
		obj['damage'] = damage
		obj['damage_type'] = damage_type
		obj['effective_power'] = num_units * damage
		obj['id'] = id

		if is_immune:
			obj['type'] = 'immune'
			immune[id] = obj
		elif is_infection:
			obj['type'] = 'infection'
			infection[id] = obj

		id += 1

def get_effective_damage(unit, opp):
	damage = 0
	damage += unit['effective_power']
	if unit['damage_type'] in opp['weak']:
		damage *= 2
	elif unit['damage_type'] in opp['immune']:
		damage = 0
	return damage

def rank_targets(unit, opponents):
	targets = []

	for opp in opponents:
		opp = opponents[opp]

		opp['effective_damage'] = get_effective_damage(unit, opp)
		targets.append(opp)

	targets = sorted(targets, key=lambda x: (-x['effective_damage'], -x['effective_power'], -x['initiative']))
	if len(targets) == 0 or targets[0]['effective_damage'] <= 0:
		return None
	return targets[0]


def run(immune, infection, boost):
	for i in immune:
		immune[i]['damage'] += boost
		immune[i]['effective_power'] = immune[i]['num_units'] * immune[i]['damage']

	while True:
		damage_done = False
		# print
		# print
		# # n += 1
		# # if n == 10:
		# # 	break
		# print "Immune:"
		# for i in immune:
		# 	print str(immune[i]['num_units']) + " damage type: "+immune[i]['damage_type']+ " weak: "+''.join(immune[i]['weak']) + " immune: " + ''.join(immune[i]['immune'])
		# print "Infection:"
		# for i in infection:
		# 	print str(infection[i]['num_units']) + " damage type: "+infection[i]['damage_type']  + " weak: "+''.join(infection[i]['weak']) + " immune: " + ''.join(infection[i]['immune'])
		selection_order = immune.values() + infection.values()
		selection_order = sorted(selection_order, key=lambda x: (-x['effective_power'], -x['initiative']))
		attack_order = sorted(selection_order, key=lambda x: -x['initiative'])

		immune_left = copy.deepcopy(immune)
		infection_left = copy.deepcopy(infection)

		# Selection Phase
		immune_map = {}
		infection_map = {}
		for grp in selection_order:
			type = grp['type']
			id = grp['id']
			selected = None
			if type == 'immune':
				target = rank_targets(grp, infection_left)
				if target != None:
					immune_map[id] = copy.deepcopy(target)
					for i in infection_left:
						if infection_left[i]['id'] == target['id']:
							infection_left.pop(i, None)
							break
				else:
					immune_map[id] = None


			elif type == 'infection':
				target = rank_targets(grp, immune_left)

				if target != None:
					infection_map[id] = copy.deepcopy(target)
					for i in immune_left:
						if immune_left[i]['id'] == target['id']:
							immune_left.pop(i, None)
							break
				else:
					infection_map[id] = None

		# Attack Phase
		# for i in selection_order:
		# 	print i
		# for i in immune_map:
		# 	print i, immune_map[i]
		# for i in infection_map:
		# 	print i, infection_map[i]
		# sys.exit()
		for grp in attack_order:
			type = grp['type']
			id = grp['id']
			if type == 'immune':
				target = immune_map[id]
				if target == None or id not in immune:
					continue
				unit = immune[id]
				target_id = target['id']
				effective_damage = get_effective_damage(unit, target)
				num_units_killed = effective_damage / target['hp']
				new_num_units = infection[target_id]['num_units'] - num_units_killed
				new_num_units = new_num_units if new_num_units >= 0 else 0

				if num_units_killed > 0:
					damage_done = True

				infection[target_id]['num_units'] = new_num_units
				# print infection[target_id]['num_units']
				# print target_id
				# print grp
				# print "Immune inflicts "+str(effective_damage)+" damage. Units killed: "+str(num_units_killed)
				if infection[target_id]['num_units'] <= 0:
					infection.pop(target_id)
					if len(infection) == 0:
						total_num_units = 0
						for unit_i in immune:
							unit = immune[unit_i]
							total_num_units += unit['num_units']
						return (type, total_num_units)
				else:
					infection[target_id]['effective_power'] = infection[target_id]['num_units'] * infection[target_id]['damage']
			elif type == 'infection':
				target = infection_map[id]
				if target == None  or id not in infection:
					continue

				unit = infection[id]

				target_id = target['id']
				effective_damage = get_effective_damage(unit, target)
				num_units_killed = effective_damage / target['hp']
				new_num_units = immune[target_id]['num_units'] - num_units_killed
				new_num_units = new_num_units if new_num_units >= 0 else 0
				if num_units_killed > 0:
					damage_done = True

				immune[target_id]['num_units'] = new_num_units
				# print "Infection inflicts "+str(effective_damage)+" damage. Units killed: "+str(num_units_killed)
				if immune[target_id]['num_units'] <= 0:
					immune.pop(target_id)
					if len(immune) == 0:
						total_num_units = 0
						for unit_i in infection:
							unit = infection[unit_i]
							total_num_units += unit['num_units']
						return (type, total_num_units)

				else:
					immune[target_id]['effective_power'] = immune[target_id]['num_units'] * immune[target_id]['damage']
		# sys.exit()

		if not damage_done:
			return ('stalemate', 0)

	# 20274 -> too low
	# 20340 -> correct!

boost = 32
while True:
	(type, total_num_units) = run(copy.deepcopy(immune), copy.deepcopy(infection), boost)
	print boost, type, total_num_units
	if type == 'immune':
		sys.exit()
	boost += 1