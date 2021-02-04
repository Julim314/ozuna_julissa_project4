while True:
    if input.acceleration(Dimension.Y) > 2:
        light.set_all(color.rgb(255, 255, 255))
    if input.rotation(Rotation.ROLL)> 0 :
        music.siren.play_until_done ()
    else:
        light.clear ()
        music.siren.stop()
        