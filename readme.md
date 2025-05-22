# Tic-Tac-Toe AI Implementation Report
[youtube link](https://youtu.be/Ih5iCrml-J0)
## Introduction

This report explains the implementation of an artificially intelligent player for the classic game of Tic-Tac-Toe. The implementation features two algorithms: the standard Minimax algorithm and its optimized version using Alpha-Beta Pruning. This report breaks down the key components, explains the algorithms, and analyzes their performance differences.

## Game Logic Implementation

The game is implemented through the `TicTacToe` class, which handles the core mechanics:

- The board is represented as a 1-dimensional array with 9 positions (0-8)
- Player moves are tracked by placing 'X' or 'O' in the array
- Win conditions are checked after each move (rows, columns, and diagonals)
- Game state tracking determines when the game reaches a terminal state (win or draw)

## Minimax Algorithm

The Minimax algorithm is a decision-making algorithm used for finding the optimal move in two-player zero-sum games like Tic-Tac-Toe. Key characteristics:

- It recursively evaluates all possible future game states
- Assumes both players play optimally
- Creates a complete game tree from the current state to all possible end states
- Assigns values to terminal states (+10 for AI win, -10 for opponent win, 0 for draw)
- For non-terminal states, takes maximum or minimum of child values depending on whose turn it is
- Decides the move that leads to the best possible outcome assuming optimal play by both sides

In the implementation, the `minimax` method in the `MiniMaxAI` class:
1. Checks for terminal states (win, loss, or draw)
2. If not terminal, recursively evaluates each valid move
3. Maximizes score when it's the AI's turn
4. Minimizes score when it's the opponent's turn
5. Returns the best score achievable from the current state

## Alpha-Beta Pruning Optimization

Alpha-Beta Pruning is an optimization technique for the Minimax algorithm that significantly reduces the number of nodes evaluated in the search tree. It works by:

- Maintaining two values, alpha and beta, during tree traversal
- Alpha represents the minimum score the maximizing player is assured
- Beta represents the maximum score the minimizing player is assured
- Pruning branches that cannot affect the final decision
- Skipping evaluation of moves that are provably worse than previously examined moves

The `minimax_alpha_beta` method implements this optimization by:
1. Tracking alpha and beta values throughout the recursion
2. Updating alpha when a better move is found for the maximizer
3. Updating beta when a better move is found for the minimizer
4. Stopping evaluation of remaining moves when beta ≤ alpha (pruning)

## Performance Comparison

The implementation includes a `compare_performance` function that demonstrates the efficiency difference between the two algorithms:

1. **Empty Board Test**:
   - Standard Minimax evaluates a large number of nodes
   - Alpha-Beta Pruning evaluates significantly fewer nodes
   - Both algorithms find the same optimal move

2. **Partially Filled Board Test**:
   - As the game progresses, the efficiency advantage of Alpha-Beta increases
   - The time difference becomes more pronounced
   - Decision quality remains identical

## User Interface

The program provides a simple text-based interface that allows users to:
1. Play against the AI (using either algorithm)
2. Compare the performance of both algorithms
3. Exit the program

During gameplay, users can see:
- The current board state
- Number of nodes evaluated by the AI
- Time taken to make decisions
- Final game outcome

## Conclusion

Both Minimax and Alpha-Beta Pruning enable the AI to play Tic-Tac-Toe perfectly, always choosing the optimal move. However, Alpha-Beta Pruning achieves this optimality with significantly greater efficiency.

The implementation demonstrates that:
- Standard Minimax guarantees optimal play but can be computationally expensive
- Alpha-Beta Pruning maintains optimality while reducing computational cost
- For simple games like Tic-Tac-Toe, the performance difference may be modest in absolute terms
- However, the relative efficiency gain demonstrates the power of this optimization technique, which becomes crucial for more complex games