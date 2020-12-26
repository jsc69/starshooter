controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    projectile = sprites.createProjectileFromSprite(img`
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
        `, rocket, 0, -100)
    projectile.setFlag(SpriteFlag.AutoDestroy, true)
    music.pewPew.playUntilDone()
})
sprites.onOverlap(SpriteKind.Enemy, SpriteKind.Projectile, function (sprite, otherSprite) {
    sprite.destroy()
    otherSprite.destroy()
    info.changeScoreBy(1)
    music.powerUp.playUntilDone()
    if (info.score() == 100) {
        game.over(true)
    }
})
info.onLifeZero(function () {
    game.over(false)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite, otherSprite) {
    otherSprite.destroy()
    sprite.startEffect(effects.spray, 1000)
    info.changeLifeBy(-1)
    music.jumpDown.playUntilDone()
})
let alien: Sprite = null
let i = 0
let projectile: Sprite = null
let rocket: Sprite = null
effects.starField.startScreenEffect()
rocket = sprites.create(img`
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
    `, SpriteKind.Player)
rocket.setPosition(80, 104)
rocket.setFlag(SpriteFlag.StayInScreen, true)
controller.moveSprite(rocket)
info.setScore(0)
info.setLife(3)
game.onUpdateInterval(500, function () {
    i = 0
    for (let index = 0; index < 10; index++) {
        if (7 > randint(0, 100 - info.score())) {
            alien = sprites.create(img`
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
                `, SpriteKind.Enemy)
            alien.setPosition(8 + 16 * i, 0)
            alien.setVelocity(0, 50)
            alien.setFlag(SpriteFlag.AutoDestroy, true)
        }
        i += 1
    }
})
