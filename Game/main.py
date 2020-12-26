import snake
import pygame,sys

player = snake.Snake_game()

while True:
    pygame.time.delay(160 - player.speed * 10) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Xử lí sự kiện bàn phím
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.move = 'RIGHT'
            if event.key == pygame.K_LEFT:
                player.move = 'LEFT'
            if event.key == pygame.K_DOWN:
                player.move = 'DOWN'
            if event.key == pygame.K_UP:
                player.move = 'UP'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.evet.event(pygame.QUIT))

        # Xử lí hướng đi của rắn
    if player.move == 'RIGHT' and not player.direction == 'LEFT':
        player.direction = 'RIGHT'
    if player.move == 'LEFT' and not player.direction == 'RIGHT':
        player.direction = 'LEFT'
    if player.move == 'UP' and not player.direction == 'DOWN':
        player.direction = 'UP'
    if player.move == 'DOWN' and not player.direction == 'UP':
        player.direction = 'DOWN'

    
    # Chạm vào viền chết

    if player.snakepos[0] > player.width - player.left -20  or player.snakepos[0] < player.left:
        player.gameover()
    if player.snakepos[1] > player.height - player.top or player.snakepos[1] < player.top:
        player.gameover()

    if player.direction == 'RIGHT':
        player.snakepos[0] += player.px     # player.px = 20
    if player.direction == 'LEFT':
        player.snakepos[0] -= player.px
    if player.direction == 'UP':
        player.snakepos[1] -= player.px
    if player.direction == 'DOWN':
        player.snakepos[1] += player.px

    player.DrawFood()
    player.refresh()
    player.render() #render object
    
    # nếu rắn chạm vào quả táo, tăng chiều dài rắn
    player.snakebody.insert(0,list(player.snakepos))
    if player.snakepos[0] == player.fpos[0] and player.snakepos[1] == player.fpos[1]: 
        player.Eat_sound.play()
        player.score += len(player.snakebody)* 10 # điểm được tính bằng độ dài * 10
        if player.speed < player.maxspeed: # max = 13
            if player.score > player.speed * 500:
                player.speed += 1
                player.height -= 20
                player.width -= 30
                player.resetpos()
                
        player.Have_Food = False
    else:
        player.snakebody.pop()

        # Chạm vào thân chết
    for die in player.snakebody[1:]:
        if player.snakepos[0] == die[0] and player.snakepos[1] == die[1]:
            player.gameover()

       

    player.drawline(player.left, player.top, player.width - player.left - 20, player.height-player.top - 20)
    player.displayscore()
    pygame.display.flip()
