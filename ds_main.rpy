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
    
    def ds_initialize():
        ds_screens_save_act()
        meet('me', u"Ты")
        meet('uvp', u"Кошкодевочка")
    
    def ds_finalize():
        ds_screens_diact()
        meet('me', u"Семён")
        meet('uvp', u"Cтранная девочка")

init:
    $ mods["disco_sovenok"] = u"{font=mods/disco_sovenok/gui/fonts/VtcBadvision.otf}DISCO SOVENOK{/font}"
    if persistent.ds_settings['replace_interface']:
        $ config.start_callbacks.append(ds_initialize)

label disco_sovenok:
    window hide
    scene black with fade
    if not persistent.ds_settings['replace_interface']:
        $ ds_initialize()
    return

label ds_quit:
    window hide
    stop music fadeout 3
    scene black with fade
    $ ds_finalize()
    $ MainMenu(confirm=False)()

label ds_start:
    scene black

    show screen ds_call_hud

    python:
        if ds_archetype != 0:
            for skill in ds_archetype_presets[ds_archetype]:
                ds_skill_list[skill].set_level(ds_archetype_presets[ds_archetype][skill])
    
        ds_health.reset()
        ds_morale.reset()
        ds_semtype = 0

        ds_game_started = True

        for ch in ds_met:
            ds_met[ch] = 0

        meet('me', u"Ты")

        set_mode_adv()

    play music ds_dream fadein 2

    show ds_epigraph with dissolve2
    $ renpy.pause(3.0, hard=True)
    hide ds_epigraph with dissolve2

    show screen ds_start_game with dissolve2
    $ ui.interact()
    hide screen ds_start_game

    jump ds_prologue