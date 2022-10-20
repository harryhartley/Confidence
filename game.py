import random

with open('players.txt') as f: crew_list = [crew for crew in f.read().split('\n')]
with open('questions.txt') as f: question_list = [question.split(',') for question in f.read().split('\n')]

current_player_idx = 0
question_idx = 0
team_a = []
team_b = []
team_a_score = 0
team_b_score = 0
turn_counter = 0

print("░█████╗░░█████╗░███╗░░██╗███████╗██╗██████╗░███████╗███╗░░██╗░█████╗░███████╗\n██╔══██╗██╔══██╗████╗░██║██╔════╝██║██╔══██╗██╔════╝████╗░██║██╔══██╗██╔════╝\n██║░░╚═╝██║░░██║██╔██╗██║█████╗░░██║██║░░██║█████╗░░██╔██╗██║██║░░╚═╝█████╗░░\n██║░░██╗██║░░██║██║╚████║██╔══╝░░██║██║░░██║██╔══╝░░██║╚████║██║░░██╗██╔══╝░░\n╚█████╔╝╚█████╔╝██║░╚███║██║░░░░░██║██████╔╝███████╗██║░╚███║╚█████╔╝███████╗\n░╚════╝░░╚════╝░╚═╝░░╚══╝╚═╝░░░░░╚═╝╚═════╝░╚══════╝╚═╝░░╚══╝░╚════╝░╚══════╝\n")
input('')

while True:
    turn_counter += 1

    if len(crew_list) == 1:
        crew_list.append(team_b[0])

    player_a = crew_list[current_player_idx]
    print(f"Player for Team A: {player_a}")
    while input('(a)bsent? ') == 'a':
        current_player_idx = (current_player_idx + 1) % len(crew_list)
        player_a = crew_list[current_player_idx]
        print(f"New player for Team A: {player_a}")
    team_a.append(player_a)
    print('')

    current_player_idx = (current_player_idx + 1) % len(crew_list)

    player_b = crew_list[current_player_idx]
    print(f"Player for Team B: {player_b}")
    while input('(a)bsent?' ) == 'a':
        current_player_idx = (current_player_idx + 1) % len(crew_list)
        player_b = crew_list[current_player_idx]
        print(f"New player for Team B: {player_b}")
    team_b.append(player_b)
    print('')

    current_player_idx = (current_player_idx + 1) % len(crew_list)

    print(f"Here's your question:\n{question_list[question_idx][0]}\n")

    asking = True
    while asking:
        try:
            player_a_low = int(input("{}'s low guess: ".format(player_a)))
            asking = False
        except:
            print('invalid guess')
    
    asking = True
    while asking:
        try:
            player_a_high = int(input("{}'s high guess: ".format(player_a)))
            asking = False
        except:
            print('invalid guess')

    print('')

    asking = True
    while asking:
        try:
            player_b_low = int(input("{}'s low guess: ".format(player_b)))
            asking = False
        except:
            print('invalid guess')
    
    asking = True
    while asking:
        try:
            player_b_high = int(input("{}'s high guess: ".format(player_b)))
            asking = False
        except:
            print('invalid guess')

    print('')

    player_a_range = player_a_high - player_a_low
    player_b_range = player_b_high - player_b_low

    player_a_correct = False
    if player_a_low <= int(question_list[question_idx][1]) <= player_a_high:
        player_a_correct = True

    player_b_correct = False
    if player_b_low <= int(question_list[question_idx][1]) <= player_b_high:
        player_b_correct = True

    if player_a_range < player_b_range:
        print('Team A: {} is the most confident with a range of {} ({} -> {})'.format(player_a, player_a_range, player_a_low, player_a_high))
        print('Team B: {} is the least confident with a range of {} ({} -> {})'.format(player_b, player_b_range, player_b_low, player_b_high))

        print('The correct answer is...')
        input('')
        print('{}!'.format(question_list[question_idx][1]))
        input('')

        if player_a_correct and player_b_correct:
            print('Both players are correct!\n\n{} scores 2 points\n{} scores 1 point'.format(player_a, player_b))
            team_a_score += 2
            team_b_score += 1
        elif player_a_correct:
            print('Only {} is correct!\n\n{} scores 2 points\n{} scores 0 points'.format(player_a, player_a, player_b))
            team_a_score += 2
        elif player_b_correct:
            print('Only {} is correct!\n\n{} scores 2 point\n{} scores 0 points'.format(player_b, player_b, player_a))
            team_b_score += 2
        else:
            print('Neither player is correct!\n\n{} scores 0 points\n{} scores 0 points'.format(player_a, player_b))

    elif player_b_range < player_a_range:
        print('Team A: {} is the most confident with a range of {} ({} -> {})'.format(player_b, player_b_range, player_b_low, player_b_high))
        print('Team B: {} is the least confident with a range of {} ({} -> {})'.format(player_a, player_a_range, player_a_low, player_a_high))

        print('The correct answer is...')
        input('')
        print('{}!'.format(question_list[question_idx][1]))
        input('')

        if player_a_correct and player_b_correct:
            print('Both players are correct!\n\n{} scores 2 points\n{} scores 1 point'.format(player_b, player_a))
            team_a_score += 1
            team_b_score += 2
        elif player_a_correct:
            print('Only {} is correct!\n\n{} scores 2 points\n{} scores 0 points'.format(player_a, player_a, player_b))
            team_a_score += 2
        elif player_b_correct:
            print('Only {} is correct!\n\n{} scores 2 points\n{} scores 0 points'.format(player_b, player_b, player_a))
            team_b_score += 2
        else:
            print('Neither player is correct!\n\n{} scores 0 points\n{} scores 0 points'.format(player_a, player_b))

    else:
        print('Both players are equally confident with a range of {}!'.format(player_a_range))

        print('The correct answer is...')
        input('')
        print('{}!'.format(question_list[question_idx][1]))
        input('')

        if player_a_correct and player_b_correct:
            print('Both players are correct!\n{} scores 2 points\n{} scores 2 points'.format(player_b, player_a))
            team_a_score += 2
            team_b_score += 2
        else:
            print('Neither player is correct!\n{} scores 0 points\n{} scores 0 points'.format(player_a, player_b))
    
    input('')
    print('After round {}, the current team scores are:\nTeam A: {}\nTeam B: {}'.format(turn_counter, team_a_score, team_b_score))
    input('')

    question_idx = (question_idx + 1) % len(question_list)

    if input("Next question?\n") == 'q':
        break

print('')
print('The final results:')
input('')
if team_a_score > team_b_score:
    print("Team A are the winners with {} points!".format(team_a_score))
    input('')
    print("Team B are the losers with {} points!".format(team_b_score))
    input('')
    print("Congrats to: \n{}".format('\n'.join(team_a)))

elif team_b_score > team_a_score:
    print("Team B are the winners with {} points!".format(team_b_score))
    input('')
    print("Team A are the losers with {} points!".format(team_a_score))
    input('')
    print("Congrats to: \n{}".format('\n'.join(team_b)))

else:
    print("The game is a tie!")
    input('')
    print("Both teams scored {} points!".format(team_a_score))
input('')
