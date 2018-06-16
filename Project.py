#**********************  Project.py  *********************
#
# Name: Kaleb Green
#
# Course: CSCI 1470
#
# Assignment: Project
#
#Helpful terms:
##Name- the charaters name
##Hp- Health points (how much damage you can take before you die
##MxHP- The maximum amount of HP a character can have
##Mp – Magic Points(how many points you have to use spells)
##MxMp- Maximum amount of MP a character can have
##MG- Magic(how hard you hit with magic)
##Str – Strenth(How hard you hit)
##Def- Defense(How sturdy you are)
##Acc- Accuracy how likely you are to hit
##Dex – dexterity How likely you are to avoid an attack
##Res –magic defense
##Sp –speed decides who go first
##Dn- density(how heavy you are)
##INV- The inventory of the player
##SplList- A list of all spells the user knows
##Gld- The amount of gold the player has/ the enemy will give if defeated
##Exp- The amount experience that player has/the enemy will give if defeated
##Drp- The items the player may receive if they defeat the enemy
##Abl- Abilities, the things that the enemy can do
##
##Import turtle to print out info if the play dies/wins
##Import random to generate random numbers
##Create a list called Spell list that is a list of all spells, their mana cost, and their damage
##Effect_spell_list is list of all spells that inflict a status ailment
##Item_list is a list of all items
##Heal_spell is a list of all healing spells
##Armor_list is a list of all armor that player can equip
##Weapon_list is a list of all weapons that the player can equip
##Create a dictionary called status_ail_player with poision , burn and confuse
##Create a dictionary called status_ail_enemy with poison, burn and confuse 
##player info is in this format:
##[Name,Hp,MxHp,Mp,MxMP,MG,Str,Def,Acc,Dex,Res,Spd,[spells],Dn,[Inventory],Gld,Exp]
##
##Player:
##	[“”,10,10,10,10,1,1,1,1,1,1,1, [cure1,MagicMissle]]1,[burger, burger ,burger, poison heal],50,0,
##Enemy info is in this format:
##	[Name,Hp,MxHp,Mp,MxMP,MG,Str,Def,Acc,Dex,Res,Spd,[abl][Inventory],Gld,Exp,[Drp],
##Goblin:	
##[Goblin,15,10,0,0,0,3,3,3,5,2,6, ],[enemy_attack, use_item_enemy],,[rock, dynamite,rock,rock,rock,burger,burger],50,50,[rock ,dynamite ,iron sword, basic armor, burger]
##Ogre:
## [Ogre,25,25,1000,1000,5,5,5,4,4,2,4, ],[enemy_attack, earthquake],[],100,100[steel sword, steel armor
##Wolf:
##	[Wolf, 10,10,0,0,0,1,1,1,1,0,1, ,[enemy_attack] ,[],10,25,[burger]]
##Fuming_shroom:
##	[Fuming Shromm, 5,5,10,10,0,1,1,1,1,1,1,[poison spore,enemy_attack],[],10,10,[stick, bare cloths]
##Warlock:
##	[Warlock,50,50,200,200,7,4,4,7,7,9,7,[magic missle,fire2,earquake2,use_item_enemy],[cake],200,200,[magic armor, magic sword]
##witch:
##[witch,50,50,200,200,7,4,4,7,7,9,7,[magic missle, fire2, earquake2 ,use_item_enemy],[cake],200,200,[magic armor, magic sword]
##
##Dragon:
## 	[Dragon,200,200,10000,10000,10,10,10,10,10,10,10, ,[],[fire breath, poison fang, enemy_attack, fireball3, earquake3,beguiling eyes]
##,[],20000,2000]
##Dire_Wolf
##	[Dire Wolf,25,25,100,100,2,3,3,3,3,3,4,6, ],[healing howl, ferocious bite],[],500,200,[iron hammer]]
##Goblin_King
##	[Goblin King, 50,50,100,100,6,6,6,6,6,6,6,[SMASH ATTACK, belch,use_item_enemy],[dynamite, dynamite, dynamite],200,1000]
##Necromancer:
##	[Necromancer,150,150,200,200,8,4,4,8,9,9,7,[magic missle,fire3,earquake2,use_item_enemy],[cake,ake],250,1200,[DragonSlayer]
##A list of area and the monsters that will appear there
##Woods:
##	[Fuming_shroom,wolf, ]
##Mountain:
##	[Goblin ,Ogre,]
##Swamp:
##	[Witch, Warlock, ]
##	
##
##
##
##f
##Create a function called player_win with no parameters:
##	Use turtle to print out a message saying that the player has won
##Create a function called environment death:
##	Use turtle to print out a message saying that the player has drowned/been hit by lightning
##Create a function called buy with parameters player and seller and item_list, spell_list, effect_spell_list, and heal_list:
##	Print out a message asking the player what they want to do, set that to question	
##	While question is not quit:
##		If question is set to buy:
##			Print out the seller’s inventory items with their represented prices
##			Ask player what they want to buy, set that to buy
##			If player gold is greater than or equal to item price:
##				If buy is in spell_list or in effect_spell_list or heal_list:
##					Print out that user learned buy
##					Add buy to user ability list
##					Subtract the item cost from player gold
##				Else:
##Print out a message saying that player bought item
##					Subtract the item cost from player gold
##			Else:
##				Print out you don’t have enough gold
##		If question is set to sell:
##			Print out player inventory with it’s prices
##			Ask player what they want to sell and set that equal to sell
##			If sell not in inventory:
##				Print out that player does not have one of those
##			Else:
##Remove the item from player inventory and add the money to player gold
##Print out how munch money the player got
##		Return “thanks for your patronage!”
##			
##		
##
##Define the function attack with parameters attacker, defender, weapon :
##Create a random number called dex_check that generates a random number between 1 and 10
##	Create  a random number called crit that generates a random number between 1 and 10
##	Percentage_chance is equal to (attackers accuracy/defenders dexterity)*10
##	If Percentage_chance is greater than or equal to dex_check:
##		If crit >9:
##The Defender takes damage equal to twice the value of the attackers strength stat plus their weapon equipped
##If The defenders defense stat  is greater than or equal to the attackers strength stat + weapon:
##			The Defender takes 1 damage
##		Else:
##			Defenders health = defenders health – (attackers strength +weapon)-(defensers defenders defense ))
##		print the amount of damage done to defender
##	else:
##		print attacker missed
##Define the function magic_attack with parameters attacker, defender, spell:
##	If spell cost > mana:
##		Return that attacker did not have enough mana
##	User mana = user mana – spell cost
##	Create a random number called dex_check that generates a random number between 1 and 10
##Create  a random number called crit that generates a random number between 1 and 10
##	Percentage_chance is equal to (attacker accuracy/defender dexterity)*10
##	If Percentage_chance is greater than or equal to dex_check:
##		If crit > 9:
##			The spell does double damage and ignores the enemy’s defense
##			
##		If defenders’ resistance is greater than or equal to attacker magic+ spell:
##			Attacker deals 1 damage
##		Else:
##			Defender health = defender health– (attacker’s magic + spell - defender’s resistance)
##		Return  the amount of damage done to defender and what spell was used
##	else:
##		return miss
##Define the function enemy_attack with parameters attacker, defender, armor :
##	Create a random number called dex_check that generates a random numdber between 1 and 10
##	Create  a random number called crit that generates a random number between 1 and 10
##	Percentage_chance is equal to (attackers accuracy/defenders dexterity)*10
##	If Percentage_chance is greater than or equal to dex_check:
##		If crit >9:
##The Defender takes damage equal to twice the value of the attackers strength stat 
##If The defenders defense stat +armor is greater than or equal to the attackers strength stat :
##			The Defender takes 1 damage
##		Else:
##Defenders health = defenders health – (attackers strength)-(defensers defense +armor))
##		print the amount of damage done to defender
##	else:
##		print attacker missed
##Define the function magic_attack with parameters attacker, defender, spell:
##	If spell cost > mana:
##		Return that attacker did not have enough mana
##	User mana = user mana – spell cost
##	Create a random number called dex_check that generates a random number between 1 and 10
##Create  a random number called crit that generates a random number between 1 and 10
##	Percentage_chance is equal to (attacker accuracy/defender dexterity)*10
##	If Percentage_chance is greater than or equal to dex_check:
##		If crit > 9:
##			
##		If defenders’ resistance is greater than or equal to attacker magic+ spell:
##			Attacker deals 1 damage
##		Else:
##			Defender health = defender health– (attacker’s magic + spell - defender’s resistance)
##		print the amount of damage done to defender and what spell was used
##	else:
##		print miss
##
##
##define the function heal with parameters user,heal_spell_list and spell:
##	if spell cost > mana:
##		return that user did not have enough mana
##	user mana = user mana – spell cost
##	if spell is equal to Heal1 or Heal 2 or Heal3
##		create an integer called starting health and set it equal to starting health
##		user is healed (player magic * spell) amount of points	
##		if  user health > user max health:
##			set health equal to max health
##
##healed_points is equal to user health – starting health
##return user was health healed_points
##	if spell is equal to Cure_All:
##		change all values in dictionary to 0
##define the function use_item with paraments user,enemy and item list:	
##	print out the players inventory
##	ask the player what they want to use, and set that equal to item_check
##	if item_check is not in inventory and item_check is in item list:
##		return player tried to use item_check, but they didn’t have any!
##	If item_check is burger:
##		create an integer called starting health and set it equal to starting health
##		user is healed 10 points
##		if user health is greater than user max health:
##			set user health equal to max health
##		return the amount of points healed
##	if item_check is cake:
##create an integer called starting health and set it equal to starting health
##		user is healed 20 points
##		if user health is greater than user max health:
##			set user health equal to max health
##		return the amount of points healed
##	if item_check is magic apple:
##create an integer called starting health and set it equal to starting health
##		user is healed 50 points
##		if user health is greater than user max health:
##			set user health equal to max health
##		remove magic apple from inventory
##		return the amount of points healed
##	if item_check is rock:
##		enemy is dealt 2 damage
##		remove rock from inventory
##		return damage dealt
##	if item_check is dynamite:
##		enemy is dealt 20 damge
##		remove dynamite from inventory
##		return damage delt
##	if item_check is poision heal:
##		remove poison status from user
##		remove poison heal from inventory
##		return that user was healed of poison
##	if item_check is burn heal:
##		remove burn status from user
##		remove burn heal from inventory
##		return that user was healed of burn
##	if item_check is full cure:
##		remove all status ailments from usr
##		remove full cure from inventory		
##		return that the user was healed of all ailments
##	if user inventory is an empty list:
##		return that the user tried to use an item, but they didn’t have anything to use
##	if item_check is not in item_list:
##		return that user did not know how to use that
##		
##define the function use_item_enemy with parameters enemy and player:
##	if enemy inventory is empty:
##		return that the enemy tried to use an item but they didn’t have anything to use
##create a random number between 0 and the length of the enemy inventory – 1 and set that to a variable called decide
##	set item_check equal to enemy[12][decide]
##	If item_check is burger:
##		create an integer called starting health and set it equal to starting health
##		enemy is healed 10 points
##		remove burger from enemy inventory
##		if enemy health is greater than user max health:
##			set user health equal to max health
##		return the amount of points healed
##	if item_check is cake:
##create an integer called starting health and set it equal to starting health
##		enemy is healed 20 points
##		if enemy health is greater than enemy max health:
##			set enemy health equal to max health
##		remove cake from inventory
##		return the amount of points healed
##	if item_check is magic apple:
##create an integer called starting health and set it equal to starting health
##		user is healed 50 points
##		if enemy health is greater than enemy max health:
##			set enemy health equal to max health
##		remove magic apple from enemy inventory
##		return the amount of points healed
##	if item_check is rock:
##		player is dealt 2 damage
##		remove rock from enemy inventory
##		return damage dealt
##	if item_check is dynamite:
##		player is dealt 20 damage
##		remove dynamite from enemy inventory
##		return damage delt
##
##
##define the function level_up_chck with parameters player,level_up:
##	loop = 0
##	while player EXP is greater than or equal to Level_Up:		
##		set player Exp equal to player experience -level_up
##		set Level_UP to Level_Up +50
##		create a random number called increase_Mxhp and set it equal to either 1 or 2 
##		create a random number called increase_Mxmp and set it equal to either 1 or 2 
## 		create a random number called increase_str and set it equal to either 1 or 2  
##		create a random number called increase_def and set it equal to either 1 or 2 
##		create a random number called increase_Mg and set it equal to either 1 or 2 
##		create a random number called increase_Res and set it equal to either 1 or 2
##		create a random number called increase_dex and set it equal to either 1 or 2
##		create a random number called increase_acc and set it equal to either 1 or 2 
##		create a random number called increase_Sp and set it equal to either 1 or 2 
##		if increase_Mxhp is greather 1:
##			increase the user’s maxium hp by 10
##		if increase_Mxmp is greather than 1:
##			increase the user’s maximum mana by 5
##		if increase_str is greather than 1 and user’s strength is  less than 10
##create a random number called str_increased that generates a number between 1 and 3
##			add str_increased to the user’s strength
##			If user’s str is greater than 10:	
##				set user’s str to 10
##if increase_def is greater than 1 and user’s defense is  less than 10
##create a random number called str_defense that generates a number between 1 and 3
##			add str_defense to the user’s defense
##			if user’s def is greater than 10:	
##				set user’s def to 10
##if increase_mg is greater than 1 and user’s magic is  less than 10
##create a random number called mg_increased that generates a number between 1 and 3
##			add mg_increased to the user’s magic
##			if user’s mg is greater than 10:	
##				set user’s mg to 10
##if increase_res is greater than 1 and user’s resitance is  less than 10
##create a random number called res_increased that generates a number between 1 and 3
##			add res_increased to the user’s resitance
##			if user’s res is greater than 10:	
##				set user’s res to 10
##if increase_dex is greater than 1 and user’s dexterity is  less than 10
##create a random number called dex_increased that generates a number between 1 and 3
##			add dex_increased to the user’s dexterity
##			If user’s dex is greater than 10:	
##				set user’s dex to 10
##if increase_acc is greater than 1 and user’s accuracy is  less than 10
##create a random number called acc_increased that generates a number between 1 and 3
##			add acc_increased to the user’s accuracy
##			if user’s acc is greater than 10:	
##				set user’s acc to 10
##if increase_sp is greater than 1 and user’s speed is  less than 10
##create a random number called sp_increased that generates a number between 1 and 3
##			add sp_increased to the user’s speed
##			if user’s sp is greater than 10:	
##				set user’s sp to 10
##		loop = loop +1
##	if loop > 0:
##		return the user’s stats
##	else :
##		return “\n”
##define the function battle_death:
##		prints out a picture informing the player that they have died in battle
##
##define the function equip with parameters player, weapon, armor, weapon_list , and armor_list
##	print out the player’s inventory
##	ask the player what they want to equip and set it equal to equip
##	if equip is in inventory and weapon_list:
##		set weapon to equip
##		return you equipped equip
##	if equip is in inventory and armor_list:
##		set armor to equip
##		if equip is iron or steel armor:
##			set density to 5
##		return you put on equip
##	if equip not in inventory
##		return you don’t have one of those
##	else:
##		return don’t know what that is 
##
##define the function de-quip with parameters player, weapon, and armor:
##	print out weapon and armor
##	ask the user what they want to take off and set it equal to de-quip
##	if de-quip is the same as weapon:
##		set weapon equal to an empty list
##	if de-quip is the same as armor:
##		set armor equal to an empty list	
##		set density equal to 1
##	return the player’s armor and weapon
##
##define the function confused_attack with parameters inflicted, armor, weapon:
##	inflected takes damage equal to their attack +armor – defense+armor
##	return that inflicted hit themselves in the confusion
##define the function status_effect_spell with paramets status_ail_enemy, user, afflicted , status_spell_list, spell:
##	if spell cost is greater than mana:
##		return that user didn’t have enough mana
##	mana = mana – spell cost
##	if spell is poison:
##		poison_chance is a random number between 1 and 10
##		poison_percent is equal to user’s accuracy over afflicted’s dexterity *10
##		if poison_percent is greater than poison chance:
##			change status_ail_enemy[poison] to equal 1
##			return user used status_effect_spell and afflicted became poisoned
##		burn_chance is a random number between 1 &10
##		burn_percent is equal to user’s accuracy over affliced’s dexterity*10
##		if burn_percent is greater than burn_chance:
##			change status_ail_enemy[burn] to equal 1
##			return that afflicted became burned
##define the function status_effect_spell_enemy with paramets status_ail_player, enemy, afflicted , status_spell_list, spell:
##	if spell cost is greater than mana:
##		return that user didn’t have enough mana
##	mana = mana – spell cost
##	if spell is poison:
##		poison_chance is a random number between 1 and 10
##		poison_percent is equal to user’s accuracy over afflicted’s dexterity *10
##		if poison_percent is greater than poison chance:
##			change status_ail_enemy[poison] to equal 1
##			return user used status_effect_spell and afflicted became poisoned
##		burn_chance is a random number between 1 &10
##		burn_percent is equal to user’s accuracy over affliced’s dexterity*10
##		if burn_percent is greater than burn_chance:
##			change status_ail_enemy[burn] to equal 1
##			return that afflicted became burned
##confuse_chance is a random number between 1 &10
##		confuse_percent is equal to user’s accuracy over affliced’s dexterity*10
##		if confuse_percent is greater than confuse_chance:
##			change status_ail_enemy[confuse] to equal 1
##			return afflicted became confused
##
##define function poison with parameters afflicted:
##	afflicted takes damage equal to 1/16 it’s total health
##	set 1/16 of afflicted health equal to poison_damage
##	return that afflicted took poison_damge amount of poison damage
##define the function burn with parameters afflicted:
##	afflicted takes damage equal to 3/16 it’s total health
##	set 3/16 of afflicted total health equal to burn_damage
##	return that afflicted took burn_damge amount of burn damage
##define the function escape with parameters enemy and player:
##	set escape_chance equal to a random number between 1 and 10
##	set escape_percent equal to player dexterity/enemy accuracy *10
##	set escape_lucky_break to a random number between 1 and 10
##	if escape_percent is greater than or equal to escape chance or escape_lucky_chance is greater than 7:
##		return True
##	else:
##		return False
##define the function battle with parameters player, enemy,spell_list,enemy_list,item_list status_spell_list,  status_ail_enemy, and status_ail_player:
##	print out that player was attacked by enemy
##	confused_count = 0
##	while player health and enemy health are greater than 0:
##		if player  confused:
##			create a number between 0 and 1 called confused attack
##			confused_count = confused_count +1
##			if confused_cout divded by 4 has a remainder of 0:
##				cure player of confustion
##			if confused attack = 1
##run function confused_attack with parameters player weapon and armor	
##create a random number between 0 and the amount of actions enemy has – 1 and set it equal to action_decide
##use this number to decide what the enemy will do and set that equal to enemy_action
##if enemy_action is equal to attack
##	print and run function enemy_attack with parameters enemy, player and armor
##if enemy_action is equal to use item
##	print and run use_item_enemy with paramets enemy and player
##if enemy_action in spell_list :
##print and run magic_attack with paramets enemy, player, and enemy_action
##			if enemy_action in status_spell_list:
##print and run the function status_spell_enemy with parameters, status_effect_player, enemy, player, and enemy_action
##			if enemy_action in heal_spell_list:
##print and run heal_spell with parameters enemy, heal_spell_list, and enemy_action
##
##			else:
##				print out What would you like to do: Attack, Cast a spell, Use Item, or escape	and set answer to action
##If action = cast a spell
##Print out the players abilites, ask them what they want to use and set that equal to action
##		If action equals use item:
##Print out player inventory and ask them what they want to use and set that equal to action
##		else:
##				print did not understand
##				
##
##if player speed is equal to enemy speed:
##	create a random number speed_tie between 0 and 1
##		if player speed is greater than enemy speed or speed tie is equal to 0:
##			if action is equal to attack:
##				run attack with parameters player ,enemy, weapon
##		
##			if action is in spell_list:
##print and run function magic_attack with parameters player, enemy, action
##
##			if action is in status_spell_list:
##print and run function status_effect_spell with paramets status_ail_enemy, player, enemy  , status_spell_list, action
##			if action is in heal_spell_list:
##print and run function heal with parameters player, heal_spell_list, action
##			if action is equal to Use Item:
##print and run function use_item with parameters player, enemy and item list
##			if action is equal to Escape
##set the function escape (with paramers player and enemy) equal to check
##				if check:
##					return that Player escaped from battle
##				else:
##					print that user tried to escape from battle, but failed
##			
##create a random number between 0 and the amount of actions enemy has – 1 and set it equal to action_decide
##use this number to decide what the enemy will do and set that equal to enemy_action
##if enemy_action is equal to attack
##	print and run function enemy_attack with parameters enemy, player and armor
##if enemy_action is equal to use item
##	print and run use_item_enemy with paramets enemy and player
##if enemy_action in spell_list :
##print and run magic_attack with paramets enemy, player, and enemy_action
##			if enemy_action in status_spell_list:
##print and run the function status_spell_enemy with parameters, status_effect_player, enemy, player, and enemy_action
##			if enemy_action in heal_spell_list:
##print and run heal_spell with parameters enemy, heal_spell_list, and enemy_action
##		if enemy speed > player speed or speed_tie equals 1:
##			create a random number between 0 and the amount of actions enemy has – 1 and set it equal to action_decide
##use this number to decide what the enemy will do and set that equal to enemy_action
##if enemy_action is equal to attack
##	print and run function enemy_attack with parameters enemy, player and armor
##if enemy_action is equal to use item
##	print and run use_item_enemy with paramets enemy and player
##if enemy_action in spell_list :
##print and run magic_attack with paramets enemy, player, and enemy_action
##			if enemy_action in status_spell_list:
##print and run the function status_spell_enemy with parameters, status_effect_player, enemy, player, and enemy_action
##			if enemy_action in heal_spell_list:
##print and run heal_spell with parameters enemy, heal_spell_list, and enemy_action
##	
##			if action is equal to attack:
##				run attack with parameters player ,enemy, weapon
##		
##			if action is in spell_list:
##print and run function magic_attack with parameters player, enemy, action
##
##			if action is in status_spell_list:
##print and run function status_effect_spell with paramets status_ail_enemy, player, enemy  , status_spell_list, action
##			if action is in heal_spell_list:
##print and run function heal with parameters player, heal_spell_list, action
##			if action is equal to Use Item:
##print and run function use_item with parameters player, enemy and item list
##			if action is equal to Escape
##set the function escape (with parameters player and enemy) equal to check
##				if check:
##					return that Player escaped from battle
##				else:
##					print that user tried to escape from battle, but failed
##			if player is poisoned:
##				run the function poison with parameter player
##			if enemy poisoned:
##				run the function poison with parameter enemy
##			if player burned:
##				run the function burn with parameter player
##			if enemy burned:
##				run the function burn with parameter enemy
##
##
##		else:	
##print out What would you like to do: Attack, Cast a spell, Use Item, or escape	and set answer to action
##If action = cast a spell
##Print out the players abilites, ask them what they want to use and set that equal to action
##		If action equals use item:
##Print out player inventory and ask them what they want to use and set that equal to action
##		else:
##				print did not understand
##				
##
##if player speed is equal to enemy speed:
##	create a random number speed_tie between 0 and 1
##		if player speed is greater than enemy speed or speed tie is equal to 0:
##			if action is equal to attack:
##				run attack with parameters player ,enemy, weapon
##		
##			if action is in spell_list:
##print and run function magic_attack with parameters player, enemy, action
##
##			if action is in status_spell_list:
##print and run function status_effect_spell with paramets status_ail_enemy, player, enemy  , status_spell_list, action
##			if action is in heal_spell_list:
##print and run function heal with parameters player, heal_spell_list, action
##			if action is equal to Use Item:
##print and run function use_item with parameters player, enemy and item list
##			if action is equal to Escape
##set the function escape (with paramers player and enemy) equal to check
##				if check:
##					return that Player escaped from battle
##				else:
##					print that user tried to escape from battle, but failed
##			
##create a random number between 0 and the amount of actions enemy has – 1 and set it equal to action_decide
##use this number to decide what the enemy will do and set that equal to enemy_action
##if enemy_action is equal to attack
##	print and run function enemy_attack with parameters enemy, player and armor
##if enemy_action is equal to use item
##	print and run use_item_enemy with paramets enemy and player
##if enemy_action in spell_list :
##print and run magic_attack with paramets enemy, player, and enemy_action
##			if enemy_action in status_spell_list:
##print and run the function status_spell with parameters, status_effect_player, enemy, player, and enemy_action
##			if enemy_action in heal_spell_list:
##print and run heal_spell with parameters enemy, heal_spell_list, and enemy_action
##		if enemy speed > player speed or speed_tie equals 1:
##			create a random number between 0 and the amount of actions enemy has – 1 and set it equal to action_decide
##use this number to decide what the enemy will do and set that equal to enemy_action
##if enemy_action is equal to attack
##	print and run function enemy_attack with parameters enemy, player and armor
##if enemy_action is equal to use item
##	print and run use_item_enemy with paramets enemy and player
##if enemy_action in spell_list :
##print and run magic_attack with paramets enemy, player, and enemy_action
##			if enemy_action in status_spell_list:
##print and run the function status_spell with parameters, status_effect_player, enemy, player, and enemy_action
##			if enemy_action in heal_spell_list:
##print and run heal_spell with parameters enemy, heal_spell_list, and enemy_action
##	
##			if action is equal to attack:
##				run attack with parameters player ,enemy, weapon
##		
##			if action is in spell_list:
##print and run function magic_attack with parameters player, enemy, action
##
##			if action is in status_spell_list:
##print and run function status_effect_spell with paramets status_ail_enemy, player, enemy  , status_spell_list, action
##			if action is in heal_spell_list:
##print and run function heal with parameters player, heal_spell_list, action
##			if action is equal to Use Item:
##print and run function use_item with parameters player, enemy and item list
##			if action is equal to Escape
##set the function escape (with parameters player and enemy) equal to check
##				if check:
##					return that Player escaped from battle
##				else:
##					print that user tried to escape from battle, but failed
##			if player is poisoned:
##				run the function poison with parameter player
##			if enemy poisoned:
##				run the function poison with parameter enemy
##			if player burned:
##				run the function burn with parameter player
##			if enemy burned:
##				run the function burn with parameter enemy
##	if player health is less than or equal to 0:
##		return function battle_death
##	if enemy health is less than or equal to 0:
##		cure all enemy and player ailments 
##create a random number called drop that generates a random number between 0 and the number of items in enemy drop list -1
##add the corresponding item to the player’s inventory
##print what item was dropped
##add the enemy gold to player gold
##print how much gold was obtained
##if  enemy is not goblin king and not dragon and not necromancer and not dire wolf:
##	revert enemy inventory, hp, and mp to how
##add enemy experience to player experience
##print the amount of experience gained
##return the function level_up_check with parameters player and level_up
##
##set player to an empty string
##set count = 0
##Ask the player what their name is, set that equal to player
##Print out a message saying that the player was called to see the king
##Print out king dialoged informing the player that his daughter was kidnapped by a dragon and to task the player with rescuing her
##
##While player health and dragon Health are greater than 0
##Ask the player what they want to do: leave town, talk to blacksmith, talk to distress girl, talk to shop keeper, talk to sullen man and set that equal to go
##If go is equal to sullen man and dire wolf health is greater than 0: 
##Inform the player that the man’s wife was killed by a dire wolf and that he is willing to pay you if you can kill it
##	Else if go is equal to sullen man:
##		Thank the player and give them 500 gold	
##	If go is equal to distressed girl and goblin king health > 0:
##Inform the player that the girl’s brother was kidnapped by gobins and dragged off to their lair
##	Else if go is equal to distressed girl:
##		Give the player the knights of the round spell
##	If go is equal to blacksmith and necromancer health is greater than 0:
##Inform the player that the blacksmith had his master work stolen by an evil necromancer
##	Else If go is equal to blacksmith:
##		Give the player the berserker armor
##	If go is equal to shop keeper:
##		Run the buy function with item list and player as parametersb
##	If go is equal to leave town:
##		While go doesn’t equal town:
##Print where would you like to go, woods, mountain, swamp, castle, or town
##If go equals woods:
##	While go does not equal leave woods:
##		set count = 0
##	
##		if count greater or equal to 1 and not equal to 10:
##create a random number called random_encounter and set it equal to a number between 0 and 3
##if random is greater than or equal to the length of the list woods:
##battle the corresponding monster in the woods list
##ask the player what the would like to do: equip, dequip or move forward, or leave woods
##if equip:
##	run equip function
##if dequip
##	run dequip function
##if move forward
##	set count equal to count + 1
##if count equal to 10:
##	run the battle function with dire wolf as enemy
##
##
##	
##			If go equals mountain:
##		While go does not equal leave mountain:
##		set count = 0
##	
##		if count greater or equal to 1 and not equal to 15:
##create a random number called random_encounter and set it equal to a number between 0 and 3
##if random is greater than or equal to the length of the list mountain:
##battle the corresponding monster in the mountain list
##ask the player what the would like to do: equip, dequip or move forward, or leave woods
##if equip:
##	run equip function
##if dequip
##	run dequip function
##if move forward
##	set count equal to count + 1
##if count equal to 15:
##	run the battle function with goblin king as enemy
##
##			If go equal swamp:
##While go does not equal leave woods:
##		set count = 0
##	
##		if count greater or equal to 1 and not equal to 20:
##create a random number called random_encounter and set it equal to a number between 0 and 3
##if random is greater than or equal to the length of the list swamp:
##battle the corresponding monster in the swamp list
##ask the player what the would like to do: equip, dequip or move forward, or leave woods
##if equip:
##	run equip function
##if dequip
##	run dequip function
##if move forward
##	set count equal to count + 1
##if count equal to 10:
##	run the battle function with necromancer as enemy
##
##			If go equals castle:
##				Run the battle function with dragon as enemy
##			Else:
##				Print didn’t understand
##	Else:
##		Print didn’t understand
##
##if dragon health is less than or equal to 0:
##	run the player_win function
##	

#**********************************************************




import turtle
import random

#lists of all spells/items/equipment in the game

#[name,cost,heal/damage]
burger = ["burger",10,15]
cookie = ["cookie",15,20]
cake = ["cake", 20, 25]
steak = ["steak", 200, 150]
full_cure = ["full cure",100,1000]
burn_heal = ["burn heal",50,0]
poison_heal = ["poison heal", 50,0]
paralysis_heal = ["paralysis heal",50,0]
confuse_heal = ["confuse heal",50,0]
dynamite = ["dynamite", 20, 100]
rock = ["rock", 2, 10]
ether = ["ether",100,10]
ether2 = ["ether2",150,25]
max_ether = ["max ether", 250,200]

brother = ["a girl's lost brother"]
lost_ring = ["A lost Ring"]
princess = ["The Princess!"]

heal_item_list = [burger,cookie,cake,steak,full_cure]
mana_item_list = [ether,ether2,max_ether]

damage_item_list = [dynamite,rock]

status_item_list = [burn_heal,poison_heal,paralysis_heal,confuse_heal]

item_list = [heal_item_list,damage_item_list,status_item_list,mana_item_list]


#[spell name,gil cost, mana cost,attack bonus ]

magic_missle = ["magic missile", 0, 2, 1]
fireball = ["fire ball", 200, 20, 10]
earthquake = ["earthquake", 250,25,15]
tsunami = ["tsunami",300,30,25]
fireball_d = ["fire ball", 0, 20, 60]
earthquake_d = ["earthquake", 0,25,60]
tsunami_d = ["tsunami",0,30,65]
knights_of_the_round = ["knights of the round", 0, 40, 60]

damage_spell_list = [magic_missle,knights_of_the_round,fireball,earthquake,tsunami,fireball_d,earthquake_d,tsunami_d]

#[spell name,gil cost, mana cost,heal bonus ]
cure1 = ["cure1",100,10,2]
cure2 = ["cure2",250,20,4]
max_cure =["max cure", 400, 30, 10]
heal_spell_list = [cure1,cure2,max_cure]

#[spell name,gil cost, mana cost ]

poison = ["poison", 100, 15]
burn = ["burn", 200, 20]
paralysis = ["paralysis", 200, 20]
confuse = ["confuse", 200, 10]
poison_fang = ["Poison Fang", 0, 10]
fire_breath = ["Fire Breath",0,10]
dragon_eyes = ["Dragon Eyes", 0, 10]
piercing_eye = ["Piercing Eye", 0, 10]



status_spell_list = [poison,burn,paralysis,confuse,poison_fang,fire_breath,dragon_eyes,piercing_eye]

spell_list = [damage_spell_list,heal_spell_list,status_spell_list]
#[armor name, defense bonus]
tunic = ["tunic", 1 , "not sell"]
basic_armor = ["basic armor", 2, "not sell"]
knights_armor = ["knights armor", 10, "not sell"]
magic_armor = ["magic armor", 20, "not sell"]

berserker_armor = ["berserker armor", 60, "not sell"]

armor_list = [basic_armor,berserker_armor,tunic,knights_armor,magic_armor]
heavy_armor = [berserker_armor,knights_armor]
lightning_armor = [berserker_armor,knights_armor]

stick = ["stick", 1, "not sell"]
iron_sword = ["iron sword",2, "not sell"]
steel_sword = ["steel sword", 10, "not sell"]
magic_sword = ["magic sword", 20, "not sell"]
dragon_slayer = ["dragon slayer", 60, "not sell"]

weapon_list = [stick,iron_sword,steel_sword,magic_sword,dragon_slayer]

# dictionary of all the possible status effects

status_ail_player = {"Poison" : 0, "Confuse": 0, "Burn": 0, "Paralysis": 0 }
status_ail_enemy = {"Poison" : 0, "Confuse": 0, "Burn": 0, "Paralysis": 0 }

#list of all enemyies in the game, in this format:
#[Name, Max HP, HP, Max MP, MP, Strength, Defense, Magic, Res,Dex,Acc,Spd,
#[abl],[Inv],gil,EXP,[Drp],LVL]

#woods enemys
wolf = ["Wolf",10,10,0,0,1,1,1,1,1,1,1,["enemy attack"],[],15,25,[iron_sword,basic_armor,cookie],1]
wolf_start = ["Wolf",10,10,0,0,1,1,1,1,1,1,1,["enemy attack"],[],15,25,[iron_sword,basic_armor,cookie],1]
wolf_escape = ["Wolf",10,10,0,0,1,1,1,1,1,1,1,["enemy attack"],[],15,25,[iron_sword,basic_armor,cookie],1]

fuming_shroom = ["Fuming Shroom",15,15,200,200,1,1,2,2,1,1,2,[confuse,poison,"enemy attack"],[],15,25,[iron_sword,basic_armor,cookie],1]
fuming_shroom_start = ["Fuming Shroom",15,15,200,200,1,1,2,2,2,2,2,[confuse,poison,"enemy attack"],[],15,25,[iron_sword,basic_armor,cookie],1]
fuming_shroom_escape = ["Fuming Shroom",15,15,200,200,1,1,2,2,2,2,2,[confuse,poison,"enemy attack"],[],15,25,[iron_sword,basic_armor,cookie],1]

dire_wolf = ["Dire Wolf", 50,50,200,200,3,3,3,3,3,3,3,["enemy attack",piercing_eye,poison_fang],[],100,100,[lost_ring],1]
dire_wolf_escape = ["Dire Wolf", 50,50,200,200,3,3,3,3,3,3,3,["enemy attack",piercing_eye,poison_fang],[],100,100,[lost_ring],1]
dire_wolf_dead = ["Dire Wolf", 50,0,200,200,3,3,3,3,3,3,3,["enemy attack",piercing_eye,poison_fang],[],100,100,[lost_ring],1]




#mountain enemys
goblin= ["Goblin",35,35,100,100,4,4,0,0,3,3,4,["enemy attack", "use item", poison],[rock,
dynamite,rock,rock,rock,burger,burger],50,50,[rock,dynamite,steel_sword,knights_armor,steak],2]
goblin_start= ["Goblin",35,35,100,100,4,4,0,0,3,3,4,["enemy attack", "use item", poison],[rock,
dynamite,rock,rock,rock,burger,burger],50,50,[rock,dynamite,steel_sword,knights_armor,steak],2]
goblin_escape= ["Goblin",35,35,100,100,4,4,0,0,3,3,4,["enemy attack", "use item", poison],[rock,
dynamite,rock,rock,rock,burger,burger],50,50,[rock,dynamite,steel_sword,knights_armor,steak],2]

orc = ["Orc",60,60,100,100,6,6,4,4,5,4,2,["enemy attack",burn,piercing_eye],[],75,75,[steel_sword,knights_armor,steak],2]
orc_start = ["Orc",60,60,100,100,6,6,4,4,5,4,2,["enemy attack",burn,piercing_eye],[],75,75,[steel_sword,knights_armor,steak],2]
orc_escape = ["Orc",60,60,100,100,6,6,4,4,5,4,2,["enemy attack",burn,piercing_eye],[],75,75,[steel_sword,knights_armor,steak],2]

goblin_king = ["Goblin King", 150,150,1000,1000,7,7,7,7,7,7,7,["enemy attack", "use item",piercing_eye,poison,confuse],[dynamite,burger,burger],200,400,[brother]]
goblin_king_escape = ["Goblin King", 150,150,1000,1000,7,7,7,7,7,7,7,["enemy attack", "use item",piercing_eye,poison,confuse],[dynamite,burger,burger],400,200,[brother]]
goblin_king_dead = ["Goblin King", 150,0,1000,1000,7,7,7,7,7,7,7,["enemy attack", "use item",piercing_eye,poison,confuse],[dynamite,burger,burger],200,400,[brother]]

#swamp enemys
witch = ["Witch",100,100,200,200,0,4,9,9,7,7,7,[tsunami,fireball,earthquake,"use item"],[ether2,ether2,ether2],150,150,[magic_armor,magic_sword,full_cure],3]
witch_start = ["Witch",100,100,200,200,0,4,9,9,7,7,7,[tsunami,fireball,earthquake,"use item"],[ether2,ether2,ether2],150,150,[magic_armor,magic_sword,full_cure],3]
witch_escape = ["Witch",100,100,200,200,0,4,9,9,7,7,7,[tsunami,fireball,earthquake,"use item"],[ether2,ether2,ether2],150,150,[magic_armor,magic_sword,full_cure],3]

warlock = ["Witch",150,100,200,200,0,4,9,9,7,7,7,[tsunami,fireball,earthquake,"use item"],[ether2,ether2,ether2],175,200,[magic_armor,magic_sword,full_cure],3]
warlock_start = ["Witch",150,100,200,200,0,4,9,9,7,7,7,[tsunami,fireball,earthquake,"use item"],[ether2,ether2,ether2],175,200,[magic_armor,magic_sword,full_cure],3]
warlock_escape = ["Witch",150,100,200,200,0,4,9,9,7,7,7,[tsunami,fireball,earthquake,"use item"],[ether2,ether2,ether2],175,200,[magic_armor,magic_sword,full_cure],3]
    
necromancer = ["Necromancer",300,300,1000,1000,9,2,9,9,8,8,8,[tsunami,fireball,earthquake,confuse,poison,burn,cure1,"use item"],[ether2,ether2,ether2],300,500,[dragon_slayer],3]
necro5mancer_escape = ["Necromancer",300,300,1000,1000,9,2,9,9,8,8,8,[tsunami,fireball,earthquake,confuse,poison,burn,cure1,"use item"],[ether2,ether2,ether2],500,300,[dragon_slayer],3]
necromancer_dead = ["Necromancer",300,0,1000,1000,9,2,9,9,8,8,8,[tsunami,fireball,earthquake,confuse,poison,burn,cure1,"use item"],[ether2,ether2,ether2],300,500,[dragon_slayer],3]

#castle enemys
mimic = ["Mimic", 200,200,1000,1000,15,10,10,10,10,10,10,["enemy attack"],[],1000,500,[magic_armor,magic_sword],4]
mimic_escape = ["Mimic", 200,200,1000,1000,15,10,10,10,10,10,10,["enemy attack"],[],1000,500,[magic_armor,magic_sword],4]
mimic_start = ["Mimic", 200,200,1000,1000,15,10,10,10,10,10,10,["enemy attack"],[],1000,500,[magic_armor,magic_sword],4]


dragon = ["Dragon", 500, 500, 1000,1000,10,10,10,10,10,10,10,[poison_fang,fire_breath,fireball_d,dragon_eyes,earthquake_d,piercing_eye,"enemy attack"],[],1000,1000,[princess],4]
dragon_escape = ["Dragon", 250, 250, 1000,1000,10,10,10,10,10,10,10,[poison_fang,fire_breath,fireball_d,dragon_eyes,earthquake_d,piercing_eye,"enemy attack"],[tunic],1000,1000,[princess],4]
dragon_dead = ["Dragon", 250, 0, 1000,1000,10,10,10,10,10,10,10,[poison_fang,fire_breath,fireball_d,dragon_eyes,earthquake_d,piercing_eye,"enemy attack"],[tunic],1000,1000,[princess],4]


#Player list
#[Name, Max HP, HP, Max MP, MP, Strength, Defense, Magic, Res,Dex,Acc,Spd,
#[spells],[INV],[armor],[weapon],Dn,gil,EXP,lightning hit,level_up]
player = ["",30,30,10,10,1,1,1,1,1,1,1,[magic_missle],[rock,tunic,stick,cake,cookie,poison_heal],tunic,stick,0,50,0,0,50]



#all battle mechanic functions
#basic attacks
def player_attack(attacker,defender):
    """ Attack function to be used when the player chooses to attack, can return a regualar hit,
    a crit, or a miss """
    dex_check = random.randint(1,10)
    percent_chance = (attacker[10]/defender[9])*10
    critical = random.randint(1,10)
    if percent_chance >= dex_check:
        if critical > 9:
            defender[2] = defender[2] - (attacker[5]+attacker[15][1])*2
            return str(attacker[0])+ " hit for "+str(((attacker[5]+attacker[15][1])*2))+" damage.A critical HIT!"
        if defender[6]*defender[17] >= attacker[5]+attacker[15][1]:
            defender[2] = defender[2] - 1
            return attacker[0]+" hit for 1 damage"
        else:
            defender[2] = defender[2] -((attacker[5]+attacker[15][1]) - (defender[6]*defender[17]))
            return str(attacker[0])+" hit for "+str((attacker[5]+attacker[15][1]) - (defender[6]))+" damage"
    else:
        return "The "+defender[0]+" avoided the attack!"

def enemy_attack(attacker,defender):
    """ Attack function to be used when the enemy chooses to attack, can return a regualar hit,
    a crit, or a miss """
    dex_check = random.randint(1,10)
    percent_chance = (attacker[10]/defender[9])*10
    critical = random.randint(1,10)
    if percent_chance >= dex_check:
        if critical > 9:
            defender[2] = defender[2] - (attacker[5]*attacker[17])*2
            return str(attacker[0])+ " hit for "+str(((attacker[5]*attacker[17])*2))+" damage.A critical HIT!"
        if defender[6]+defender[14][1] >= attacker[5]*attacker[17]:                
            defender[2] = defender[2] - 1
            return attacker[0]+" hit for 1 damage"
        else:
            defender[2] = defender[2] -((attacker[5]*attacker[17]) - (defender[6]+defender[14][1]))
        return str(attacker[0])+" hit for "+str((attacker[5]*attacker[17]) - (defender[5]+defender[14][1]))+" damage"
    else:
        return "The "+defender[0]+" avoided the attack!"
# using spells    
def use_spell(user,defender,spell,spell_list,status_ail_player,status_ail_enemy):
    """spell functin to be used when enemy/player decides to use a spell. If it is a damage spell it
    can return a regular hit, a crit,or a miss, if player has the berserker armor equipped, then that
    is taken into account when calculating damage. If it is a heal spell it heals the user based on the magic
    and the spell they used. If they used a status inflicting move then they can either hit to cause a status
    ailment or miss. If they don't have enough mana it prints out that they didn't have enough mana.
    """
    
    if spell[2] > user[4]:
        return str(user[0])+" tried to use "+str(spell[0])+" but they didn't have enought mana"
    else:
        user[4] = user[4] - spell[2]

        if spell in damage_spell_list:         

            dex_check = random.randint(1,10)
            percent_chance = (user[10]/defender[9])*10
            crit = random.randint(1,10)
            
            if percent_chance >= dex_check:
                if crit > 9:
                    defender[2] = defender[2] - ((user[7]+spell[3]))*2
                    return str(user[0])+" used "+str(spell[0])+" and delt "+str((user[7]+spell[3])*2) +"damage"
                elif defender[14] == berserker_armor:
                    if  ((user[7]+spell[3])-(defender[8]+defender[14][1])) > 0:
                        defender[2] = defender[2] - ((attacker[7]+spell[3])-(defender[8]+defender[14][1]))
                        return str(user[0])+" used "+str(spell[0])+" and hit for "+str((user[7]+spell[3])-(defender[8]+defender[14][1]))+"damage!"
                    else: 
                        defender[2] = defender[2] - 1
                        return str(user[0])+" used "+str(spell[0])+" and hit for 1 damage!"
                elif ((user[7]+spell[3])-(defender[8])) > 0:
                    
                    defender[2] = defender[2] - ((user[7]+spell[3])-(defender[8]))
                    return str(user[0])+" used "+str(spell[0])+" and hit for "+str((user[7]+spell[3])-(defender[8]))+" damage!"
                else:
                    defender[2] = defender[2] - 1
                    return str(user[0])+" used "+str(spell[0])+" and hit for 1 damage!"
            else:
                return str(user[0])+"Tried to use "+ str(spell[0]) +" but they missed!"
        if spell in heal_spell_list:
            start_health = user[2]
            user[2] = user[2] + (user[7]*spell[3])
            if user[2] > user[1]:
                user[2] = user[1]
            return str(user[0])+" healed themself "+ str(user[2] -start_health) + " points!"
        if spell in status_spell_list:
            dex_check = random.randint(1,10)
            percent_chance = (user[10]/defender[9])*10*(3/4)
            
            if dex_check <= percent_chance:
                if user[0] == player[0]:
                    if spell == poison or spell == poison_fang:
                        if spell == poison:                            
                            status_ail_enemy["Poison"] = 1                        
                            return str(user[0])+" used Poison and " + str(defender[0]) + " was poisoned!"
                        if spell == poison_fang:                            
                            status_ail_enemy["Poison"] = 1
                            return str(user[0])+" used Poison Fang and " + str(defender[0]) + " was poisoned!"
                    if spell == burn or spell == fire_breath:
                        if spell == burn:                            
                            status_ail_enemy["Burn"] = 1
                            return str(user[0])+" used Burn and the " +str(defender[0]) + " became burned!"
                        if spell == fire_breath:                            
                            status_ail_enemy["Burn"] = 1
                            return str(user[0])+" used Fire Breath and " +str(defender[0]) + " became burned!"
                    if spell == paralysis or spell == piercing_eye:
                        if spell == paralysis:
                            status_ail_enemy["Paralysis"] = 1
                            return "The "+str(user[0])+" used Paralysis " +str(defender[0]) + " was paralyized!"
                        if spell == piercing_eye:
                            status_ail_enemy["Paralysis"] = 1
                            return "The "+str(user[0])+" used Piercing Eyes " +str(defender[0]) + " was paralyized!"
                            
                        
                    if spell == confuse or spell == dragon_eyes:
                        if spell == confuse:
                            status_ail_enemy["Confuse"] = 1
                            return str(user[0]) +" used Confuse and "+str(defender[0]) + " became confused!"
                        if spell == dragon_eyes:
                            status_ail_enemy["Confuse"] = 1
                            return str(user[0]) +" used Dragon Eyes and "+str(defender[0]) + " became confused!"
                else:
                    if spell == poison or spell == poison_fang:
                        if spell == poison:                            
                            status_ail_player["Poison"] = 1
                            return str(user[0])+" used Poison and " + str(defender[0]) + " was poisoned!"
                        if spell == poison_fang:                            
                            status_ail_player["Poison"] = 1
                            return str(user[0])+" used Poison Fang and " + str(defender[0]) + " was poisoned!"
                    if spell == burn or spell == fire_breath:
                        if spell == burn:                            
                            status_ail_player["Burn"] = 1
                            return str(user[0])+" used Burn and""The " +str(defender[0]) + " became burned!"
                        if spell == fire_breath:                            
                            status_ail_player["Burn"] = 1
                            return str(user[0])+" used Fire Breath and""The " +str(defender[0]) + " became burned!"
                    if spell == paralysis or spell == piercing_eye:
                        if spell == paralysis:
                            status_ail_player["Paralysis"] = 1
                            return "The "+str(user[0])+" used Paralysis " +str(defender[0]) + " was paralyized!"
                        if spell == piercing_eye:
                            status_ail_player["Paralysis"] = 1
                            return "The "+str(user[0])+" used Piercing eyes " +str(defender[0]) + " was paralyized!"
                            
                        
                    if spell == confuse or spell == dragon_eyes:
                        if spell == confuse:
                            status_ail_player["Confuse"] = 1
                            return str(user[0]) +" used Confuse and "+str(defender[0]) + " became confused!"
                        if spell == dragon_eyes:
                            status_ail_player["Confuse"] = 1
                            return str(user[0]) +" used Dragon Eyes and "+str(defender[0]) + " became confused!"
            else:
                return str(user[0])+" tried to use "+ str(spell[0]) +" but they missed!"
                    
                
                
                


#using items
def use_item(user,defender,item_list,item,status_ail_player):
    """funcion to use an item, the item can either, heal the user, hurt the user's targer,
    or cure the user of their status ailement"""
    if item in user[13]:
        if item in heal_item_list:
            start_health = user[2]
            user[2] = user[2] + item[2]
            if user[2] > user[1]:
                user[2] = user[1]            
            user[13].remove(item)
            return str(user[0]) + " used "+str(item[0])+" and was healed "+str(user[2] - start_health)+" points!"

        if item in status_item_list:
            if item == poison_heal:
                status_ail_player["Poison"] = 0                
                user[13].remove(item)
                return str(user[0])+" was healed of their poison"
            if item == burn_heal:                
                user[13].remove(item)
                status_ail_player["Burn"] = 0
                return str(user[0])+"was healed of their burn"
            if item == paralysis_heal:                
                user[13].remove(item)
                status_ail_player["Paralysis"] = 0
                return str(user[0])+" was healed of their paralysis"
            if item == confuse_heal:                
                user[13].remove(item)
                status_ail_player["Confuse"] = 0
                return str(user[0])+" was healed of their confusion"            
        if item in damage_item_list:
        
            defender[2] = defender[2]- item[1]        
            user[13].remove(item)
            return str(user[0])+" used "+str(item[0])+" and delt "+str(item[1])+" damage!"
        if item in mana_item_list:
            user[4] = user[3] + item[2]
            user[13].remove(item)
            if user[4] > user[3]:
                user[4] = user[3]
            print("{0} regained {1} mana!".format(user[0],item[2]))
    elif item in item_list and item not in user[13]:
        return str(user[0])+" tried to use "+str(item[0])+"but they didn't have one"
    elif user[13] == []:
        return str(user[0])+" tried to use an item, but they didn't have anything to use"

    
#The status ailments effects
    
def poisoned(inflicted):
    """calculates how much poison damage is done to the inflicted player/enemy and retuns that they have taken that much damage"""
    inflicted[2] = inflicted[2] - round(inflicted[2]* (1/16))
    return str(inflicted[0])+" took "+str(round(inflicted[2]* (1/16)))+" points of poison damage"

def burned(inflicted):
    """calculates how much burn damage is done to the inflicted player/enemy and retuns that they have taken that much damage"""
    inflicted[2] = inflicted[2] - round(inflicted[2]* (3/16))
    return str(inflicted[0])+" took "+str(round(inflicted[2]* (3/16)))+" points of burn damage"

def confused_attack(inflicted):
    inflicted[2] = inflicted[2] - inflicted[5]
    return "In the confusion "+ str(inflicted[0]) + " hit themself for " + str(inflicted[5]) + " damage!"
#misc
def check(enemy):
    """a function that allows the player to see how much health the enemy has"""
    return str(enemy[0])+": "+str(enemy[2])+"/"+str(enemy[1])

def escape(player,enemy):
    """a function that decides if the player can escape a battle. If the player gets way
    over their head, i.e. the enemy has a much higher acc stat, then they still have 3/10
    chance of escaping."""
    escape_chance = random.randint(1,10)
    escape_percent = (player[9]/enemy[10])*10
    escape_lucky_break = random.randint(1,10)

    if escape_percent >= escape_chance or escape_lucky_break > 7:
        return True
    else:
        return False



#functions/variables that deal with level ups and other end of battle functions

level_up = 50

def level_up_check (player, level_up):
    """A function to be used at the end of a battle, it checks to see if the player has enough experiance to gain a level,
    if they do the player has a 1 in 2 chance of increasing each on of their stats. The maximum amount any stat can reach
    (excluding max hp and max mp) is 10. The function keeps looping until the player no longer has enough exp to level up
    if the player did level up it returns the players new stats, otherwise it starts a new line"""
    loop = 0
    while player[18] >= player[20]:
        player[18] = player[18] - player[20]
        player[20] = player[20] +50
        increase_Mxhp = random.randint(0,2)
        increase_Mxmp = random.randint(0,2)
        increase_str = random.randint(0,1)
        increase_def = random.randint(0,1)
        increase_mg = random.randint(0,1)
        increase_res = random.randint(0,1)
        increase_dex = random.randint(0,1)
        increase_acc = random.randint(0,2)
        increase_sp = random.randint(0,1)

        if increase_Mxhp > 0:
            increased_mxhp = random.randint(1,3)
            player[1] = player[1] + 10*increased_mxhp
        if increase_Mxmp > 0:
            increased_mxmp = random.randint(1,3)
            player[3] = player[3] + 5*increased_mxmp
        if increase_str == 1:
            str_increase = random.randint(1,3)
            player[5] = player[5] + str_increase
            if player[5] > 10:
                player[5] = 10
        if increase_def == 1:
            def_increase = random.randint(1,3)
            player[6] = player[6] + def_increase
            if player[6] > 10:
                player[6] = 10
        if increase_mg == 1:
            mg_increase = random.randint(1,3)
            player[7] = player[7] + mg_increase
            if player[7] > 10:
                player[7] = 10
        if increase_res == 1:
            res_increase = random.randint(1,3)
            player[8] = player[8] + res_increase
            if player[8] > 10:
                player[8] = 10
        if increase_dex == 1:
            dex_increase = random.randint(1,3)
            player[9] = player[9] + dex_increase
            if player[9] > 10:
                player[9] = 10
        if increase_acc > 0:
            acc_increase = random.randint(1,3)
            player[10] = player[10] + acc_increase
            if player[10] > 10:
                player[10] = 10
        if increase_sp == 1:
            sp_increase = random.randint(1,3)
            player[11] = player[11] + sp_increase
            if player[11] > 10:
                player[11] = 10
        loop = loop +1
    if loop > 0:
        return "You Leveled UP!!!!\nHit points: "+str(player[1])+"\nMagic Points: "+str(player[3])+"\nStrength: "+str(player[5])+"\nDefense: "+str(player[6])+"\nMagic: "+str(player[7])+"\nResitance: "+str(player[8])+"\nDexterity: "+str(player[9])+"\nAccuracy: "+str(player[10])+"\nSpeed: "+str(player[11])+"\nTo next level: "+str(player[20])
    else:
        return "\n"

def lose_battle():
    """a function that pulls up an image indicating that the player has died"""
    lost = turtle.Screen()
    lost.bgpic("tombstone.png")
    lost.mainloop()
    return lost
        
        
#battle function

def battle(player,enemy,spell_list,item_list,status_ail_player,status_ail_enemy,enemy_start,enemy_escape):
    """ Function to be used when the player is attacked by an enemy, player can attack,use spell, use item, check the enemy, and escape"""
    print("You were attacked by a "+str(enemy[0])+"\n")
    para = 0
    con = 0
    para2 = 0
    con2 = 0
   
    
    while player[2] > 0 and enemy[2] > 0:
        check1 = 0
        check2 = 0
        check3 = 0
        check4 = 0
        
        print("Health: "+str(player[2])+"/"+str(player[1])+ " Mana: " +str(player[4])+"/"+ str(player[3]))
        action = input("What would you like to do? Attack, Spell, Use item, Check or Escape: ")
        if action == "spell" or action == "Spell":
            for i in range(len(player[12])):
                print(str(player[12][i][0])+": (cost)"+str(player[12][i][2]))
            spell = input("Which spell would you like to use?(cancel to go back): ")
            for m in range(len(spell_list)):
                for k in range(len(spell_list[m])):
                    for z in range(len(spell_list[m][k])):
                        if spell == spell_list[m][k][z]:
                            check1 = 1
                    
            if check1 != 1:                    
                print("don't know what that is")
                continue
            for y in range(len(player[12])):
                for x in range(len(player[12][y])):
                    if spell == player[12][y][x]:                  
                        check2 = 1
                        spell = player[12][y]
                    
            if check2 != 1:
                print("You don't know that one yet")
                continue
            elif spell == "cancel":
                continue               
                           
        if action == "use item" or action == "Use item":
            if player[13] == []:
                print("You don't have anything to use")
                continue                
            else:
                for h in range(len(player[13])):
                    if player[13][h] in heal_item_list or player[13][h] in damage_item_list or player[13][h] in mana_item_list or player[13][h] in status_item_list:
                        print(str(player[13][h][0]))
                item = input("What would you like to use?(cancel to go back): ")
                for n in range(len(item_list)):
                    for o in range(len(item_list[n])):
                        for p in range(len(item_list[n][o])):
                            if item == item_list[n][o][p]:
                                check3 = 1
                if check3 != 1 and (item not in weapon_list or item not in armor_list):
                                    print("You can't use that one" )
                                    continue
                
                for d in range(len(player[13])):
                    for e in range(len(player[13][d])):
                        if item == player[13][d][e]:
                            check4 = 1
                            item = player[13][d]
                if check4 != 1:
                    print("you don't have one of those")
                    continue
                elif item == "cancel":
                        continue             
        if action != "attack" and action != "Attack" and action != "spell" and action != "Spell" and action != "Use item" and action != "use item" and action != "Escape" and action != "escape" and action != "Check" and action != "check":
            print("did not understand")
            continue
            

        speed_tie = random.randint(0,1)
        paralysis_player = random.randint(0,1)
        paralysis_enemy = random.randint(0,1)
        confuse_player = random.randint(0,2)
        confuse_enemy = random.randint(0,2)
        if player[11] > enemy[11] or (player[11] == enemy[11] and speed_tie == 1):
            if status_ail_player["Paralysis"] == 1 and paralysis_player == 1 :
                print("You tried to act, but you were paralyzed")
                para2 = para2 +1        
                if para2 % 4:                    
                    print("You were cured of your paralysis")
                    status_ail_player["Paralysis"] = 0
                    para2 = para2 +1
            elif status_ail_player["Confuse"] == 1 and confuse_player > 0 :
                print(confused_attack(player))
                con2 = con2 + 1
                if con2%3 == 0:                    
                    print("You were cured of your confusion")
                    status_ail_player["Confuse"] = 0
                    con2 = con2 +1
            elif action == "spell" or action == "Spell":
                print(use_spell(player,enemy,spell,spell_list,status_ail_player,status_ail_enemy))
                if enemy[2] <= 0:
                    break
            elif action == "attack" or action == "Attack":
                print(player_attack(player,enemy))
                if enemy[2] <= 0:
                    break
            elif action == "Use item" or action == "use item":
                print(use_item(player,enemy,item_list,item,status_ail_player))
                if enemy[2] <= 0:
                    break
                
            elif action == "check" or action == "Check":
                print(check(enemy))
            elif action == "escape" or action == "Escape":
                
                if escape(player,enemy):
                    print("You escaped safely!")
                    status_ail_enemy["Poison"] = 0
                    status_ail_enemy["Burn"] = 0
                    status_ail_enemy["Confuse"] = 0
                    status_ail_enemy["Paralysis"] = 0
                    enemy[2] = enemy_escape[2]
                    enemy[13] = enemy_escape[13]
                    enemy[3] = enemy_escape[4]
                    return enemy
                else:
                    print("You tried to escape, but couldn't!")
            enemy_choose = random.randint(0,(len(enemy[12]) -1) )
            enemy_move = enemy[12][enemy_choose]
            if status_ail_enemy["Paralysis"] == 1 and paralysis_enemy == 1 :
                print("The enemy tried to act, but they were paralyzed")
                para = para +1        
                if para % 4 == 0:                    
                    print("The enemy was cured of their paralysis")
                    status_ail_enemy["Paralysis"] = 0
                    para = para +1
            elif status_ail_enemy["Confuse"] == 1 and confuse_enemy > 0 :
                print(confused_attack(enemy))
                con = con + 1
                if con%3 == 0:                    
                    print("The enemy was cured of their confusion")
                    status_ail_enemy["Confuse"] = 0
                    con = con +1
            elif enemy_move == "enemy attack":
                print(enemy_attack(enemy,player))
            elif enemy_move == "use item":
                choose_item = random.randint(0,(len(enemy[13]) - 1))
                choose_item = enemy[13][choose_item]
                print(use_item(enemy,player,item_list,choose_item,status_ail_player))
            elif enemy_move in status_spell_list or enemy_move in heal_spell_list or enemy_move in damage_spell_list:
                print(use_spell(enemy,player,enemy_move,spell_list,status_ail_player,status_ail_enemy))
            else:
                print('error')
        else:
            enemy_choose = random.randint(0,(len(enemy[12]) -1) )
            enemy_move = enemy[12][enemy_choose]
            if status_ail_enemy["Paralysis"] == 1 and paralysis_enemy == 1 :
                print("The enemy tried to act, but they were paralyzed")
                para = para +1        
                if para % 4==0:                    
                    print("The enemy was cured of their paralysis")
                    status_ail_enemy["Paralysis"] = 0
                    para = para +1
            elif status_ail_enemy["Confuse"] == 1 and confuse_enemy > 0 :
                print(confused_attack(enemy))
                con = con + 1
                if con%3 == 0:                    
                    print("The enemy was cured of their confusion")
                    status_ail_enemy["Confuse"] = 0
                    con = con +1
            elif enemy_move == "enemy attack":
                print(enemy_attack(enemy,player))
                if player[2] <= 0:
                    break
            elif enemy_move in status_spell_list or enemy_move in heal_spell_list or enemy_move in damage_spell_list:
                print(use_spell(enemy,player,enemy_move,spell_list,status_ail_player,status_ail_enemy))
                if player[2] <= 0:
                    break
            elif enemy_move == "use item":
                choose_item = random.randint(0,(len(enemy[13]) - 1))
                choose_item= enemy[13][choose_item]
                print(use_item(enemy,player,item_list,choose_item,status_ail_player))
                if player[2] <= 0:
                    break
            else:
                print("error")
            if status_ail_player["Paralysis"] == 1 and paralysis_player == 1 :
                print("You tried to act, but you were paralyzed")
                para2 = para2 +1        
                if para2 % 4:                    
                    print("You were cured of your paralysis")
                    status_ail_player["Paralysis"] = 0
                    para2 = para2 +1
            elif status_ail_player["Confuse"] == 1 and confuse_player > 0 :
                print(confused_attack(player))
                con2 = con2 + 1
                if con2%3 == 0:                    
                    print("You were cured of your confusion")
                    status_ail_player["Confuse"] = 0
                    con2 = con2 +1
         
               
            elif action == "spell" or action == "Spell":
                print(use_spell(player,enemy,spell,spell_list,status_ail_player,status_ail_enemy))
            elif action == "attack" or action == "Attack":
                print(player_attack(player,enemy))
            elif action == "Use item" or action == "use item":
                print(use_item(player,enemy,item_list,item,status_ail_player))                
            elif action == "check" or action == "Check":
                print(check(enemy))
            elif action == "escape" or action == "Escape":
                
                if escape(player,enemy):
                    print("You escaped safely!")
                    status_ail_enemy["Poison"] = 0
                    status_ail_enemy["Burn"] = 0
                    status_ail_enemy["Confuse"] = 0
                    status_ail_enemy["Paralysis"] = 0
                    enemy[2] = enemy_escape[2]
                    enemy[13] = enemy_escape[13]
                    enemy[3] = enemy_escape[4]
                    return enemy
                else:
                    print("You tried to escape, but couldn't!")
        if status_ail_player["Poison"] == 1:
            print(poisoned(player))
        if status_ail_player["Burn"] == 1:
            print(burned(player))
        if status_ail_enemy["Poison"] == 1:
            print(poisoned(enemy))
        if status_ail_enemy["Burn"] == 1:
            print(burned(enemy))
                          




            
    if player[2] <= 0:
        print("You fell in battle!")
        return print(lose_battle())
    
    elif enemy[2] <= 0:
        
        print("You WON!!!!")
        get_item = random.randint(0,(len(enemy[16])-1))
        player[13].append(enemy[16][get_item])
        print("You recieved: "+str(enemy[16][get_item][0]))
        player[18] = player[18] +enemy[15]
        print("You recieved: "+str(enemy[15])+"EXP")
        player[17] = player[17] + enemy[14]
        print("You recieved: "+str(enemy[14])+" gil")
        print(level_up_check(player,level_up))
        status_ail_enemy["Poison"] = 0
        status_ail_enemy["Burn"] = 0
        status_ail_enemy["Confuse"] = 0
        status_ail_enemy["Paralysis"] = 0
        enemy[2] = enemy_start[2]
        enemy[13] = enemy_start[13]
        enemy[4] = enemy_start[3]
        
        return print(level_up_check(player,level_up)),enemy
    else:
        return print("\n")
        
    
    
        


# outside of battle functions

def equip(player,armor_list, weapon_list,heavy_amor,lightning_armor):
    """A functon to be used when the player wants to equip/de-quip their armor/weapon"""
    
    choice1 = ""
    while choice1 != "end":
        check_if_in =0
        choice1 = input("What would you like to do?(equip/dequip/end): ")
        if choice1 == "equip":
            choice2 = input("What would you like to equip?(weapon/armor): ")
            if choice2 == "weapon" :
                for i in range(len(player[13])):
                    if player[13][i] in weapon_list:
                        print(str(player[13][i][0])+": {0}".format(player[13][i][1]))
                choice3 = input("\nwhat would you like to equip: ")
                for j in range(len(player[13] )):
                        if choice3 == player[13][j][0]:
                            check_if_in = 1
                            choice3 = player[13][j]
                if check_if_in != 1:
                        print( "You dont' have that!")
                        continue
                elif choice3 in weapon_list:
                   
                
                    player[15] = choice3
                    print( "You equiped: "+str(player[15][0]))
                    player[13]
                else:
                    print("cant equip that")
                    continue
                
            if choice2 == "armor" :
                for i in range(len(player[13])):
                    if player[13][i] in armor_list:
                        print(str(player[13][i][0])+": {0}".format(player[13][i][1]))
                choice3 = input("\nwhat would you like to equip: ")
                for j in range(len(player[13] )):
                        if choice3 == player[13][j][0]:
                            check_if_in = 1
                            choice3 = player[13][j]
                if check_if_in != 1:
                        print( "You dont' have that!")
                        continue
                elif choice3 in armor_list:
                   
                
                    player[14] = choice3
                    print( "You equiped: "+str(player[14][0]))
                    if player[14] in heavy_armor:
                        player[16] = 2
                        print("you felt quite heavy")
                    if player[14] in lightning_armor:
                        player[19] = 1
                        print("you felt like you better not wear this in a storm")
                    
                else:
                    print("cant equip that")
            
        if choice1 == "dequip":
            choice3 = input("weapon or armor: ")
            if choice3 == "weapon":
                if player[15] != []:
                    print("You took off "+str(player[15][0]))
                    player[15] = []
                else:
                    print("you don't have a weapon equipped")
                    
            if choice3 == "armor":
                if player[14] != []:
                    print("You took off "+str(player[14][0]))
                    if player[14] in heavy_armor:
                        player[16] = 0
                        print("You felt like a weight was lifted off your shoulders")
                    if player[14] in lightning_armor:
                        player[19] = 0
                        print("You felt like storms were now safer to go in")                                           
                    player[14] = []
                else:
                    print("You weren't wearing anything")
        else:
            return "\n"

def buy(player,item_list,spell_list):
    """allows players to buy spells and items, and sell items."""
    choice1 = ""
    while choice1 != "end":
        check_if_in = 0
        print("Gil: "+str(player[17]))
        choice1 = input("What would you like to do? (buy/sell/end): ")
        if choice1 == "buy":
            choice2 = input("What would you like to buy?(item/spell): ")
            if choice2 == "item":
                for i in range(len(item_list)):
                    for j in range(len(item_list[i])):
                        print(str(item_list[i][j][0])+": "+str(item_list[i][j][1]))
                choice3 = input("What would you like to buy?: ")
                for n in range(len(item_list)):
                    for o in range(len(item_list[n])):
                        for p in range(len(item_list[n][o])):
                            if choice3 == item_list[n][o][p]:
                                check_if_in = 1
                                choice3 = item_list[n][o]
                if check_if_in != 1:
                    print("Don't know what that is.")

                else:
                    if player[17] < choice3[1]:
                        print("You don't have enough gil.")
                    else:
                        print("You bought a "+str(choice3[0]))
                        player[17] = player[17] - choice3[1]
                        player[13].append(choice3)

            if choice2 == "spell":
                for i in range(len(spell_list)):
                    for j in range(len(spell_list[i])):
                        if spell_list[i][j][1] > 0: 
                            print(str(spell_list[i][j][0])+": "+str(spell_list[i][j][1]))
                choice3 = input("What would you like to buy?: ")
                for n in range(len(spell_list)):
                    for o in range(len(spell_list[n])):
                        for p in range(len(spell_list[n][o])):
                            if choice3 == spell_list[n][o][p]:
                                check_if_in = 1
                                choice3 = spell_list[n][o]
                if check_if_in != 1:
                    print("Don't know what that is.")

                else:
                    if choice3 not in player[12]:
                        if player[17] < choice3[1]:
                            print("You don't have enough gil.")
                        else:
                            print("You bought: "+str(choice3[0]))
                            player[17] = player[17] - choice3[1]
                            player[12].append(choice3)
                    else:
                        print("You already have that one!")
        if choice1 == "sell":
            for i in range(len(player[13])):
                if player[13][i][2] != "not sell":
                    print(str(player[13][i][0])+": "+str(player[13][i][1]))
            choice2 = input("What would you like to sell?")
            for d in range(len(player[13])):
                for e in range(len(player[13][d])):
                    if choice2 == player[13][d][e]:
                        check_if_in = 1
                        choice2 = player[13][d]
            if check_if_in != 1:
                print("You don't have one of those")
            else:
                player[17] = player[17] + choice2[1]
                player[13].remove(choice2)
                print("You sold your " +str(choice2[0]))
                print("You recieved: " + str(choice2[1]))
    return "Thanks for your patronage!"
                       
#other losing conditons

def said_no():
    """function to be used if you say no to the king"""
    said_no = turtle.Screen()
    said_no.setup(904,619)
    said_no.title("Said no")
    said_no.bgpic("said no.png")
    return said_no
                                                
def lightning():
    """function to be used if the player gets struck by lightning"""
    """function to be used if you drown"""
    print(" You were struck by lighning!")
    
    struck = turtle.Screen()
    struck.setup(190,189)
    struck.bgpic("lightning.png")
    struck.mainloop()
    return struck

def drowning():
    """function to be used if the player drowns"""
    print("You drowned")
    drowned = turtle.Screen()
    drowned.setup(330,153)
    drowned.bgpic("drowning.png")
    drowned.mainloop()
    return drowned

#Winning condition
def win():
    """function to be used when the player has won"""
    print("Congratulations!!!")
    win = turtle.Screen()
    win.setup(916,226)
    win.bgpic("Saved the princess.png")
    win.mainloop()
    return win
    
                
                
#The actual game


name = input("What is your name?: ")
player[0] = name

man_count = 0


print("{1}{0}! WAKE UP!\n{1}The King has summoned you!".format(player[0],"???: "))
wait = input()
print("After thanking James you hurriedly put on your clothes and go to your summons.")
wait = input()
print("King: You are the greatest knight in this land and for that reason, I will entrust you with a mission you must tell no other")
wait = input()
print("King: My daughter has been stolen by a wreched dragon. If anyone else were to find out the kingdom would be in shambles.Will you save her?")
KingQ = input("Will you do it(yes/no)?: ")
if KingQ == "yes":
    print("King: Thank you! You are trulely a knight amoung knights!")
    while player[2] > 0 and princess not in player[13]:
        Q = input("What would you like to do?\nTalk to distressed girl\nTalk to sullen man\nTalk to disgruntled blacksmith\nstay at inn\nshop\nleave\n(girl/man/blacksmith/inn/shop/leave): ")
        if Q == "girl" and brother not in player[13] and knights_of_the_round not in player[12]:
            print("Girl: Waaa!Waaa!")
            Q2 = input("ask her what's wrong?(yes/no): ")
            if Q2 == "yes":
                print("Girl: My brother got stolen by a band of goblins on our way to the Kingdom. Please Save Him!")
                wait = input()
            else:
                continue
        if Q == "girl" and brother in player[13]:
            print("Girl: BROTHER!!! I thought you were dead for sure!!")
            wait = input()
            print("Girl's brother: I'm so glad to see you too sister!!")
            wait = input()
            print("Girl: Here mister knight, Have this. I found it on our way here!")
            player[13].remove(brother)
            player[12].append(knights_of_the_round)
            print("You learned: {0}".format(knights_of_the_round[0]))
            wait = input()
        if Q == "girl" and knights_of_the_round in player[12]:
            print("Girl: Thannks Mister!")
            wait = input()
        if Q == "man" and man_count != 1:
            print("Man: ...")
            Q2 = input("Ask him what's wrong?(yes/no): ")
            if Q2 == "yes":
                print("Man: My wife killed by that cursed Dire Wolf that lives in the woods!")
                wait = input()
                print("Man: I'll give a bounty to whoever takes that things head!")
                wait = input()
        if Q == "man" and lost_ring in player[13]:
            print("Man: Wait, you! Where did you get that ring?")
            wait = input()
            print("Man: You killed it? Really? Thank you Thank you THANK YOU, here take this!!!")
            player[13].remove(lost_ring)
            player[17] = player[17] + 1000
            print("You gave the ring back to him, and he gave you 1000 gil")
            wait = input()
            man_count = 1
        if Q == "man" and man_count == 1:
            print("Man: Thank you!!!")
            wait = input()
        if Q == "blacksmith" and dragon_slayer != player[15] and berserker_armor not in player[13]:
            print("Blacksmith: (Cursed Necromancer)")
            Q2 = input("Ask him whats wrong?(yes/no): ")
            if Q2 == "yes":
                print("Blacksmith: Buzz off")
                wait = input()
            else:
                continue
        if Q == "blacksmith" and dragon_slayer == player[15] and berserker_armor not in player[13]:
            print("Blacksmith: You managed to kill him? Impressive.")
            wait = input()
            print("Blacksmith: Here, take this. I'll never use it. It is the only armor in the world that protects against magic attacks")
            player[13].append(berserker_armor)
            
            print("You recieved: {0}".format(berserker_armor[0]))
            wait = input()
        if Q == "blacksmith" and berserker_armor in player[13]:
            print("Blacksmith:...Thanks...I guess")
            wait = input()
        if Q == "shop":
            print(buy(player,item_list,spell_list))
        if Q == "inn":
            if player[17] < 15:
                print("No Pay NO STAY!!!")
                wait = input()
            else:
                print("You payed 15 gil, health and mana restored!")
                player[2] = player[1]
                player[4] = player[3]
                status_ail_player["Poison"] = 0
                status_ail_player["Burn"] = 0
                status_ail_player["Confuse"] = 0
                status_ail_player["Paralysis"] = 0
                player[17] = player[17] - 15
                wait = input()
        if Q == "leave":
            count_forest = 0
            count_mountain = 0
            count_swamp = 0
            count_castle = 0
            where = input("Where would you like to go: forest(lvl 1), mountain (lvl 2), swamp (lvl 3), castle (lvl 4), cancel: ")
            if where == "forest":
                what = ""
                compare = 0
                while what != "leave" and player[2] > 0:
                    forest_battle = random.randint(1,8)

                    what = input("What would you like to do?(equip/use item/move/leave): ")
                   
                    compare = count_forest
                    if what == "move":
                        print("You moved forward")
                        count_forest = count_forest + 1
                    if what == "use item":
                        item = ""
                        check3 = 0
                        check4 = 0
                        while item != "cancel":
                            if player[13] == []:
                                print("You don't have anything to use")
                                break              
                            else:
                                for h in range(len(player[13])):
                                    if player[13][h] in damage_item_list or player[13][h] in heal_item_list or player[13][h] in status_item_list or player[13][h] in mana_item_list:
                                        print(str(player[13][h][0]))
                                item = input("What would you like to use?(cancel to go back): ")
                                for n in range(len(item_list)):
                                    for o in range(len(item_list[n])):
                                        for p in range(len(item_list[n][o])):
                                            if item == item_list[n][o][p]:
                                                check3 = 1
                                if check3 != 1 and (item not in weapon_list or item not in armor_list):
                                    print("You can't use that one" )
                                    continue
                                elif check3 != 1:
                                    print("did not understand")
                                    continue
                                for d in range(len(player[13])):
                                    for e in range(len(player[13][d])):
                                        if item == player[13][d][e]:
                                            check4 = 1
                                            item = player[13][d]
                                if check4 != 1:
                                    print("you don't have one of those")
                                    continue
                                else:
                                    print(use_item(player,player,item_list,item,status_ail_player))
                    if what == "equip":
                        print(equip(player,armor_list,weapon_list,heavy_armor,lightning_armor))
                    if what == "leave":
                        print("You returned to the kingdom")
                    
                    if count_forest == 10 and dire_wolf[2] >  0 and what != "leave":
                       battle(player,dire_wolf,spell_list,item_list,status_ail_player,status_ail_enemy,dire_wolf_dead,dire_wolf_escape)
                    if compare < count_forest and count_forest != 10:
                        if 1 <= forest_battle <= 2:
                            battle(player,wolf,spell_list,item_list,status_ail_player,status_ail_enemy,wolf_start,wolf_escape)
                        if 3 <= forest_battle <= 4:
                            battle(player,fuming_shroom,spell_list,item_list,status_ail_player,status_ail_enemy,fuming_shroom_start,fuming_shroom_escape)
                    
                
            if where == "mountain":
                storm = 0
                what = ""
                compare = 0
                while what != "leave" and player[2] > 0:
                    mountain_battle = random.randint(1,8)
                    storming = random.randint(1,2)
                   
                    
                    what = input("What would you like to do?(equip/use item/move/leave): ")
                    
                    compare = count_mountain
                    if what == "move":
                        print("You moved forward")
                        count_mountain = count_mountain + 1
                    if what == "use item":
                        item = ""
                        check3 = 0
                        check4 = 0
                        while item != "cancel":
                            if player[13] == []:
                                print("You don't have anything to use")
                                break              
                            else:
                                for h in range(len(player[13])):
                                    if player[13][h] in damage_item_list or player[13][h] in heal_item_list or player[13][h] in status_item_list or player[13][h] in mana_item_list:
                                        print(str(player[13][h][0]))
                                item = input("What would you like to use?(cancel to go back): ")
                                for n in range(len(item_list)):
                                    for o in range(len(item_list[n])):
                                        for p in range(len(item_list[n][o])):
                                            if item == item_list[n][o][p]:
                                                check3 = 1
                                if check3 != 1 and (item not in weapon_list or item not in armor_list):
                                    print("You can't use that one" )
                                    continue
                                else:
                                    print("did not understand")
                                    continue
                                for d in range(len(player[13])):
                                    for e in range(len(player[13][d])):
                                        if item == player[13][d][e]:
                                            check4 = 1
                                            item = player[13][d]
                                if check4 != 1:
                                    print("you don't have one of those")
                                    continue
                                else:
                                    print(use_item(player,player,item_list,item,status_ail_player))
                    if what == "equip":
                        ask = input("do you want to contine equipping?(yes/no): ")
                        while ask == "yes":
                            print(equip(player,armor_list,weapon_list,heavy_armor,lightning_armor))
                            ask = input("do you want to contine equipping?(yes/no): ")
                    if what == "leave":
                        print("You returned to the kingdom")
                    if count_mountain == 15 and goblin_king [2] > 0 and what != "leave":
                        battle(player,goblin_king,spell_list,item_list,status_ail_player,status_ail_enemy,goblin_king_dead,goblin_king_escape)
                    if compare < count_mountain and count_mountain != 15:
                        if storming == 1:
                            print("It started storming!")
                            storm = 1
                        if storming == 2:
                            print("It stopped storming!")
                            storm = 0
                        if 1 <= mountain_battle <= 2:
                            battle(player,goblin,spell_list,item_list,status_ail_player,status_ail_enemy,goblin_start,goblin_escape)
                        if 3 <= mountain_battle <= 4:
                            battle(player,orc,spell_list,item_list,status_ail_player,status_ail_enemy,orc_start,orc_escape)
                    if storm == 1 and player[19] > 0 and compare < count_mountain:
                        player[2]  = 0
                        lightning()
                    
        
            if where == "swamp":
                what = ""
                compare = 0
                while what != "leave" and player[2] > 0:
                    swamp_battle = random.randint(1,8)
                    
                    what = input("What would you like to do?(equip/use item/move/leave): ")
                    
                    compare = count_swamp 
                    if what == "move":
                        print("You moved forward")
                        count_swamp = count_swamp + 1
                    if what == "use item":
                        item = ""
                        check3 = 0
                        check4 = 0
                        while item != "cancel":
                            if player[13] == []:
                                print("You don't have anything to use")
                                break              
                            else:
                                for h in range(len(player[13])):
                                   if player[13][h] in damage_item_list or player[13][h] in heal_item_list or player[13][h] in status_item_list or player[13][h] in mana_item_list:
                                        print(str(player[13][h][0]))
                                item = input("What would you like to use?(cancel to go back): ")
                                for n in range(len(item_list)):
                                     for o in range(len(item_list[n])):
                                         for p in range(len(item_list[n][o])):
                                            if item == item_list[n][o][p]:
                                                check3 = 1
                                if check3 != 1 and (item not in weapon_list or item not in armor_list):
                                    print("You can't use that one" )
                                    continue
                                else:
                                    print("did not understand")
                                    continue
                                for d in range(len(player[13])):
                                    for e in range(len(player[13][d])):
                                        if item == player[13][d][e]:
                                            check4 = 1
                                            item = player[13][d]
                                if check4 != 1:
                                    print("you don't have one of those")
                                    continue
                                else:
                                    print(use_item(player,player,item_list,item,status_ail_player))
                    if what == "equip":
                        print(equip(player,armor_list,weapon_list,heavy_armor,lightning_armor))
                    if what == "leave":
                        print("You returned to the kingdom")
                    if count_swamp == 20 and necromancer [2] > 0 and what != "leave":
                        battle(player,necromancer,spell_list,item_list,status_ail_player,status_ail_enemy,necromancer_dead,necromancer_escape)
                    if compare < count_swamp and count_swamp != 20:
                        if 1 <= swamp_battle <= 2:
                            battle(player,witch,spell_list,item_list,status_ail_player,status_ail_enemy,witch_start,witch_escape)
                        if 3 <= swamp_battle <= 4:
                           battle(player,warlock,spell_list,item_list,status_ail_player,status_ail_enemy,warlock_start,warlock_escape)
                               
            if where == "castle":
                print("There is a moat")
                Question = input("What will you do? (swim/go back/equip): ")
                while Question != "go back" and player[2] > 0:
                    
                    if Question == "swim":
                        if player[16] > 0:
                            player[2] = 0
                            drowning()
                        what = ""
                        compare = 0
                        while what != "leave" and player[2] > 0 and princess not in player[13]:
                            castle_chest = random.randint(0,1)
                           
                                            
                                                      
                                  
                               
                            if princess not in player[13]:
                                what = input("What would you like to do?(equip/use item/move/leave): ")
                            compare = count_castle
                            if what == "move":
                                print("You moved forward")
                                count_castle = count_castle + 1
                            if what == "use item":
                                item = ""
                                check3 = 0
                                check4 = 0
                                while item != "cancel":
                                    if player[13] == []:
                                        print("You don't have anything to use")
                                        break              
                                    else:
                                        for h in range(len(player[13])):
                                           if player[13][h] in damage_item_list or player[13][h] in heal_item_list or player[13][h] in status_item_list or player[13][h] in mana_item_list:
                                                print(str(player[13][h][0]))
                                                
                                        item = input("What would you like to use?(cancel to go back): ")
                                        for n in range(len(item_list)):
                                            for o in range(len(item_list[n])):
                                                for p in range(len(item_list[n][o])):
                                                    if item == item_list[n][o][p]:
                                                        check3 = 1
                                        if check3 != 1 and (item not in weapon_list or item not in armor_list):
                                            print("You can't use that one" )
                                            continue
                                        else:
                                            print("did not understand")
                                            continue 
                                        for d in range(len(player[13])):
                                            for e in range(len(player[13][d])):
                                                if item == player[13][d][e]:
                                                    check4 = 1
                                                    item = player[13][d]
                                        if check4 != 1:
                                            print("you don't have one of those")
                                            continue
                                        
                                        else:
                                            print(use_item(player,player,item_list,item,status_ail_player))
                            if what == "equip":
                                print(equip(player,armor_list,weapon_list,heavy_armor,lightning_armor))
                            if what == "leave":
                                print("You returned to the kingdom")
                            if count_castle == 5 and dragon[2] > 0 and what != "leave":
                                battle(player,dragon,spell_list,item_list,status_ail_player,status_ail_enemy,dragon_dead,dragon_escape)
                            if compare < count_castle:
                                if  castle_chest == 0:
                                    print("You found a chest")
                                    Question  = input("What will you do? (open it/nothing): ")
                                    if Question == "open it":
                                        mimic_chance = random.randint(0,1)
                                        if mimic_chance == 0:                                                                                   
                                            battle(player,mimic,spell_list,item_list,status_ail_player,status_ail_enemy,mimic_start,mimic_escape)
                                        else:
                                            player[17] = player[17] + 1000
                                            print("You found 1000 Gil!!!")
                                
                    elif Question == "equip":
                        print(equip(player,armor_list,weapon_list,heavy_armor,lightning_armor))
                    
                    
                    
                        
                          
                     
                    if princess not in player[13]:
                        Question = input("What will you do? (swim/go back/equip): ")
                    

            

            
                    
else:
    print("King: I cannot belive your insolence!!!! Guards! TAKE HIM AWAY!")
    said_no()                       
                
if princess in player[13]:
    print("You saved the Princess!")
    win()

            

    



    

    






