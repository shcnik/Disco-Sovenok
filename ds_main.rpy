init:
    $ mods["disco_sovenok"] = u"Disco Sovenok"

label disco_sovenok:
    window hide
    scene black with fade
    $ ds_screens_save_act()
    return

label ds_quit:
    window hide
    stop music fadeout 3
    scene black with fade
    $ ds_screens_diact()
    $ MainMenu(confirm=False)()

label ds_start:
    scene black with dissolve

    show screen ds_call_hud

    if ds_archetype == 1:
        $ ds_skill_points['logic'], ds_skill_points['encyclopedia'], ds_skill_points['rhetoric'], ds_skill_points['drama'], ds_skill_points['conceptualization'], ds_skill_points['visual_calculus'] = 3, 4, 1, 3, 4, 3
        $ ds_skill_points['volition'], ds_skill_points['inland_empire'], ds_skill_points['authority'], ds_skill_points['empathy'], ds_skill_points['esprit'], ds_skill_points['suggestion'] = 2, 1, 1, 3, 1, 1
        $ ds_skill_points['endurance'], ds_skill_points['pain_threshold'], ds_skill_points['physical_instrument'], ds_skill_points['instinct'], ds_skill_points['shivers'], ds_skill_points['half_light'] = 3, 4, 3, 6, 3, 3
        $ ds_skill_points['perception'], ds_skill_points['coordination'], ds_skill_points['reaction_speed'], ds_skill_points['savoir_faire'], ds_skill_points['interfacing'], ds_skill_points['composure'] = 4, 3, 3, 4, 4, 5
    if ds_archetype == 2:
        $ ds_skill_points['logic'], ds_skill_points['encyclopedia'], ds_skill_points['rhetoric'], ds_skill_points['drama'], ds_skill_points['conceptualization'], ds_skill_points['visual_calculus'] = 2, 5, 4, 3, 5, 3
        $ ds_skill_points['volition'], ds_skill_points['inland_empire'], ds_skill_points['authority'], ds_skill_points['empathy'], ds_skill_points['esprit'], ds_skill_points['suggestion'] = 2, 4, 3, 4, 3, 3
        $ ds_skill_points['endurance'], ds_skill_points['pain_threshold'], ds_skill_points['physical_instrument'], ds_skill_points['instinct'], ds_skill_points['shivers'], ds_skill_points['half_light'] = 3, 3, 2, 3, 3, 3
        $ ds_skill_points['perception'], ds_skill_points['coordination'], ds_skill_points['reaction_speed'], ds_skill_points['savoir_faire'], ds_skill_points['interfacing'], ds_skill_points['composure'] = 4, 3, 4, 3, 4, 4
    if ds_archetype == 3:
        $ ds_skill_points['logic'], ds_skill_points['encyclopedia'], ds_skill_points['rhetoric'], ds_skill_points['drama'], ds_skill_points['conceptualization'], ds_skill_points['visual_calculus'] = 3, 1, 6, 5, 3, 3
        $ ds_skill_points['volition'], ds_skill_points['inland_empire'], ds_skill_points['authority'], ds_skill_points['empathy'], ds_skill_points['esprit'], ds_skill_points['suggestion'] = 4, 2, 6, 2, 4, 6
        $ ds_skill_points['endurance'], ds_skill_points['pain_threshold'], ds_skill_points['physical_instrument'], ds_skill_points['instinct'], ds_skill_points['shivers'], ds_skill_points['half_light'] = 5, 6, 5, 5, 2, 4
        $ ds_skill_points['perception'], ds_skill_points['coordination'], ds_skill_points['reaction_speed'], ds_skill_points['savoir_faire'], ds_skill_points['interfacing'], ds_skill_points['composure'] = 3, 5, 5, 2, 3, 6
    if ds_archetype == 0:
        pass
    
    $ ds_health = 0
    $ ds_morale = 0
    $ ds_semtype = 0

    $ ds_game_started = True

    $ ds_met['dv'] = 0
    $ ds_met['un'] = 0
    $ ds_met['sl'] = 0
    $ ds_met['us'] = 0
    $ ds_met['mi'] = 0
    $ ds_met['el'] = 0
    $ ds_met['mt'] = 0
    $ ds_met['mz'] = 0

    $ meet('me', u"Ты")

    $ set_mode_adv()

    play music ds_dream fadein 2

    # show ds_epigraph with dissolve2
    # renpy.pause(3.0)
    # hide ds_epigraph with dissolve2

    menu:
        "Начать":
            pass

    jump ds_prologue