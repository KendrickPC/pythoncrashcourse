# 6-12. Extensions: We aree now working with examples that are complex enough that they can be extended in any number of ways. Use one of the example pro- grams from this chapter, and extend it by adding new keys and values, chang- ing the context of the program or improving the formatting of the output.

# 6-12 Extensions
NBA_teams_2018 = {

'golden state warriors 2018': {
	'guards': ['stephen curry', 'shaun livingston'],
	'shooting_guards': ['klay thompson', 'patrick mccaw'],
	'small_forwards': ['kevin durant', 'andre igoudala'],
	'power_forwards': ['draymond green', 'david west'],
	'centers': ['javale mcgee', 'zaza pachulia'],
	},	
'houston rockets 2018': {
	'guards': ['chris paul', 'eric gordon'],
	'shooting_guards': ['james harden', 'gerald green'],
	'small_forwards': ['trevor ariza', 'pj tucker'],
	'power_forwards': ['ryan anderson', 'tarik black'],
	'centers': ['clint capela', 'nene hilario'],
	},
}


for playoff_teams, basketball_players in NBA_teams_2018.items():
	guard_depth_chart = basketball_players['guards']
	shooting_guard_depth_chart = basketball_players['shooting_guards']
	small_forward_depth_chart = basketball_players['small_forwards']
	power_forward_depth_chart = basketball_players['power_forwards']
	center_depth_chart = basketball_players['centers']
	print("The " + playoff_teams.title() + " team has a roster of " +\
	"\n\t" + str(guard_depth_chart).title() +\
	"\n\t" + str(shooting_guard_depth_chart).title() +\
	"\n\t" + str(small_forward_depth_chart).title() +\
	"\n\t" + str(power_forward_depth_chart).title() +\
	"\n\t" + str(center_depth_chart).title() \
	)
