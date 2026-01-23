def Achievement_analytics(alice: set, bob: set, charlie: set) -> None:
    if not alice or not bob or not charlie:
        return
    print("\n=== Achievement Analytics ===\n")

    uniqs = alice.union(bob).union(charlie)
    intersec = alice.intersection(bob).intersection(charlie)
    diff = (
            charlie.difference(bob, alice)
            .union(bob.difference(alice, charlie))
            .union(alice.difference(charlie, bob))
           )
    print(f"All unique achievements: {uniqs}")
    print(f"Total unique achievements: {len(uniqs)}\n")
    print(f"Common to all players: {intersec}")
    print(f"Rare achievements (1 player): {diff}\n")
    print(f"Alice vs Bob common: {alice.intersection(bob)}")
    print(f"Alice unique: {alice.difference(bob)}")
    print(f"Bob unique: {bob.difference(alice)}")


def achievement_tracker() -> None:
    print("=== Achievement Tracker System ===\n")

    alice_achievement = {'first_kill', 'level_10',
                         'treasure_hunter', 'speed_demon'}

    bob_achievement = {'first_kill', 'level_10', 'boss_slayer', 'collector'}

    charlie_achievement = {'level_10', 'treasure_hunter', 'boss_slayer',
                           'speed_demon', 'perfectionist'}

    print(f"Player alice achievements: {alice_achievement}")
    print(f"Player bob achievements: {bob_achievement}")
    print(f"Player charlie achievements: {charlie_achievement}")

    Achievement_analytics(None, bob_achievement,
                          charlie_achievement)


achievement_tracker()
