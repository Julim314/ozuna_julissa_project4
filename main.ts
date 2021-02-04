while (true) {
    if (input.acceleration(Dimension.Y) > 2) {
        light.setAll(color.rgb(255, 255, 255))
    }
    
    if (input.rotation(Rotation.Roll) > 0) {
        music.siren.playUntilDone()
    }
    
}
