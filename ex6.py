list_player = []
dict_player = {'alice': 2300,  'bob': 1800, 'charlie': 2150, 'diana': 2050}
player2 = {      'alice':   {'score': 2300, 'status': 'online', 'achievements': {"first_kill", "level_10"}, 'region': "north" }
               , 'bob':     {'score': 1800, 'status': 'online', 'achievements': {"level_10"}, 'region': "east"    }
               , 'charlie': {'score': 2150, 'status': 'online', 'achievements': {"boss_slayer"} , 'region': "central"   }
               , 'diana':   {'score': 2050, 'status': 'offline', 'achievements': {"GG"} , 'region': "central"  }
          }


high_scores = [key for key in player2.keys()
                   for elem, value in player2[key].items()
                   if elem == 'score' and value > 2000 ]
double_scores = [value * 2 for key in player2.keys()
                   for elem, value in player2[key].items()
                   if elem == 'score' ]

active_players = [key for key in player2.keys()
                      for elem, value in player2[key].items()
                      if elem == 'status' and value == 'online']
        
print(high_scores)
print(double_scores)
print(active_players)

player_scores = {key: value for key in player2 
                            for elem, value in player2[key].items()
                            if elem == 'score'            
                }

print(player_scores)

scores_categorie = {'high': len({key: value for key in player2
                            for elem, value in player2[key].items()
                            if elem == 'score' and value > 3000})
                    ,'medium': len({key: value for key in player2
                            for elem, value in player2[key].items()
                            if elem == 'score' and  3000 > value > 2000})
                    ,'low': len({key: value for key in player2
                            for elem, value in player2[key].items()
                            if elem == 'score' and 2000> value > 1000})
                    }

print(scores_categorie)

uniqe_players = {key for key in player2}
print(uniqe_players)
un_achev = {ach for key in player2
                    for elem, value in player2[key].items()
                    if elem == 'achievements'
                    for ach in value}
print(un_achev)

activ_rg = {value for key in player2
                    for elem, value in player2[key].items()
                    if elem == 'region'}
print(activ_rg)


total = len([key for key in player2])
print(total)
total_uniq_ach = len({ach for key in player2
                          for elem, value in player2[key].items()
                          if elem == 'achievements'
                          for ach in value})
print(total_uniq_ach)
avrg = sum([value for key in player2
                  for elem, value in player2[key].items()
                  if elem == "score" ])/total
print(avrg)

top = max(player_scores.values())
top = {key: value for key in player2
                  for elem, value in player2[key].items()
                  if elem == "score"}

print(top)
top = sorted(top.items())
print(top[0][0] )
print(top[0][1])
print(  len(ach for key , value in player2[top[0][0]].items()
                          if key == 'achievements'
                          for ach in value) )