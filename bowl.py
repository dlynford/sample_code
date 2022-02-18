

scores = [162, 147, 137, 180, 300]
rolls = {
    'game_1': [7, 2, 8, 2, 10, 7, 1, 8, 2, 7, 3, 10, 10, 5, 4, 8, 2, 7],
    'game_2': [2, 6, 2, 6, 9, 1, 10, 10, 10, 5, 1, 4, 5, 9, 0, 9, 1, 6],
    'game_4': [6, 4, 2, 7, 8, 1, 2, 4, 6, 3, 10, 6, 2, 1, 9, 6, 4, 10, 10, 10],
    'game_5': [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
}


def bowling_score(rolls):
    game_score = 0
    for key, value in rolls.items():
        game_score += value['game']
        print(game_score)

    #sum the values in the nested list


bowling_score(rolls)


def test_bowling_score():
    for score in scores:
        try:
            assert bowling_score(scores) == score
        except AssertionError:
            print(f"the roll value:{rolls} != {score}. ")
        else:
            print(f"The values are the same.")

    assert(bowling_score([7,2,8,2,10,7,1,8,2,7,3,10,10,5,4,8,2,7]) == 162)
    assert(bowling_score([2,6,2,6,9,1,10,10,10,5,1,4,5,9,0,9,1,6])==147)
    assert(bowling_score([6,4,2,7,8,1,2,4,6,3,10,6,2,1,9,6,4,10,10,10])==137)
    assert(bowling_score([8,2,10,10,10,5,4,10,8,0,10,10,3,6])==180)
    assert(bowling_score([10]*12)==300)

# test_bowling_score()

