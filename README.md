# Macragon

### Hexagonal macropad powered by a Waveshare 2040-zero with multiple keyboard layers, USB-C connectivity, RGB LEDs, and planned voice keyboard functionality.

[![zine poster](/assets/images/fallout_zine_image.png)](/assets/fallout_zine_macropad.pdf)

[![Onshape link](/assets/images/cad_isometric_view.png)](https://cvilleschools.onshape.com/documents/f18c9192e8883840eb23ee3e/w/cfee4e89906b8c2d7cd90130/e/c8d4c75ffcaf924e3f809773)

## Origins:
To be honest, my main motivation behind this project is mostly laziness :>. Long story short, my engineering class's keyboards are a bit annoying. To use them properly, one has to actually sit in their chair close to one's respective desk (it's more tiring than it sounds after an hour and a half). The chair arms are too far apart to support the keyboard away from the desk, and the rubber pads on the bottom of the keyboard mean that dust and debris will collect on your pants if the keyboard is in your lap. So, what I wanted to do is to have a little mic I could carry around that functioned as a voice keyboard, so I could actually slouch in my chair comfortably at a distance. That, combined with me seeing a lot of other Hackclub projects being macropads, meant I decided to make a fusion between the two. Ideally, the goal was to learn how to read and make schematics, PCB design, and improve my coding skills. The (farfetched) dream would be to have a voice keyboard that could recognize CAD commands while also having buttons for manual functions. Unfortunately, implementing a voice keyboard that plugs in as a USB audio device was harder than I expected in Python (I decided to use KMK instead of QMK), and as such has been left off until v2 of the macragon. However, the macropad keys still work, and as a bonus they have RGB LEDs. Additionally, the hardware for the microphone is on the PCB, and QMK supports the microprocessor, etc., so adding a voice keyboard will simply be a firmware update.

Another segment of motivation is just my fingers getting mad at me after I'd been creating hexagons and other repetitive tasks in Onshape without convienient keybinds for two hours a day for a week. (Yeah, I probably should have just unbound some other keybind I wasn't using.)

On the other hand, choosing the shape of my macropad was [easy](https://www.youtube.com/watch?v=thOifuHs6eY).

## Wiring Schematic
### Done in EasyEDA Pro
![macragon wiring schematic](/assets/images/macragon_wiring_schematic.png)


## PCB
### Done in EasyEDA Pro
Top layer:
![macragon pcb top view](/assets/images/pcb_top_view.png)

Bottom layer:
![macragon pcb bottom view](/assets/images/pcb_bottom_view.png)


## CAD
### Done in Onshape
Isometric:
![Macragon assembly isometric view](/assets/images/cad_isometric_view.png)

Top:
![Macragon assembly top view](/assets/images/cad_top_view.png)

Bottom:
![Macragon assembly bottom view](/assets/images/cad_bottom_view.png)

Side:
![Macragon assembly side view](/assets/images/cad_side_view.png)
(how low can it go?)

## PCB Order

## Credits
CAD completed in Onshape

PCB design completed in EasyEDA Pro

Zine designed in Canva

Sources of knowledge and inspiration (for design, layout, and also just because I don't know how to organize a repo well):
[NotARoomba's Cyberboard v2](https://blueprint.hackclub.com/projects/491)

Hackclub Fallout's pages on [good projects](https://fallout.hackclub.com/docs/project-resources/good-fallout-projects) and [zines](https://fallout.hackclub.com/docs/requirements/fallout-zine)

[Hackclub Magazine](https://magazine.hackclub.com/)

[s-ol's 0xC macropad](https://hw.s-ol.nu/0xC.pad/)
(how I found existing hexagonal keycaps)

[KMK Firmware Documentation](https://github.com/KMKfw/kmk_firmware)

[Github's Basic Markdown Documentation](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)


