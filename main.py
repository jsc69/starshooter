def on_a_pressed():
    global projectile
    projectile = sprites.create_projectile_from_sprite(img("""
            . . . . . . . b b . . . . . . . 
                    . . . . . . d b b a . . . . . . 
                    . . . . . . d b b a . . . . . . 
                    . . . . . . d 2 2 a . . . . . . 
                    . . . . . . d 4 4 a . . . . . . 
                    . . . . . . 5 5 5 5 . . . . . . 
                    . . . . . . . 5 5 . . . . . . . 
                    . . . . . . . 5 5 . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        rocket,
        0,
        -100)
    projectile.set_flag(SpriteFlag.AUTO_DESTROY, True)
    music.pew_pew.play_until_done()
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite, otherSprite):
    sprite.destroy()
    otherSprite.destroy()
    info.change_score_by(1)
    music.power_up.play_until_done()
    if info.score() == 100:
        game.over(True)
sprites.on_overlap(SpriteKind.enemy, SpriteKind.projectile, on_on_overlap)

def on_life_zero():
    game.over(False)
info.on_life_zero(on_life_zero)

def on_on_overlap2(sprite, otherSprite):
    otherSprite.destroy()
    sprite.start_effect(effects.spray, 1000)
    info.change_life_by(-1)
    music.jump_down.play_until_done()
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

alien: Sprite = None
i = 0
projectile: Sprite = None
rocket: Sprite = None
effects.star_field.start_screen_effect()
rocket = sprites.create(img("""
        . . . . . . . 9 8 . . . . . . . 
            . . . . . . 9 6 6 8 . . . . . . 
            . . . . . . 9 6 6 8 . . . . . . 
            . . . . . 9 6 6 6 6 8 . . . . . 
            . . . . . 9 6 1 f 6 8 . . . . . 
            . . . . . 9 6 f f 6 8 . . . . . 
            . . . . 9 6 1 f f f 6 8 . . . . 
            . 6 . . 9 6 f f f f 6 8 . . 6 . 
            9 6 8 6 9 6 6 6 6 6 6 8 6 9 6 8 
            9 6 8 6 9 6 6 6 6 6 6 8 6 9 6 8 
            9 6 8 6 9 6 6 6 6 6 6 8 6 9 6 8 
            9 6 8 6 9 9 6 6 6 6 8 8 6 9 6 8 
            9 6 8 6 9 9 9 6 6 8 8 8 6 9 6 8 
            . 6 . . 9 9 9 6 6 8 8 . . . 6 . 
            . . . . . 9 6 6 6 8 . . . . . . 
            . . . . . . 5 2 5 . . . . . . .
    """),
    SpriteKind.player)
rocket.set_position(80, 104)
rocket.set_flag(SpriteFlag.STAY_IN_SCREEN, True)
controller.move_sprite(rocket)
info.set_score(0)
info.set_life(3)

def on_update_interval():
    global i, alien
    i = 0
    for index in range(10):
        if 7 > randint(0, 100 - info.score()):
            alien = sprites.create(img("""
                    . . . . . . . . . b b b b . . . 
                                    . . . . . . b b b d d d d b . . 
                                    . . . . . . b d d d d d d b . . 
                                    . . . . b b d d d d d b b d . . 
                                    . . . . b d d d d d d b b d b . 
                                    . . . . c d d d d d b b d b c . 
                                    . . . b c c b b b b d d b c c . 
                                    . . b b c c c b d d b c c c c . 
                                    . b b d d d b b b b b b c c c c 
                                    . c d d d d d d b d b c c c b c 
                                    . c b d d d b b d b c c c b b c 
                                    c b c c c c b d d b b b b b c c 
                                    c c b b b d d b c c b b b b c c 
                                    c c c c c c c c c b b b b c c . 
                                    . c c c c b b b b b b b c c . . 
                                    . . . . c c c c c c c c . . . .
                """),
                SpriteKind.enemy)
            alien.set_position(8 + 16 * i, 0)
            alien.set_velocity(0, 50)
            alien.set_flag(SpriteFlag.AUTO_DESTROY, True)
        i += 1
game.on_update_interval(500, on_update_interval)
