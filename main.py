import time
import random

class TicTacToe:
    def __init__(self):
        # Initialize empty 3x3 board
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'
        self.winner = None
        self.game_over = False
        
    def print_board(self):
        # Print the current state of the board
        for i in range(0, 9, 3):
            print(f" {self.board[i]} | {self.board[i+1]} | {self.board[i+2]} ")
            if i < 6:
                print("-----------")
                
    def available_moves(self):
        # Return list of available moves (indices of empty spaces)
        return [i for i, spot in enumerate(self.board) if spot == ' ']
    
    def make_move(self, position, player):
        # Make a move on the board
        if self.board[position] == ' ':
            self.board[position] = player
            self.check_winner()
            return True
        return False
    
    def check_winner(self):
        # Check if there's a winner or if the game is a draw
        
        # Check rows
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i+1] == self.board[i+2] != ' ':
                self.winner = self.board[i]
                self.game_over = True
                return
                
        # Check columns
        for i in range(3):
            if self.board[i] == self.board[i+3] == self.board[i+6] != ' ':
                self.winner = self.board[i]
                self.game_over = True
                return
                
        # Check diagonals
        if self.board[0] == self.board[4] == self.board[8] != ' ':
            self.winner = self.board[0]
            self.game_over = True
            return
            
        if self.board[2] == self.board[4] == self.board[6] != ' ':
            self.winner = self.board[2]
            self.game_over = True
            return
            
        # Check for draw 
        if ' ' not in self.board:
            self.game_over = True
            return
            
        # Switch current player
    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

        # Check if the game has ended
    def is_terminal(self):
        return self.game_over

        # Return a copy of the current board state
    def get_board_state(self):
        return self.board.copy()

        # Reset the game
    def reset(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'
        self.winner = None
        self.game_over = False


class MiniMaxAI:
    def __init__(self, player_symbol, use_alpha_beta=False):
        self.player_symbol = player_symbol  # 'X' or 'O'
        self.opponent_symbol = 'O' if player_symbol == 'X' else 'X'
        self.use_alpha_beta = use_alpha_beta
        self.nodes_evaluated = 0
        
    def get_best_move(self, game):
        self.nodes_evaluated = 0
        start_time = time.time()
        
        if self.use_alpha_beta:
            best_score = float('-inf')
            best_move = None
            
            for move in game.available_moves():
                # Try this move
                game.board[move] = self.player_symbol
                
                # Calculate score from this move
                score = self.minimax_alpha_beta(game, 0, False, float('-inf'), float('inf'))
                
                # Undo the move
                game.board[move] = ' '
                
                # Update best move if needed
                if score > best_score:
                    best_score = score
                    best_move = move
        else:
            best_score = float('-inf')
            best_move = None
            
            for move in game.available_moves():
                # Try this move
                game.board[move] = self.player_symbol
                
                # Calculate score from this move
                score = self.minimax(game, 0, False)
                
                # Undo the move
                game.board[move] = ' '
                
                # Update best move if needed
                if score > best_score:
                    best_score = score
                    best_move = move
        
        end_time = time.time()
        execution_time = end_time - start_time
        
        return best_move, self.nodes_evaluated, execution_time
    
    def minimax(self, game, depth, is_maximizing):
        """Standard Minimax implementation"""
        self.nodes_evaluated += 1
        
        # Check terminal state
        if self._is_winner(game.board, self.player_symbol):
            return 10 - depth
        elif self._is_winner(game.board, self.opponent_symbol):
            return depth - 10
        elif not game.available_moves():  # Draw
            return 0
            
        if is_maximizing:
            best_score = float('-inf')
            for move in game.available_moves():
                # Try move
                game.board[move] = self.player_symbol
                # Recursive call
                score = self.minimax(game, depth + 1, False)
                # Undo move
                game.board[move] = ' '
                # Update best score
                best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for move in game.available_moves():
                # Try move
                game.board[move] = self.opponent_symbol
                # Recursive call
                score = self.minimax(game, depth + 1, True)
                # Undo move
                game.board[move] = ' '
                # Update best score
                best_score = min(score, best_score)
            return best_score
    
    def minimax_alpha_beta(self, game, depth, is_maximizing, alpha, beta):
        """Alpha-Beta Pruning optimized Minimax"""
        self.nodes_evaluated += 1
        
        # Check terminal state
        if self._is_winner(game.board, self.player_symbol):
            return 10 - depth
        elif self._is_winner(game.board, self.opponent_symbol):
            return depth - 10
        elif not game.available_moves():  # Draw
            return 0
            
        if is_maximizing:
            best_score = float('-inf')
            for move in game.available_moves():
                # Try move
                game.board[move] = self.player_symbol
                # Recursive call
                score = self.minimax_alpha_beta(game, depth + 1, False, alpha, beta)
                # Undo move
                game.board[move] = ' '
                # Update best score
                best_score = max(score, best_score)
                # Update alpha
                alpha = max(alpha, best_score)
                # Alpha-beta pruning
                if beta <= alpha:
                    break
            return best_score
        else:
            best_score = float('inf')
            for move in game.available_moves():
                # Try move
                game.board[move] = self.opponent_symbol
                # Recursive call
                score = self.minimax_alpha_beta(game, depth + 1, True, alpha, beta)
                # Undo move
                game.board[move] = ' '
                # Update best score
                best_score = min(score, best_score)
                # Update beta
                beta = min(beta, best_score)
                # Alpha-beta pruning
                if beta <= alpha:
                    break
            return best_score
    
    def _is_winner(self, board, player):
        """Check if the given player has won on the board"""
        # Check rows
        for i in range(0, 9, 3):
            if board[i] == board[i+1] == board[i+2] == player:
                return True
                
        # Check columns
        for i in range(3):
            if board[i] == board[i+3] == board[i+6] == player:
                return True
                
        # Check diagonals
        if board[0] == board[4] == board[8] == player:
            return True
            
        if board[2] == board[4] == board[6] == player:
            return True
            
        return False


def compare_performance():
    """Compare standard Minimax vs Alpha-Beta Pruning"""
    game = TicTacToe()
    standard_ai = MiniMaxAI('X', use_alpha_beta=False)
    alpha_beta_ai = MiniMaxAI('X', use_alpha_beta=True)
    
    print("\n===== PERFORMANCE COMPARISON =====")
    print("Testing first move calculation (empty board):")
    
    # Test standard Minimax
    move, nodes, time_taken = standard_ai.get_best_move(game)
    print(f"\nStandard Minimax:")
    print(f"- Best move: {move}")
    print(f"- Nodes evaluated: {nodes}")
    print(f"- Time taken: {time_taken:.6f} seconds")
    
    # Test Alpha-Beta pruning
    move, nodes, time_taken = alpha_beta_ai.get_best_move(game)
    print(f"\nAlpha-Beta Pruning:")
    print(f"- Best move: {move}")
    print(f"- Nodes evaluated: {nodes}")
    print(f"- Time taken: {time_taken:.6f} seconds")
    
    # Create a board with some moves already made
    print("\nTesting with partially filled board:")
    test_board = [' ', 'X', 'O', 
                 'O', 'X', ' ', 
                 ' ', ' ', ' ']
    game.board = test_board
    
    # Test standard Minimax
    move, nodes, time_taken = standard_ai.get_best_move(game)
    print(f"\nStandard Minimax:")
    print(f"- Best move: {move}")
    print(f"- Nodes evaluated: {nodes}")
    print(f"- Time taken: {time_taken:.6f} seconds")
    
    # Test Alpha-Beta pruning
    move, nodes, time_taken = alpha_beta_ai.get_best_move(game)
    print(f"\nAlpha-Beta Pruning:")
    print(f"- Best move: {move}")
    print(f"- Nodes evaluated: {nodes}")
    print(f"- Time taken: {time_taken:.6f} seconds")
    
    print("\n=== EFFICIENCY GAIN ===")
    print("The Alpha-Beta Pruning optimization significantly reduces the number of nodes evaluated")
    print("while still finding the same optimal move.")


def play_game():
    """Play a game of Tic-Tac-Toe against the AI"""
    game = TicTacToe()
    
    print("Welcome to Tic-Tac-Toe!")
    print("You are 'O', the AI is 'X'.")
    print("Enter positions as numbers from 0-8:")
    print("0|1|2")
    print("-----")
    print("3|4|5")
    print("-----")
    print("6|7|8")
    
    # Choose AI type
    choice = input("\nChoose AI type:\n1. Standard Minimax\n2. Alpha-Beta Pruning\nYour choice (1/2): ")
    use_alpha_beta = (choice == "2")
    
    ai = MiniMaxAI('X', use_alpha_beta=use_alpha_beta)
    
    # Randomly decide who goes first
    ai_turn = random.choice([True, False])
    
    while not game.is_terminal():
        game.print_board()
        
        if ai_turn:
            print("\nAI is thinking...")
            move, nodes, time_taken = ai.get_best_move(game)
            print(f"AI chose position {move} (evaluated {nodes} nodes in {time_taken:.4f} seconds)")
            game.make_move(move, 'X')
        else:
            valid_move = False
            while not valid_move:
                try:
                    position = int(input("\nYour move (0-8): "))
                    if 0 <= position <= 8:
                        valid_move = game.make_move(position, 'O')
                        if not valid_move:
                            print("That position is already taken!")
                    else:
                        print("Please enter a number between 0 and 8.")
                except ValueError:
                    print("Please enter a valid number.")
        
        ai_turn = not ai_turn
    
    # Game over
    game.print_board()
    if game.winner:
        if game.winner == 'X':
            print("AI wins!")
        else:
            print("You win!")
    else:
        print("It's a draw!")


if __name__ == "__main__":
    while True:
        print("\n=== TIC-TAC-TOE MENU ===")
        print("1. Play against AI")
        print("2. Compare Minimax vs Alpha-Beta")
        print("3. Exit")
        
        choice = input("Your choice: ")
        
        if choice == "1":
            play_game()
        elif choice == "2":
            compare_performance()
        elif choice == "3":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please try again.")