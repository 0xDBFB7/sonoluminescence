# PyLuminescence

A simple GUI with sound output to control sonoluminescence systems.

---------------------

Sonoluminescence is an interesting phenomenon in which certain conditions can make water glow. If you're here, you probably know all about it. Let's dive in.

**The minimum required hardware setup:**

This is essentially the easiest possible sonoluminescent setup. I've drawn inspiration from the setups at techmind.org/sl as well as my own experience in sonoluminesce to create the simplest and lowest entry cost setup.

Required parts (total cost ~$40, no/minimal soldering required):

* A 25khz, ~60W piezo power transducer ([Reference transducer](http://www.ebay.com/itm/60W-25KHz-Ultrasonic-Piezoelectric-Transducer-Cleaner-Medical-Beauty-/161346061040?hash=item2590f982f0:g:9QQAAOSw3ydVzhOu)) 
* A >7w audio amplifier capable of outputting at 23khz at a reasonable power (most can, [reference part](https://www.canakit.com/5w-audio-amplifier-kit-ck153-uk153.html)). Even a stereo system amp should work.
* A 5-12v to 120v ~2amp transformer. This will be used to drive the transducer. [Reference part](http://www.mouser.com/ProductDetail/Hammond/166K6B/?qs=%2fha2pyFaduicWE%252bPDHDp88Z74tQbXOB3gxOnro9YHf4%3d)
* A 150ml flask, round/round-bottomed/spherical,distillation/boiling. [Reference.](https://www.amazon.ca/213L12-Karter-Scientific-Florence-Boiling/dp/B006VYY3UC/ref=sr_1_1?s=industrial&ie=UTF8&qid=1472616089&sr=1-1&keywords=150ml+round+bottom)
* A small piezo disk.
* A ~50k ohm potentiometer
* A phono cable.
* A computer with a sound card capable of at least 96000s/s output, and at least 44100s/s microphone input.

Additionally, you'll need:
* An airtight mason jar.
* Distilled water.
* Epoxy.
* A small dropper or syringe.

That's it!

### Setup guide ###

Super simple:

Glue the power transducer to the bottom of the flask, glue the sense transducer to the side of the flask, solder the L+R of the phono cable to one wire of the sense transducer, solder the GND of the phono cable to the other wire, solder the potentiometer across the sense transducer and adjust half-way or so.

Connect the 6.3v side of the transformer to the audio amp, connect the 120v side to the power transducer, connect power, connect the audio amp to your computer.

Done!

### Installation guide ###

*WINDOWS:*

I'm going to publish a .exe in a few commits. 

*LINUX:*

PyLu runs under python 2.7, with tkinter.

You also need:
    sudo apt-get install python-pyaudio

And you also need to install PyGame.



### Usage guide ###

WARNING: 

The steps below to remove gases from the water involve close contact with very hot boiling water. Scalding is very easy. Be careful, wear baking gloves, and I'm not responsible if anything goes wrong :)

*Put a wooden toothpick into a mason jar.* This prevents superheating and flesh-searing consequences. Don't skip this step.
Fill to the brim with distilled water.

Put in a microwave and wait ~4m until the water is vigorously boiling.

*Here's the dangerous bit.* Wearing thick rubber gloves, quickly open the microwave and screw the lid of the mason jar on very tightly.

Wait to cool for ~10 minutes.

Place in a fridge, and wait until the jar is quite cold: >30 min, but never wait longer than ~3 hours.

Take out the water and remove the cap: you should hear a pop of a vacuum. Very gently (without stirring up bubbles) pour it into the flask. You may find it helpful to pour down the inside of the flask to avoid bubbles.

Turn the audio amplifier to ~10 watts. Connect your computer. Run PyLuminescence. Click the "Tune" button, and wait for the coarse and fine tuning to complete. You should see a graph with a set of side lobes form, with one major lobe in the center.



