def CtoF():
    global celsius, fahrenheit
    game.splash("Ingrese la temperatura en Celsius:")
    celsius = game.ask_for_number("Celsius:", 4)
    fahrenheit = Math.round(celsius * 9 / 5 + 32)
    game.splash("" + str(celsius) + "°C es igual a " + ("" + str(fahrenheit)) + "°F")
def FtoC():
    global fahrenheit, celsius
    game.splash("Ingrese la temperatura en Fahrenheit:")
    fahrenheit = game.ask_for_number("Fahrenheit:", 4)
    celsius = Math.round((fahrenheit - 32) * (5 / 9))
    game.splash("" + str(fahrenheit) + "°F es igual a " + ("" + str(celsius)) + "°C")
celsius = 0
fahrenheit = 0
scene.set_background_image(img("""
    6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        666666666666666666666666666666666666666666666666666666666666666666666666666fffffffff6666666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666fffcdddddddddcfff666666666666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666666666666fffcdddddddddcfff666666666666666666666666666666666666666666666666666666666666666666666666
        666666666666666666666666666666666666666666666666666666666666666666666fcdddddddddddddddddcf6666666666666666666666666666666666666666666666666666666666666666666666
        666666666666666666666666666666666666666666666666666666666666666666666fcddddd1d111111ddddcf6666666666666666666666666666666666666666666666666666666666666666666666
        666666666666666666666666666666666666666666666666666666666666666666cfcdddddbcccccccccbdddddbfc6666666666666666666666666666666666666666666666666666666666666666666
        666666666666666666666666666666666666666666666666666666666666666666cfcdddbcc1d1111111bcbdddbfc6666666666666666666666666666666666666666666666666666666666666666666
        666666666666666666666666666666666666666666666666666666666666666666cfcdddbcb1ddddddddbcbdddbfc6666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666cfcbdddcbddddbbdddddddbbbdddbfc66666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666cfcddddcb1ddbbbdddddddbcbdddbfc66666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666cfcddddcb1ddbbbdddddddbcbdddbfc66666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666cfcdbbbcb1ddbbbbbbddddbcbdddbfc66666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666cfcdbcccb1dddbbbbbbdddbcbdddbfc66666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666cfcddddcb1dddbbbbbddd1bcbdddbfc66666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666cfcddddcb1dddbbbbbddddbcbdddbfc66666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666cfcddddcb1dddbbbbbddddbcbdddbfc66666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666cfcdbfccb1dddbbbbbddd1bcbdddbfc66666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666cfcdbcccb1dddbbbbbddddbcbdddbfc66666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666cfcdd1dcb1ddbbbbbbddd1bcbdddbfc66666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666cfcddddcb1dbbbbbbbbbddbcbdddbfc66666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666cfcddddccdd224444444ddbcbdddbfc66666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666cfcdbccce4422444444444bcbdddbfc66666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666cfcdbccce4422444444444bcbdddbfc66666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666cfcdddbce4422442224444bbbdddbfc66666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666cfcddddfe4422442224444bcbdddbfc66666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666cfcddddfe4422442224444bcbdddbfc66666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666cfcddddfe4422442224444bcbdddbfc66666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666cfcdbccce4422442224444bcbdddbfc66666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666cfcdbfcce4422442224444bcbdddbfc66666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666cfcddbbce4422442224444bcbdddbfc66666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666cfcddddfe4422442224444bcbdddbfc66666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666cfcddddfe4422442224444bcbdddbfc66666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666cfcddddfe4422442224444bcbdddbfc66666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666cfcddddfe4422442224444bcbdddbfc66666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666cfcdddbfe4422442224444bcbdddbfc66666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666cfcdbccce4422442224444bcbdddbfc66666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666cfcddddfe4422442224444bcbdddbfc66666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666cfcddddfe4422442224444bcbdddbfc66666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666cfcddddfe4422442224444bcbdddbfc66666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666cfcddddfe4422442224444bcbdddbfc66666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666cfcddddfe4422442224444bcbdddbfc66666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666cfcdbccce4422442224444bcbdddbfc66666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666cfcdddbfe4422442224444bcbdddbfc66666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666cfcddddfe4422442224444bcbdddbfc66666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666cfcddddfe4422442224444bcbdddbfc66666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666cfcddddfe4422442224444bcbdddbfc66666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666cfbddddfe4422442224444bbbdddbfc66666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666bbbddddfe44e2442224444bcbddddbc66666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666ffbddddddfe4422442224444bcbdddddbff666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666bbddddddbee22224422244444bbbdddddbc666666666666666666666666666666666666666666666666666666666666666
        666666666666666666666666666666666666666666666666666666666666bcddddbbbee22222244444444dddbbbddddddbc6666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666ffddddddcfe442222224444444ddddd4bcbdddd1dff66666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666ffddddbbbee22e222224444444ddddd44ebddddddff66666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666ccddbbcce22222222224444444dddd44444bbddddcc66666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666ffbdddcce422222222222444444444444444444bbddddff666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666ffddddcce422e22222222444444444444444444cbddddff666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666ffddddcfe422e2222222244444444444444444efcddddff666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666ffddddcfe4222e222222244444444444444444effddddff666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666ffddddcfe42e22222222244444444444444444effddddff666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666ffddddcfe4eeee222222222444444444444442effddddff666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666ffddddcfe4eee2222222222444444444444422effddddff666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666ffddddcfe4eee2e22222222222444444442222effddddff666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666ffddddcce4eeeee22222222222222222222222eccddddff666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666ffddddcce4eeeeee2222222222222222222222eccddddff666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666ffbbbbcce44eeeeee2222222222222222eeccbbddff66666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666ffbbbbcceeeeeeeee222222222222222eecbbbbbbff66666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666ffbbbbbccce44eeee22222222ee22222eccbbbbbbff66666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666ccccbbbbcce44eeeeeeeeeeee2e222eeccbbbbbcccc66666666666666666666666666666666666666666666666666666666666
        666666666666666666666666666666666666666666666666666666666666ccccccccccc44eeeeeeeeee222eeccbbbbbbbc86666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666cfccccbbcce4444444444444ecbbbbbbcff666666666666666666666666666666666666666666666666666666666666666
        66666666666666666666666666666666666666666666666666666666666666cfcbbccccce4444444444444ecbbbbbbbf8666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666cfcbcccbcffffcccccccccbbbbbbcfc66666666666666666666666666666666666666666666666666666666666666666
        666666666666666666666666666666666666666666666666666666666666666666cfcbcccbbbbcbbbbbbbbbbbbcfc6666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666fccccccccccbbbbbbbbbbbbcf66666666666666666666666666666666666666666666666666666666666666666666
        666666666666666666666666666666666666666666666666666666666666666666666fffcbcccccccbbbbbcfff6666666666666666666666666666666666666666666666666666666666666666666666
        666666666666666666666666666666666666666666666666666666666666666666666fffccccccccccbbbbcfff6666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666fffffffffffff66666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
        6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
"""))
while True:
    CtoF()
    fahrenheit = 0
    celsius = 0
    FtoC()
    fahrenheit = 0
    celsius = 0