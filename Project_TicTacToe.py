# -------
# MODULES
# -------
import pygame, sys
import numpy as np
from constant import *
import os

# initializes pygame
pygame.init()
# initializes font
pygame.font.init()
# initializes mixer
pygame.mixer.init()
# init default path
currentDirectory = os.path.dirname(os.path.realpath(__file__))

# ------
# SCREEN
# ------
screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption( 'TIC TAC TOE' )

# -----------
# CUSTOM ICON
# -----------
icon = pygame.image.load(currentDirectory + "/icon.png")
pygame.display.set_icon(icon)

# ------------
# CUSTOM FRAME
# ------------
imageFrame = pygame.image.load(currentDirectory + "/Frame1.png")

# -------------
# CONSOLE BOARD
# -------------
board = np.zeros( (BOARD_ROWS, BOARD_COLS) )

fontBig = pygame.font.Font(currentDirectory + "/cooper-black-five/CooperFiveOpti-Black.otf", 36)
font = pygame.font.Font(currentDirectory + "/cooper-black-five/CooperFiveOpti-Black.otf", 30)
fontMd = pygame.font.Font(currentDirectory + "/cooper-black-five/CooperFiveOpti-Black.otf", 26)
fontSm = pygame.font.Font(currentDirectory + "/cooper-black-five/CooperFiveOpti-Black.otf", 16)

# -----
# SOUND
# -----
isPlay = True #Default
pygame.mixer.music.load(currentDirectory + "/song.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play()

# ----
# STEP
# ----
isMain = False
isRound = False
isPlayer1 = False
isPlayer2 = False
isGame = False
isCredit = False
isTheme = False

# ---------
# FUNCTIONS
# ---------
def draw_lines():
	# 1 horizontal
	pygame.draw.line( screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH )
	# 2 horizontal
	pygame.draw.line( screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH )
	# 3 horizontal
	pygame.draw.line( screen, LINE_COLOR, (0, 3 * SQUARE_SIZE), (WIDTH, 3 * SQUARE_SIZE), LINE_WIDTH )

	# 1 vertical
	pygame.draw.line( screen, LINE_COLOR, (SQUARE_SIZE, 200), (SQUARE_SIZE, HEIGHT), LINE_WIDTH )
	# 2 vertical
	pygame.draw.line( screen, LINE_COLOR, (2 * SQUARE_SIZE, 200), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH )

def draw_figures():
	for row in range(BOARD_ROWS):
		if row != 0 :
			for col in range(BOARD_COLS):
				if board[row][col] == 1:
					pygame.draw.circle( screen, CIRCLE_COLOR, (int( col * SQUARE_SIZE + SQUARE_SIZE//2 ), int( row * SQUARE_SIZE + SQUARE_SIZE//2 )), CIRCLE_RADIUS, CIRCLE_WIDTH )
				elif board[row][col] == 2:
					pygame.draw.line( screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH )	
					pygame.draw.line( screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH )

def mark_square(row, col, player):
	board[row][col] = player

def available_square(row, col):
	return board[row][col] == 0

def is_board_full():
	for row in range(BOARD_ROWS):
		if row != 0 :
			for col in range(BOARD_COLS):
				if board[row][col] == 0:
					return False

	return True

def check_win(player):
	# vertical win check
	for col in range(BOARD_COLS):
		if board[1][col] == player and board[2][col] == player and board[3][col] == player:
			draw_vertical_winning_line(col, player)
			return True

	# horizontal win check
	for row in range(BOARD_ROWS):
		if board[row][0] == player and board[row][1] == player and board[row][2] == player:
			draw_horizontal_winning_line(row, player)
			return True

	# asc diagonal win check
	if board[3][0] == player and board[2][1] == player and board[1][2] == player:
		draw_asc_diagonal(player)
		return True

	# desc diagonal win chek
	if board[1][0] == player and board[2][1] == player and board[3][2] == player:
		draw_desc_diagonal(player)
		return True

	return False

def draw_vertical_winning_line(col, player):
	posX = col * SQUARE_SIZE + SQUARE_SIZE//2

	if player == 1:
		color = CIRCLE_COLOR
	elif player == 2:
		color = CROSS_COLOR

	pygame.draw.line( screen, color, (posX, 215), (posX, HEIGHT - 15), LINE_WIDTH )

def draw_horizontal_winning_line(row, player):
	posY = row * SQUARE_SIZE + SQUARE_SIZE//2

	if player == 1:
		color = CIRCLE_COLOR
	elif player == 2:
		color = CROSS_COLOR

	pygame.draw.line( screen, color, (15, posY), (WIDTH - 15, posY), WIN_LINE_WIDTH )

def draw_asc_diagonal(player):
	if player == 1:
		color = CIRCLE_COLOR
	elif player == 2:
		color = CROSS_COLOR

	pygame.draw.line( screen, color, (15, HEIGHT - 15), (WIDTH - 15, 215), WIN_LINE_WIDTH )

def draw_desc_diagonal(player):
	if player == 1:
		color = CIRCLE_COLOR
	elif player == 2:
		color = CROSS_COLOR

	pygame.draw.line( screen, color, (15, 215), (WIDTH - 15, HEIGHT - 15), WIN_LINE_WIDTH )

def restart():
	screen.fill( BG_COLOR )
	draw_lines()
	draw_logo()
	for row in range(BOARD_ROWS):
		for col in range(BOARD_COLS):
			board[row][col] = 0

# ---------------
# CUSTOM FUCNTION
# ---------------
def start():
	print("test")
	screen.fill( BG_COLOR )
	draw_lines()
	draw_logo()
	
	draw_player(player)
	draw_score()
	draw_round(roundgame , currentround)

def draw_logo():
	image = pygame.image.load(currentDirectory + "/logo.png")
	image = pygame.transform.scale(image, DEFAULT_IMAGE_SMALL_SIZE)
	screen.blit(image, DEFAULT_IMAGE_POSITION)

def draw_logo_center():
	image = pygame.image.load(currentDirectory + "/logo.png")
	image = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)
	screen.blit(image, DEFAULT_IMAGE_POSITION_CENTER)

def draw_main_page():
	textStartDesc = fontSm.render("Press S to Start!!", True, TEXT_NO_BOX_COLOR, BG_COLOR)
	screen.blit(textStartDesc, textStartDesc.get_rect(center = (WIDTH // 2, (HEIGHT // 2) - 55)))
	textStartBtn = font.render("START", True, NAME_COLOR)
	screen.blit(textStartBtn, textStartBtn.get_rect(center = (WIDTH // 2, HEIGHT- 390)))

	textQuitDesc = fontSm.render("Press Q to QUIT!!", True, TEXT_NO_BOX_COLOR, BG_COLOR)
	screen.blit(textQuitDesc, textQuitDesc.get_rect(center = (WIDTH // 2, HEIGHT - 305)))
	textQuitBtn = font.render("QUIT", True, NAME_COLOR,)
	screen.blit(textQuitBtn, textQuitBtn.get_rect(center = (WIDTH // 2, HEIGHT - 240)))

	textThemeDesc = fontSm.render("Press T to change theme color", True, TEXT_NO_BOX_COLOR, BG_COLOR)
	screen.blit(textThemeDesc, textThemeDesc.get_rect(center = (WIDTH // 2, HEIGHT - 155)))
	textThemeBtn = font.render("Theme", True, NAME_COLOR,)
	screen.blit(textThemeBtn, textThemeBtn.get_rect(center = (WIDTH // 2, HEIGHT - 90)))

	textCredit = fontSm.render("Press C to Credit Page", True, TEXT_NO_BOX_COLOR, BG_COLOR)
	screen.blit(textCredit, textCredit.get_rect(center = (WIDTH // 2, HEIGHT - 30)))

def draw_btn_main_page():
	pygame.draw.rect( screen, BTN_COLOR, pygame.Rect(100, (HEIGHT // 2) - 30, 400, 80), 40, 20)
	pygame.draw.rect( screen, BTN_COLOR, pygame.Rect(100, HEIGHT - 280, 400, 80), 40, 20)
	pygame.draw.rect( screen, BTN_COLOR, pygame.Rect(100, HEIGHT - 130, 400, 80), 40, 20)

def draw_round_page():
	textOneDesc = fontMd.render("Press 1 to choose", True, TEXT_NO_BOX_COLOR, BG_COLOR)
	screen.blit(textOneDesc, textOneDesc.get_rect(center = (WIDTH // 2, (HEIGHT // 2) - 55)))
	textOne = font.render("Best of One", True, NAME_COLOR)
	screen.blit(textOne, textOne.get_rect(center = (WIDTH // 2, HEIGHT - 390)))

	textThreeDesc = fontMd.render("Press 3 to choose", True, TEXT_NO_BOX_COLOR, BG_COLOR)
	screen.blit(textThreeDesc, textThreeDesc.get_rect(center = (WIDTH // 2, HEIGHT - 305)))
	textThree = font.render("Best of Three", True, NAME_COLOR)
	screen.blit(textThree, textThree.get_rect(center = (WIDTH // 2, HEIGHT - 240)))

	textFiveDesc = fontMd.render("Press 5 to choose", True, TEXT_NO_BOX_COLOR, BG_COLOR)
	screen.blit(textFiveDesc, textFiveDesc.get_rect(center = (WIDTH // 2, HEIGHT - 155)))
	textFive = font.render("Best of Five", True, NAME_COLOR)
	screen.blit(textFive, textFive.get_rect(center = (WIDTH // 2, HEIGHT - 90)))

def draw_btn_round_page():
	pygame.draw.rect( screen, BTN_COLOR, pygame.Rect(100, (HEIGHT // 2) - 30, 400, 80), 40, 20)
	pygame.draw.rect( screen, BTN_COLOR, pygame.Rect(100, HEIGHT - 280, 400, 80), 40, 20)
	pygame.draw.rect( screen, BTN_COLOR, pygame.Rect(100, HEIGHT - 130, 400, 80), 40, 20)

def draw_round(roundgame , currentround):
	text = fontMd.render(get_round(roundgame) + " : Round " + str(currentround), True, TEXT_NO_BOX_COLOR, BG_COLOR)
	screen.blit(text, text.get_rect(center = (((WIDTH - 200) // 2) + 200, 30)))

def draw_player(player):
	text = font.render(get_name(player) + "'S TURN", True, TEXT_NO_BOX_COLOR, BG_COLOR)
	# screen.fill(BG_COLOR, DEFAULT_NAME_POSITION_BG)
	screen.fill(BG_COLOR, DEFAULT_NAME_POSITION_BG)
	screen.blit(text, text.get_rect(center = (((WIDTH - 200) // 2) + 200, 80)))
	textName1 = font.render(get_name(1), True, NAME_COLOR, BG_COLOR)
	screen.blit(textName1, textName1.get_rect(center = ((WIDTH // 2) , 120)))
	textName2 = font.render(get_name(2), True, NAME_COLOR, BG_COLOR)
	screen.blit(textName2, textName2.get_rect(center = (((WIDTH - 200) // 2) + 300, 120)))

def draw_score():
	textScore1 = font.render("Score : " + str(player_1_Score), True, TEXT_NO_BOX_COLOR, BG_COLOR)
	screen.blit(textScore1, textScore1.get_rect(center = ((WIDTH // 2) , 160)))
	textScore2 = font.render("Score : " + str(player_2_Score), True, TEXT_NO_BOX_COLOR, BG_COLOR)
	screen.blit(textScore2, textScore2.get_rect(center = (((WIDTH - 200) // 2) + 300, 160)))

def draw_win_player(player):
	text = font.render("PLAYER" + str(player), True, TEXT_NO_BOX_COLOR, BG_COLOR)
	# screen.fill(BG_COLOR, DEFAULT_NAME_POSITION_BG)
	screen.fill(BG_COLOR, DEFAULT_NAME_POSITION_BG)
	screen.blit(text, text.get_rect(center = (((WIDTH - 200) // 2) + 200, 60)))
	textName = font.render(get_name(player) + " Win !!!", True, TEXT_NO_BOX_COLOR, BG_COLOR)
	screen.blit(textName, textName.get_rect(center = (((WIDTH - 200) // 2) + 200, 120)))

def draw_enter_name(player):
	text = font.render("ENTER YOUR NAME PLAYER" + str(player) + " :", True, TEXT_NO_BOX_COLOR)
	screen.blit(text, text.get_rect(center = (WIDTH // 2, (HEIGHT // 2) - 60)))
	textRule = fontSm.render("CERTIFIED ONLY IN ENGLISH", True, TEXT_NO_BOX_COLOR)
	screen.blit(textRule, textRule.get_rect(center = (WIDTH // 2, (HEIGHT // 2) + 60)))
	textEnt = fontSm.render("IF FINISH PLEASE ENTER", True, TEXT_NO_BOX_COLOR)
	screen.blit(textEnt, textEnt.get_rect(center = (WIDTH // 2, (HEIGHT // 2) + 100)))
	pygame.draw.rect( screen, TEXTBOX_COLOR, pygame.Rect(100, (HEIGHT // 2) - 30, 400, 60), 30, 20)

def draw_win_sum():
	image = pygame.image.load(currentDirectory + "/WINK4.png")
	screen.blit(image, (0,0))
	text = font.render(get_round(roundgame), True, BLACK)
	screen.blit(text, text.get_rect(center = (((WIDTH) // 2), 210)))
	win_name = ""
	maxScore = 0
	if player_1_Score > player_2_Score:
		win_name = player_1_name
		maxScore = player_1_Score
	else:
		win_name = player_2_name
		maxScore = player_2_Score
	text_win = fontBig.render(win_name + " Win !!!", True, BLACK)
	screen.blit(text_win, text_win.get_rect(center = (((WIDTH) // 2), 310)))
	text_win = font.render("Score : " + str(maxScore), True, BLACK)
	screen.blit(text_win, text_win.get_rect(center = (((WIDTH) // 2), 410)))

def draw_btn_home():
	pygame.draw.rect( screen, BTN_COLOR, pygame.Rect(100, HEIGHT - 280, 400, 80), 40, 20)
	text = font.render("Back To Home", True, NAME_COLOR)
	screen.blit(text, text.get_rect(center = (WIDTH // 2, HEIGHT - 245)))
	textDesc = fontSm.render("Press H to back to home", True, TEXT_NO_BOX_COLOR, BG_COLOR)
	screen.blit(textDesc, textDesc.get_rect(center = (WIDTH // 2, HEIGHT - 180)))

def draw_theme():
	pygame.draw.rect( screen, NAME_COLOR, pygame.Rect(50, 110, 500, 390), 200, 20)
	pygame.draw.circle( screen, BTN_COLOR, (140, 225), 70)
	pygame.draw.circle( screen, BTN_COLOR, (300, 225), 70)
	pygame.draw.circle( screen, BTN_COLOR, (460, 225), 70)
	pygame.draw.circle( screen, BTN_COLOR, (140, 385), 70)
	pygame.draw.circle( screen, BTN_COLOR, (300, 385), 70)
	pygame.draw.circle( screen, BTN_COLOR, (460, 385), 70)

	pygame.draw.circle( screen, PINK, (140, 225), 50)
	pygame.draw.circle( screen, ORANGE, (300, 225), 50)
	pygame.draw.circle( screen, YELLOW, (460, 225), 50)
	pygame.draw.circle( screen, GREEN, (140, 385), 50)
	pygame.draw.circle( screen, BLUE, (300, 385), 50)
	pygame.draw.circle( screen, PURPLE, (460, 385), 50)

	textPink = fontSm.render("Press 1", True, WHITE)
	screen.blit(textPink, textPink.get_rect(center = (140, 225)))
	textOrange = fontSm.render("Press 2", True, WHITE)
	screen.blit(textOrange, textOrange.get_rect(center = (300, 225)))
	textYellow = fontSm.render("Press 3", True, BLACK)
	screen.blit(textYellow, textYellow.get_rect(center = (460, 225)))
	textGreen = fontSm.render("Press 4", True, BLACK)
	screen.blit(textGreen, textGreen.get_rect(center = (140, 385)))
	textBlue = fontSm.render("Press 5", True, BLACK)
	screen.blit(textBlue, textBlue.get_rect(center = (300, 385)))
	textPurple = fontSm.render("Press 6", True, WHITE)
	screen.blit(textPurple, textPurple.get_rect(center = (460, 385)))

def get_name(player): 
	if player == 1:
		return player_1_name
	else:
		return player_2_name
	
def get_round(roundgame): 
	if roundgame == 1:
		return "Best of One"
	elif roundgame == 3:
		return "Best of Three"
	else:
		return "Best of Five"
	
def draw_music():
	if isPlay:
		image = pygame.image.load(currentDirectory + "/play.png")
	else:
		image = pygame.image.load(currentDirectory + "/mute.png")
	image = pygame.transform.scale(image, DEFAULT_IMAGE_MUSIC_SIZE)
	screen.blit(image, DEFAULT_IMAGE_POSITION)

def play_mute_music():
	global isPlay 
	isPlay = not isPlay
	if isPlay:
		pygame.mixer.music.play()
	else:
		pygame.mixer.music.pause()

def reset_variables():
	global player
	player = 1
	global game_over
	game_over = False
	global roundgame
	roundgame = 1
	global currentround
	currentround = 1
	global player_1_Score
	player_1_Score = 0
	global player_2_Score
	player_2_Score = 0
	global player_1_name
	player_1_name = ""
	global player_2_name
	player_2_name = ""
	global turn
	turn = 0
	global board
	board = np.zeros( (BOARD_ROWS, BOARD_COLS) )
	global game_draw
	game_draw = False

def reset_for_draw():
	global player
	player = 1
	global game_over
	game_over = False
	global turn
	turn = 0
	global board
	board = np.zeros( (BOARD_ROWS, BOARD_COLS) )
	global game_draw
	game_draw = False

def draw_frame():
	screen.blit(imageFrame, (0,0))

def draw_credit():
	pygame.draw.rect( screen, NAME_COLOR, pygame.Rect(50, 100, 500, 160), 80, 20)
	text = font.render("BASE CODE BY", True, CROSS_COLOR)
	screen.blit(text, text.get_rect(center = (WIDTH // 2, HEIGHT - 650)))
	textpeople = fontMd.render("Alejandro González D.", True, CROSS_COLOR)
	screen.blit(textpeople, textpeople.get_rect(center = (WIDTH // 2, HEIGHT - 580)))
	pygame.draw.rect( screen, NAME_COLOR, pygame.Rect(50, 280, 500, 220), 110, 20)
	text1 = font.render("MODIFIED BY", True, CROSS_COLOR)
	screen.blit(text1, text1.get_rect(center = (WIDTH // 2, HEIGHT - 480)))
	textID1 = fontSm.render("Manissara Saejan 66102010151", True, CROSS_COLOR)
	screen.blit(textID1, textID1.get_rect(center = (WIDTH // 2, HEIGHT - 430)))
	textID2 = fontSm.render("Siwaschaya Rasree 66102010570", True, CROSS_COLOR)
	screen.blit(textID2, textID2.get_rect(center = (WIDTH // 2, HEIGHT - 380)))
	textID3 = fontSm.render("Amy Louis Brown 66102010572", True, CROSS_COLOR)
	screen.blit(textID3, textID3.get_rect(center = (WIDTH // 2, HEIGHT - 330)))
				
# ---------
# VARIABLES
# ---------
player = 1
game_over = False

# ---------------
# CUSTOM VARIABLE
# ---------------
roundgame = 1
currentround = 1
player_1_Score = 0
player_2_Score = 0
turn = 0
game_draw = False
player_1_name = ""
player_2_name = ""

# --------
# MAINLOOP
# --------
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		
		if not isMain:
			screen.fill(BG_COLOR)
			draw_frame()
			draw_logo_center()
			draw_btn_main_page()
			draw_main_page()
			reset_variables()
			print(player_1_name)

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_s:
					isMain = True
					isCredit = True
					isTheme = True
				elif event.key == pygame.K_t:
					isMain = True
				elif event.key == pygame.K_c:
					isMain = True
					isTheme = True
				elif event.key == pygame.K_q:
					sys.exit()

		elif not isTheme:
			screen.fill(BG_COLOR)
			draw_theme()
			draw_btn_home()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_h:
					isMain = False
					isCredit = False
					isTheme = False
					isRound = False
					isPlayer1 = False
					isPlayer2 = False
					isGame = False
				elif event.key == pygame.K_1:
					BG_COLOR = PINK
					LINE_COLOR = PINK_LINE
					TEXT_NO_BOX_COLOR = WHITE
					imageFrame = pygame.image.load(currentDirectory + "/Frame1.png")
				elif event.key == pygame.K_2:
					BG_COLOR = ORANGE
					LINE_COLOR = ORANGE_LINE
					TEXT_NO_BOX_COLOR = WHITE
					imageFrame = pygame.image.load(currentDirectory + "/Frame2.png")
				elif event.key == pygame.K_3:
					BG_COLOR = YELLOW
					LINE_COLOR = YELLOW_LINE
					TEXT_NO_BOX_COLOR = BLACK
					imageFrame = pygame.image.load(currentDirectory + "/Frame3.png")
				elif event.key == pygame.K_4:
					BG_COLOR = GREEN
					LINE_COLOR = GREEN_LINE
					TEXT_NO_BOX_COLOR = BLACK
					imageFrame = pygame.image.load(currentDirectory + "/Frame4.png")
				elif event.key == pygame.K_5:
					BG_COLOR = BLUE
					LINE_COLOR = BLUE_LINE
					TEXT_NO_BOX_COLOR = BLACK
					imageFrame = pygame.image.load(currentDirectory + "/Frame5.png")
				elif event.key == pygame.K_6:
					BG_COLOR = PURPLE
					LINE_COLOR = PURPLE_LINE
					TEXT_NO_BOX_COLOR = WHITE
					imageFrame = pygame.image.load(currentDirectory + "/Frame6.png")

		elif not isCredit:
			screen.fill(BG_COLOR)
			draw_credit()
			draw_btn_home()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_h:
					isMain = False
					isCredit = False
					isTheme = False
					isRound = False
					isPlayer1 = False
					isPlayer2 = False
					isGame = False
		
		elif not isRound:
			screen.fill(BG_COLOR)
			draw_logo_center()
			draw_btn_round_page()
			draw_round_page()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_1:
					roundgame = 1
					isRound = True
				elif event.key == pygame.K_3:
					roundgame = 3
					isRound = True
				elif event.key == pygame.K_5:
					roundgame = 5
					isRound = True

		elif not isPlayer1:
			screen.fill(BG_COLOR)
			draw_logo_center()
			draw_enter_name(1)
			text_surf = font.render(player_1_name, True, NAME_INPUT_COLOR)
			screen.blit(text_surf, text_surf.get_rect(center = screen.get_rect().center))

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN: #Enter
					isPlayer1 = True
				elif event.key == pygame.K_BACKSPACE: #ลบตัวอักษรตัวสุดท้าย
					player_1_name =  player_1_name[:-1]
				else:
					player_1_name += event.unicode

		elif not isPlayer2:
			screen.fill(BG_COLOR)
			draw_logo_center()
			draw_enter_name(2)
			text_surf = font.render(player_2_name, True, NAME_INPUT_COLOR)
			screen.blit(text_surf, text_surf.get_rect(center = screen.get_rect().center))

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					isPlayer2 = True
					start()
				elif event.key == pygame.K_BACKSPACE:
					player_2_name =  player_2_name[:-1]
				else:
					player_2_name += event.unicode

		elif event.type == pygame.MOUSEBUTTONDOWN and not game_over and not isGame:
			mouseX = event.pos[0] # x
			mouseY = event.pos[1] # y

			clicked_row = int(mouseY // SQUARE_SIZE)
			clicked_col = int(mouseX // SQUARE_SIZE)

			if available_square( clicked_row, clicked_col ):

				mark_square( clicked_row, clicked_col, player )
				
				if check_win( player ):
					draw_win_player(player)
					if player == 1:
						player_1_Score = player_1_Score + 1
					else:
						player_2_Score = player_2_Score +1
					game_over = True
					game_draw = False
				elif is_board_full():
					print('t2')
					game_over = True
					game_draw = True

				turn += 1
				player = player % 2 + 1

				draw_figures()

				if not game_over:
					draw_player(player)
					draw_score()
					draw_round(roundgame , currentround)
		
		elif (game_over and game_draw) and not isGame:
			currentround = currentround + 1
			game_over = False
			reset_for_draw()
			restart()
			draw_player(player)					
			draw_score()
			draw_round(roundgame , currentround)

		elif game_over and not isGame:
			pygame.time.delay(2 * 1000)
			maxScore = 0
			if player_1_Score > player_2_Score:
				maxScore = player_1_Score
			else:
				maxScore = player_2_Score
			if roundgame == 1:
				if maxScore == 1:
					isGame = True
			elif roundgame == 3:
				if maxScore == 2:
					isGame = True
				else:
					currentround = currentround + 1
					restart()
					player = 1
					draw_player(player)					
					draw_score()
					draw_round(roundgame , currentround)
					game_over = False
			elif roundgame == 5:
				if maxScore == 3:
					isGame = True
				else:
					currentround = currentround + 1
					restart()
					player = 1
					draw_player(player)
					draw_score()
					draw_round(roundgame , currentround)
					game_over = False
		elif isGame:
			screen.fill(BG_COLOR)
			draw_win_sum()
			draw_btn_home()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_h:
					isMain = False
					isCredit = False
					isTheme = False
					isRound = False
					isPlayer1 = False
					isPlayer2 = False
					isGame = False

		draw_music()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_F1:
				play_mute_music()

	pygame.display.update()