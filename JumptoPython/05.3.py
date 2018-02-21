# import game_05.sound.echo
# game_05.sound.echo.echo_test()
#
# from game_05.sound import echo
# echo.echo_test()
#
# from game_05.sound.echo import echo_test
# echo_test()
#
# 밑에처럼만 실행하면 오류가 생긴다.
# __init__ 안에 __all__ 이라는 변수를 설정하고 improt 할 수 있는 모듈을 정의해 주어야 한다.
# +++ D:/__Python/game_05/sound/__init__.py 에 __all__ 변수를 추가하면 *으로 import 가능해진다.
# from game_05.sound import *
# echo.echo_test()


# +++ render.py 에 echo 를 추가했다.
from game_05.graphic.render import render_test
render_test()