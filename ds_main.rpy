init python:
    if persistent.ds_achievements == None:
        persistent.ds_achievements = {
            'preterm': False,
            'bus_crash': False,
            'beat_girls': False,
            'know_history': False,
            'had_sex': False,
            'us_gone': False,
            'mi_rape': False,
            'arstotzka': False,
            'electrocution': False,
            'us_escape': False,
        }
        persistent.ds_achievements['preterm'] = False
        persistent.ds_achievements['bus_crash'] = False
        persistent.ds_achievements['beat_girls'] = False
        persistent.ds_achievements['know_history'] = False
        persistent.ds_achievements['had_sex'] = False
        persistent.ds_achievements['us_gone'] = False
        persistent.ds_achievements['mi_rape'] = False
        persistent.ds_achievements['arstotzka'] = False
        persistent.ds_achievements['electrocution'] = False
        persistent.ds_achievements['us_escape'] = False
    
    if persistent.ds_settings == None:
        persistent.ds_settings = {}

        persistent.ds_settings['hentai'] = True
        persistent.ds_settings['obscene'] = True
        persistent.ds_settings['replace_interface'] = False
        persistent.ds_settings['show_other_saves'] = True
        persistent.ds_settings['cheat_codes'] = 0

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

    show screen ds_start_game with dissolve2
    $ ui.interact()
    hide screen ds_start_game

    jump ds_prologue