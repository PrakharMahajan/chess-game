import pygame
import chess

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Chess')

# Set up the chess game
board = chess.Board()

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Handle mouse clicks
            if board.turn == chess.WHITE:
                x, y = pygame.mouse.get_pos()
                file = int(x / (screen_width / 8))
                rank = 7 - int(y / (screen_height / 8))
                src_square = chess.square(file, rank)
                dst_squares = [move.to_square for move in board.legal_moves if move.from_square == src_square]
                if dst_squares:
                    dst_square = dst_squares[0]  # Select the first legal destination square
                    move = chess.Move(src_square, dst_square)
                    board.push(move)
            else:
                # Make a random move for the black player (just for demonstration purposes)
                move = chess.Move.null()
                while move not in board.legal_moves:
                    move = chess.Move.from_uci('a7a5')
                board.push(move)

    # Draw the chessboard
    square_size = screen_height / 8
    for file in range(8):
        for rank in range(8):
            rect = pygame.Rect(file * square_size, rank * square_size, square_size, square_size)
            color = WHITE if (file + rank) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, rect)
            piece = board.piece_at(chess.square(file, 7 - rank))
            if piece is not None:
                filename = f"img/pieces/{piece.color}{piece.symbol()}.png"
                image = pygame.image.load(filename)
                screen.blit(image, rect)

    # Update the screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()
