# 1/31/2022

def score(rolls):
    active_bonus = 0
    last_roll = 0
    newFrame = True
    total = 0
    for roll in rolls:
        if active_bonus > 0:
            active_bonus -= 1
            total += roll
        print(f"TOTAL: {total}; LAST: {last_roll}; ROLL: {roll}; BONUS; {active_bonus}; NEW FRAME: {newFrame}")
        if roll == 10 and newFrame:
            print("*** STRIKE!")
            # STRIKE! add 2 to the bonus
            active_bonus += 2
            # update totals
            total += roll
            last_roll = roll
            # start a new frame because STRIKE
            newFrame = True
        elif last_roll + roll == 10 and not newFrame:
            print("*** SPARE!")
            # SPARE! add 1 to the bonus
            active_bonus += 1
            # update totals
            total += roll
            last_roll = roll
            # start a new frame
            newFrame = True

        else:
            # if first roll, this is False
            # if second roll, this is True
            newFrame = not newFrame
            total += roll
            last_roll = roll
    return total


game_score = [10, 7, 8, 9, 7, 2, 5, 8, 9, 8]
score(game_score)
