CONFIG = dict(
    CYCLODATA = [
        'curr_range',
        'sample_rate',
        'volt_min',
        'volt_max',
        "volt_per_sec",
        'shift',
        'num_cycle',
        'quiet_value',
        'quiet_time',
    ],

    SQUAREWAVEDATA = [

    ],

    BUTTONS = [
        'start',
        'stop',
        'clear' 
    ],

    LABELS = {
        'curr_range'   : 'Current Range: ',
        'sample_rate'  : 'Sample Range: ',
        'volt_min'     : 'Volt Min: ',
        'volt_max'     : 'Volt Max: ',
        'volt_per_sec' : 'Volt / sec: ',
        'shift'        : 'Shift: ',
        'num_cycle'    : 'Num Cycle: ',
        'quiet_value'  : 'Quiet Value: ',
        'quiet_time'   : 'Quiet Time: ',

        'confirm'      : 'Bestätigen',
        'start'        : 'Messung starten!',
        'stop'         : 'Messung stoppen!',
        'clear'        : 'Clear'
    },

    TOOLTIPS = {
        'curr_range'   : 'Der Parameter currentRange beschreibt den Strombereich an der Y-Achse im Voltagramm.\nEs ist eine currentRange zwischen -100µA und 100µA möglich!',
        'sample_rate'  : 'Der Parameter sampleRate beschreibt die Abtastraste der Messung (Hz). Hinweis: Die Abtastrate ist 1/sample_period in Sekunden.',
        'volt_min'     : 'Der Parameter voltMin beschreibt die minimalste Spannung im Potential-Zeit-Diagramm und legt somit den Anfangs- und Endpunkt der Kurve fest.\nDie Amplitude resultiert aus (voltMax-voltMin)/2.',
        'volt_max'     : 'Der Parameter voltMax beschreibt die maximale Spannung im Potential-Zeit-Diagramm und legt somit den Peak der Kurve fest.\nDie Amplitude resultiert aus (voltMax-voltMin)/2.',
        'volt_per_sec' : 'Text.',
        'shift'        : 'Der Parameter shift gibt die Phasenverschiebung der Kurve an der X-Achse an.\n0 = keine Phasenverschiebung, 0,5 = 180° Phasenverschiebung',
        'num_cycle'    : 'Der Parameter numCycle gibt die Anzahl der Zyklen/Perioden an.\nEin Zyklus entspricht erst ein linear ansteigendes oder abfallendes Potential und anschließend ein rückläufiges Potential.',
        'quiet_value'  : 'Der Parameter quietValue gibt an, ab welchem Potential die Cyclovoltametrie beginnen soll\nDies ist ein optionaler Wert.',
        'quiet_time'   : 'Der Parameter quietTime gibt an, wie lange der quietValue-Wert gehalten werden soll.\nDie ist ein optionaler Wert.',

        'start'        : 'Die Messung wird gestartet.',
        'stop'         : 'Die Messung wird gestoppt.',
        'clear'        : 'Die Messung wird gelöscht.'
    }
)