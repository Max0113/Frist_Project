import curses
import random


def jouer_snake():
    score = 0
    # إعداد الشاشة
    screen = curses.initscr()
    curses.curs_set(0)
    screen_height, screen_width = screen.getmaxyx()
    window = curses.newwin(screen_height, screen_width, 0, 0)
    window.keypad(1)
    window.timeout(100)
    window.border(0)
    
    # إعداد الثعبان والطعام
    snk_x = screen_width//4
    snk_y = screen_height//2
    snake = [
        [snk_y, snk_x],
        [snk_y, snk_x-1],
        [snk_y, snk_x-2]
    ]
    food = [screen_height//2, screen_width//2]
    window.addch(food[0], food[1], curses.ACS_PI)

    # إعداد الاتجاه
    key = curses.KEY_RIGHT

    while True:
        next_key = window.getch()
        key = key if next_key == -1 else next_key

        # شروط الخسارة
        if (
            snake[0][0] in [0, screen_height] or
            snake[0][1] in [0, screen_width] or
            snake[0] in snake[1:]
        ):
            curses.endwin()
            print(f"💀 Game over ?? Score : {score}")
            return  # تخرج من اللعبة

        # تحديث رأس الثعبان
        new_head = [snake[0][0], snake[0][1]]

        if key == curses.KEY_DOWN:
            new_head[0] += 1
        if key == curses.KEY_UP:
            new_head[0] -= 1
        if key == curses.KEY_LEFT:
            new_head[1] -= 1
        if key == curses.KEY_RIGHT:
            new_head[1] += 1

        snake.insert(0, new_head)

        # عند أكل الطعام
        if snake[0] == food:
            score += 1
            food = None
            while food is None:
                nf = [
                    random.randint(1, screen_height-1),
                    random.randint(1, screen_width-1)
                ]
                food = nf if nf not in snake else None
            window.addch(food[0], food[1], curses.ACS_PI)
        else:
            tail = snake.pop()
            window.addch(tail[0], tail[1], ' ')

        window.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)

def demarrer_jeu():
    while True:
        jouer_snake()
        choix = input("Do you want to play again? (Yes/No): ").lower()
        if choix in ['Yes', 'yes', 'y' , 'Y']:
            continue
        elif choix in ['No', 'no', 'n', 'N']:
            print("👋 Thanks for playing! See you!")
            break
        else:
            print("⚠️ Incomprehensible choice, the game will be terminated.")
            break

demarrer_jeu()






