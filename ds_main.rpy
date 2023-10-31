init:
    $ mods["disco_sovenok"] = u"{font=mods/disco_sovenok/gui/fonts/VtcBadvision.otf}DISCO SOVENOK{/font}"

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
    scene black

    show screen ds_call_hud

    if ds_archetype == 1:
        $ ds_skill_points['logic'], ds_skill_points['encyclopedia'], ds_skill_points['rhetoric'], ds_skill_points['drama'], ds_skill_points['conceptualization'], ds_skill_points['visual_calculus'] = 5, 6, 5, 5, 5, 5
        $ ds_skill_points['volition'], ds_skill_points['inland_empire'], ds_skill_points['authority'], ds_skill_points['empathy'], ds_skill_points['esprit'], ds_skill_points['suggestion'] = 2, 2, 2, 2, 2, 2
        $ ds_skill_points['endurance'], ds_skill_points['pain_threshold'], ds_skill_points['physical_instrument'], ds_skill_points['instinct'], ds_skill_points['shivers'], ds_skill_points['half_light'] = 1, 1, 1, 1, 1, 1
        $ ds_skill_points['perception'], ds_skill_points['coordination'], ds_skill_points['reaction_speed'], ds_skill_points['savoir_faire'], ds_skill_points['interfacing'], ds_skill_points['composure'] = 4, 4, 4, 4, 4, 4
    if ds_archetype == 2:
        $ ds_skill_points['logic'], ds_skill_points['encyclopedia'], ds_skill_points['rhetoric'], ds_skill_points['drama'], ds_skill_points['conceptualization'], ds_skill_points['visual_calculus'] = 3, 3, 3, 3, 3, 3
        $ ds_skill_points['volition'], ds_skill_points['inland_empire'], ds_skill_points['authority'], ds_skill_points['empathy'], ds_skill_points['esprit'], ds_skill_points['suggestion'] = 5, 6, 5, 5, 5, 5
        $ ds_skill_points['endurance'], ds_skill_points['pain_threshold'], ds_skill_points['physical_instrument'], ds_skill_points['instinct'], ds_skill_points['shivers'], ds_skill_points['half_light'] = 2, 2, 2, 2, 2, 2
        $ ds_skill_points['perception'], ds_skill_points['coordination'], ds_skill_points['reaction_speed'], ds_skill_points['savoir_faire'], ds_skill_points['interfacing'], ds_skill_points['composure'] = 2, 2, 2, 2, 2, 2
    if ds_archetype == 3:
        $ ds_skill_points['logic'], ds_skill_points['encyclopedia'], ds_skill_points['rhetoric'], ds_skill_points['drama'], ds_skill_points['conceptualization'], ds_skill_points['visual_calculus'] = 1, 1, 1, 1, 1, 1
        $ ds_skill_points['volition'], ds_skill_points['inland_empire'], ds_skill_points['authority'], ds_skill_points['empathy'], ds_skill_points['esprit'], ds_skill_points['suggestion'] = 2, 2, 2, 2, 2, 2
        $ ds_skill_points['endurance'], ds_skill_points['pain_threshold'], ds_skill_points['physical_instrument'], ds_skill_points['instinct'], ds_skill_points['shivers'], ds_skill_points['half_light'] = 5, 5, 6, 5, 5, 5
        $ ds_skill_points['perception'], ds_skill_points['coordination'], ds_skill_points['reaction_speed'], ds_skill_points['savoir_faire'], ds_skill_points['interfacing'], ds_skill_points['composure'] = 4, 4, 4, 4, 4, 4
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

    show ds_epigraph with dissolve2
    $ renpy.pause(3.0, hard=True)
    hide ds_epigraph with dissolve2

    menu:
        "Начать":
            pass

    jump ds_prologue