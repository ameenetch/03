if __name__ == '__main__':
    player2 = {
            'alice': {'score': 2300, 'status': 'online', 'achievements':
                      {"first_kill", "level_10"}, 'region': "north"},


            'bob': {'score': 1800, 'status': 'online',
                    'achievements': {"level_10"}, 'region': "east"},


            'charlie': {'score': 2150, 'status': 'online',
                        'achievements': {"boss_slayer"}, 'region': "central"},


            'diana': {'score': 2050, 'status': 'offline',
                      'achievements': {"GG"}, 'region': "central"}
            }
    print("=== Game Analytics Dashboard ===\n")
    print("=== List Comprehension Examples ===")
    high_scores = [key for key in player2.keys()
                   for elem, value in player2[key].items()
                   if elem == 'score' and value > 2000]

    double_scores = [value * 2 for key in player2.keys()
                     for elem, value in player2[key].items()
                     if elem == 'score']

    active_players = [key for key in player2.keys()
                      for elem, value in player2[key].items()
                      if elem == 'status' and value == 'online']

    print("High scorers (>2000): ", high_scores)
    print("Scores doubled: ", double_scores)
    print("Active players: ", active_players)

    print("\n=== Dict Comprehension Examples ===")

    player_scores = {key: value for key in player2
                     for elem, value in player2[key].items()
                     if elem == 'score'}

    scores_categorie = {'high': len({key: value for key in player2
                                    for elem, value in player2[key].items()
                                    if elem == 'score' and value > 3000}),

                        'medium': len(
                                 {key: value for key in player2
                                  for elem, value in player2[key].items()
                                  if elem == 'score' and 3000 > value > 2000}),

                        'low': len(
                            {key: value for key in player2
                             for elem, value in player2[key].items()
                             if elem == 'score' and 2000 > value > 1000})
                        }

    uniqe_players = {key for key in player2}

    print("Player scores: ", player_scores)
    print("Score categories: ", scores_categorie)
    print("Achievement counts:", uniqe_players)

    print("\n=== Set Comprehension Examples ===")
    unique_achiev = {ach for key in player2
                     for elem, value in player2[key].items()
                     if elem == 'achievements'
                     for ach in value}

    activ_region = {value for key in player2
                    for elem, value in player2[key].items()
                    if elem == 'region'}

    print("Unique players: ", uniqe_players)
    print("Unique achievements:", unique_achiev)
    print("Active regions:", activ_region)

    print("\n=== Combined Analysis ===")
    total = len([key for key in player2])

    total_uniq_ach = len({ach for key in player2
                         for elem, value in player2[key].items()
                         if elem == 'achievements'
                         for ach in value})

    avrg = sum([value for key in player2
                for elem, value in player2[key].items()
                if elem == "score"])/total

    print("Total players: ", total)
    print("Total unique achievements:", total_uniq_ach)
    print("Average score:", avrg)

    top_score = max(player_scores.values())

    who_top_scor = [key for key, value in player_scores.items()
                    if value == top_score]

    print(
      f"Top performer: {who_top_scor[0]} ({player_scores[who_top_scor[0]]} "
      f"points, {len(player2[who_top_scor[0]]['achievements'])} achievements)")
