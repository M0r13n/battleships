from game import *

logging.basicConfig(filename='log.log', level=logging.DEBUG)


def main():
    # network setup
    host = 'localhost'
    port = 5000
    last_shot_hit = False
    last_move = None
    player_won = False
    is_server = input("Are you a server or a client? (c/s)").lower()[0] == "s"
    player_turn = not is_server

    if not is_server:
        host = input("Enter hostname (default: localhost)") or host
        port = int(input("Enter port (default: 5000)") or port)

    with Network(host, port, is_server) as net:
        # init
        player_board = create_empty_board()
        enemy_board = create_empty_board()

        place_ships(player_board, enemy_board)

        print("Okay, let's start:")
        print_boards(player_board, enemy_board)

        # game on
        while not player_lost(player_board):

            if player_turn:
                x, y, exit_ = ask_player_for_shot()
                if exit_:
                    break
                last_move = Shot(x, y, last_shot_hit)
                net.send(bytes(last_move))

            else:
                print("Waiting for response...")
                data = net.recv()
                if not data:
                    player_won = True
                    break

                enemy_shot = Shot.decode(data)

                # true if enemy hit player
                last_shot_hit = update_player_board(enemy_shot, player_board)

                if last_move:
                    last_move.last_shot_hit = enemy_shot.last_shot_hit
                    update_enemy_board(last_move, enemy_board)

            print_boards(player_board, enemy_board)
            player_turn = not player_turn

        if player_won:
            print("You won!")
        else:
            print("You lost!")


if __name__ == "__main__":
    main()
