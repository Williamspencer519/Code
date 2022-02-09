from sample_structures import *



def test_taking_damage_works_by_subtracting_defence_from_damage_then_applying_to_hp():
	actor = Actor()
	damage = 20
	actor.take_damage(damage)
	assert actor.hp == 90 #only take 10 damage because I have 10 defense, so 20-10 = 10 damage

def test_a_druid_can_turn_into_a_cat():
	druid = Druid()
	druid.transfrom("Cat")
	assert druid.form == "Cat"

def test_cast_moonfire_with_a_d4_plus_attack_power():
	'''this test is gonna cast moonfire a ton of times and make sure the damage falls in the expected range of attack_power + 1d4'''
	sev = Druid()
	sum_of_damage = 0
	for i in range(0,1000):
		damage = sev.moonfire()
		sum_of_damage += damage
	average_damage = sum_of_damage/1000.0
	assert average_damage > 4.2
	assert average_damage < 4.88

def test_i_can_make_a_warrior_class():
	'''you need to implement a warrior class, this one will fail by failing to even construct a warrior'''
	zaquaeis = Warrior()


def test_warrior_cleave_does_attack_power_plus_1d5():
	'''this is asserting false and will never pass.  Change this test to be like the other one for moonfire, but code in a cleave attack for the warrior'''
	assert False