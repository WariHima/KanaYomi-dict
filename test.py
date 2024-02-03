import pyopenjtalk

pyopenjtalk.update_global_jtalk_with_user_dict("kanayomi-dict.dic")

print(pyopenjtalk.g2p("archive"))
print(pyopenjtalk.g2p("eye"))
print(pyopenjtalk.g2p("あーかいぶ"))
print(pyopenjtalk.g2p("あいこん"))