#!/usr/bin/env python3
"""Standalone import script for GA012 — GA012 - Die Stufen der höheren Erkenntnis (1905 – 1908)"""

import subprocess
import sys
from pathlib import Path

# === CONFIGURATION ===
BOOK_TITLE = """GA012 - Die Stufen der höheren Erkenntnis (1905 – 1908)"""
GA_NUMBER = "GA012"
DB_NAME = "steiner_reader"
DB_USER = "steiner"
DOCKER_CONTAINER = "steiner-postgres"

# === CHAPTER DATA ===
CHAPTERS = [
  {
    "order": 1,
    "title_de": "Inhalt",
    "paragraphs": [
      "RUDOLF STEINER",
      "DER HÖHEREN ERKENNTNIS",
      "Mit Vor- und Nachwort von Marie Steiner",
      "VERLAG DER RUDOLF STEINER-NACHLASSVERWALTUNG",
      "DORNACH / SCHWEIZ",
      "bei der Rudolf Steiner-Nachlaßverwaltung, Dornach",
      "Zuerst erschienen in der Zeitschrift «Lucifer-Gnosis»",
      "in den Nummern 29, 30, 32, 34 und 35",
      "(Oktober 1905Mai 1908)",
      "(Oktober 1905Mai 1908)",
      "©  1959 by Rudolf Steiner-Nachlaßverwaltung, Dornach /Schweiz",
      "Typographie und Druck: Benteli AG, Bern-Bümpliz",
      "Printed in Switzerland",
      "Vorwort von Marie Steiner    7",
      "Aus der Vorrede zur fünften Auflage des Buches",
      "«Wie erlangt man Erkenntnisse der höheren",
      "Welten?»    13",
      "Die Stufen der höheren Erkenntnis    15",
      "Die Imagination    35",
      "Die Inspiration    50",
      "Inspiration und Intuition    66",
      "Aus dem Nachwort von Marie Steiner    79",
      "Zur Neuauflage 1959    81",
      "Übersicht über die Rudolf Steiner-Gesamtausgabe  82"
    ],
    "sentences": [
      [
        "RUDOLF STEINER"
      ],
      [
        "DER HÖHEREN ERKENNTNIS"
      ],
      [
        "Mit Vor- und Nachwort von Marie Steiner"
      ],
      [
        "VERLAG DER RUDOLF STEINER-NACHLASSVERWALTUNG"
      ],
      [
        "DORNACH / SCHWEIZ"
      ],
      [
        "bei der Rudolf Steiner-Nachlaßverwaltung, Dornach"
      ],
      [
        "Zuerst erschienen in der Zeitschrift «Lucifer-Gnosis»"
      ],
      [
        "in den Nummern 29, 30, 32, 34 und 35"
      ],
      [
        "(Oktober 1905Mai 1908)"
      ],
      [
        "(Oktober 1905Mai 1908)"
      ],
      [
        "© 1959 by Rudolf Steiner-Nachlaßverwaltung, Dornach /Schweiz"
      ],
      [
        "Typographie und Druck: Benteli AG, Bern-Bümpliz"
      ],
      [
        "Printed in Switzerland"
      ],
      [
        "Vorwort von Marie Steiner 7"
      ],
      [
        "Aus der Vorrede zur fünften Auflage des Buches"
      ],
      [
        "«Wie erlangt man Erkenntnisse der höheren"
      ],
      [
        "Welten?» 13"
      ],
      [
        "Die Stufen der höheren Erkenntnis 15"
      ],
      [
        "Die Imagination 35"
      ],
      [
        "Die Inspiration 50"
      ],
      [
        "Inspiration und Intuition 66"
      ],
      [
        "Aus dem Nachwort von Marie Steiner 79"
      ],
      [
        "Zur Neuauflage 1959 81"
      ],
      [
        "Übersicht über die Rudolf Steiner-Gesamtausgabe 82"
      ]
    ]
  },
  {
    "order": 2,
    "title_de": "Vorwort von Marie Steiner",
    "paragraphs": [
      "Die von Rudolf Steiner im Dienste der Geisteswissenschaft herausgegebene Zeitschrift «Luzifer » erfuhr im Jahre 1904 eine Erweiterung durch ihre Vereinigung mit der in Öster­reich erscheinenden Zeitschrift «Gnosis». Unter dem Dop­pelnamen «Lucifer-Gnosis» brachte sie dann jene Aufsätze Rudolf Steiners, die später, gesammelt, das Buch wurden, das neben der «Theosophie» und «Geheimwissenschaft» zu den grundlegenden Werken gehört für die Einführung in die anthroposophisch orienterte Geisteswissenschaft.",
      "Eine Fortsetzung jener Aufsätze erschien unter dem Titel «Die Stufen der höheren Erkenntnis». Es war gedacht, sie späterhin zu einem zweiten Bande zu gestalten, als Weiter­führung der in «Wie erlangt man Erkenntnisse der höheren Welten?» begonnenen Betrachtungen.",
      "Die Überfülle der Arbeit jedoch, die außerordentliche Inanspruchnahme Ru­dolf Steiners durch Vortragstätigkeit, machte es allmählich unmöglich, sich der Zeitschrift in genügendem Maße zu widmen, obgleich sie an Verbreitung stetig gewann. Aus Mangel an Zeit mußte sie eingestellt werden.",
      "So wurde denn auch das weitere Erscheinen jener Aufsätze über «Die Stufen der höheren Erkenntnis» unterbrochen. Es ist öfters die Bitte an uns herangetreten, durch eine Neuausgabe sie wieder zugänglich zu machen.",
      "Diesem Wunsche wird hier­mit nachgekommen. Da der Text plötzlich abbricht, kann das Buch nicht den Wert der Vollständigkeit beanspruchen. So war es berechtigt, sich die Frage zu stellen, ob die Her­ausgabe nicht besser unterbleiben solle.",
      "Die hier in Aus­sicht gestellten nicht zum Abschluß gekommenen Darle­gungen sind ja vielfach in anderer Form, unter anderen Ti­teln",
      "schon veröffentlicht worden. Doch bleibt es für den Geistessucher eine Tatsache, daß die Eroberung der geisti­gen Wirklichkeit nur dann möglich ist und keine Illusion, wenn immer wieder zurückgegriffen wird zu den einmal durchgearbeiteten, nie genug verarbeiteten geistigen In­halten, wenn immer wieder der Weg neu erlebt wird, der einmal die Richtung zum Geistgebiet gewiesen hat. Das Seelenleben des meditativ Arbeitenden muß so beweglich gehalten werden, daß die Ausblicke, die ihm der eine Weg gegeben hat, ihn um so empfänglicher machen für die Fernblicke von anderen Gesichtspunkten aus.",
      "Die hier veröffentlichten Aufsätze haben zugleich einen historischen Wert. Sie zeigen den Ausgangspunkt, den die esoterischen Unterweisungen Rudolf Steiners haben neh­men müssen; sie zeigen uns, wie er der bahnbrechende Füh­rer geworden ist auch auf diesem Gebiet, auf welchem zum erstenmal durch ihn der Mensch der Freiheit übergeben werden durfte. Dazu mußte mit weltumspannendem Blick und größtem Verantwortlichkeitsgefühl eine Grundlage vorgebaut, eine Geisthaltung geschaffen werden, die es dem Menschen möglich macht, in sich selbst den festen morali­schen Halt findend, in dieser Freiheit nicht den Versuchun­gen, der Verirrung anheimzufallen, Um eine solche Tat am entscheidenden Wendepunkte historischer Umwälzungen, inmitten feindlicher Gegenkräfte, nur auf sich selbst ge­stellt, zu vollbringen, war das ungeheure Ethos notwendig, welches das ganze Lebenswerk Rudolf Steiners durchpulst und nichts anderes mehr für ihn in Betracht kommen ließ als das Wohl der Menschheit, die Rettung des Abendlandes vor dem drohenden Untergange. Dazu mußte von den Fundamenten aus gebaut werden in einer Art, die den For­derungen",
      "der Zeit entsprach. Die Synthese alles Wissens war dazu notwendig.",
      "Greift man zu diesen Aufsätzen, die am Anfang jenes er­staunlichen Lebenswerkes geschrieben worden sind, das am 30. März 1925 seinen Abschluß fand und, bald nach der Jahrhundertwende, einen schicksalsgewollten Einschlag er­halten hatte durch die Verbindung mit den aus orientali­schen Quellen gespeisten theosophischen Kreisen, so wird man zur Frage gedrängt: Wie ist es zu verstehen, daß Ru­dolf Steiner, der uns auch auf dem Gebiete der Esoterik zur Freiheit führte, auch hier uns auf uns selber stellte und nur unserm eigenen höhern Ich uns geloben ließ, was sonst der Schüler dem Lehrer als Gelöbnis zu leisten hatte, daß Ru­dolf Steiner hier in diesen Aufsätzen noch von der Notwen­digkeit des strengen Anschlusses an den Führer spricht, den Schüler gleichsam in die Abhängigkeit des Lehrers stellt?",
      "In Wahrheit handelt es sich bei Rudolf Steiner nur um die Beschreibung eines Vertrauensverhältnisses. Das Auto­ritative hat er von Anfang an vermieden und von sich ge­wiesen. In alten Zeiten übernahmen die initiierenden Prie­ster die volle Verantwortung für den in die Mysterien des geistigen Seins Einzuweihenden und wirkten mit ihrem Willen in ihn hinein. So war er zugleich geschützt und ge­führt und konnte den Gefahren entrinnen, die ihn sonst überwältigt hätten. Sein Ich schwebte ja noch über seinen physischen Hüllen, sein Selbstbewußtsein war nicht er­wacht. Dieses immer mehr zur Erweckung zu bringen, war der Weg der fortschreitenden Mysterienschulung. Und in der christlichen Einweihung sehen wir durch den Hinweis auf den Weltenlehrer die Abhängigkeit vom persönlichen Lehrer schon gemildert, wenn auch noch vorhanden. Sie",
      "verliert immer mehr ihren persönlichen Charakter in der rosenkreuzerischen Schulung und gestaltet sich um zum Vertrauensverhältnis. Der Lehrer steht dem Schüler bei, zeigt ihm den Weg, den jener sucht und allein nicht finden kann, stützt ihn moralisch, weist ihn auf die Gefahren hin, die seinem Charakter drohen - aus Eitelkeit, aus der Vor­gaukelung trügerischer Bilder, die er unterscheiden lernen muß von wahrer geistiger Wirklichkeit. So ist der Lehrer ein Helfer, der sich in dem Augenblicke sogleich zurück­ziehen würde, wo das Vertrauen abhanden käme. An dem Schicksalswendepunkte, in dem wir stehen, mußte der für die Jetztzeit wirkende Lehrer hinweisen auf die Vergangen­heit, Gegenwart und Zukunft menschlichen Geistesstre­bens und, indem er mit der Erziehung des Einzelnen be­gann, sein Werk so ausbauen, daß es als Menschheitstat da­stehen konnte: ein für die Nachwelt neuerrungenes Le­benselement. So schuf Rudolf Steiner eine Initiationswis­senschaft, in der von nun an jeder ernste, sittlich strebende Mensch den Boden wird finden können, der ihn trägt, die Elemente wird greifen können, die ihm das Unterschei­dungsvermögen schärfen, während sich ihm neue Welten eröffnen. Er braucht nicht unsicher zu sein, er hat genug, um sich durchzutasten, bis er in geistigen Landen den Füh­rer findet.",
      "Ein solches war nicht vorhanden, bevor Rudolf Steiner sein Geisteswerk begann. Seine Tat ist - die «Wissenschaft» von der Initiation. Durch sie wird entsiegelt, was verbor­gen lag in den Mysterien der alten Tempel: neben dem Wis­sen des Werdens der Welten das Wissen vom kommenden Niederstieg des Christus; und was versiegelt ward in der Kirche: die erlösende Tat der Menschheitsbefreiung durch",
      "den Christus, die im Laufe der Zeit durch Ihn sich vollzie­hende Ich-Durchdringung des Einzelnen. Statt der persön­lichen Führung wird es nun Aufgabe, durch die Kräfte des Zeitgeistes den Menschen den Weg finden zu lassen zum Menschheits-Ich, zum Christus. Das Bewußtsein des ein­zelnen Menschen wird reif gemacht zum Entgegennehmen der höheren Ichkraft, das Selbstbewußtsein wird emporge­hoben zum Geistselbst.",
      "Es ist die Arbeit der Zukunft. Aber nur auf dem Boden der Vergangenheit stehend, kann man, Künftiges vorberei­tend, die Gegenwart befruchten. Sonst schafft man ins Lee­re. Metamorphose auch hier. Die Zukunft wird gestaltet, indem die auf dem Boden der Vergangenheit stehende Ge­genwart umgeformt wird, Neues tritt hinzu, wie der neue Frühling dem Winter folgt. Sonnenkraft durchfeuert die Erde; Ersterbendes, in Wesenhaftes sich Umwandelndes wird zu neuem Leben entfacht, indem sich von oben die Gnade hinuntersenkt.",
      "Auch auf dem Gebiet der Esoterik entwickelt sich kon­tinuierliches historisches Geschehen durch das Gesetz der steigenden Entwickelung und der auf- und abflutenden Welle des vergehenden und auf blühenden Lebens bis zudem scheinbar plötzlichen Augenblick, wo die Gnade überstrah­lend hereinbricht, gleich dem Wunder der auf leuchtenden Blüte in der grünen Pflanzenwelt. Doch ohne diese durch weise Mächte von Form zu Form durchgeführte Wand­lung und stete Steigerung auf allen Gebieten der Lebensäußerung würden die neuen Werte, die Gaben des Geistes, die feurigen Zungen des Wortes, sich nicht zu uns hernie­dersenken. Ohne Kenntnis solchen Geschehens wären die Empfangenden nicht in der Lage, zu ermessen, was unter",
      "ihnen sich vollziehen will. Das neue Große könnte sich nicht auswirken, die Zukunft nicht gerettet werden.",
      "Die nach geistigen Erkenntnissen ringenden Seelen, die an Rudolf Steiner herantraten, waren das schicksalgewoll­te, von der Zeit ihm zugeführte Menschenmaterial, mit dem Rudolf Steiner zu arbeiten hatte, aus deren Bedürfnissen und Voraussetzungen heraus er das zu gestalten hatte, was auf Grund eines erkenntnismäßig fundamentierten Auf­baus zur Wissenschaft der Initiation werden konnte. Aus der Trägheit der Zeit dem Geiste gegenüber galt es, Men­schen herauszureißen, die Brücke würden sein können für die Forderungen der Zukunft.",
      "Am schwersten war es, den Sinn zu wecken für die innere Freiheit und das Auf-sich-selbst-gestellt-Sein in eigener Verantwortung. In peinlichster Berücksichtigung dieses Zieles hat Rudolf Steiner nichts anderes den Menschen sein wollen als Unterweiser und  wo man ihn darum bat, Bera­ter, Erwecker von menschheitlichen Geistimpulsen. Er konnte Darsteller werden von geistigen Tatsachen, weil sein Denken und Schauen lebendurchtränkt war und sich von Glied zu Glied entfaltete mit der Kraft eines naturhaf­ten Organismus. Sein Geisteswerk steht vor uns: die wie­derhergestellte Einheit von Wissenschaft, Kunst und Reli­gion."
    ],
    "sentences": [
      [
        "Die von Rudolf Steiner im Dienste der Geisteswissenschaft herausgegebene Zeitschrift «Luzifer » erfuhr im Jahre 1904 eine Erweiterung durch ihre Vereinigung mit der in Öster­reich erscheinenden Zeitschrift «Gnosis».",
        "Unter dem Dop­pelnamen «Lucifer-Gnosis» brachte sie dann jene Aufsätze Rudolf Steiners, die später, gesammelt, das Buch wurden, das neben der «Theosophie» und «Geheimwissenschaft» zu den grundlegenden Werken gehört für die Einführung in die anthroposophisch orienterte Geisteswissenschaft."
      ],
      [
        "Eine Fortsetzung jener Aufsätze erschien unter dem Titel «Die Stufen der höheren Erkenntnis».",
        "Es war gedacht, sie späterhin zu einem zweiten Bande zu gestalten, als Weiter­führung der in «Wie erlangt man Erkenntnisse der höheren Welten?» begonnenen Betrachtungen."
      ],
      [
        "Die Überfülle der Arbeit jedoch, die außerordentliche Inanspruchnahme Ru­dolf Steiners durch Vortragstätigkeit, machte es allmählich unmöglich, sich der Zeitschrift in genügendem Maße zu widmen, obgleich sie an Verbreitung stetig gewann.",
        "Aus Mangel an Zeit mußte sie eingestellt werden."
      ],
      [
        "So wurde denn auch das weitere Erscheinen jener Aufsätze über «Die Stufen der höheren Erkenntnis» unterbrochen.",
        "Es ist öfters die Bitte an uns herangetreten, durch eine Neuausgabe sie wieder zugänglich zu machen."
      ],
      [
        "Diesem Wunsche wird hier­mit nachgekommen.",
        "Da der Text plötzlich abbricht, kann das Buch nicht den Wert der Vollständigkeit beanspruchen.",
        "So war es berechtigt, sich die Frage zu stellen, ob die Her­ausgabe nicht besser unterbleiben solle."
      ],
      [
        "Die hier in Aus­sicht gestellten nicht zum Abschluß gekommenen Darle­gungen sind ja vielfach in anderer Form, unter anderen Ti­teln"
      ],
      [
        "schon veröffentlicht worden.",
        "Doch bleibt es für den Geistessucher eine Tatsache, daß die Eroberung der geisti­gen Wirklichkeit nur dann möglich ist und keine Illusion, wenn immer wieder zurückgegriffen wird zu den einmal durchgearbeiteten, nie genug verarbeiteten geistigen In­halten, wenn immer wieder der Weg neu erlebt wird, der einmal die Richtung zum Geistgebiet gewiesen hat.",
        "Das Seelenleben des meditativ Arbeitenden muß so beweglich gehalten werden, daß die Ausblicke, die ihm der eine Weg gegeben hat, ihn um so empfänglicher machen für die Fernblicke von anderen Gesichtspunkten aus."
      ],
      [
        "Die hier veröffentlichten Aufsätze haben zugleich einen historischen Wert.",
        "Sie zeigen den Ausgangspunkt, den die esoterischen Unterweisungen Rudolf Steiners haben neh­men müssen; sie zeigen uns, wie er der bahnbrechende Füh­rer geworden ist auch auf diesem Gebiet, auf welchem zum erstenmal durch ihn der Mensch der Freiheit übergeben werden durfte.",
        "Dazu mußte mit weltumspannendem Blick und größtem Verantwortlichkeitsgefühl eine Grundlage vorgebaut, eine Geisthaltung geschaffen werden, die es dem Menschen möglich macht, in sich selbst den festen morali­schen Halt findend, in dieser Freiheit nicht den Versuchun­gen, der Verirrung anheimzufallen, Um eine solche Tat am entscheidenden Wendepunkte historischer Umwälzungen, inmitten feindlicher Gegenkräfte, nur auf sich selbst ge­stellt, zu vollbringen, war das ungeheure Ethos notwendig, welches das ganze Lebenswerk Rudolf Steiners durchpulst und nichts anderes mehr für ihn in Betracht kommen ließ als das Wohl der Menschheit, die Rettung des Abendlandes vor dem drohenden Untergange.",
        "Dazu mußte von den Fundamenten aus gebaut werden in einer Art, die den For­derungen"
      ],
      [
        "der Zeit entsprach.",
        "Die Synthese alles Wissens war dazu notwendig."
      ],
      [
        "Greift man zu diesen Aufsätzen, die am Anfang jenes er­staunlichen Lebenswerkes geschrieben worden sind, das am 30.",
        "März 1925 seinen Abschluß fand und, bald nach der Jahrhundertwende, einen schicksalsgewollten Einschlag er­halten hatte durch die Verbindung mit den aus orientali­schen Quellen gespeisten theosophischen Kreisen, so wird man zur Frage gedrängt: Wie ist es zu verstehen, daß Ru­dolf Steiner, der uns auch auf dem Gebiete der Esoterik zur Freiheit führte, auch hier uns auf uns selber stellte und nur unserm eigenen höhern Ich uns geloben ließ, was sonst der Schüler dem Lehrer als Gelöbnis zu leisten hatte, daß Ru­dolf Steiner hier in diesen Aufsätzen noch von der Notwen­digkeit des strengen Anschlusses an den Führer spricht, den Schüler gleichsam in die Abhängigkeit des Lehrers stellt?"
      ],
      [
        "In Wahrheit handelt es sich bei Rudolf Steiner nur um die Beschreibung eines Vertrauensverhältnisses.",
        "Das Auto­ritative hat er von Anfang an vermieden und von sich ge­wiesen.",
        "In alten Zeiten übernahmen die initiierenden Prie­ster die volle Verantwortung für den in die Mysterien des geistigen Seins Einzuweihenden und wirkten mit ihrem Willen in ihn hinein.",
        "So war er zugleich geschützt und ge­führt und konnte den Gefahren entrinnen, die ihn sonst überwältigt hätten.",
        "Sein Ich schwebte ja noch über seinen physischen Hüllen, sein Selbstbewußtsein war nicht er­wacht.",
        "Dieses immer mehr zur Erweckung zu bringen, war der Weg der fortschreitenden Mysterienschulung.",
        "Und in der christlichen Einweihung sehen wir durch den Hinweis auf den Weltenlehrer die Abhängigkeit vom persönlichen Lehrer schon gemildert, wenn auch noch vorhanden."
      ],
      [
        "verliert immer mehr ihren persönlichen Charakter in der rosenkreuzerischen Schulung und gestaltet sich um zum Vertrauensverhältnis.",
        "Der Lehrer steht dem Schüler bei, zeigt ihm den Weg, den jener sucht und allein nicht finden kann, stützt ihn moralisch, weist ihn auf die Gefahren hin, die seinem Charakter drohen - aus Eitelkeit, aus der Vor­gaukelung trügerischer Bilder, die er unterscheiden lernen muß von wahrer geistiger Wirklichkeit.",
        "So ist der Lehrer ein Helfer, der sich in dem Augenblicke sogleich zurück­ziehen würde, wo das Vertrauen abhanden käme.",
        "An dem Schicksalswendepunkte, in dem wir stehen, mußte der für die Jetztzeit wirkende Lehrer hinweisen auf die Vergangen­heit, Gegenwart und Zukunft menschlichen Geistesstre­bens und, indem er mit der Erziehung des Einzelnen be­gann, sein Werk so ausbauen, daß es als Menschheitstat da­stehen konnte: ein für die Nachwelt neuerrungenes Le­benselement.",
        "So schuf Rudolf Steiner eine Initiationswis­senschaft, in der von nun an jeder ernste, sittlich strebende Mensch den Boden wird finden können, der ihn trägt, die Elemente wird greifen können, die ihm das Unterschei­dungsvermögen schärfen, während sich ihm neue Welten eröffnen.",
        "Er braucht nicht unsicher zu sein, er hat genug, um sich durchzutasten, bis er in geistigen Landen den Füh­rer findet."
      ],
      [
        "Ein solches war nicht vorhanden, bevor Rudolf Steiner sein Geisteswerk begann.",
        "Seine Tat ist - die «Wissenschaft» von der Initiation.",
        "Durch sie wird entsiegelt, was verbor­gen lag in den Mysterien der alten Tempel: neben dem Wis­sen des Werdens der Welten das Wissen vom kommenden Niederstieg des Christus; und was versiegelt ward in der Kirche: die erlösende Tat der Menschheitsbefreiung durch"
      ],
      [
        "den Christus, die im Laufe der Zeit durch Ihn sich vollzie­hende Ich-Durchdringung des Einzelnen.",
        "Statt der persön­lichen Führung wird es nun Aufgabe, durch die Kräfte des Zeitgeistes den Menschen den Weg finden zu lassen zum Menschheits-Ich, zum Christus.",
        "Das Bewußtsein des ein­zelnen Menschen wird reif gemacht zum Entgegennehmen der höheren Ichkraft, das Selbstbewußtsein wird emporge­hoben zum Geistselbst."
      ],
      [
        "Es ist die Arbeit der Zukunft.",
        "Aber nur auf dem Boden der Vergangenheit stehend, kann man, Künftiges vorberei­tend, die Gegenwart befruchten.",
        "Sonst schafft man ins Lee­re.",
        "Metamorphose auch hier.",
        "Die Zukunft wird gestaltet, indem die auf dem Boden der Vergangenheit stehende Ge­genwart umgeformt wird, Neues tritt hinzu, wie der neue Frühling dem Winter folgt.",
        "Sonnenkraft durchfeuert die Erde; Ersterbendes, in Wesenhaftes sich Umwandelndes wird zu neuem Leben entfacht, indem sich von oben die Gnade hinuntersenkt."
      ],
      [
        "Auch auf dem Gebiet der Esoterik entwickelt sich kon­tinuierliches historisches Geschehen durch das Gesetz der steigenden Entwickelung und der auf- und abflutenden Welle des vergehenden und auf blühenden Lebens bis zudem scheinbar plötzlichen Augenblick, wo die Gnade überstrah­lend hereinbricht, gleich dem Wunder der auf leuchtenden Blüte in der grünen Pflanzenwelt.",
        "Doch ohne diese durch weise Mächte von Form zu Form durchgeführte Wand­lung und stete Steigerung auf allen Gebieten der Lebensäußerung würden die neuen Werte, die Gaben des Geistes, die feurigen Zungen des Wortes, sich nicht zu uns hernie­dersenken.",
        "Ohne Kenntnis solchen Geschehens wären die Empfangenden nicht in der Lage, zu ermessen, was unter"
      ],
      [
        "ihnen sich vollziehen will.",
        "Das neue Große könnte sich nicht auswirken, die Zukunft nicht gerettet werden."
      ],
      [
        "Die nach geistigen Erkenntnissen ringenden Seelen, die an Rudolf Steiner herantraten, waren das schicksalgewoll­te, von der Zeit ihm zugeführte Menschenmaterial, mit dem Rudolf Steiner zu arbeiten hatte, aus deren Bedürfnissen und Voraussetzungen heraus er das zu gestalten hatte, was auf Grund eines erkenntnismäßig fundamentierten Auf­baus zur Wissenschaft der Initiation werden konnte.",
        "Aus der Trägheit der Zeit dem Geiste gegenüber galt es, Men­schen herauszureißen, die Brücke würden sein können für die Forderungen der Zukunft."
      ],
      [
        "Am schwersten war es, den Sinn zu wecken für die innere Freiheit und das Auf-sich-selbst-gestellt-Sein in eigener Verantwortung.",
        "In peinlichster Berücksichtigung dieses Zieles hat Rudolf Steiner nichts anderes den Menschen sein wollen als Unterweiser und wo man ihn darum bat, Bera­ter, Erwecker von menschheitlichen Geistimpulsen.",
        "Er konnte Darsteller werden von geistigen Tatsachen, weil sein Denken und Schauen lebendurchtränkt war und sich von Glied zu Glied entfaltete mit der Kraft eines naturhaf­ten Organismus.",
        "Sein Geisteswerk steht vor uns: die wie­derhergestellte Einheit von Wissenschaft, Kunst und Reli­gion."
      ]
    ]
  },
  {
    "order": 3,
    "title_de": "AUS DER VORREDE ZUR FÜNFTEN AUFLAGE DES BUCHES «WIE ERLANGT MAN ERKENNTNISSE DER HÖHEREN WELTEN?»",
    "paragraphs": [
      "Als ich die Aufsätze schrieb, aus welchen das Buch zusam­mengesetzt ist, mußte über manches auch aus dem Grunde anders gesprochen werden als gegenwärtig, weil ich auf den Inhalt dessen, was ich in den letzten zehn Jahren über Tat­sachen der Erkenntnis geistiger Welten veröffentlicht habe, damals anders hinzudeuten hatte, als es jetzt, nach der Ver­öffentlichung, zu geschehen hat. In meiner «Geheimwis­senschaft»,in der «Führung des Menschen und der Mensch­heit», in «Ein Weg zur Selbsterkenntnis» und besonders in «Die Schwelle der geistigen Welt», auch in anderen meiner Schriften sind geistige Vorgänge geschildert, auf deren Vor­handensein dieses Buch vor mehr als zehn Jahren zwar schon hindeuten mußte, dies aber doch mit anderen Wor­ten, a]s es gegenwärtig richtig scheint.",
      "Ich mußte damals von vielem, das in dem Buche noch nicht geschildert wur­de, sagen, es könne durch «mündliche Mitteilung » erfah­ren werden. Gegenwärtig ist nun vieles von dem veröffentlicht, was mit solchen Hinweisen gemeint war.",
      "Es waren aber diese Hinweise, die irrtümliche Meinungen bei den Lesern vielleicht nicht völlig ausschlossen. Man könnte etwa in dem persönlichen Verhältnis zu diesem oder jenem Lehrer bei dem nach Geistesschulung Strebenden etwas viel Wesentlicheres sehen, als gesehen werden soll.",
      "Ich hoffe, daß es mir gelungen ist, in dieser neuen Auflage durch die Art der Darstellung mancher Einzelheiten schär­fer zu betonen, wie es bei dem, der Geistesschulung sucht im Sinne der gegenwärtigen geistigen Bedingungen, viel",
      "mehr auf ein völlig unmittelbares Verhältnis zur objektiven Geisteswelt als auf ein Verhältnis zur Persönlichkeit eines Lehrers ankommt. Dieser wird auch in der Geistesschulung immer mehr die Stellung nur eines solchen Helfers anneh­men, die der Lehrende, gemäß den neueren Anschauungen, in irgendeinem anderen Wissenszweige innehat. Ich glaube genügend darauf hingewiesen zu haben, daß des Lehrers Autorität und der Glaube an ihn in der Geistesschulung keine andere Rolle spielen sollten, als dies der Fall ist auf irgendeinem anderen Gebiete des Wissens und Lebens. Mir scheint viel darauf anzukommen, daß immer richtiger be­urteilt werde gerade dieses Verhältnis des Geistesforschers zu Menschen, die Interesse entwickeln für die Ergebnisse seines Forschens. So glaube ich das Buch verbessert zu haben, wo ich das Verbesserungsbedürftige nach zehn Jah­ren zu finden in der Lage war.",
      "An diesen ersten Teil soll sich ein zweiter anschließen. Dieser soll weitere Ausführungen über die Seelenverfassung bringen, welche den Menschen zum Erleben der hö­heren Welten führt.",
      "Berlin, 7. September 1914"
    ],
    "sentences": [
      [
        "Als ich die Aufsätze schrieb, aus welchen das Buch zusam­mengesetzt ist, mußte über manches auch aus dem Grunde anders gesprochen werden als gegenwärtig, weil ich auf den Inhalt dessen, was ich in den letzten zehn Jahren über Tat­sachen der Erkenntnis geistiger Welten veröffentlicht habe, damals anders hinzudeuten hatte, als es jetzt, nach der Ver­öffentlichung, zu geschehen hat.",
        "In meiner «Geheimwis­senschaft»,in der «Führung des Menschen und der Mensch­heit», in «Ein Weg zur Selbsterkenntnis» und besonders in «Die Schwelle der geistigen Welt», auch in anderen meiner Schriften sind geistige Vorgänge geschildert, auf deren Vor­handensein dieses Buch vor mehr als zehn Jahren zwar schon hindeuten mußte, dies aber doch mit anderen Wor­ten, a]s es gegenwärtig richtig scheint."
      ],
      [
        "Ich mußte damals von vielem, das in dem Buche noch nicht geschildert wur­de, sagen, es könne durch «mündliche Mitteilung » erfah­ren werden.",
        "Gegenwärtig ist nun vieles von dem veröffentlicht, was mit solchen Hinweisen gemeint war."
      ],
      [
        "Es waren aber diese Hinweise, die irrtümliche Meinungen bei den Lesern vielleicht nicht völlig ausschlossen.",
        "Man könnte etwa in dem persönlichen Verhältnis zu diesem oder jenem Lehrer bei dem nach Geistesschulung Strebenden etwas viel Wesentlicheres sehen, als gesehen werden soll."
      ],
      [
        "Ich hoffe, daß es mir gelungen ist, in dieser neuen Auflage durch die Art der Darstellung mancher Einzelheiten schär­fer zu betonen, wie es bei dem, der Geistesschulung sucht im Sinne der gegenwärtigen geistigen Bedingungen, viel"
      ],
      [
        "mehr auf ein völlig unmittelbares Verhältnis zur objektiven Geisteswelt als auf ein Verhältnis zur Persönlichkeit eines Lehrers ankommt.",
        "Dieser wird auch in der Geistesschulung immer mehr die Stellung nur eines solchen Helfers anneh­men, die der Lehrende, gemäß den neueren Anschauungen, in irgendeinem anderen Wissenszweige innehat.",
        "Ich glaube genügend darauf hingewiesen zu haben, daß des Lehrers Autorität und der Glaube an ihn in der Geistesschulung keine andere Rolle spielen sollten, als dies der Fall ist auf irgendeinem anderen Gebiete des Wissens und Lebens.",
        "Mir scheint viel darauf anzukommen, daß immer richtiger be­urteilt werde gerade dieses Verhältnis des Geistesforschers zu Menschen, die Interesse entwickeln für die Ergebnisse seines Forschens.",
        "So glaube ich das Buch verbessert zu haben, wo ich das Verbesserungsbedürftige nach zehn Jah­ren zu finden in der Lage war."
      ],
      [
        "An diesen ersten Teil soll sich ein zweiter anschließen.",
        "Dieser soll weitere Ausführungen über die Seelenverfassung bringen, welche den Menschen zum Erleben der hö­heren Welten führt."
      ],
      [
        "Berlin, 7.",
        "September 1914"
      ]
    ]
  },
  {
    "order": 4,
    "title_de": "DIE STUFEN DER HÖHEREN ERKENNTNIS",
    "paragraphs": [
      "Bis zu der Begegnung mit den beiden «Hütern der Schwel­le» ist in dem Buche «Wie erlangt man Erkenntnisse der höheren Welten?» der Weg zur höheren Erkenntnis ver­folgt worden. Nun sollen auch noch die Verhältnisse ge­schildert werden, in denen die Seele zu den verschiedenen Welten steht, wenn sie durch die aufeinanderfolgenden Erkenntnis stufen hindurchschreitet. Damit wird das gegeben, was man die «Erkenntnislehre der Geheimwissenschaft» nennen kann.",
      "Bevor der Mensch den Pfad höherer Erkenntnis betritt, kennt er nur die erste von vier Erkenntnisstufen. Es ist die­jenige, welche ihm im gewöhnlichen Leben innerhalb der Sinnenwelt eigen ist. Auch in dem, was zunächst «Wissen­schaft» genannt wird, hat man es nur mit dieser ersten Er­kenntnisstufe zu tun. Denn diese Wissenschaft arbeitet ja nur das gewöhnliche Erkennen feiner aus, macht es diszi­plinierter. Sie bewaffnet die Sinne durch Instrumente - Mikroskop, Fernrohr usw. -, um genauer zu sehen, was die unbewaffneten Sinne nicht sehen. Aber die Erkenntnisstufe bleibt doch dieselbe, ob man normal große Dinge mit dem gewöhnlichen Auge sieht, oder ob man sehr kleine Gegenstände und Vorgänge mit dem Vergrößerungsglase ver­folgt. Auch in der Anwendung des Denkens auf die Dinge und Tatsachen bleibt diese Wissenschaft bei dem stehen, was schon im alltäglichen Leben getrieben wird. Man ord­net die Gegenstände, beschreibt und vergleicht sie, man sucht sich ein Bild von ihren Veränderungen zu machen usw. Der strengste Naturforscher tut im Grunde in dieser Beziehung nichts anderes, als daß er das Beobachtungsver­fahren",
      "des alltäglichen Lebens in einer kunstgemäßen Art ausbildet. Seine Erkenntnis wird umfangreicher, komplizierter, logischer; aber er schreitet nicht zu einer anderen Erkenntnisart vor.",
      "Man nennt diese erste Erkenntnis stufe in der Geheimwis­senschaft die «materielle Erkenntnisart». Dazu kommen dann zunächst drei höhere. An sie schließen sich dann noch weitere an. Sie sollen hier beschrieben werden, bevor in der Schilderung des «Erkenntnispfades » weitergegangen wird. Nimmt man das gewöhnliche - und sinnlich-wissen­schaftliche - Erkennen als die erste Stufe an, so hat man zunächst folgende vier Stufen zu unterscheiden :",
      "1.    Die materielle Erkenntnis.",
      "2.    Die imaginative Erkenntnis.",
      "3.    Die inspirierte Erkenntnis, die man auch die «willensartigen» nennen kann.",
      "4.    Die intuitive Erkenntnis.",
      "Diese Stufen sollen im weiteren zur Sprache kommen. Man muß sich zunächst klarmachen, womit man es bei die­sen verschiedenen Erkenntnisarten zu tun hat. - Beim ge­wöhnlichen sinnlichen Erkennen kommen vier Elemente in Betracht : 1. Der Gegenstand, welcher auf die Sinne einen Eindruck macht. 2. Das Bild, das sich der Mensch von diesem Gegenstande macht. 3. Der Begriff, durch den der Mensch zu einer geistigen Erfassung einer Sache oder eines Vorganges kommt. 4. Das «Ich», welches sich auf Grund des Eindruckes vom Gegenstande Bild und Begriff bildet. Bevor sich der Mensch ein Bild - eine «Vorstellung » macht, ist ein Gegenstand da, welcher ihn dazu veranlaßt. Diesen bildet er nicht selbst, er nimmt ihn wahr. Und auf Grund dieses Gegenstandes entsteht das Bild. Solange man ein",
      "Ding anblickt, hat man es mit diesem selbst zu tun. In dem Augenblicke, wo man von dem Dinge hinwegtritt, besitzt man nur noch das Bild. Den Gegenstand verläßt man, das Bild bleibt in der Erinnerung «haften».",
      "Aber man kann nicht dabei stehenbleiben, sich bloß «Bilder» zu machen. Man muß zu «Begriffen » kommen. Die Unterscheidung von «Bild » und «Begriff» ist unbedingt notwendig, wenn man sich hier ganz klarwerden will.",
      "Man stelle sich einmal vor, man sehe einen Gegenstand, welcher kreisförmig ist. Dann drehe man sich um, und man behalte das Bild des Kreises im Gedächtnisse. Da hat man noch nicht den «Be­griff» des Kreises.",
      "Dieser ergibt sich erst, wenn man sich sagt : «Ein Kreis ist eine Figur, bei der alle Punkte von ei­nem Mittelpunkte gleich weit entfernt sind. » Erst wenn man sich von einer Sache einen «Begriff» gemacht hat, ist man zum Verständnisse derselben gekommen. Es gibt viele Kreise : kleine, große, rote, blaue usw.; aber es gibt nur einen Begriff «Kreis». - Auf alles dieses soll im weiteren noch näher eingegangen werden; vorläufig soll nur skizziert werden, was zur Charakteristik der vier ersten Erkenntnisstufen notwendig ist. - Das vierte Element, das bei der materiellen Erkenntnis in Betracht kommt, ist das «Ich».",
      "In demselben kommt eine Einheit der Bilder und Begriffe zustande. Dieses «Ich» bewahrt in seinem Gedächtnisse die Bilder. Wäre das nicht der Fall, so entstände kein fortlaufendes inneres Leben. Die Bilder der Dinge blieben nur so lange vorhanden, als diese Dinge selbst auf die Seele wirken.",
      "Das innere Leben aber hängt davon ab, daß Wahrnehmung an Wahrnehmung gereiht wird. Das «Ich» orientiert sich «heute » in der Welt, weil ihm bei gewissen Gegenständen die Bilder der gleichen Gegenstände von",
      "«gestern » auftauchen. Man vergegenwärtige sich nur, wie unmöglich das Seelenleben wäre, wenn man nur so lange ein Bild eines Dinges hätte, als dieses selbst vor einem steht. - Auch bezüglich der Begriffe bildet das «Ich» die Einheit. Es verbindet seine Begriffe und verschafft sich auf diese Art einen Überblick, das heißt ein Verständnis der Welt. Diese Verbindung der Begriffe geschieht im «Urteilen». Ein Wesen, das nur lose Begriffe hätte, könnte sich in der Welt nicht zurechtfinden. Alle Tätigkeit des Menschen beruht auf seiner Fähigkeit, Begriffe zu verbinden, das heißt",
      "auf seinem «Urteilen».",
      "Das «materielle Erkennen» beruht darauf, daß der Mensch durch seine Sinne einen Eindruck von Dingen und Vorstellungen der Außenwelt erhält. Er hat die Fähigkeit des Empfindens oder die Sensibilität. Der «von außen »empfangene Eindruck wird auch Sensation genannt. Daher kommen bei der «materiellen Erkenntnis» die vier Ele­mente in Betracht : Sensation, Bild, Begriff, Ich. - Bei der nächsthöheren Stufe des Erkennens fällt nun der Eindruck auf die äußeren Sinne, die «Sensation», weg. Ein äußerer Sinnesgegenstand ist nicht mehr vorhanden. Es bleiben al­so von den Elementen, an welche der Mensch von der ge­wöhnlichen Erkenntnis her gewöhnt ist, nur die drei: Bild, Begriff und Ich.",
      "Das gewöhnliche Erkennen bildet bei einem gesunden Menschen kein Bild und keinen Begriff, wenn ein äußerer Sinnesgegenstand nicht vorhanden ist. Das «Ich» bleibt dann untätig. Wer sich Bilder formt, denen Sinnesgegen­stände entsprechen sollen, wo in Wahrheit keine sind, lebt in Phantastik. - Nun aber erwirbt sich der Geheimschüler eben die Fähigkeit, Bilder zu formen, auch wo keine Sin­nesgegenstände",
      "vorhanden sind. Es muß dann bei ihm an die Stelle des «äußeren Gegenstandes» ein anderer treten. Er muß Bilder haben können, auch wenn kein Gegenstand seine Sinne berührt. An die Stelle der «Sensation» muß etwas anderes treten.",
      "Dies ist die Imagination. Bei dem Ge­heimschüler auf dieser Stufe treten Bilder auf genau so, wie wenn ein Sinnesgegenstand auf ihn einen Eindruck machen würde; sie sind so lebhaft und wahr wie die Sinnesbilder, nur kommen sie nicht vom «Materiellen», sondern vom «Seelischen» und «Geistigen».",
      "Die Sinne bleiben da­bei vollständig untätig. - Es ist einleuchtend, daß sich der Mensch diese Fähigkeit, inhaltvolle Bilder zu haben ohne Sinneseindrücke, erst erwerben muß. Es geschieht dies durch die Meditation, durch die Übungen, welche in den Darstellungen des Buches «Wie erlangt man Erkenntnisse der höheren Welten?» beschrieben worden sind.",
      "Der auf die Sinnenwelt beschränkte Mensch lebt nur in dem Um­kreis einer Bilderwelt, welche erst durch die Sinne in ihn Einlaß gefunden haben. Der imaginative Mensch hat eine solche Bilderwelt, die von einer höheren Welt ihren Zufluß erhält.",
      "Es gehört eine sehr sorgfältige Schulung dazu, in­nerhalb dieser höheren Bilderwelt Täuschung von Wirklich­keit zu unterscheiden. Nur zu leicht sagt sich der Mensch, wenn solche Bilder zunächst vor seine Seele hintreten: «Ach, das sind ja nur Einbildungen, bloße Ausflüsse mei­nes Vorstellungslebens.» Das ist nur zu begreiflich.",
      "Denn der Mensch ist zunächst ja daran gewöhnt, nur dasjenige «wirklich » zu nennen, was, ohne sein Zutun, ihm durch die feste Grundlage seiner Sinneswahrnehmung gegeben ist. Und er muß sich erst hineinfinden, Dinge für «wirkli­che» zu nehmen, die von ganz anderer Seite veranlaßt werden.",
      "Und er kann auch darinnen nicht vorsichtig genug sein, wenn er nicht zum Phantasten werden will. Die Entscheidung darüber, was auf höherem Gebiete «wirklich» ist, was nur «Illusion», die kann nur von der Erfahrung kommen. Und man muß sich diese Erfahrung in einem stil­len, geduldigen Innenleben aneignen. Zunächst muß man durchaus darauf gefaßt sein, daß einem die «Illusion» böse Streiche spielt. Überall lauern die Möglichkeiten, daß Bil­der auftauchen, die nur auf Täuschungen der äußeren Sin­ne, des abnormen Lebens beruhen. Alle solche Möglich­keiten müssen zuerst hinweggeräumt werden. Man muß zu­erst die Quellen der Phantastik ganz verstopfen, dann kann man erst zu der Imagination kommen. Ist man so weit, dann wird man allerdings sich klar darüber, daß die Welt, in die man in solcher Art eintritt, nicht nur so wirklich ist wie die sinnliche, sondern daß sie eine gewöhnlich viel wirklichere ist.",
      "Bei der dritten Stufe der Erkenntnis bleiben nun auch die Bilder weg. Der Mensch hat es nur noch mit «Begriff» und «Ich» zu tun. Hat er auf der zweiten Stufe noch eine Bil­derwelt um sich, die erinnert an die Augenblicke, wo das lebhafte Gedächtnis sich die Eindrücke der Außenwelt vor die Seele zaubert, ohne selbst solche Eindrücke zu haben: auf der dritten Stufe sind auch solche Bilder nicht mehr vorhanden. Der Mensch lebt ganz in einer rein geistigen Welt. Wer nur gewöhnt ist, sich an die Sinne zu halten, wird versucht sein, zu glauben, daß diese Welt eine blasse, ge­spenstige sei. Das ist sie aber ganz und gar nicht. Auch die Bilderwelt der zweiten Stufe hat nichts Blasses, Schatten­haftes. So sind ja allerdings die Bilder zumeist, die im Ge­dächtnisse haften bleiben, wenn die äußeren Dinge weg sind. Aber die Bilder der Imagination sind von einer Leb­haftigkeit",
      "und Inhaltsfülle, mit der sich nicht nur die schat­tenhaften Erinnerungsbilder der Sinnenwelt nicht ver­gleichen lassen, sondern sogar nicht einmal die ganze bunte, wechselreiche Sinnenwelt selbst. Auch diese ist gegen das Reich der Imagination nur ein Schatten. - Und nun gar die Welt der dritten Erkenntnisstufe! Von ihrem Reichtum und ihrer Fülle gibt nichts in der Sinnenwelt eine Vorstellung. Was für die erste Stufe die Sensation, für die zweite die Imagination, das ist für sie die Inspiration. Die Inspiration gibt die Eindrücke, und das «Ich» formt die Begriffe. Will man durchaus mit dieser Welt etwas Sinnliches vergleichen, so kann nur die Tonwelt des Hörens zu einem solchen Ver­gleiche herangezogen werden. Aber nicht mit Tönen wie in der sinnlichen Musik hat man es zu tun, sondern mit ei­nem rein «geistigen Tönen». Man beginnt zu «hören», was im Innern der Dinge vorgeht. Der Stein, die Pflanze usw. werden zu «geistigen Worten». Die Welt beginnt der Seele gegenüber ihr Wesen wirklich selbst auszusprechen. Es klingt grotesk; aber es ist wörtlich wahr : auf dieser Stufe des Erkennens «hört man geistig das Gras wachsen». Man vernimmt die Form des Kristalles als Klang; die sich öff­nende Blüte «spricht» da zum Menschen. Der Inspirierte vermag das innere Wesen der Dinge zu künden; alle Dinge werden in neuer Art vor seiner Seele auferstehen. Er spricht eine Sprache, die aus einer anderen Welt stammt, und wel­che doch erst die alltägliche Welt begreiflich macht.",
      "Auf der vierten Erkenntnisstufe endlich hört auch die In­spiration auf. Von den Elementen, die man vom alltägli­chen Erkennen her gewohnt ist, zu betrachten, ist nur noch das «Ich» dasjenige, welches in Betracht kommt. Der Ge­heimschüler merkt an einer ganz bestimmten inneren Erfahrung,",
      "daß er bis zu dieser Stufe aufgestiegen ist. Diese Erfahrung drückt sich darin aus, daß er das Gefühl hat: er stehe jetzt nicht mehr außer den Dingen und Vorgängen, welche er erkennt, sondern innerhalb derselben.",
      "Bilder sind nicht der Gegenstand; sie drücken ihn bloß aus. Auch was die Inspiration gibt, ist nicht der Gegenstand. Sie spricht ihn nur aus. Das aber, was jetzt in der Seele lebt, ist wirk­lich der Gegenstand selbst.",
      "Das Ich hat sich ergossen über alle Wesen; es ist mit ihnen zusammengeflossen. Das Leben der Dinge in der Seele ist nun die Intuition. Es ist eben ganz wörtlich zu nehmen, wenn man von der Intuition sagt: man kriecht durch sie in alle Dinge hinein. - Im gewöhnlichen Leben hat der Mensch nur eine Intuition, das ist diejenige des «Ich» selber.",
      "Denn das «Ich» kann auf keine Weise von außen wahrgenommen werden, es kann nur im Innern erlebt werden. Eine einfache Erwägung kann das klarma­chen. Es ist dies eine Erwägung, die allerdings von den Psychologen nicht mit der wünschenswerten Schärfe ge­macht wird.",
      "So unscheinbar sie aber ist: für den, der sie ganz versteht, ist sie von der allerweittragendsten Bedeu­tung. Sie ist die folgende: Ein jedes Ding der Außenwelt kann von allen Menschen mit demselben Namen genannt werden.",
      "Der Tisch kann von allen mit «Tisch», die Tulpe von allen mit «Tulpe», der Herr Müller von allen mit «Herr Müller» angesprochen werden. Aber es gibt ein Wort, das jeder nur zu sich selbst sprechen kann.",
      "Dies ist das Wort «Ich». Kein anderer kann zu mir «Ich» sagen, für jeden anderen bin ich ein «Du». Ebenso ist jeder andere für mich ein «Du». Nur er selbst kann zu sich «Ich» sagen. Das rührt davon her, daß man nicht außer, sondern in dem «Ich» lebt.",
      "Und so lebt man durch die intuitive Erkenntnis in allen Dingen.",
      "Die Wahrnehmung des eigenen «Ich» ist das Vorbild für alle intuitive Erkenntnis. Um so in die Dinge hineinzu­kommen, muß man allerdings erst aus sich selbst heraustreten. Man muß «selbstlos» werden, um mit dem «Selbst», dem «Ich», einer anderen Wesenheit zu verschmelzen.",
      "Meditation und Konzentration sind die sicheren Mittel, um zu dieser Stufe, ebenso wie zu den früheren, hinanzu­steigen. Allerdings müssen sie in stiller, geduldiger Art ge­übt werden. Wer da glaubt, daß er tumultuarisch, mit Ge­waltmitteln zu den höheren Welten steigen kann, der irrt sich. Und einem solchen Glauben würde sich derjenige hin­geben, welcher erwartete, daß ihm die Wirklichkeit auf hö­heren Gebieten in ebensolcher Art entgegentritt wie in der Sinnenwelt. So lebhaft und reich auch die Welten sind, zu denen man hinansteigt, sie sind fein und subtil, während die Sinnenwelt grob und derb ist. Das Wichtigste, was man lernen muß, ist gerade die Gewöhnung daran, etwas ganz anderes «wirklich» zu nennen, als was man im Bereich der Sinne so bezeichnet. Und dies ist nicht ganz leicht. Deshalb wird so mancher, der den Geheimpfad so gerne gehen möchte, schon bei den ersten Schritten zurückgeschreckt. Er hat erwartet, daß ihm Dinge entgegentreten, welche sind wie Tische und Stühle, und er findet «Geister». Weil aber «Geister» nicht dicht sind wie Stühle und Tische, so kommen sie ihm als «Einbildungen » vor. Daran ist nichts anderes schuld als die Ungewohntheit. Man muß sich erst die rechte Empfindung für die geistige Welt erwerben, dann wird man das Geistige nicht bloß schauen, sondern auch anerkennen. Und ein großer Teil der Geheimschulung be­zieht sich auf diese richtige Anerkennung und Einschät­zung des Geistigen.",
      "Man muß zunächst den Schlafzustand betrachten, wenn man Aufschluß erlangen will über die imaginative Erkennt­nis. Solange der Mensch keine höhere Erkenntnisstufe er­langt hat als die materielle, lebt die Seele zwar während des Schlafes, aber sie kann in der Welt, in welcher sie schlafend lebt, nichts wahrnehmen.",
      "Sie ist in dieser Welt wie ein Blinder in der materiellen. Ein solcher lebt in der Welt des Lichtes und der Farben; aber er nimmt sie nicht wahr. - Von den äußeren Sinnesorganen, dem Auge, dem Ohr, der gewöhn­lichen Gehirntätigkeit usw. hat sich die Seele im Schlafe zurückgezogen.",
      "Sie erhält durch die Sinne keine Eindrücke. Was tut sie nun während des Schlafes? Klar muß man sich darüber sein, daß die Seele während des Wachens in einer fortwährenden Tätigkeit ist. Sie empfängt die äußeren Sin­neseindrücke und verarbeitet sie: das ist ihre Tätigkeit.",
      "Diese stellt sie während des Schlafes ein. Aber sie ist kei­neswegs untätig. Sie arbeitet schlafend an dem einen Lei­be. Dieser wird ja während der wachen Tagesarbeit abge­nützt. Das drückt sich in der Ermüdung aus.",
      "Und während des Schlafes beschäftigt sich die Seele mit dem eigenen Leib, um ihn für weitere wache Tagesarbeit wieder geeig­net zu machen. Man sieht daraus, wie wesentlich der rich­tige Schlaf dem Gedeihen des Leibes ist.",
      "Ein Mensch, der nicht entsprechend schläft, läßt seine Seele an dem Leibe nicht die notwendige Verbesserungsarbeit tun. - Und die Folge davon muß sein, daß der Leib herunterkommt. - Die Kräfte, mit denen die Seele während des Schlafes am Leibe arbeitet, sind dieselben, durch welche sie auch im Wachzustande tätig ist. Nur werden sie in dem letzteren dazu verwendet, die Eindrücke der äußeren Sinne aufzu­nehmen und sie zu verarbeiten.",
      "Tritt nun die imaginative Erkenntnis beim Menschen ein, so muß ein Teil der im Schlafe auf den Leib gewende­ten Kräfte in einer anderen Art verbraucht werden. Durch diese Kräfte werden nunmehr die geistigen Sinnesorgane gebildet, die es ermöglichen, daß die Seele in einer höheren Welt nicht bloß lebt, sondern auch wahrnimmt. So arbeitet die Seele schlafend an sich, nicht mehr bloß an ihrem Leibe. Bewirkt wird diese Arbeit durch die Meditation und Kon­zentration sowie durch andere Übungen. Es ist schon öfters in diesen Aufsätzen über höhere Erkenntnis gesagt worden, daß die besonderen Anweisungen über solche Übungen nur von Mensch zu Mensch gegeben werden. Niemand sollte auf eigene Hand diese Übungen unternehmen, denn nur wer Erfahrung auf diesem Gebiete hat, kann ermessen, wel­che Wirkung bei dem einen oder dem anderen Menschen sich einstellen muß, wenn er es unternimmt, seine Seelenarbeit von dem Leibe abzuziehen und in einer höheren Art anzuwenden.",
      "Meditation, Konzentration und andere Übungen bewir­ken, daß die Seele sich für eine Weile zurückzieht von ihrer Verbindung mit den Sinnesorganen. Sie ist dann in sich selbst versenkt. Ihre Tätigkeit ist nach innen gewendet. Im Anfange dieser Versenkung unterscheidet sich zwar diese ihre innere Tätigkeit nicht erheblich von der alltäglichen. Sie muß dieselben Vorstellungen, Gefühle und Empfindun­gen verwenden während der Innenarbeit, welche sie auch im gewöhnlichen Leben hat. Je mehr sie sich aber daran gewöhnt, gewissermaßen «blind und taub » gegenüber der sinnlichen Umgebung zu sein, je mehr sie in sich lebt, desto fähiger macht sie sich zu innerer Leistung. Und was sie bei der Versenkung in das Innere geleistet hat, das trägt seine",
      "Früchte zunächst im Zustande des Schlafes. Ist die Seele des Nachts vom Leibe befreit, so wirkt das in ihr fort, was durch die Übungen am Tage angeregt worden ist. Es bil­den sich in ihr Organe, durch welche sie mit einer höheren Umgebung gerade so in Verbindung kommt wie vorher durch die äußeren Sinnesorgane mit der körperlichen Um­welt.",
      "Aus dem Dunkel der nächtlichen Umgebung treten die Lichterscheinungen der höheren Welt heraus. Zart und intim ist dieser Verkehr zunächst. Und der Mensch muß durchaus damit rechnen, daß für eine lange Zeit beim Auf­wachen das Licht des Tages sofort wieder einen dichten Vorhang zieht vor die Erlebnisse der Nacht.",
      "Die Erinne­rung, daß man in der Nacht wahrgenommen hat, tritt nur ganz langsam und allmählich ein. Denn der Schüler lernt nicht leicht auf die zarten Gebilde seiner Seele achten, die sich im Laufe seiner Entwickelung hineinmischen in die groben Erlebnisse des alltäglichen Sinneslebens.",
      "Anfangs erscheinen ihm solche Gebilde wie das, was man zufällige Eindrücke der Seele nennt. Alles kommt darauf an, daß er unterscheiden lernt, was er der gewöhnlichen Welt verdankt von dem, was durch seine eigene Wesenheit als Kund­gebung höherer Welten sich darstellt.",
      "In einem stillen, in sich gekehrten Gemütsleben muß er sich diese Unterschei­dung aneignen. Es ist notwendig, daß er sich erst ein Ge­fühl davon erwerbe, welches der Wert und die Bedeutung der intimen Seelengebilde ist, die wie «zufällige Einfälle» sich in das Tagesleben einmischen und welche doch Er­innerungen an den nächtlichen Verkehr in einer höheren Welt sind.",
      "Sobald man diese Dinge irgendwie grob anfaßt und sie mit dem Maßstab des Sinneslebens mißt, zerstie­ben sie.",
      "Es ist aus obigem ersichtlich, daß durch die Arbeit in einer höheren Welt die Seele dem Leibe etwas von ihrer sonst fürsorglichen Tätigkeit entziehen muß. Sie überläßt den­selben in einer gewissen Beziehung sich selbst.",
      "Er braucht einen Ersatz für das, was sie ihm vorher geleistet hat. Er­hält er einen solchen Ersatz nicht, so kommt er in die Ge­fahr, verderblichen Kräften zu verfallen. Man muß sich nämlich darüber klar sein, daß der Mensch fortwährend den Einflüssen seiner Umgebung ausgesetzt ist.",
      "Er lebt ja nur durch die Einwirkungen dieser Umgebung. Zunächst kommen innerhalb der Umgebung die Reiche der sichtba­ren Natur in Betracht. Der Mensch gehört dieser sichtba­ren Natur an. Gäbe es um ihn herum nicht das Mineral-, Pflanzen-, Tierreich und dasjenige der anderen Menschen: er könnte nicht leben.",
      "Man denke sich den Menschen von der Erde hinweggehoben in den Weltenraum hinaus, er müßte als physischer Mensch sogleich zugrunde gehen, wie die Hand verdorrt, wenn man sie vom Leibe trennt. So stark die Illusion wäre, deren sich die menschliche Hand schuldig machte, wenn sie glaubte, sie könne ohne den Leib leben, so stark wäre auch die Täuschung, in welche der Mensch verfiele, wenn er behauptete, er könne ohne das Mineral-, Tier-, Pflanzenreich und ohne die anderen Menschen als physisches Wesen existieren. - Nun gibt es aber außer den genannten Reichen noch drei andere, die sich für gewöhnlich der menschlichen Aufmerksamkeit entziehen.",
      "Es sind die drei Elementarreiche. Sie stehen in einer gewissen Beziehung unter dem Mineralreiche. Es gibt Wesen, die es nicht bis zur mineralischen Verdichtung bringen, die aber deshalb nicht weniger da sind und ihre Wirkung auf den Menschen haben. (Man vergleiche über",
      "diese Elementarreiche, was über sie in den Aufsätzen «Aus der Akasha-Chronik» gesagt ist, sowie die Bemerkungen darüber in meiner «Theosophie».) Der Mensch ist somit Einflüssen aus Naturreichen ausgesetzt, die in einer gewis­sen Richtung unsichtbare genannt werden müssen. Wenn nun die Seele am Leibe arbeitet, so besteht ein wesentlicher Teil ihrer Tätigkeit darinnen, die Einflüsse der Elementarreiche so zu regeln, daß sie für den Menschen gedeihliche sind. - In dem Augenblicke nun, in dem die Seele ihre Tä­tigkeit zum Teil dem Leibe entzieht, können sich seiner verderbliche Kräfte aus den Elementarreichen bemächti­gen.",
      "Darin besteht eine Gefahr der höheren Entwickelung. Es muß daher dafür gesorgt werden, daß, sobald sich die Seele vom Körper zurückzieht, er durch sich selbst nur gu­ten Einflüssen von Seiten der elementaren Welt zugänglich ist. - Wird darauf nicht geachtet, so verkommt der gewöhn­liche Mensch in einer gewissen Beziehung physisch und auch moralisch, trotzdem er den Zugang zu höheren Wel­ten gewinnt.",
      "Während die Seele in höheren Gebieten lebt, nisten sich im dichten physischen Leib und im Ätherleib schädliche Kräfte ein. Dies ist der Grund, warum gewisse schlechte Eigenschaften, die vor der höheren Entwickelung durch die ausgleichende Wirkung der Seele niedergehalten worden sind, bei Mangel an Vorsicht zum Ausdruck kom­men können.",
      "Menschen, welche vorher gute, moralische Naturen waren, können unter solchen Umständen dann, wenn sie an höhere Welten herantreten, allerlei niedrige Neigungen, erhöhte Selbstsucht, Unwahrhaftigkeit, Rach­sucht, Zorn usw. usw. hervorkehren. - Niemand darf von dieser Tatsache sich zurückschrecken lassen, in die höheren Welten aufzusteigen; aber vorgesorgt muß werden, daß",
      "solche Dinge nicht eintreten. Die niedere Natur des Men­schen muß gefestet und unzugänglich gemacht werden ge­fährlichen elementarischen Einflüssen. Das eben geschieht durch die bewußte Ausbildung gewisser Tugenden. Diese Tugenden werden in den Schriften, welche von geistiger Entwickelung handeln, angegeben. Hier aber hat man den Grund, warum auf sie Sorgfalt gelegt werden muß. Es sind die folgenden.",
      "Zuerst muß der Mensch in ganz bewußter Weise bei al­len Dingen fortwährend darauf bedacht sein, das Bleiben­de, Unvergängliche von dem Vergänglichen abzusondern, und auf das erstere seine Aufmerksamkeit richten. In jedem Dinge und Wesen kann der Mensch ein Etwas vermuten oder erkennen, das bleibt, wenn die vergängliche Erschei­nung entschwindet. Sehe ich eine Pflanze, dann kann ich sie zunächst betrachten, wie sie sich den Sinnen darbietet. Das soll man gewiß nicht versäumen. Und niemand wird das Ewige in den Dingen entdecken, der sich nicht zuerst mit dem Vergänglichen gründlich bekannt gemacht hat. Diejenigen, welche sich immer besorgt zeigen, daß dem Menschen, der den Blick auf das Geistig-Unvergängliche richtet, die «Frische und Natürlichkeit des Lebens» verlo­rengehe: sie wissen eben noch nicht, um was es sich dabei eigentlich handelt. Aber, wenn ich so die Pflanze anschaue, kann mir klarwerden, daß in ihr ein bleibender Lebenstrieb ist, der in einer neuen zum Vorschein kommen werde, wenn die gegenwärtige Pflanze längst zerstoben sein wird. Solche Art, sich zu den Dingen zu stellen, muß man in die ganze Verfassung seines Gemütes aufnehmen. - Dann muß man sein Herz auf das Wertvolle, Gediegene heften und dieses höher schätzen lernen als das Vorübergehende, Bedeutungslose.",
      "Man soll sich bei allen seinen Empfindungen und Handlungen den Wert vor Augen halten, den etwas im Zusammenhange eines Ganzen hat. - Zum dritten soll man sechs Eigenschaften in sich ausbilden: Kontrolle der Ge­dankenwelt, Kontrolle der Handlungen, Ertragsamkeit, Unbefangenheit, Vertrauen in die Umwelt und inneres Gleichgewicht. Kontrolle der Gedankenwelt erreicht man, wenn man sich bemüht, dem Irrlichtelieren der Gedanken und Empfindungen, die beim gewöhnlichen Menschen im­mer auf- und abwogen, entgegenzuarbeiten.",
      "Im alltäglichen Leben ist der Mensch nicht der Führer seiner Gedanken; sondern er wird von ihnen getrieben. Das kann natürlich auch gar nicht anders sein. Denn das Leben treibt den Men­schen. Und er muß als ein Wirkender sich diesem Treiben des Lebens überlassen.",
      "Während des gewöhnlichen Lebens wird das gar nicht anders sein können. Will man aber in ei­ne höhere Welt aufsteigen, so muß man sich wenigstens ganz kurze Zeiten aussondern, in denen man sich zum Herrn seiner Gedanken- und Empfindungswelt macht.",
      "Man stellt da einen Gedanken aus völliger innerer Freiheit in den Mittelpunkt seiner Seele, während sich sonst die Vor­stellungen von außen aufdrängen. Dann versucht man alle aufsteigenden Gedanken und Gefühle fernzuhalten und nur das mit dem ersten Gedanken zu verbinden, von dem man selbst will, daß es dazu gehöre.",
      "Eine solche Übung wirkt wohltätig auf die Seele und dadurch auch auf den Leib. Sie bringt den letzteren in eine solche harmonische Verfassung, daß er sich schädlichen Einflüssen entzieht, wenn die Seele auch nicht unmittelbar auf ihn wirkt. - Kontrolle der Handlungen besteht in einer ähnlichen Re­gelung derselben durch innere Freiheit.",
      "Man beginnt gut",
      "damit, daß man sich anschickt, irgend etwas regelmäßig zu tun, wozu man durch das gewöhnliche Leben nicht gekom­men wäre. In dem letzteren wird ja der Mensch von außen zu seinen Handlungen getrieben. Die kleinste Tat aber, die man aus der ureigensten Initiative heraus unternimmt, wirkt in der angegebenen Richtung mehr als alles, wozu man vom äußeren Leben gedrängt wird. - Ertragsamkeit ist das Entfernthalten von jener Stimmung, die man be­zeichnen kann mit dem Wechsel zwischen «Himmelhoch jauchzend, zu Tode betrübt». Der Mensch wird hin- und hergetrieben zwischen allen möglichen Stimmungen. Die Lust macht ihn froh, der Schmerz drückt ihn herab. Das hat seine Berechtigung. Wer aber den Weg sucht zu höhe­rer Erkenntnis, der muß sich in der Lust und auch im Schmerze mäßigen können. Er muß «ertragsam» werden. Maßvoll muß er sich den lusterregenden Eindrücken hin­geben können und auch den schmerzlichen Erlebnissen : immer durch beides mit Würde hindurchschreiten. Von nichts sich übermannen, außer Fassung bringen lassen. Das begründet nicht Gefühllosigkeit, sondern macht den Men­schen zum festen Mittelpunkt innerhalb der Lebenswellen, die rings um ihn auf- und niedersteigen. Er hat sich stets in der Hand.",
      "Eine ganz besonders wichtige Eigenschaft ist der «Sinn für die Bejahung». Es kann ihn derjenige bei sich entwickeln, welcher das Augenmerk in allen Dingen auf die gu­ten, schönen und zweckvollen Eigenheiten richtet und nicht in erster Linie auf das Tadelnswerte, Häßliche und Widerspruchsvolle. Es gibt eine schöne, in der persischen Dichtung vorhandene Legende von Christus, die zur An­schauung bringt, was mit dieser Eigenschaft gemeint ist :",
      "Ein toter Hund liegt an einem Wege. Unter den an ihm Vorübergehenden ist auch Christus. Alle anderen wenden sich ab von dem häßlichen Anblick, den das Tier bietet; nur Christus spricht bewundernd von den schönen Zähnen des Tieres.",
      "So kann man den Dingen gegenüber empfin­den; in allem, auch dem Widrigsten, mag sich für den, wel­cher ernstlich sucht, etwas Anerkennenswertes finden. Und das Fruchtbare an den Dingen ist ja nicht, was ihnen fehlt, sondern dasjenige, was sie haben. - Weiter ist bedeutsam, die Eigenschaft der «Unbefangenheit» zu entwickeln.",
      "Ein jeder Mensch hat ja seine Erfahrungen gemacht und sich dadurch eine bestimmte Menge von Meinungen gebildet, die ihm dann im Leben zur Richtschnur werden. So selbst­verständlich es auf der einen Seite ist, sich nach seinen Er­fahrungen zu richten, so wichtig ist es für den, welcher eine geistige Entwickelung zur höheren Erkenntnis hin durch­machen will, daß er sich stets den Blick frei erhält für alles Neue, ihm noch Unbekannte, das ihm entgegentritt.",
      "Er wird so vorsichtig wie irgend möglich sein mit dem Ur­teil: «das ist unmöglich», «das kann ja gar nicht sein». Mag ihm seine Meinung nach den bisherigen Erfahrungen was immer sagen: er ist in jedem Augenblick bereit, sich von etwas Neuem, das ihm entgegenkommt, zu einer ande­ren Meinung bringen zu lassen.",
      "Jede Eigenliebe der Mei­nung gegenüber muß schwinden. - Wenn die bisher genannten fünf Eigenschaften von der Seele erworben sind, dann stellt sich eine sechste ganz von selbst ein: das innere Gleichgewicht, die Harmonie der geistigen Kräfte. Der Mensch muß etwas in sich finden wie einen geistigen Schwerpunkt, der ihm Festigkeit und Sicherheit gibt ge­genüber allem, was im Leben da- oder dorthin zieht.",
      "muß nicht etwa vermeiden, mit allem mitzuleben, alles auf sich wirken zu lassen. Nicht die Flucht vor den hin- und widerziehenden Tatsachen des Lebens ist das Richtige, son­dern im Gegenteil: das volle Hingeben an das Leben und trotzdem die sichere, feste Bewahrung von innerem Gleich­gewicht und Harmonie.",
      "Endlich kommt für den Suchenden der «Wille zur Frei­heit» in Betracht. Es hat ihn jemand, der zu allem, was er vollbringt, die Stütze und Grundlage in sich selbst findet. Er ist deshalb so schwer zu erringen, weil taktvoll der Aus­gleich notwendig ist zwischen dem Öffnen des Sinnes ge­genüber allem Großen und Guten und der gleichzeitigen Ablehnung eines jeglichen Zwanges. Man sagt so leicht: Einwirkung von außen und Freiheit vertragen sich nicht. Daß sie sich in der Seele vertragen: darauf kommt es aber gerade an. Wenn mir jemand etwas mitteilt, und ich nehme es unter dem Zwange seiner Autorität an: dann bin ich un­frei. Aber ich bin nicht minder unfrei, wenn ich mich ver­schließe vor dem Guten, das ich auf diese Art empfangen kann. Denn dann übt in der eigenen Seele das Schlechtere, das ich habe, auf mich einen Zwang aus. Und bei der Frei­heit kommt es nicht allein darauf an, daß ich nicht unter dem Zwange einer äußeren Autorität stehe, sondern vor allen Dingen auch nicht unter derjenigen eigener Vorur­teile, Meinungen, Empfindungen und Gefühle. Nicht blin­de Unterwerfung unter das Empfangene ist das Richtige, sondern sich von ihm anregen lassen, es ganz unbefangen aufnehmen, um sich «frei» dazu zu bekennen. Eine fremde Autorität soll nicht anders als so wirken, daß man sich sagt: Ich mache mich gerade dadurch frei, daß ich ihrem Guten folge, das heißt, es zu dem meinigen mache. Und",
      "eine auf der Geheimwissenschaft fußende Autorität will auch gar nicht anders als in dieser Art wirken. Sie gibt, was sie zu geben hat, nicht um selbst Macht über den Beschenk­ten zu gewinnen, sondern allein darum, daß der Beschenkte durch die Gabe reicher und freier werde.",
      "Es ist auf die Bedeutung der angeführten Eigenschaften schon früher bei Besprechung der «Lotusblumen » hinge­wiesen worden. Dort wurde gezeigt, welche Beziehung sie zu der Entwickelung der zwölfblätterigen Lotusblume in der Herzgegend und der daran sich schließenden Strömun­gen des Ätherkörpers haben. Aus dem jetzt Gesagten ist ersichtlich, daß sie im wesentlichen die Aufgabe haben, dem physischen Körper des Suchenden jene Kräfte entbehr­lich zu machen, die ihm sonst während des Schlafzustandes zugute kommen und die ihm wegen der Ausbildung entzo­gen werden müssen. Unter solchen Einwirkungen entwickelt sich die imaginative Erkenntnis."
    ],
    "sentences": [
      [
        "Bis zu der Begegnung mit den beiden «Hütern der Schwel­le» ist in dem Buche «Wie erlangt man Erkenntnisse der höheren Welten?» der Weg zur höheren Erkenntnis ver­folgt worden.",
        "Nun sollen auch noch die Verhältnisse ge­schildert werden, in denen die Seele zu den verschiedenen Welten steht, wenn sie durch die aufeinanderfolgenden Erkenntnis stufen hindurchschreitet.",
        "Damit wird das gegeben, was man die «Erkenntnislehre der Geheimwissenschaft» nennen kann."
      ],
      [
        "Bevor der Mensch den Pfad höherer Erkenntnis betritt, kennt er nur die erste von vier Erkenntnisstufen.",
        "Es ist die­jenige, welche ihm im gewöhnlichen Leben innerhalb der Sinnenwelt eigen ist.",
        "Auch in dem, was zunächst «Wissen­schaft» genannt wird, hat man es nur mit dieser ersten Er­kenntnisstufe zu tun.",
        "Denn diese Wissenschaft arbeitet ja nur das gewöhnliche Erkennen feiner aus, macht es diszi­plinierter.",
        "Sie bewaffnet die Sinne durch Instrumente - Mikroskop, Fernrohr usw. -, um genauer zu sehen, was die unbewaffneten Sinne nicht sehen.",
        "Aber die Erkenntnisstufe bleibt doch dieselbe, ob man normal große Dinge mit dem gewöhnlichen Auge sieht, oder ob man sehr kleine Gegenstände und Vorgänge mit dem Vergrößerungsglase ver­folgt.",
        "Auch in der Anwendung des Denkens auf die Dinge und Tatsachen bleibt diese Wissenschaft bei dem stehen, was schon im alltäglichen Leben getrieben wird.",
        "Man ord­net die Gegenstände, beschreibt und vergleicht sie, man sucht sich ein Bild von ihren Veränderungen zu machen usw.",
        "Der strengste Naturforscher tut im Grunde in dieser Beziehung nichts anderes, als daß er das Beobachtungsver­fahren"
      ],
      [
        "des alltäglichen Lebens in einer kunstgemäßen Art ausbildet.",
        "Seine Erkenntnis wird umfangreicher, komplizierter, logischer; aber er schreitet nicht zu einer anderen Erkenntnisart vor."
      ],
      [
        "Man nennt diese erste Erkenntnis stufe in der Geheimwis­senschaft die «materielle Erkenntnisart».",
        "Dazu kommen dann zunächst drei höhere.",
        "An sie schließen sich dann noch weitere an.",
        "Sie sollen hier beschrieben werden, bevor in der Schilderung des «Erkenntnispfades » weitergegangen wird.",
        "Nimmt man das gewöhnliche - und sinnlich-wissen­schaftliche - Erkennen als die erste Stufe an, so hat man zunächst folgende vier Stufen zu unterscheiden :"
      ],
      [
        "Die materielle Erkenntnis."
      ],
      [
        "Die imaginative Erkenntnis."
      ],
      [
        "Die inspirierte Erkenntnis, die man auch die «willensartigen» nennen kann."
      ],
      [
        "Die intuitive Erkenntnis."
      ],
      [
        "Diese Stufen sollen im weiteren zur Sprache kommen.",
        "Man muß sich zunächst klarmachen, womit man es bei die­sen verschiedenen Erkenntnisarten zu tun hat. - Beim ge­wöhnlichen sinnlichen Erkennen kommen vier Elemente in Betracht : 1.",
        "Der Gegenstand, welcher auf die Sinne einen Eindruck macht. 2.",
        "Das Bild, das sich der Mensch von diesem Gegenstande macht. 3.",
        "Der Begriff, durch den der Mensch zu einer geistigen Erfassung einer Sache oder eines Vorganges kommt. 4.",
        "Das «Ich», welches sich auf Grund des Eindruckes vom Gegenstande Bild und Begriff bildet.",
        "Bevor sich der Mensch ein Bild - eine «Vorstellung » macht, ist ein Gegenstand da, welcher ihn dazu veranlaßt.",
        "Diesen bildet er nicht selbst, er nimmt ihn wahr.",
        "Und auf Grund dieses Gegenstandes entsteht das Bild.",
        "Solange man ein"
      ],
      [
        "Ding anblickt, hat man es mit diesem selbst zu tun.",
        "In dem Augenblicke, wo man von dem Dinge hinwegtritt, besitzt man nur noch das Bild.",
        "Den Gegenstand verläßt man, das Bild bleibt in der Erinnerung «haften»."
      ],
      [
        "Aber man kann nicht dabei stehenbleiben, sich bloß «Bilder» zu machen.",
        "Man muß zu «Begriffen » kommen.",
        "Die Unterscheidung von «Bild » und «Begriff» ist unbedingt notwendig, wenn man sich hier ganz klarwerden will."
      ],
      [
        "Man stelle sich einmal vor, man sehe einen Gegenstand, welcher kreisförmig ist.",
        "Dann drehe man sich um, und man behalte das Bild des Kreises im Gedächtnisse.",
        "Da hat man noch nicht den «Be­griff» des Kreises."
      ],
      [
        "Dieser ergibt sich erst, wenn man sich sagt : «Ein Kreis ist eine Figur, bei der alle Punkte von ei­nem Mittelpunkte gleich weit entfernt sind. » Erst wenn man sich von einer Sache einen «Begriff» gemacht hat, ist man zum Verständnisse derselben gekommen.",
        "Es gibt viele Kreise : kleine, große, rote, blaue usw.; aber es gibt nur einen Begriff «Kreis». - Auf alles dieses soll im weiteren noch näher eingegangen werden; vorläufig soll nur skizziert werden, was zur Charakteristik der vier ersten Erkenntnisstufen notwendig ist. - Das vierte Element, das bei der materiellen Erkenntnis in Betracht kommt, ist das «Ich»."
      ],
      [
        "In demselben kommt eine Einheit der Bilder und Begriffe zustande.",
        "Dieses «Ich» bewahrt in seinem Gedächtnisse die Bilder.",
        "Wäre das nicht der Fall, so entstände kein fortlaufendes inneres Leben.",
        "Die Bilder der Dinge blieben nur so lange vorhanden, als diese Dinge selbst auf die Seele wirken."
      ],
      [
        "Das innere Leben aber hängt davon ab, daß Wahrnehmung an Wahrnehmung gereiht wird.",
        "Das «Ich» orientiert sich «heute » in der Welt, weil ihm bei gewissen Gegenständen die Bilder der gleichen Gegenstände von"
      ],
      [
        "«gestern » auftauchen.",
        "Man vergegenwärtige sich nur, wie unmöglich das Seelenleben wäre, wenn man nur so lange ein Bild eines Dinges hätte, als dieses selbst vor einem steht. - Auch bezüglich der Begriffe bildet das «Ich» die Einheit.",
        "Es verbindet seine Begriffe und verschafft sich auf diese Art einen Überblick, das heißt ein Verständnis der Welt.",
        "Diese Verbindung der Begriffe geschieht im «Urteilen».",
        "Ein Wesen, das nur lose Begriffe hätte, könnte sich in der Welt nicht zurechtfinden.",
        "Alle Tätigkeit des Menschen beruht auf seiner Fähigkeit, Begriffe zu verbinden, das heißt"
      ],
      [
        "auf seinem «Urteilen»."
      ],
      [
        "Das «materielle Erkennen» beruht darauf, daß der Mensch durch seine Sinne einen Eindruck von Dingen und Vorstellungen der Außenwelt erhält.",
        "Er hat die Fähigkeit des Empfindens oder die Sensibilität.",
        "Der «von außen »empfangene Eindruck wird auch Sensation genannt.",
        "Daher kommen bei der «materiellen Erkenntnis» die vier Ele­mente in Betracht : Sensation, Bild, Begriff, Ich. - Bei der nächsthöheren Stufe des Erkennens fällt nun der Eindruck auf die äußeren Sinne, die «Sensation», weg.",
        "Ein äußerer Sinnesgegenstand ist nicht mehr vorhanden.",
        "Es bleiben al­so von den Elementen, an welche der Mensch von der ge­wöhnlichen Erkenntnis her gewöhnt ist, nur die drei: Bild, Begriff und Ich."
      ],
      [
        "Das gewöhnliche Erkennen bildet bei einem gesunden Menschen kein Bild und keinen Begriff, wenn ein äußerer Sinnesgegenstand nicht vorhanden ist.",
        "Das «Ich» bleibt dann untätig.",
        "Wer sich Bilder formt, denen Sinnesgegen­stände entsprechen sollen, wo in Wahrheit keine sind, lebt in Phantastik. - Nun aber erwirbt sich der Geheimschüler eben die Fähigkeit, Bilder zu formen, auch wo keine Sin­nesgegenstände"
      ],
      [
        "vorhanden sind.",
        "Es muß dann bei ihm an die Stelle des «äußeren Gegenstandes» ein anderer treten.",
        "Er muß Bilder haben können, auch wenn kein Gegenstand seine Sinne berührt.",
        "An die Stelle der «Sensation» muß etwas anderes treten."
      ],
      [
        "Dies ist die Imagination.",
        "Bei dem Ge­heimschüler auf dieser Stufe treten Bilder auf genau so, wie wenn ein Sinnesgegenstand auf ihn einen Eindruck machen würde; sie sind so lebhaft und wahr wie die Sinnesbilder, nur kommen sie nicht vom «Materiellen», sondern vom «Seelischen» und «Geistigen»."
      ],
      [
        "Die Sinne bleiben da­bei vollständig untätig. - Es ist einleuchtend, daß sich der Mensch diese Fähigkeit, inhaltvolle Bilder zu haben ohne Sinneseindrücke, erst erwerben muß.",
        "Es geschieht dies durch die Meditation, durch die Übungen, welche in den Darstellungen des Buches «Wie erlangt man Erkenntnisse der höheren Welten?» beschrieben worden sind."
      ],
      [
        "Der auf die Sinnenwelt beschränkte Mensch lebt nur in dem Um­kreis einer Bilderwelt, welche erst durch die Sinne in ihn Einlaß gefunden haben.",
        "Der imaginative Mensch hat eine solche Bilderwelt, die von einer höheren Welt ihren Zufluß erhält."
      ],
      [
        "Es gehört eine sehr sorgfältige Schulung dazu, in­nerhalb dieser höheren Bilderwelt Täuschung von Wirklich­keit zu unterscheiden.",
        "Nur zu leicht sagt sich der Mensch, wenn solche Bilder zunächst vor seine Seele hintreten: «Ach, das sind ja nur Einbildungen, bloße Ausflüsse mei­nes Vorstellungslebens.» Das ist nur zu begreiflich."
      ],
      [
        "Denn der Mensch ist zunächst ja daran gewöhnt, nur dasjenige «wirklich » zu nennen, was, ohne sein Zutun, ihm durch die feste Grundlage seiner Sinneswahrnehmung gegeben ist.",
        "Und er muß sich erst hineinfinden, Dinge für «wirkli­che» zu nehmen, die von ganz anderer Seite veranlaßt werden."
      ],
      [
        "Und er kann auch darinnen nicht vorsichtig genug sein, wenn er nicht zum Phantasten werden will.",
        "Die Entscheidung darüber, was auf höherem Gebiete «wirklich» ist, was nur «Illusion», die kann nur von der Erfahrung kommen.",
        "Und man muß sich diese Erfahrung in einem stil­len, geduldigen Innenleben aneignen.",
        "Zunächst muß man durchaus darauf gefaßt sein, daß einem die «Illusion» böse Streiche spielt.",
        "Überall lauern die Möglichkeiten, daß Bil­der auftauchen, die nur auf Täuschungen der äußeren Sin­ne, des abnormen Lebens beruhen.",
        "Alle solche Möglich­keiten müssen zuerst hinweggeräumt werden.",
        "Man muß zu­erst die Quellen der Phantastik ganz verstopfen, dann kann man erst zu der Imagination kommen.",
        "Ist man so weit, dann wird man allerdings sich klar darüber, daß die Welt, in die man in solcher Art eintritt, nicht nur so wirklich ist wie die sinnliche, sondern daß sie eine gewöhnlich viel wirklichere ist."
      ],
      [
        "Bei der dritten Stufe der Erkenntnis bleiben nun auch die Bilder weg.",
        "Der Mensch hat es nur noch mit «Begriff» und «Ich» zu tun.",
        "Hat er auf der zweiten Stufe noch eine Bil­derwelt um sich, die erinnert an die Augenblicke, wo das lebhafte Gedächtnis sich die Eindrücke der Außenwelt vor die Seele zaubert, ohne selbst solche Eindrücke zu haben: auf der dritten Stufe sind auch solche Bilder nicht mehr vorhanden.",
        "Der Mensch lebt ganz in einer rein geistigen Welt.",
        "Wer nur gewöhnt ist, sich an die Sinne zu halten, wird versucht sein, zu glauben, daß diese Welt eine blasse, ge­spenstige sei.",
        "Das ist sie aber ganz und gar nicht.",
        "Auch die Bilderwelt der zweiten Stufe hat nichts Blasses, Schatten­haftes.",
        "So sind ja allerdings die Bilder zumeist, die im Ge­dächtnisse haften bleiben, wenn die äußeren Dinge weg sind.",
        "Aber die Bilder der Imagination sind von einer Leb­haftigkeit"
      ],
      [
        "und Inhaltsfülle, mit der sich nicht nur die schat­tenhaften Erinnerungsbilder der Sinnenwelt nicht ver­gleichen lassen, sondern sogar nicht einmal die ganze bunte, wechselreiche Sinnenwelt selbst.",
        "Auch diese ist gegen das Reich der Imagination nur ein Schatten. - Und nun gar die Welt der dritten Erkenntnisstufe!",
        "Von ihrem Reichtum und ihrer Fülle gibt nichts in der Sinnenwelt eine Vorstellung.",
        "Was für die erste Stufe die Sensation, für die zweite die Imagination, das ist für sie die Inspiration.",
        "Die Inspiration gibt die Eindrücke, und das «Ich» formt die Begriffe.",
        "Will man durchaus mit dieser Welt etwas Sinnliches vergleichen, so kann nur die Tonwelt des Hörens zu einem solchen Ver­gleiche herangezogen werden.",
        "Aber nicht mit Tönen wie in der sinnlichen Musik hat man es zu tun, sondern mit ei­nem rein «geistigen Tönen».",
        "Man beginnt zu «hören», was im Innern der Dinge vorgeht.",
        "Der Stein, die Pflanze usw. werden zu «geistigen Worten».",
        "Die Welt beginnt der Seele gegenüber ihr Wesen wirklich selbst auszusprechen.",
        "Es klingt grotesk; aber es ist wörtlich wahr : auf dieser Stufe des Erkennens «hört man geistig das Gras wachsen».",
        "Man vernimmt die Form des Kristalles als Klang; die sich öff­nende Blüte «spricht» da zum Menschen.",
        "Der Inspirierte vermag das innere Wesen der Dinge zu künden; alle Dinge werden in neuer Art vor seiner Seele auferstehen.",
        "Er spricht eine Sprache, die aus einer anderen Welt stammt, und wel­che doch erst die alltägliche Welt begreiflich macht."
      ],
      [
        "Auf der vierten Erkenntnisstufe endlich hört auch die In­spiration auf.",
        "Von den Elementen, die man vom alltägli­chen Erkennen her gewohnt ist, zu betrachten, ist nur noch das «Ich» dasjenige, welches in Betracht kommt.",
        "Der Ge­heimschüler merkt an einer ganz bestimmten inneren Erfahrung,"
      ],
      [
        "daß er bis zu dieser Stufe aufgestiegen ist.",
        "Diese Erfahrung drückt sich darin aus, daß er das Gefühl hat: er stehe jetzt nicht mehr außer den Dingen und Vorgängen, welche er erkennt, sondern innerhalb derselben."
      ],
      [
        "Bilder sind nicht der Gegenstand; sie drücken ihn bloß aus.",
        "Auch was die Inspiration gibt, ist nicht der Gegenstand.",
        "Sie spricht ihn nur aus.",
        "Das aber, was jetzt in der Seele lebt, ist wirk­lich der Gegenstand selbst."
      ],
      [
        "Das Ich hat sich ergossen über alle Wesen; es ist mit ihnen zusammengeflossen.",
        "Das Leben der Dinge in der Seele ist nun die Intuition.",
        "Es ist eben ganz wörtlich zu nehmen, wenn man von der Intuition sagt: man kriecht durch sie in alle Dinge hinein. - Im gewöhnlichen Leben hat der Mensch nur eine Intuition, das ist diejenige des «Ich» selber."
      ],
      [
        "Denn das «Ich» kann auf keine Weise von außen wahrgenommen werden, es kann nur im Innern erlebt werden.",
        "Eine einfache Erwägung kann das klarma­chen.",
        "Es ist dies eine Erwägung, die allerdings von den Psychologen nicht mit der wünschenswerten Schärfe ge­macht wird."
      ],
      [
        "So unscheinbar sie aber ist: für den, der sie ganz versteht, ist sie von der allerweittragendsten Bedeu­tung.",
        "Sie ist die folgende: Ein jedes Ding der Außenwelt kann von allen Menschen mit demselben Namen genannt werden."
      ],
      [
        "Der Tisch kann von allen mit «Tisch», die Tulpe von allen mit «Tulpe», der Herr Müller von allen mit «Herr Müller» angesprochen werden.",
        "Aber es gibt ein Wort, das jeder nur zu sich selbst sprechen kann."
      ],
      [
        "Dies ist das Wort «Ich».",
        "Kein anderer kann zu mir «Ich» sagen, für jeden anderen bin ich ein «Du».",
        "Ebenso ist jeder andere für mich ein «Du».",
        "Nur er selbst kann zu sich «Ich» sagen.",
        "Das rührt davon her, daß man nicht außer, sondern in dem «Ich» lebt."
      ],
      [
        "Und so lebt man durch die intuitive Erkenntnis in allen Dingen."
      ],
      [
        "Die Wahrnehmung des eigenen «Ich» ist das Vorbild für alle intuitive Erkenntnis.",
        "Um so in die Dinge hineinzu­kommen, muß man allerdings erst aus sich selbst heraustreten.",
        "Man muß «selbstlos» werden, um mit dem «Selbst», dem «Ich», einer anderen Wesenheit zu verschmelzen."
      ],
      [
        "Meditation und Konzentration sind die sicheren Mittel, um zu dieser Stufe, ebenso wie zu den früheren, hinanzu­steigen.",
        "Allerdings müssen sie in stiller, geduldiger Art ge­übt werden.",
        "Wer da glaubt, daß er tumultuarisch, mit Ge­waltmitteln zu den höheren Welten steigen kann, der irrt sich.",
        "Und einem solchen Glauben würde sich derjenige hin­geben, welcher erwartete, daß ihm die Wirklichkeit auf hö­heren Gebieten in ebensolcher Art entgegentritt wie in der Sinnenwelt.",
        "So lebhaft und reich auch die Welten sind, zu denen man hinansteigt, sie sind fein und subtil, während die Sinnenwelt grob und derb ist.",
        "Das Wichtigste, was man lernen muß, ist gerade die Gewöhnung daran, etwas ganz anderes «wirklich» zu nennen, als was man im Bereich der Sinne so bezeichnet.",
        "Und dies ist nicht ganz leicht.",
        "Deshalb wird so mancher, der den Geheimpfad so gerne gehen möchte, schon bei den ersten Schritten zurückgeschreckt.",
        "Er hat erwartet, daß ihm Dinge entgegentreten, welche sind wie Tische und Stühle, und er findet «Geister».",
        "Weil aber «Geister» nicht dicht sind wie Stühle und Tische, so kommen sie ihm als «Einbildungen » vor.",
        "Daran ist nichts anderes schuld als die Ungewohntheit.",
        "Man muß sich erst die rechte Empfindung für die geistige Welt erwerben, dann wird man das Geistige nicht bloß schauen, sondern auch anerkennen.",
        "Und ein großer Teil der Geheimschulung be­zieht sich auf diese richtige Anerkennung und Einschät­zung des Geistigen."
      ],
      [
        "Man muß zunächst den Schlafzustand betrachten, wenn man Aufschluß erlangen will über die imaginative Erkennt­nis.",
        "Solange der Mensch keine höhere Erkenntnisstufe er­langt hat als die materielle, lebt die Seele zwar während des Schlafes, aber sie kann in der Welt, in welcher sie schlafend lebt, nichts wahrnehmen."
      ],
      [
        "Sie ist in dieser Welt wie ein Blinder in der materiellen.",
        "Ein solcher lebt in der Welt des Lichtes und der Farben; aber er nimmt sie nicht wahr. - Von den äußeren Sinnesorganen, dem Auge, dem Ohr, der gewöhn­lichen Gehirntätigkeit usw. hat sich die Seele im Schlafe zurückgezogen."
      ],
      [
        "Sie erhält durch die Sinne keine Eindrücke.",
        "Was tut sie nun während des Schlafes?",
        "Klar muß man sich darüber sein, daß die Seele während des Wachens in einer fortwährenden Tätigkeit ist.",
        "Sie empfängt die äußeren Sin­neseindrücke und verarbeitet sie: das ist ihre Tätigkeit."
      ],
      [
        "Diese stellt sie während des Schlafes ein.",
        "Aber sie ist kei­neswegs untätig.",
        "Sie arbeitet schlafend an dem einen Lei­be.",
        "Dieser wird ja während der wachen Tagesarbeit abge­nützt.",
        "Das drückt sich in der Ermüdung aus."
      ],
      [
        "Und während des Schlafes beschäftigt sich die Seele mit dem eigenen Leib, um ihn für weitere wache Tagesarbeit wieder geeig­net zu machen.",
        "Man sieht daraus, wie wesentlich der rich­tige Schlaf dem Gedeihen des Leibes ist."
      ],
      [
        "Ein Mensch, der nicht entsprechend schläft, läßt seine Seele an dem Leibe nicht die notwendige Verbesserungsarbeit tun. - Und die Folge davon muß sein, daß der Leib herunterkommt. - Die Kräfte, mit denen die Seele während des Schlafes am Leibe arbeitet, sind dieselben, durch welche sie auch im Wachzustande tätig ist.",
        "Nur werden sie in dem letzteren dazu verwendet, die Eindrücke der äußeren Sinne aufzu­nehmen und sie zu verarbeiten."
      ],
      [
        "Tritt nun die imaginative Erkenntnis beim Menschen ein, so muß ein Teil der im Schlafe auf den Leib gewende­ten Kräfte in einer anderen Art verbraucht werden.",
        "Durch diese Kräfte werden nunmehr die geistigen Sinnesorgane gebildet, die es ermöglichen, daß die Seele in einer höheren Welt nicht bloß lebt, sondern auch wahrnimmt.",
        "So arbeitet die Seele schlafend an sich, nicht mehr bloß an ihrem Leibe.",
        "Bewirkt wird diese Arbeit durch die Meditation und Kon­zentration sowie durch andere Übungen.",
        "Es ist schon öfters in diesen Aufsätzen über höhere Erkenntnis gesagt worden, daß die besonderen Anweisungen über solche Übungen nur von Mensch zu Mensch gegeben werden.",
        "Niemand sollte auf eigene Hand diese Übungen unternehmen, denn nur wer Erfahrung auf diesem Gebiete hat, kann ermessen, wel­che Wirkung bei dem einen oder dem anderen Menschen sich einstellen muß, wenn er es unternimmt, seine Seelenarbeit von dem Leibe abzuziehen und in einer höheren Art anzuwenden."
      ],
      [
        "Meditation, Konzentration und andere Übungen bewir­ken, daß die Seele sich für eine Weile zurückzieht von ihrer Verbindung mit den Sinnesorganen.",
        "Sie ist dann in sich selbst versenkt.",
        "Ihre Tätigkeit ist nach innen gewendet.",
        "Im Anfange dieser Versenkung unterscheidet sich zwar diese ihre innere Tätigkeit nicht erheblich von der alltäglichen.",
        "Sie muß dieselben Vorstellungen, Gefühle und Empfindun­gen verwenden während der Innenarbeit, welche sie auch im gewöhnlichen Leben hat.",
        "Je mehr sie sich aber daran gewöhnt, gewissermaßen «blind und taub » gegenüber der sinnlichen Umgebung zu sein, je mehr sie in sich lebt, desto fähiger macht sie sich zu innerer Leistung.",
        "Und was sie bei der Versenkung in das Innere geleistet hat, das trägt seine"
      ],
      [
        "Früchte zunächst im Zustande des Schlafes.",
        "Ist die Seele des Nachts vom Leibe befreit, so wirkt das in ihr fort, was durch die Übungen am Tage angeregt worden ist.",
        "Es bil­den sich in ihr Organe, durch welche sie mit einer höheren Umgebung gerade so in Verbindung kommt wie vorher durch die äußeren Sinnesorgane mit der körperlichen Um­welt."
      ],
      [
        "Aus dem Dunkel der nächtlichen Umgebung treten die Lichterscheinungen der höheren Welt heraus.",
        "Zart und intim ist dieser Verkehr zunächst.",
        "Und der Mensch muß durchaus damit rechnen, daß für eine lange Zeit beim Auf­wachen das Licht des Tages sofort wieder einen dichten Vorhang zieht vor die Erlebnisse der Nacht."
      ],
      [
        "Die Erinne­rung, daß man in der Nacht wahrgenommen hat, tritt nur ganz langsam und allmählich ein.",
        "Denn der Schüler lernt nicht leicht auf die zarten Gebilde seiner Seele achten, die sich im Laufe seiner Entwickelung hineinmischen in die groben Erlebnisse des alltäglichen Sinneslebens."
      ],
      [
        "Anfangs erscheinen ihm solche Gebilde wie das, was man zufällige Eindrücke der Seele nennt.",
        "Alles kommt darauf an, daß er unterscheiden lernt, was er der gewöhnlichen Welt verdankt von dem, was durch seine eigene Wesenheit als Kund­gebung höherer Welten sich darstellt."
      ],
      [
        "In einem stillen, in sich gekehrten Gemütsleben muß er sich diese Unterschei­dung aneignen.",
        "Es ist notwendig, daß er sich erst ein Ge­fühl davon erwerbe, welches der Wert und die Bedeutung der intimen Seelengebilde ist, die wie «zufällige Einfälle» sich in das Tagesleben einmischen und welche doch Er­innerungen an den nächtlichen Verkehr in einer höheren Welt sind."
      ],
      [
        "Sobald man diese Dinge irgendwie grob anfaßt und sie mit dem Maßstab des Sinneslebens mißt, zerstie­ben sie."
      ],
      [
        "Es ist aus obigem ersichtlich, daß durch die Arbeit in einer höheren Welt die Seele dem Leibe etwas von ihrer sonst fürsorglichen Tätigkeit entziehen muß.",
        "Sie überläßt den­selben in einer gewissen Beziehung sich selbst."
      ],
      [
        "Er braucht einen Ersatz für das, was sie ihm vorher geleistet hat.",
        "Er­hält er einen solchen Ersatz nicht, so kommt er in die Ge­fahr, verderblichen Kräften zu verfallen.",
        "Man muß sich nämlich darüber klar sein, daß der Mensch fortwährend den Einflüssen seiner Umgebung ausgesetzt ist."
      ],
      [
        "Er lebt ja nur durch die Einwirkungen dieser Umgebung.",
        "Zunächst kommen innerhalb der Umgebung die Reiche der sichtba­ren Natur in Betracht.",
        "Der Mensch gehört dieser sichtba­ren Natur an.",
        "Gäbe es um ihn herum nicht das Mineral-, Pflanzen-, Tierreich und dasjenige der anderen Menschen: er könnte nicht leben."
      ],
      [
        "Man denke sich den Menschen von der Erde hinweggehoben in den Weltenraum hinaus, er müßte als physischer Mensch sogleich zugrunde gehen, wie die Hand verdorrt, wenn man sie vom Leibe trennt.",
        "So stark die Illusion wäre, deren sich die menschliche Hand schuldig machte, wenn sie glaubte, sie könne ohne den Leib leben, so stark wäre auch die Täuschung, in welche der Mensch verfiele, wenn er behauptete, er könne ohne das Mineral-, Tier-, Pflanzenreich und ohne die anderen Menschen als physisches Wesen existieren. - Nun gibt es aber außer den genannten Reichen noch drei andere, die sich für gewöhnlich der menschlichen Aufmerksamkeit entziehen."
      ],
      [
        "Es sind die drei Elementarreiche.",
        "Sie stehen in einer gewissen Beziehung unter dem Mineralreiche.",
        "Es gibt Wesen, die es nicht bis zur mineralischen Verdichtung bringen, die aber deshalb nicht weniger da sind und ihre Wirkung auf den Menschen haben. (Man vergleiche über"
      ],
      [
        "diese Elementarreiche, was über sie in den Aufsätzen «Aus der Akasha-Chronik» gesagt ist, sowie die Bemerkungen darüber in meiner «Theosophie».) Der Mensch ist somit Einflüssen aus Naturreichen ausgesetzt, die in einer gewis­sen Richtung unsichtbare genannt werden müssen.",
        "Wenn nun die Seele am Leibe arbeitet, so besteht ein wesentlicher Teil ihrer Tätigkeit darinnen, die Einflüsse der Elementarreiche so zu regeln, daß sie für den Menschen gedeihliche sind. - In dem Augenblicke nun, in dem die Seele ihre Tä­tigkeit zum Teil dem Leibe entzieht, können sich seiner verderbliche Kräfte aus den Elementarreichen bemächti­gen."
      ],
      [
        "Darin besteht eine Gefahr der höheren Entwickelung.",
        "Es muß daher dafür gesorgt werden, daß, sobald sich die Seele vom Körper zurückzieht, er durch sich selbst nur gu­ten Einflüssen von Seiten der elementaren Welt zugänglich ist. - Wird darauf nicht geachtet, so verkommt der gewöhn­liche Mensch in einer gewissen Beziehung physisch und auch moralisch, trotzdem er den Zugang zu höheren Wel­ten gewinnt."
      ],
      [
        "Während die Seele in höheren Gebieten lebt, nisten sich im dichten physischen Leib und im Ätherleib schädliche Kräfte ein.",
        "Dies ist der Grund, warum gewisse schlechte Eigenschaften, die vor der höheren Entwickelung durch die ausgleichende Wirkung der Seele niedergehalten worden sind, bei Mangel an Vorsicht zum Ausdruck kom­men können."
      ],
      [
        "Menschen, welche vorher gute, moralische Naturen waren, können unter solchen Umständen dann, wenn sie an höhere Welten herantreten, allerlei niedrige Neigungen, erhöhte Selbstsucht, Unwahrhaftigkeit, Rach­sucht, Zorn usw. usw. hervorkehren. - Niemand darf von dieser Tatsache sich zurückschrecken lassen, in die höheren Welten aufzusteigen; aber vorgesorgt muß werden, daß"
      ],
      [
        "solche Dinge nicht eintreten.",
        "Die niedere Natur des Men­schen muß gefestet und unzugänglich gemacht werden ge­fährlichen elementarischen Einflüssen.",
        "Das eben geschieht durch die bewußte Ausbildung gewisser Tugenden.",
        "Diese Tugenden werden in den Schriften, welche von geistiger Entwickelung handeln, angegeben.",
        "Hier aber hat man den Grund, warum auf sie Sorgfalt gelegt werden muß.",
        "Es sind die folgenden."
      ],
      [
        "Zuerst muß der Mensch in ganz bewußter Weise bei al­len Dingen fortwährend darauf bedacht sein, das Bleiben­de, Unvergängliche von dem Vergänglichen abzusondern, und auf das erstere seine Aufmerksamkeit richten.",
        "In jedem Dinge und Wesen kann der Mensch ein Etwas vermuten oder erkennen, das bleibt, wenn die vergängliche Erschei­nung entschwindet.",
        "Sehe ich eine Pflanze, dann kann ich sie zunächst betrachten, wie sie sich den Sinnen darbietet.",
        "Das soll man gewiß nicht versäumen.",
        "Und niemand wird das Ewige in den Dingen entdecken, der sich nicht zuerst mit dem Vergänglichen gründlich bekannt gemacht hat.",
        "Diejenigen, welche sich immer besorgt zeigen, daß dem Menschen, der den Blick auf das Geistig-Unvergängliche richtet, die «Frische und Natürlichkeit des Lebens» verlo­rengehe: sie wissen eben noch nicht, um was es sich dabei eigentlich handelt.",
        "Aber, wenn ich so die Pflanze anschaue, kann mir klarwerden, daß in ihr ein bleibender Lebenstrieb ist, der in einer neuen zum Vorschein kommen werde, wenn die gegenwärtige Pflanze längst zerstoben sein wird.",
        "Solche Art, sich zu den Dingen zu stellen, muß man in die ganze Verfassung seines Gemütes aufnehmen. - Dann muß man sein Herz auf das Wertvolle, Gediegene heften und dieses höher schätzen lernen als das Vorübergehende, Bedeutungslose."
      ],
      [
        "Man soll sich bei allen seinen Empfindungen und Handlungen den Wert vor Augen halten, den etwas im Zusammenhange eines Ganzen hat. - Zum dritten soll man sechs Eigenschaften in sich ausbilden: Kontrolle der Ge­dankenwelt, Kontrolle der Handlungen, Ertragsamkeit, Unbefangenheit, Vertrauen in die Umwelt und inneres Gleichgewicht.",
        "Kontrolle der Gedankenwelt erreicht man, wenn man sich bemüht, dem Irrlichtelieren der Gedanken und Empfindungen, die beim gewöhnlichen Menschen im­mer auf- und abwogen, entgegenzuarbeiten."
      ],
      [
        "Im alltäglichen Leben ist der Mensch nicht der Führer seiner Gedanken; sondern er wird von ihnen getrieben.",
        "Das kann natürlich auch gar nicht anders sein.",
        "Denn das Leben treibt den Men­schen.",
        "Und er muß als ein Wirkender sich diesem Treiben des Lebens überlassen."
      ],
      [
        "Während des gewöhnlichen Lebens wird das gar nicht anders sein können.",
        "Will man aber in ei­ne höhere Welt aufsteigen, so muß man sich wenigstens ganz kurze Zeiten aussondern, in denen man sich zum Herrn seiner Gedanken- und Empfindungswelt macht."
      ],
      [
        "Man stellt da einen Gedanken aus völliger innerer Freiheit in den Mittelpunkt seiner Seele, während sich sonst die Vor­stellungen von außen aufdrängen.",
        "Dann versucht man alle aufsteigenden Gedanken und Gefühle fernzuhalten und nur das mit dem ersten Gedanken zu verbinden, von dem man selbst will, daß es dazu gehöre."
      ],
      [
        "Eine solche Übung wirkt wohltätig auf die Seele und dadurch auch auf den Leib.",
        "Sie bringt den letzteren in eine solche harmonische Verfassung, daß er sich schädlichen Einflüssen entzieht, wenn die Seele auch nicht unmittelbar auf ihn wirkt. - Kontrolle der Handlungen besteht in einer ähnlichen Re­gelung derselben durch innere Freiheit."
      ],
      [
        "Man beginnt gut"
      ],
      [
        "damit, daß man sich anschickt, irgend etwas regelmäßig zu tun, wozu man durch das gewöhnliche Leben nicht gekom­men wäre.",
        "In dem letzteren wird ja der Mensch von außen zu seinen Handlungen getrieben.",
        "Die kleinste Tat aber, die man aus der ureigensten Initiative heraus unternimmt, wirkt in der angegebenen Richtung mehr als alles, wozu man vom äußeren Leben gedrängt wird. - Ertragsamkeit ist das Entfernthalten von jener Stimmung, die man be­zeichnen kann mit dem Wechsel zwischen «Himmelhoch jauchzend, zu Tode betrübt».",
        "Der Mensch wird hin- und hergetrieben zwischen allen möglichen Stimmungen.",
        "Die Lust macht ihn froh, der Schmerz drückt ihn herab.",
        "Das hat seine Berechtigung.",
        "Wer aber den Weg sucht zu höhe­rer Erkenntnis, der muß sich in der Lust und auch im Schmerze mäßigen können.",
        "Er muß «ertragsam» werden.",
        "Maßvoll muß er sich den lusterregenden Eindrücken hin­geben können und auch den schmerzlichen Erlebnissen : immer durch beides mit Würde hindurchschreiten.",
        "Von nichts sich übermannen, außer Fassung bringen lassen.",
        "Das begründet nicht Gefühllosigkeit, sondern macht den Men­schen zum festen Mittelpunkt innerhalb der Lebenswellen, die rings um ihn auf- und niedersteigen.",
        "Er hat sich stets in der Hand."
      ],
      [
        "Eine ganz besonders wichtige Eigenschaft ist der «Sinn für die Bejahung».",
        "Es kann ihn derjenige bei sich entwickeln, welcher das Augenmerk in allen Dingen auf die gu­ten, schönen und zweckvollen Eigenheiten richtet und nicht in erster Linie auf das Tadelnswerte, Häßliche und Widerspruchsvolle.",
        "Es gibt eine schöne, in der persischen Dichtung vorhandene Legende von Christus, die zur An­schauung bringt, was mit dieser Eigenschaft gemeint ist :"
      ],
      [
        "Ein toter Hund liegt an einem Wege.",
        "Unter den an ihm Vorübergehenden ist auch Christus.",
        "Alle anderen wenden sich ab von dem häßlichen Anblick, den das Tier bietet; nur Christus spricht bewundernd von den schönen Zähnen des Tieres."
      ],
      [
        "So kann man den Dingen gegenüber empfin­den; in allem, auch dem Widrigsten, mag sich für den, wel­cher ernstlich sucht, etwas Anerkennenswertes finden.",
        "Und das Fruchtbare an den Dingen ist ja nicht, was ihnen fehlt, sondern dasjenige, was sie haben. - Weiter ist bedeutsam, die Eigenschaft der «Unbefangenheit» zu entwickeln."
      ],
      [
        "Ein jeder Mensch hat ja seine Erfahrungen gemacht und sich dadurch eine bestimmte Menge von Meinungen gebildet, die ihm dann im Leben zur Richtschnur werden.",
        "So selbst­verständlich es auf der einen Seite ist, sich nach seinen Er­fahrungen zu richten, so wichtig ist es für den, welcher eine geistige Entwickelung zur höheren Erkenntnis hin durch­machen will, daß er sich stets den Blick frei erhält für alles Neue, ihm noch Unbekannte, das ihm entgegentritt."
      ],
      [
        "Er wird so vorsichtig wie irgend möglich sein mit dem Ur­teil: «das ist unmöglich», «das kann ja gar nicht sein».",
        "Mag ihm seine Meinung nach den bisherigen Erfahrungen was immer sagen: er ist in jedem Augenblick bereit, sich von etwas Neuem, das ihm entgegenkommt, zu einer ande­ren Meinung bringen zu lassen."
      ],
      [
        "Jede Eigenliebe der Mei­nung gegenüber muß schwinden. - Wenn die bisher genannten fünf Eigenschaften von der Seele erworben sind, dann stellt sich eine sechste ganz von selbst ein: das innere Gleichgewicht, die Harmonie der geistigen Kräfte.",
        "Der Mensch muß etwas in sich finden wie einen geistigen Schwerpunkt, der ihm Festigkeit und Sicherheit gibt ge­genüber allem, was im Leben da- oder dorthin zieht."
      ],
      [
        "muß nicht etwa vermeiden, mit allem mitzuleben, alles auf sich wirken zu lassen.",
        "Nicht die Flucht vor den hin- und widerziehenden Tatsachen des Lebens ist das Richtige, son­dern im Gegenteil: das volle Hingeben an das Leben und trotzdem die sichere, feste Bewahrung von innerem Gleich­gewicht und Harmonie."
      ],
      [
        "Endlich kommt für den Suchenden der «Wille zur Frei­heit» in Betracht.",
        "Es hat ihn jemand, der zu allem, was er vollbringt, die Stütze und Grundlage in sich selbst findet.",
        "Er ist deshalb so schwer zu erringen, weil taktvoll der Aus­gleich notwendig ist zwischen dem Öffnen des Sinnes ge­genüber allem Großen und Guten und der gleichzeitigen Ablehnung eines jeglichen Zwanges.",
        "Man sagt so leicht: Einwirkung von außen und Freiheit vertragen sich nicht.",
        "Daß sie sich in der Seele vertragen: darauf kommt es aber gerade an.",
        "Wenn mir jemand etwas mitteilt, und ich nehme es unter dem Zwange seiner Autorität an: dann bin ich un­frei.",
        "Aber ich bin nicht minder unfrei, wenn ich mich ver­schließe vor dem Guten, das ich auf diese Art empfangen kann.",
        "Denn dann übt in der eigenen Seele das Schlechtere, das ich habe, auf mich einen Zwang aus.",
        "Und bei der Frei­heit kommt es nicht allein darauf an, daß ich nicht unter dem Zwange einer äußeren Autorität stehe, sondern vor allen Dingen auch nicht unter derjenigen eigener Vorur­teile, Meinungen, Empfindungen und Gefühle.",
        "Nicht blin­de Unterwerfung unter das Empfangene ist das Richtige, sondern sich von ihm anregen lassen, es ganz unbefangen aufnehmen, um sich «frei» dazu zu bekennen.",
        "Eine fremde Autorität soll nicht anders als so wirken, daß man sich sagt: Ich mache mich gerade dadurch frei, daß ich ihrem Guten folge, das heißt, es zu dem meinigen mache."
      ],
      [
        "eine auf der Geheimwissenschaft fußende Autorität will auch gar nicht anders als in dieser Art wirken.",
        "Sie gibt, was sie zu geben hat, nicht um selbst Macht über den Beschenk­ten zu gewinnen, sondern allein darum, daß der Beschenkte durch die Gabe reicher und freier werde."
      ],
      [
        "Es ist auf die Bedeutung der angeführten Eigenschaften schon früher bei Besprechung der «Lotusblumen » hinge­wiesen worden.",
        "Dort wurde gezeigt, welche Beziehung sie zu der Entwickelung der zwölfblätterigen Lotusblume in der Herzgegend und der daran sich schließenden Strömun­gen des Ätherkörpers haben.",
        "Aus dem jetzt Gesagten ist ersichtlich, daß sie im wesentlichen die Aufgabe haben, dem physischen Körper des Suchenden jene Kräfte entbehr­lich zu machen, die ihm sonst während des Schlafzustandes zugute kommen und die ihm wegen der Ausbildung entzo­gen werden müssen.",
        "Unter solchen Einwirkungen entwickelt sich die imaginative Erkenntnis."
      ]
    ]
  },
  {
    "order": 5,
    "title_de": "DIE IMAGINATION",
    "paragraphs": [
      "Es ist ganz unmöglich, wirkliche Fortschritte in bezug auf das Vordringen in höhere Welten zu machen, ohne durch die Stufen der imaginativen Erkenntnis hindurchzugehen. Damit soll allerdings nicht gesagt sein, daß bei der Geheimschulung der Mensch eine gewisse Zeit hindurch auf dieser Stufe der Imagination unbedingt stehenbleiben müsse, so daß diese so etwas wie eine Schulklasse bilden müsse, die man abzusitzen hat. Es kann dies in gewissen Fällen notwendig sein, muß es aber durchaus nicht. Das hängt ganz davon ab, was der Geheimschüler erlebt hat, bevor er in die Geheimschulung eintritt. Es wird sich im weiteren Verlaufe dieser Auseinandersetzungen zeigen, daß in bezug darauf die geistige Umgebung des Geheimschülers von Bedeutung ist und daß sich auf das Verhältnis zur geistigen Umgebung sogar ganz verschiedene Methoden des «Erkenntnispfades» begründen.",
      "Es kann von außerordentlicher Wichtigkeit sein, das Folgende zu wissen, wenn man sich auf den Weg der Geheimschulung begibt. Nicht nur als eine interessante Theorie kommt es in Betracht, sondern als etwas, dem man die man­nigfaltigsten praktischen Gesichtspunkte wird entnehmen können, wenn man auf dem «Wege zur höheren Erkennt­nis » wirklich bestehen will.",
      "Man hört ja von solchen, welche eine höhere Entwicke­lung anstreben, oft sagen: Ich möchte mich geistig vervoll­kommnen, ich möchte «den höheren Menschen» in mir ausbilden, aber nach den Erscheinungen der «astralen Welt »trage ich kein Verlangen. Dies ist begreiflich, wenn man in Betracht zieht, welche Schilderung von dieser «astralen",
      "Welt» sich in Büchern findet, die von diesen Dingen Handeln. Da wird ja von Erscheinungen und Wesenheiten ge­sprochen, welche dem Menschen alle möglichen Gefahren bringen. Da wird gesagt, daß unter dem Einflusse solcher Wesenheiten der Mensch nur gar zu leicht an seiner morali­schen Gesinnung und intellektuellen Gesundheit Schaden nehmen könne.",
      "Es wird dem Leser nahegebracht, daß auf diesem Gebiete die Scheidewand zwischen «dem guten und dem bösen Pfade» einem «Spinnewebchen» an Dicke gleichkomme und der Fall in unermeßliche Abgründe, der Ab­sturz in völlige Verworfenheit nur allzu naheliege. - Es ist ganz gewiß unmöglich, solchen Behauptungen einfach zu widersprechen. Und doch ist der Standpunkt, den man in vielen Fällen dem Betreten des Geheimpfades gegenüber einnimmt, keineswegs ein richtiger.",
      "Der einzig mögliche Gesichtspunkt ist vielmehr lediglich derjenige, welcher sagt: wegen der Gefahren darf niemand abgehalten wer­den, den Weg zur höheren Erkenntnis zu gehen, aber es muß in jedem Falle streng dafür gesorgt werden, daß diese Gefahren bestanden werden können. Das wird in manchen Fällen allerdings dazu führen, daß einem Menschen, der von einem Geheimlehrer Anweisungen zur Schulung erbit­tet, zunächst der Rat gegeben wird, mit dieser eigentlichen Schulung noch zu warten und erst gewisse Erfahrungen des gewöhnlichen Lebens durchzumachen oder Dinge zu ler­nen, welche in der physischen Welt gelernt werden können.",
      "Es wird dann die Aufgabe des Geheimlehrers sein, dem su­chenden Menschen die rechte Anleitung zu geben, um sol­che Erfahrungen zu sammeln und solche Dinge zu lernen. In weitaus den meisten Fällen wird man es erleben, daß der Geheimlehrer zunächst so verfährt.",
      "Wenn dann der Schü­ler",
      "nur genügend aufmerksam ist auf das, was ihm nun zu­stößt, nachdem er mit dem Geheimlehrer in Verbindung getreten ist, dann wird er das Mannigfaltigste bemerken können. Er wird finden, daß er nunmehr wie durch «Zufall» Erlebnisse hat und Dinge beobachten kann, denen er ganz gewiß ohne die Verbindung mit dem Geheimlehrer nicht ausgesetzt gewesen wäre. Wenn die Schüler das oft nicht bemerken und ungeduldig werden, dann liegt das nur darin, daß sie eben nicht die nötige Aufmerksamkeit ihren Erlebnissen zuwenden. Man muß auch durchaus nicht glauben, daß sich die Wirkung des Geheimlehrers auf den Schüler in deutlich wahrnehmbaren «Zauberkunststück­chen» abspielt. Diese Wirkung ist vielmehr eine ganz inti­me Sache, und wer nach ihrer Natur und Wesenheit for­schen will, ohne selbst schon eine gewisse Stufe der Ge­heimschulung erreicht zu haben, der wird ganz gewiß in die Irre gehen. Der Schüler fügt sich selbst in jedem Falle ein Unrecht zu, wenn er ungeduldig darüber wird, daß er auf «Wartezeit» gesetzt ist. Er wird dadurch in bezug auf die Schnelligkeit seines Weges durchaus nicht aufgehalten. Im Gegenteil, sein Vorwärtskommen würde gerade dadurch verlangsamt, wenn er zu früh mit der oft von ihm ungeduldig erwarteten Schulung beginnen würde.",
      "Läßt der Schüler die «Wartezeit» oder die sonstigen Ratschläge und Winke des Geheimlehrers in der richtigen Art auf sich wirken, so bereitet er sich tatsächlich dazu vor, ge­wissen Prüfungen und Gefahren standzuhalten, die an ihn herankommen, wenn er der für ihn unvermeidlichen Stufe der Imagination entgegentritt. - Unvermeidlich ist diese Stufe aus dem Grunde, weil jeder, der eine Verbindung mit der höheren Welt ohne ihr Durchschreiten sucht, dies nur",
      "unbewußt tun kann und dazu verurteilt ist, im Dunkeln zu tappen. Man kann sich ein dunkles Gefühl von dieser hö­heren Welt ohne die Imagination erwerben, man kann ohne sie gewiß zur Empfindung kommen, daß man mit «seinem Gotte» oder mit «seinem höheren Selbst» vereinigt sei, aber zu einer wirklichen Erkenntnis mit vollem Bewußt­sein in heller, lichter Klarheit kann man so nicht kommen. Deshalb ist auch alles Reden davon, daß man die Auseinan­dersetzungen mit den «niederen Welten» (der astralen und der devachanischen) nicht brauche, daß es sich nur darum handeln könne, daß der Mensch «den Gott in sich erwec­ke», nichts weiter als eine Illusion. - Wer damit zufrieden ist, dem soll in sein Streben nicht hineingeredet werden, und der Okkultist wird einem solchen auch nicht hineinre­den. Aber der wahre Okkultismus hat mit solchem Streben gar nichts zu tun. Dieser fordert ja niemanden zur Schülerschaft unmittelbar auf. Wer aber seine Schulung sucht, dem will er nicht bloß eine dunkle Empfindung von seiner «Gottähnlichkeit» erwecken, sondern er sucht ihm die gei­stigen Augen zu öffnen für das, was in höheren Welten wirklich vorhanden ist.",
      "Gewiß ist ja in jedem Menschen das «göttliche Selbst »enthalten. Aber das ist ja doch in jedem Wesen der Fall. Im Stein, in der Pflanze, im Tier ist auch das «göttliche Selbst» enthalten und wirksam. Aber nicht darauf kann es ankom­men, dies so ganz im allgemeinen zu fühlen und zu wissen, sondern darauf, wirklich in Verbindung zu treten mit den Offenbarungen dieses «göttlichen Selbstes» So wie derjenige nichts von der physischen Welt weiß, der sich nur immer wieder sagen kann: diese Welt enthält in sich verhüllt das «göttliche Selbst», so weiß auch derjenige nichts von hö­heren",
      "Welten, welcher das «göttliche Geisterreich» nur in verschwommener, unbestimmter Allgemeinheit sucht. Man soll seine Augen öffnen und die Offenbarung der Gottheit in den Dingen der physischen Welt, im Stein, in der Pflanze anschauen, nicht davon träumen, daß dies jedoch alles nur «Erscheinungen» seien und daß Gottes wahre Gestalt dahinter «verborgen» sei. Nein, Gott offenbart sich in seinen Schöpfungen, und wer Gott erkennen will, muß das We­sen dieser Schöpfungen erkennen lernen. Deshalb muß man auch das wirklich anschauen lernen, was in höheren Welten vorgeht und lebt, wenn man das «Göttliche» erkennen will. Das Bewußtsein, daß der «Gottmensch» in einem lebt, kann höchstens den Anfang bilden. Aber dieser An­fang wird, wenn er in rechter Weise erlebt wird, zum An­trieb, wirklich aufzusteigen in die höheren Welten. Das kann man aber nur, wenn man die geistigen «Sinne» dazu in sich ausbildet. Alles andere stellt sich ja doch nur auf den Standpunkt: Ich will bleiben, wie ich bin, und nur errei­chen, was mir so zu erreichen möglich ist. Der Standpunkt des Okkultismus ist aber, ein anderer Mensch zu werden, damit man anderes als das Gewöhnliche schauen und erle­ben kann.",
      "Und dazu ist eben der Durchgang durch die imaginative Erkenntnis notwendig. Es ist gesagt worden, daß diese Stufe der Imagination nicht aufgefaßt zu werden braucht wie eine Schulklasse, die man durchaus «absitzen» müsse. Das ist so zu verstehen, daß es namentlich in unsrem ge­genwärtigen Leben Personen gibt, welche solche Vorbe­dingungen mitbringen, daß der Geheimlehrer bei ihnen gleichzeitig oder wenigstens fast gleichzeitig mit der ima­ginativen Erkenntnis die inspirierte und die intuitive hervorrufen",
      "kann. Aber es darf durchaus nicht so verstanden werden, als ob es irgend jemand geben könnte, dem der Durchgang durch die Imagination zu ersparen wäre.",
      "Auf den Grund der Gefahr innerhalb der imaginativen Erkenntnis ist ja in meiner Schrift «Wie erlangt man Er­kenntnisse der höheren Welten?» bereits hingedeutet wor­den. Dieser Grund liegt darin, daß der Mensch beim Ein­tritte in diese Welt gewissermaßen den Boden unter den Füßen verliert. Wodurch er in der physischen Welt Festig­keit hat, das geht ihm zunächst scheinbar ganz verloren. Nimmt man in dieser physischen Welt etwas wahr, so fragt man sich : Woher kommt diese Wahrnehmung? Man tut das ja zumeist unbewußt. Aber man ist sich eben «unbewußt» darüber klar, daß die Ursachen der Wahrnehmungen die Gegenstände «draußen im Raume» sind. Die Farben, die Töne, die Gerüche gehen von diesen Gegenständen aus. Man sieht nicht freischwebende Farben, man hört nicht Tö­ne, ohne daß man sich bewußt werden könnte, an welchen Gegenständen diese Farben als Eigenschaften «haften», von welchen Gegenständen die Töne herrühren. Dieses Be­wußtsein, daß die Gegenstände und Wesenheiten sie verur­sachen, gibt den physischen Wahrnehmungen und damit dem Menschen selbst Festigkeit und einen sicheren Halt. Hat jemand Wahrnehmungen ohne äußere Ursache, so spricht man von abnormen, krankhaften Zuständen. Man nennt solche ursachlose Wahrnehmungen Illusionen, Hal­luzinationen, Visionen.",
      "Nun zunächst ganz äußerlich betrachtet besteht die ganze imaginative Welt aus solchen Halluzinationen, Visionen und Illusionen. Es ist gezeigt worden in «Wie erlangt man Er­kenntnisse der höheren Welten?», wie durch die Geheimschulung",
      "künstlich solche Visionen usw. erzeugt werden. Durch das Hinlenken des Bewußtseins auf ein Samenkorn oder auf eine absterbende Pflanze werden gewisse Gestal­ten vor die Seele gezaubert, die nichts weiter zunächst sind als Halluzinationen.",
      "Die «Flammenbildung», von der dort gesagt wurde, daß sie in der Seele auftreten kann durch die Betrachtung einer Pflanze oder dergleichen und die sich nach einer Zeit ganz loslöst von der Pflanze, ist, äußerlich betrachtet, einer Halluzination gleich zu achten. Und so geht es noch weiter in der Geheimschulung, wenn man in die imaginative Welt eintritt.",
      "Das, wovon man gewöhnt war, daß es von den Dingen «draußen im Raum» ausgeht oder ihnen als Eigenschaft «anhaftet», die Farben, Töne, Gerüche usw., erfüllen nun freischwebend den Raum. Die Wahrnehmungen lösen sich los von allen äußeren Dingen und schweben frei im Raume oder fliegen darinnen herum.",
      "Und man weiß dabei doch ganz genau, daß die Dinge, die man da vor sich hat, diese Wahrnehmungen nicht hervor­gebracht haben, daß man sie vielmehr «selbst» verursacht hat. So kommt es, daß man meinen muß, man habe den «Boden unter den Füßen verloren».",
      "Im gewöhnlichen Leben in der physischen Welt muß man sich ja gerade davor hüten, Vorstellungen zu haben, die nicht von den Dingen her­rühren, die sozusagen «ohne Grund und Boden» sind. Zur Hervorrufung der imaginativen Erkenntnis aber kommt es gerade darauf an, zunächst Farben, Töne, Gerüche usw. zu haben, die ganz losgelöst von allen Dingen «frei im Raume schweben».",
      "Nun muß die nächste Stufe der imaginativen Erkenntnis darin bestehen, einen neuen «Grund und Boden» für die herrenlos gewordenen Vorstellungen zu finden. Das muß",
      "eben in der anderen Welt geschehen, die sich jetzt offenba­ren soll. Es bemächtigen sich neue Dinge und Wesenheiten dieser Vorstellungen. In der physischen Welt «haftet» zum Beispiel die blaue Farbe an einer Kornblume. In der imagi­nativen Welt darf sie nun auch nicht «freischwebend» blei­ben. Sie strömt gleichsam zu einer Wesenheit hin, und wäh­rend sie noch vorher herrenlos war, wird sie jetzt der Ausdruck einer Wesenheit. Es spricht etwas durch sie zu dem Beobachter, was dieser eben nur innerhalb der imaginati­ven Welt wahrnehmen kann. Und so sammeln sich die «freischwebenden» Vorstellungen um bestimmte Mittel­punkte. Und man wird gewahr, daß Wesen durch sie zu uns sprechen. Und wie es in der physischen Welt körperliche Dinge und Wesenheiten sind, an denen Farben, Gerüche und Töne usw. «haften» oder von denen sie herstammen, so sprechen sich jetzt «geistige Wesenheiten» durch sie aus. Diese «geistigen Wesenheiten» sind ja tatsächlich im­mer da; sie umschwirren den Menschen beständig. Aber sie können sich diesem nicht offenbaren, wenn er nicht die Ge­legenheit dazu gibt. Und diese Gelegenheit gibt er nur da­durch, daß er in sich die Fähigkeit hervorruft, Töne, Far­ben usw. auch dann vor seiner Seele entstehen zu lassen, wenn diese durch keinen physischen Gegenstand veran­laßt werden.",
      "Ganz anders sind die «geistigen Tatsachen und Wesen­heiten » als die Dinge und Wesen der physischen Welt. Es ist nicht ganz leicht, in der gewöhnlichen Sprache einen Ausdruck zu finden, welcher die Verschiedenheit auch nur annähernd charakterisiert. Vielleicht kommt man der Sache am nächsten, wenn man sagt: in der imaginativen Welt spricht alles so zum Menschen, wie wenn es unmittelbar intelligent",
      "wäre, während in der physischen Welt auch die In­telligenz nur auf dem Umwege durch die physische Kör­perlichkeit sich offenbaren kann. Das macht eben die Be­weglichkeit und Freiheit der imaginativen Welt aus, daß das Zwischenglied der äußeren Dinge fehlt, daß das Gei­stige ganz unmittelbar in den freischwebenden Tönen, Far­ben usw. sich auslebt.",
      "Nun liegt der Grund zu einer Gefahr, welche dem Men­schen von dieser Welt droht, darin, daß er die Äußerungen der «geistigen Wesen» wahrnimmt, aber nicht diese Wesen selbst. Es ist das nämlich so lange der Fall, als er nur in der imaginativen Welt bleibt und zu keiner höheren aufsteigt. Erst die Inspiration und die Intuition führen ihn allmählich zu diesen Wesen selbst hin. - Wollte aber der Geheimlehrer diese letzteren vorschnell erwecken, ohne den Schüler gründlich in das imaginative Gebiet einzuführen, dann wür­de die höhere Welt nur ein schatten- und schemenhaftes Dasein erhalten. Die ganze herrliche Fülle der Bilder ginge verloren, in denen sie sich offenbaren muß, wenn man wirklich in sie eintreten soll. - In dieser Tatsache liegt der Grund, warum der Geheimschüler einen «Führer» oder ei­nen «Guru» braucht, wie man in der Geheimwissenschaft eben diesen Führer nennt.",
      "Für den Schüler ist nämlich die imaginative Welt anfangs wirklich eine bloße «Bilderwelt», von der er vielfach nicht weiß, was sie ausdrückt. Der Geheimlehrer aber weiß, auf welche Dinge und Wesenheiten sich diese Bilder in einer noch höheren Welt beziehen. Hat der Schüler zu ihm Ver­trauen, so kann er wissen, daß sich ihm später Zusammen­hänge offenbaren werden, welche er vorläufig noch nicht durchschaut. In der physischen Welt waren die Gegenstände",
      "im Raume selbst die Führer. Er war imstande, die Rich­tigkeit seiner Vorstellungen zu prüfen. Die körperliche Wirklichkeit ist der «Fels», an dem alle Halluzinationen und Illusionen zerschellen müssen. Dieser Fels verschwin­det in einen Abgrund, wenn man in die imaginative Welt eintritt. Und deshalb muß als ein anderer solcher «Fels» der «Führer» eintreten. An dem, was er dem Schüler zu bieten vermag, muß dieser die Wirklichkeit der neuen Welt empfinden. Man kann daraus ermessen, wie groß das Ver­trauen in den Führer sein muß in jeder Geheimschulung, welche dieses Namens wirklich wert ist. Sobald man an den Führer nicht mehr glauben kann, ist es ja in dieser höheren Welt so, wie wenn einem in der physischen plötzlich alles genommen würde, worauf man den Glauben an die Wirk­lichkeit seiner Wahrnehmungen gebaut hat.",
      "Außer dieser einen Tatsache gibt es nun noch eine ande­re, durch welche der Mensch in Verwirrung gesetzt werden könnte, wenn er sich ohne Führung in die imaginative Welt begeben wollte. Es lernt nämlich der Geheimschüler von allen geistigen Wesenheiten in erster Linie sich selbst ken­nen. In dem physischen Leben hat der Mensch Gefühle, Be­gierden, Wünsche, Leidenschaften, Vorstellungen usw. Zwar werden diese alle von den Dingen und Wesenheiten der äußeren Welt veranlaßt, aber der Mensch weiß ganz ge­nau, daß sie seine innere Welt bilden, und er unterscheidet sie als das, was in seiner Seele vorgeht, von den Gegenstän­den der Außenwelt. Sobald aber der imaginative Sinn er­weckt ist, hört diese Leichtigkeit des Unterscheidens ganz auf. Seine eigenen Gefühle, Vorstellungen, Leidenschaften usw. treten buchstäblich aus ihm heraus, nehmen Gestalt, Farbe und Ton an. Er steht ihnen jetzt so gegenüber wie in",
      "der physischen Welt ganz fremden Gegenständen und We­senheiten. Und daß die Verwirrung eine vollständige wer­den kann, wird man begreifen, wenn man sich an das erin­nert, was in dem Kapitel «Über einige Wirkungen der Ein­weihung» in «Wie erlangt man Erkenntnisse der höheren Welten?» gesagt worden ist.",
      "Dort ist ja nichts anderes ge­schildert als die Art, wie die imaginative Welt für den Beob­achter auftritt. Es erscheint nämlich in ihr alles umgekehrt, wie im Spiegelbilde. Was vom Menschen ausströmt, er­scheint so, als wenn es von außen an ihn herankommen wollte.",
      "Ein Wunsch, den er hegt, verwandelt sich in eine Gestalt, beispielsweise in die Form eines phantastisch ausse­henden Tieres, oder auch wohl eines menschenähnlichen Wesens. Dieses scheint ihn zu bestürmen, einen Angriff auf ihn auszuführen oder ihn auch zu veranlassen, dieses oder jenes zu tun.",
      "So kann es kommen, daß der Mensch sich vor­kommt als umgeben und umflattert von einer ganz phan­tastischen, oft reizvollen und verführerischen, oft auch grausigen Welt. In Wahrheit stellt diese nichts anderes vor als seine eigenen Gedanken, Wünsche und Leidenschaften, welche in Bilder verwandelt sind. - Man würde sich einem großen Irrtum hingeben, wenn man glauben wollte, daß die Unterscheidung dieses in Bildern verwandelten Selb­stes von der wirklichen geistigen Welt leicht sei.",
      "Zunächst ist es für den Schüler geradezu unmöglich, diese Unter­scheidung wirklich zu vollziehen. Denn es kann genau das­selbe Bild ebensogut von einem geistigen Wesen herrühren, welches zu den Menschen spricht, wie von irgend etwas im Innern der Seele.",
      "Und übereilt der Mensch gerade dabei et­was, so setzt er sich der Gefahr aus, daß er die beiden Dinge nie ordentlich voneinander zu trennen lernt. Die größte",
      "Vorsicht ist dabei geboten. - Nur noch größer wird die Verwirrung dadurch, daß die eigenen Wünsche und Begierden der Seele sich in Bilder kleiden, die genau den ent­gegengesetzten Charakter von dem tragen, was sie wirk­lich sind. Man nehme zum Beispiel an, die Eitelkeit kleide sich auf diese Art in ein Bild.",
      "Sie kann auftreten als eine liebreizende Gestalt, welche die wunderbarsten Dinge ver­spricht, wenn man ausführt, was sie angibt. Diese ihre An­gaben scheinen etwas durchaus Gutes, Erstrebenswertes in Aussicht zu stellen; folgt man ihnen, so stürzt man sich in sein moralisches oder sonstiges Verderben.",
      "Umgekehrt kann sich eine gute Eigenschaft der Seele in ein unsympa­thisches Kleid hüllen. Nur dem wirklichen Kenner ist es möglich, da zu unterscheiden, und nur eine Persönlichkeit, die gar nicht wankend gemacht werden kann in bezug auf ein richtiges Ziel, ist sicher gegenüber den Verführungs­künsten der eigenen Seelenbilder. - Man wird in Anbe­tracht von alledem zugeben, wie notwendig die Führung eines Lehrers ist, der mit sicherem Sinn den Schüler auf­merksam macht, was auf diesem Gebiet Trugbild und was Wahrheit ist.",
      "Nicht zu glauben aber braucht man, daß die­ser Lehrer immer hinter dem Schüler stehen muß. Das räumliche Beisammensein mit dem Lehrer ist es durchaus nicht, worauf es beim Geheimschüler immer ankommt. Gewiß gibt es Augenblicke, wo ein solches räumliches Bei­sammensein wünschenswert, und auch solche, wo es durch­aus notwendig ist.",
      "Aber anderseits findet der Geheimlehrer auch die Mittel, um mit dem Schüler in Verbindung zu bleiben, auch bei räumlicher Entfernung. Und zudem kommt in Betracht, daß manches, was zwischen Lehrer und Schüler auf diesem Gebiete bei einem Beisammensein vorgeht,",
      "oftmals monate-, vielleicht jahrelang nachwirken kann. Eines aber gibt es, was sicher den notwendigen Zusammenhang zwischen Lehrer und Schüler zerreißen muß. Das tritt dann ein, wenn der letztere das Vertrauen zu dem ersteren verliert. - Und besonders schlimm ist es, wenn dieses Vertrauensband sich löst, ehe der Schüler unter­scheiden gelernt hat die Vorspiegelungen der eigenen Seele von der wahren Wirklichkeit.",
      "Nun könnte man vielleicht sagen : ja, wenn auf diese Art ein solches Gebundensein an den Lehrer eintritt, so ver­liert ja der Geheimschüler alle Freiheit und Selbständig­keit. Er gibt sich sozusagen dem Lehrer ganz in die Hand. Doch gerade dies ist in Wahrheit gar nicht der Fall. Allerdings gibt es Unterschiede in bezug auf die Abhängigkeit vom Lehrer in den verschiedenen Methoden der okkulten Schulung. Diese Abhängigkeit kann eine größere oder ge­ringere sein müssen. Sie ist die verhältnismäßig größte bei derjenigen Methode, welche von den Okkultisten des Orients befolgt wurde und von diesen auch heute noch als die ihrige gelehrt wird. In viel geringerem Maße ist diese Abhängigkeit von einem Menschen schon bei der soge­nannten christlichen Einweihung vorhanden. Und eigent­lich völlig in Wegfall kommt sie bei demjenigen Erkennt­nispfade, der seit dem vierzehnten Jahrhunderte von den sogenannten Geheimschulen der Rosenkreuzer angegeben wird. Bei diesem kann zwar nicht der Lehrer wegfallen, denn das ist unmöglich. Aber es hört wahrhaft jede Ab­hängigkeit von ihm auf. Wie das möglich ist, wird aus der Fortsetzung dieser Darstellung zu ersehen sein. Darinnen wird nämlich genau geschildert werden, wodurch sich diese drei «Erkenntnispfade» unterscheiden: der orientalische,",
      "der christliche und der rosenkreuzerische. Bei dem letzteren kommt nämlich gar nichts in Betracht, was einen modernen Menschen irgendwie in seinem Freiheitsgefühl stören könn­te. Auch wird in dieser Fortsetzung geschildert werden, wie die eine oder die andere Person als Geheimschüler dazu kommen kann, auch gegenwärtig, im modernen Europa, nicht den rosenkreuzerischen Weg zu gehen, sondern den orientalischen oder den älteren christlichen, obgleich der rosenkreuzerische gegenwärtig der natürlichste ist. Dieser ist, wie man im weiteren Verlaufe sehen wird. nicht etwa unchristlich. Es kann ihn ein Mensch gehen, ohne sein Christentum zu gefährden, und es kann ihn auch ein Mensch gehen, der auf der vollen Höhe moderner wissenschaftlicher Weltanschauung zu stehen vermeint.",
      "Ein anderes könnte aber vielleicht noch der Erklärung bedürfen. Man könnte sich versucht fühlen zu fragen, ob denn nicht dem Geheimschüler erspart bleiben könnte, durch die Vorspiegelungen seiner eigenen Seele hindurch­zugehen. Geschähe das, so würde er eben nie zu der für ihn so wünschenswerten selbständigen Unterscheidung kom­men. Denn durch nichts kann die ganz eigenartige Natur der imaginativen Welt anschaulicher werden als durch die Betrachtung der eigenen Seele. Der Mensch kennt ja das Innenleben seiner Seele zunächst von der einen Seite. Er steckt eben darinnen. Und das muß ja der Geheimschüler gerade lernen: die Dinge nicht nur von außen anzuschauen, sondern sie so zu beobachten, als ob er in ihnen allen darinnensteckte. Tritt ihm nun seine eigene Gedankenwelt so wie etwas Fremdes entgegen, dann lernt er eben dadurch ein Ding, das er schon von einer Seite her kennt, auch noch von der anderen Seite kennen. Er muß gewissermaßen",
      "sich selbst das erste Beispiel einer solchen Erkennt­nis werden. Von der physischen Welt her ist er ja an etwas ganz anderes gewöhnt. Da erblickt er alle anderen Dinge immer nur von außen, sich selbst aber erlebt er nur vom Innern. Er kann, solange er in der physischen Welt ver­bleibt, nie hinter die Oberfläche der Dinge hineinsehen. Und er kann niemals aus sich herausgehen, gleichsam «aus seiner eigenen Haut fahren», um sich von außen zu beob­achten. Das letztere obliegt ihm buchstäblich bei der Ge­heimschulung zuerst, und mit Hilfe dessen lernt er dann, auch äußeren Tatsachen und Wesenheiten hinter die Ober­fläche zu schauen."
    ],
    "sentences": [
      [
        "Es ist ganz unmöglich, wirkliche Fortschritte in bezug auf das Vordringen in höhere Welten zu machen, ohne durch die Stufen der imaginativen Erkenntnis hindurchzugehen.",
        "Damit soll allerdings nicht gesagt sein, daß bei der Geheimschulung der Mensch eine gewisse Zeit hindurch auf dieser Stufe der Imagination unbedingt stehenbleiben müsse, so daß diese so etwas wie eine Schulklasse bilden müsse, die man abzusitzen hat.",
        "Es kann dies in gewissen Fällen notwendig sein, muß es aber durchaus nicht.",
        "Das hängt ganz davon ab, was der Geheimschüler erlebt hat, bevor er in die Geheimschulung eintritt.",
        "Es wird sich im weiteren Verlaufe dieser Auseinandersetzungen zeigen, daß in bezug darauf die geistige Umgebung des Geheimschülers von Bedeutung ist und daß sich auf das Verhältnis zur geistigen Umgebung sogar ganz verschiedene Methoden des «Erkenntnispfades» begründen."
      ],
      [
        "Es kann von außerordentlicher Wichtigkeit sein, das Folgende zu wissen, wenn man sich auf den Weg der Geheimschulung begibt.",
        "Nicht nur als eine interessante Theorie kommt es in Betracht, sondern als etwas, dem man die man­nigfaltigsten praktischen Gesichtspunkte wird entnehmen können, wenn man auf dem «Wege zur höheren Erkennt­nis » wirklich bestehen will."
      ],
      [
        "Man hört ja von solchen, welche eine höhere Entwicke­lung anstreben, oft sagen: Ich möchte mich geistig vervoll­kommnen, ich möchte «den höheren Menschen» in mir ausbilden, aber nach den Erscheinungen der «astralen Welt »trage ich kein Verlangen.",
        "Dies ist begreiflich, wenn man in Betracht zieht, welche Schilderung von dieser «astralen"
      ],
      [
        "Welt» sich in Büchern findet, die von diesen Dingen Handeln.",
        "Da wird ja von Erscheinungen und Wesenheiten ge­sprochen, welche dem Menschen alle möglichen Gefahren bringen.",
        "Da wird gesagt, daß unter dem Einflusse solcher Wesenheiten der Mensch nur gar zu leicht an seiner morali­schen Gesinnung und intellektuellen Gesundheit Schaden nehmen könne."
      ],
      [
        "Es wird dem Leser nahegebracht, daß auf diesem Gebiete die Scheidewand zwischen «dem guten und dem bösen Pfade» einem «Spinnewebchen» an Dicke gleichkomme und der Fall in unermeßliche Abgründe, der Ab­sturz in völlige Verworfenheit nur allzu naheliege. - Es ist ganz gewiß unmöglich, solchen Behauptungen einfach zu widersprechen.",
        "Und doch ist der Standpunkt, den man in vielen Fällen dem Betreten des Geheimpfades gegenüber einnimmt, keineswegs ein richtiger."
      ],
      [
        "Der einzig mögliche Gesichtspunkt ist vielmehr lediglich derjenige, welcher sagt: wegen der Gefahren darf niemand abgehalten wer­den, den Weg zur höheren Erkenntnis zu gehen, aber es muß in jedem Falle streng dafür gesorgt werden, daß diese Gefahren bestanden werden können.",
        "Das wird in manchen Fällen allerdings dazu führen, daß einem Menschen, der von einem Geheimlehrer Anweisungen zur Schulung erbit­tet, zunächst der Rat gegeben wird, mit dieser eigentlichen Schulung noch zu warten und erst gewisse Erfahrungen des gewöhnlichen Lebens durchzumachen oder Dinge zu ler­nen, welche in der physischen Welt gelernt werden können."
      ],
      [
        "Es wird dann die Aufgabe des Geheimlehrers sein, dem su­chenden Menschen die rechte Anleitung zu geben, um sol­che Erfahrungen zu sammeln und solche Dinge zu lernen.",
        "In weitaus den meisten Fällen wird man es erleben, daß der Geheimlehrer zunächst so verfährt."
      ],
      [
        "Wenn dann der Schü­ler"
      ],
      [
        "nur genügend aufmerksam ist auf das, was ihm nun zu­stößt, nachdem er mit dem Geheimlehrer in Verbindung getreten ist, dann wird er das Mannigfaltigste bemerken können.",
        "Er wird finden, daß er nunmehr wie durch «Zufall» Erlebnisse hat und Dinge beobachten kann, denen er ganz gewiß ohne die Verbindung mit dem Geheimlehrer nicht ausgesetzt gewesen wäre.",
        "Wenn die Schüler das oft nicht bemerken und ungeduldig werden, dann liegt das nur darin, daß sie eben nicht die nötige Aufmerksamkeit ihren Erlebnissen zuwenden.",
        "Man muß auch durchaus nicht glauben, daß sich die Wirkung des Geheimlehrers auf den Schüler in deutlich wahrnehmbaren «Zauberkunststück­chen» abspielt.",
        "Diese Wirkung ist vielmehr eine ganz inti­me Sache, und wer nach ihrer Natur und Wesenheit for­schen will, ohne selbst schon eine gewisse Stufe der Ge­heimschulung erreicht zu haben, der wird ganz gewiß in die Irre gehen.",
        "Der Schüler fügt sich selbst in jedem Falle ein Unrecht zu, wenn er ungeduldig darüber wird, daß er auf «Wartezeit» gesetzt ist.",
        "Er wird dadurch in bezug auf die Schnelligkeit seines Weges durchaus nicht aufgehalten.",
        "Im Gegenteil, sein Vorwärtskommen würde gerade dadurch verlangsamt, wenn er zu früh mit der oft von ihm ungeduldig erwarteten Schulung beginnen würde."
      ],
      [
        "Läßt der Schüler die «Wartezeit» oder die sonstigen Ratschläge und Winke des Geheimlehrers in der richtigen Art auf sich wirken, so bereitet er sich tatsächlich dazu vor, ge­wissen Prüfungen und Gefahren standzuhalten, die an ihn herankommen, wenn er der für ihn unvermeidlichen Stufe der Imagination entgegentritt. - Unvermeidlich ist diese Stufe aus dem Grunde, weil jeder, der eine Verbindung mit der höheren Welt ohne ihr Durchschreiten sucht, dies nur"
      ],
      [
        "unbewußt tun kann und dazu verurteilt ist, im Dunkeln zu tappen.",
        "Man kann sich ein dunkles Gefühl von dieser hö­heren Welt ohne die Imagination erwerben, man kann ohne sie gewiß zur Empfindung kommen, daß man mit «seinem Gotte» oder mit «seinem höheren Selbst» vereinigt sei, aber zu einer wirklichen Erkenntnis mit vollem Bewußt­sein in heller, lichter Klarheit kann man so nicht kommen.",
        "Deshalb ist auch alles Reden davon, daß man die Auseinan­dersetzungen mit den «niederen Welten» (der astralen und der devachanischen) nicht brauche, daß es sich nur darum handeln könne, daß der Mensch «den Gott in sich erwec­ke», nichts weiter als eine Illusion. - Wer damit zufrieden ist, dem soll in sein Streben nicht hineingeredet werden, und der Okkultist wird einem solchen auch nicht hineinre­den.",
        "Aber der wahre Okkultismus hat mit solchem Streben gar nichts zu tun.",
        "Dieser fordert ja niemanden zur Schülerschaft unmittelbar auf.",
        "Wer aber seine Schulung sucht, dem will er nicht bloß eine dunkle Empfindung von seiner «Gottähnlichkeit» erwecken, sondern er sucht ihm die gei­stigen Augen zu öffnen für das, was in höheren Welten wirklich vorhanden ist."
      ],
      [
        "Gewiß ist ja in jedem Menschen das «göttliche Selbst »enthalten.",
        "Aber das ist ja doch in jedem Wesen der Fall.",
        "Im Stein, in der Pflanze, im Tier ist auch das «göttliche Selbst» enthalten und wirksam.",
        "Aber nicht darauf kann es ankom­men, dies so ganz im allgemeinen zu fühlen und zu wissen, sondern darauf, wirklich in Verbindung zu treten mit den Offenbarungen dieses «göttlichen Selbstes» So wie derjenige nichts von der physischen Welt weiß, der sich nur immer wieder sagen kann: diese Welt enthält in sich verhüllt das «göttliche Selbst», so weiß auch derjenige nichts von hö­heren"
      ],
      [
        "Welten, welcher das «göttliche Geisterreich» nur in verschwommener, unbestimmter Allgemeinheit sucht.",
        "Man soll seine Augen öffnen und die Offenbarung der Gottheit in den Dingen der physischen Welt, im Stein, in der Pflanze anschauen, nicht davon träumen, daß dies jedoch alles nur «Erscheinungen» seien und daß Gottes wahre Gestalt dahinter «verborgen» sei.",
        "Nein, Gott offenbart sich in seinen Schöpfungen, und wer Gott erkennen will, muß das We­sen dieser Schöpfungen erkennen lernen.",
        "Deshalb muß man auch das wirklich anschauen lernen, was in höheren Welten vorgeht und lebt, wenn man das «Göttliche» erkennen will.",
        "Das Bewußtsein, daß der «Gottmensch» in einem lebt, kann höchstens den Anfang bilden.",
        "Aber dieser An­fang wird, wenn er in rechter Weise erlebt wird, zum An­trieb, wirklich aufzusteigen in die höheren Welten.",
        "Das kann man aber nur, wenn man die geistigen «Sinne» dazu in sich ausbildet.",
        "Alles andere stellt sich ja doch nur auf den Standpunkt: Ich will bleiben, wie ich bin, und nur errei­chen, was mir so zu erreichen möglich ist.",
        "Der Standpunkt des Okkultismus ist aber, ein anderer Mensch zu werden, damit man anderes als das Gewöhnliche schauen und erle­ben kann."
      ],
      [
        "Und dazu ist eben der Durchgang durch die imaginative Erkenntnis notwendig.",
        "Es ist gesagt worden, daß diese Stufe der Imagination nicht aufgefaßt zu werden braucht wie eine Schulklasse, die man durchaus «absitzen» müsse.",
        "Das ist so zu verstehen, daß es namentlich in unsrem ge­genwärtigen Leben Personen gibt, welche solche Vorbe­dingungen mitbringen, daß der Geheimlehrer bei ihnen gleichzeitig oder wenigstens fast gleichzeitig mit der ima­ginativen Erkenntnis die inspirierte und die intuitive hervorrufen"
      ],
      [
        "kann.",
        "Aber es darf durchaus nicht so verstanden werden, als ob es irgend jemand geben könnte, dem der Durchgang durch die Imagination zu ersparen wäre."
      ],
      [
        "Auf den Grund der Gefahr innerhalb der imaginativen Erkenntnis ist ja in meiner Schrift «Wie erlangt man Er­kenntnisse der höheren Welten?» bereits hingedeutet wor­den.",
        "Dieser Grund liegt darin, daß der Mensch beim Ein­tritte in diese Welt gewissermaßen den Boden unter den Füßen verliert.",
        "Wodurch er in der physischen Welt Festig­keit hat, das geht ihm zunächst scheinbar ganz verloren.",
        "Nimmt man in dieser physischen Welt etwas wahr, so fragt man sich : Woher kommt diese Wahrnehmung?",
        "Man tut das ja zumeist unbewußt.",
        "Aber man ist sich eben «unbewußt» darüber klar, daß die Ursachen der Wahrnehmungen die Gegenstände «draußen im Raume» sind.",
        "Die Farben, die Töne, die Gerüche gehen von diesen Gegenständen aus.",
        "Man sieht nicht freischwebende Farben, man hört nicht Tö­ne, ohne daß man sich bewußt werden könnte, an welchen Gegenständen diese Farben als Eigenschaften «haften», von welchen Gegenständen die Töne herrühren.",
        "Dieses Be­wußtsein, daß die Gegenstände und Wesenheiten sie verur­sachen, gibt den physischen Wahrnehmungen und damit dem Menschen selbst Festigkeit und einen sicheren Halt.",
        "Hat jemand Wahrnehmungen ohne äußere Ursache, so spricht man von abnormen, krankhaften Zuständen.",
        "Man nennt solche ursachlose Wahrnehmungen Illusionen, Hal­luzinationen, Visionen."
      ],
      [
        "Nun zunächst ganz äußerlich betrachtet besteht die ganze imaginative Welt aus solchen Halluzinationen, Visionen und Illusionen.",
        "Es ist gezeigt worden in «Wie erlangt man Er­kenntnisse der höheren Welten?», wie durch die Geheimschulung"
      ],
      [
        "künstlich solche Visionen usw. erzeugt werden.",
        "Durch das Hinlenken des Bewußtseins auf ein Samenkorn oder auf eine absterbende Pflanze werden gewisse Gestal­ten vor die Seele gezaubert, die nichts weiter zunächst sind als Halluzinationen."
      ],
      [
        "Die «Flammenbildung», von der dort gesagt wurde, daß sie in der Seele auftreten kann durch die Betrachtung einer Pflanze oder dergleichen und die sich nach einer Zeit ganz loslöst von der Pflanze, ist, äußerlich betrachtet, einer Halluzination gleich zu achten.",
        "Und so geht es noch weiter in der Geheimschulung, wenn man in die imaginative Welt eintritt."
      ],
      [
        "Das, wovon man gewöhnt war, daß es von den Dingen «draußen im Raum» ausgeht oder ihnen als Eigenschaft «anhaftet», die Farben, Töne, Gerüche usw., erfüllen nun freischwebend den Raum.",
        "Die Wahrnehmungen lösen sich los von allen äußeren Dingen und schweben frei im Raume oder fliegen darinnen herum."
      ],
      [
        "Und man weiß dabei doch ganz genau, daß die Dinge, die man da vor sich hat, diese Wahrnehmungen nicht hervor­gebracht haben, daß man sie vielmehr «selbst» verursacht hat.",
        "So kommt es, daß man meinen muß, man habe den «Boden unter den Füßen verloren»."
      ],
      [
        "Im gewöhnlichen Leben in der physischen Welt muß man sich ja gerade davor hüten, Vorstellungen zu haben, die nicht von den Dingen her­rühren, die sozusagen «ohne Grund und Boden» sind.",
        "Zur Hervorrufung der imaginativen Erkenntnis aber kommt es gerade darauf an, zunächst Farben, Töne, Gerüche usw. zu haben, die ganz losgelöst von allen Dingen «frei im Raume schweben»."
      ],
      [
        "Nun muß die nächste Stufe der imaginativen Erkenntnis darin bestehen, einen neuen «Grund und Boden» für die herrenlos gewordenen Vorstellungen zu finden.",
        "Das muß"
      ],
      [
        "eben in der anderen Welt geschehen, die sich jetzt offenba­ren soll.",
        "Es bemächtigen sich neue Dinge und Wesenheiten dieser Vorstellungen.",
        "In der physischen Welt «haftet» zum Beispiel die blaue Farbe an einer Kornblume.",
        "In der imagi­nativen Welt darf sie nun auch nicht «freischwebend» blei­ben.",
        "Sie strömt gleichsam zu einer Wesenheit hin, und wäh­rend sie noch vorher herrenlos war, wird sie jetzt der Ausdruck einer Wesenheit.",
        "Es spricht etwas durch sie zu dem Beobachter, was dieser eben nur innerhalb der imaginati­ven Welt wahrnehmen kann.",
        "Und so sammeln sich die «freischwebenden» Vorstellungen um bestimmte Mittel­punkte.",
        "Und man wird gewahr, daß Wesen durch sie zu uns sprechen.",
        "Und wie es in der physischen Welt körperliche Dinge und Wesenheiten sind, an denen Farben, Gerüche und Töne usw.",
        "«haften» oder von denen sie herstammen, so sprechen sich jetzt «geistige Wesenheiten» durch sie aus.",
        "Diese «geistigen Wesenheiten» sind ja tatsächlich im­mer da; sie umschwirren den Menschen beständig.",
        "Aber sie können sich diesem nicht offenbaren, wenn er nicht die Ge­legenheit dazu gibt.",
        "Und diese Gelegenheit gibt er nur da­durch, daß er in sich die Fähigkeit hervorruft, Töne, Far­ben usw. auch dann vor seiner Seele entstehen zu lassen, wenn diese durch keinen physischen Gegenstand veran­laßt werden."
      ],
      [
        "Ganz anders sind die «geistigen Tatsachen und Wesen­heiten » als die Dinge und Wesen der physischen Welt.",
        "Es ist nicht ganz leicht, in der gewöhnlichen Sprache einen Ausdruck zu finden, welcher die Verschiedenheit auch nur annähernd charakterisiert.",
        "Vielleicht kommt man der Sache am nächsten, wenn man sagt: in der imaginativen Welt spricht alles so zum Menschen, wie wenn es unmittelbar intelligent"
      ],
      [
        "wäre, während in der physischen Welt auch die In­telligenz nur auf dem Umwege durch die physische Kör­perlichkeit sich offenbaren kann.",
        "Das macht eben die Be­weglichkeit und Freiheit der imaginativen Welt aus, daß das Zwischenglied der äußeren Dinge fehlt, daß das Gei­stige ganz unmittelbar in den freischwebenden Tönen, Far­ben usw. sich auslebt."
      ],
      [
        "Nun liegt der Grund zu einer Gefahr, welche dem Men­schen von dieser Welt droht, darin, daß er die Äußerungen der «geistigen Wesen» wahrnimmt, aber nicht diese Wesen selbst.",
        "Es ist das nämlich so lange der Fall, als er nur in der imaginativen Welt bleibt und zu keiner höheren aufsteigt.",
        "Erst die Inspiration und die Intuition führen ihn allmählich zu diesen Wesen selbst hin. - Wollte aber der Geheimlehrer diese letzteren vorschnell erwecken, ohne den Schüler gründlich in das imaginative Gebiet einzuführen, dann wür­de die höhere Welt nur ein schatten- und schemenhaftes Dasein erhalten.",
        "Die ganze herrliche Fülle der Bilder ginge verloren, in denen sie sich offenbaren muß, wenn man wirklich in sie eintreten soll. - In dieser Tatsache liegt der Grund, warum der Geheimschüler einen «Führer» oder ei­nen «Guru» braucht, wie man in der Geheimwissenschaft eben diesen Führer nennt."
      ],
      [
        "Für den Schüler ist nämlich die imaginative Welt anfangs wirklich eine bloße «Bilderwelt», von der er vielfach nicht weiß, was sie ausdrückt.",
        "Der Geheimlehrer aber weiß, auf welche Dinge und Wesenheiten sich diese Bilder in einer noch höheren Welt beziehen.",
        "Hat der Schüler zu ihm Ver­trauen, so kann er wissen, daß sich ihm später Zusammen­hänge offenbaren werden, welche er vorläufig noch nicht durchschaut.",
        "In der physischen Welt waren die Gegenstände"
      ],
      [
        "im Raume selbst die Führer.",
        "Er war imstande, die Rich­tigkeit seiner Vorstellungen zu prüfen.",
        "Die körperliche Wirklichkeit ist der «Fels», an dem alle Halluzinationen und Illusionen zerschellen müssen.",
        "Dieser Fels verschwin­det in einen Abgrund, wenn man in die imaginative Welt eintritt.",
        "Und deshalb muß als ein anderer solcher «Fels» der «Führer» eintreten.",
        "An dem, was er dem Schüler zu bieten vermag, muß dieser die Wirklichkeit der neuen Welt empfinden.",
        "Man kann daraus ermessen, wie groß das Ver­trauen in den Führer sein muß in jeder Geheimschulung, welche dieses Namens wirklich wert ist.",
        "Sobald man an den Führer nicht mehr glauben kann, ist es ja in dieser höheren Welt so, wie wenn einem in der physischen plötzlich alles genommen würde, worauf man den Glauben an die Wirk­lichkeit seiner Wahrnehmungen gebaut hat."
      ],
      [
        "Außer dieser einen Tatsache gibt es nun noch eine ande­re, durch welche der Mensch in Verwirrung gesetzt werden könnte, wenn er sich ohne Führung in die imaginative Welt begeben wollte.",
        "Es lernt nämlich der Geheimschüler von allen geistigen Wesenheiten in erster Linie sich selbst ken­nen.",
        "In dem physischen Leben hat der Mensch Gefühle, Be­gierden, Wünsche, Leidenschaften, Vorstellungen usw.",
        "Zwar werden diese alle von den Dingen und Wesenheiten der äußeren Welt veranlaßt, aber der Mensch weiß ganz ge­nau, daß sie seine innere Welt bilden, und er unterscheidet sie als das, was in seiner Seele vorgeht, von den Gegenstän­den der Außenwelt.",
        "Sobald aber der imaginative Sinn er­weckt ist, hört diese Leichtigkeit des Unterscheidens ganz auf.",
        "Seine eigenen Gefühle, Vorstellungen, Leidenschaften usw. treten buchstäblich aus ihm heraus, nehmen Gestalt, Farbe und Ton an.",
        "Er steht ihnen jetzt so gegenüber wie in"
      ],
      [
        "der physischen Welt ganz fremden Gegenständen und We­senheiten.",
        "Und daß die Verwirrung eine vollständige wer­den kann, wird man begreifen, wenn man sich an das erin­nert, was in dem Kapitel «Über einige Wirkungen der Ein­weihung» in «Wie erlangt man Erkenntnisse der höheren Welten?» gesagt worden ist."
      ],
      [
        "Dort ist ja nichts anderes ge­schildert als die Art, wie die imaginative Welt für den Beob­achter auftritt.",
        "Es erscheint nämlich in ihr alles umgekehrt, wie im Spiegelbilde.",
        "Was vom Menschen ausströmt, er­scheint so, als wenn es von außen an ihn herankommen wollte."
      ],
      [
        "Ein Wunsch, den er hegt, verwandelt sich in eine Gestalt, beispielsweise in die Form eines phantastisch ausse­henden Tieres, oder auch wohl eines menschenähnlichen Wesens.",
        "Dieses scheint ihn zu bestürmen, einen Angriff auf ihn auszuführen oder ihn auch zu veranlassen, dieses oder jenes zu tun."
      ],
      [
        "So kann es kommen, daß der Mensch sich vor­kommt als umgeben und umflattert von einer ganz phan­tastischen, oft reizvollen und verführerischen, oft auch grausigen Welt.",
        "In Wahrheit stellt diese nichts anderes vor als seine eigenen Gedanken, Wünsche und Leidenschaften, welche in Bilder verwandelt sind. - Man würde sich einem großen Irrtum hingeben, wenn man glauben wollte, daß die Unterscheidung dieses in Bildern verwandelten Selb­stes von der wirklichen geistigen Welt leicht sei."
      ],
      [
        "Zunächst ist es für den Schüler geradezu unmöglich, diese Unter­scheidung wirklich zu vollziehen.",
        "Denn es kann genau das­selbe Bild ebensogut von einem geistigen Wesen herrühren, welches zu den Menschen spricht, wie von irgend etwas im Innern der Seele."
      ],
      [
        "Und übereilt der Mensch gerade dabei et­was, so setzt er sich der Gefahr aus, daß er die beiden Dinge nie ordentlich voneinander zu trennen lernt.",
        "Die größte"
      ],
      [
        "Vorsicht ist dabei geboten. - Nur noch größer wird die Verwirrung dadurch, daß die eigenen Wünsche und Begierden der Seele sich in Bilder kleiden, die genau den ent­gegengesetzten Charakter von dem tragen, was sie wirk­lich sind.",
        "Man nehme zum Beispiel an, die Eitelkeit kleide sich auf diese Art in ein Bild."
      ],
      [
        "Sie kann auftreten als eine liebreizende Gestalt, welche die wunderbarsten Dinge ver­spricht, wenn man ausführt, was sie angibt.",
        "Diese ihre An­gaben scheinen etwas durchaus Gutes, Erstrebenswertes in Aussicht zu stellen; folgt man ihnen, so stürzt man sich in sein moralisches oder sonstiges Verderben."
      ],
      [
        "Umgekehrt kann sich eine gute Eigenschaft der Seele in ein unsympa­thisches Kleid hüllen.",
        "Nur dem wirklichen Kenner ist es möglich, da zu unterscheiden, und nur eine Persönlichkeit, die gar nicht wankend gemacht werden kann in bezug auf ein richtiges Ziel, ist sicher gegenüber den Verführungs­künsten der eigenen Seelenbilder. - Man wird in Anbe­tracht von alledem zugeben, wie notwendig die Führung eines Lehrers ist, der mit sicherem Sinn den Schüler auf­merksam macht, was auf diesem Gebiet Trugbild und was Wahrheit ist."
      ],
      [
        "Nicht zu glauben aber braucht man, daß die­ser Lehrer immer hinter dem Schüler stehen muß.",
        "Das räumliche Beisammensein mit dem Lehrer ist es durchaus nicht, worauf es beim Geheimschüler immer ankommt.",
        "Gewiß gibt es Augenblicke, wo ein solches räumliches Bei­sammensein wünschenswert, und auch solche, wo es durch­aus notwendig ist."
      ],
      [
        "Aber anderseits findet der Geheimlehrer auch die Mittel, um mit dem Schüler in Verbindung zu bleiben, auch bei räumlicher Entfernung.",
        "Und zudem kommt in Betracht, daß manches, was zwischen Lehrer und Schüler auf diesem Gebiete bei einem Beisammensein vorgeht,"
      ],
      [
        "oftmals monate-, vielleicht jahrelang nachwirken kann.",
        "Eines aber gibt es, was sicher den notwendigen Zusammenhang zwischen Lehrer und Schüler zerreißen muß.",
        "Das tritt dann ein, wenn der letztere das Vertrauen zu dem ersteren verliert. - Und besonders schlimm ist es, wenn dieses Vertrauensband sich löst, ehe der Schüler unter­scheiden gelernt hat die Vorspiegelungen der eigenen Seele von der wahren Wirklichkeit."
      ],
      [
        "Nun könnte man vielleicht sagen : ja, wenn auf diese Art ein solches Gebundensein an den Lehrer eintritt, so ver­liert ja der Geheimschüler alle Freiheit und Selbständig­keit.",
        "Er gibt sich sozusagen dem Lehrer ganz in die Hand.",
        "Doch gerade dies ist in Wahrheit gar nicht der Fall.",
        "Allerdings gibt es Unterschiede in bezug auf die Abhängigkeit vom Lehrer in den verschiedenen Methoden der okkulten Schulung.",
        "Diese Abhängigkeit kann eine größere oder ge­ringere sein müssen.",
        "Sie ist die verhältnismäßig größte bei derjenigen Methode, welche von den Okkultisten des Orients befolgt wurde und von diesen auch heute noch als die ihrige gelehrt wird.",
        "In viel geringerem Maße ist diese Abhängigkeit von einem Menschen schon bei der soge­nannten christlichen Einweihung vorhanden.",
        "Und eigent­lich völlig in Wegfall kommt sie bei demjenigen Erkennt­nispfade, der seit dem vierzehnten Jahrhunderte von den sogenannten Geheimschulen der Rosenkreuzer angegeben wird.",
        "Bei diesem kann zwar nicht der Lehrer wegfallen, denn das ist unmöglich.",
        "Aber es hört wahrhaft jede Ab­hängigkeit von ihm auf.",
        "Wie das möglich ist, wird aus der Fortsetzung dieser Darstellung zu ersehen sein.",
        "Darinnen wird nämlich genau geschildert werden, wodurch sich diese drei «Erkenntnispfade» unterscheiden: der orientalische,"
      ],
      [
        "der christliche und der rosenkreuzerische.",
        "Bei dem letzteren kommt nämlich gar nichts in Betracht, was einen modernen Menschen irgendwie in seinem Freiheitsgefühl stören könn­te.",
        "Auch wird in dieser Fortsetzung geschildert werden, wie die eine oder die andere Person als Geheimschüler dazu kommen kann, auch gegenwärtig, im modernen Europa, nicht den rosenkreuzerischen Weg zu gehen, sondern den orientalischen oder den älteren christlichen, obgleich der rosenkreuzerische gegenwärtig der natürlichste ist.",
        "Dieser ist, wie man im weiteren Verlaufe sehen wird. nicht etwa unchristlich.",
        "Es kann ihn ein Mensch gehen, ohne sein Christentum zu gefährden, und es kann ihn auch ein Mensch gehen, der auf der vollen Höhe moderner wissenschaftlicher Weltanschauung zu stehen vermeint."
      ],
      [
        "Ein anderes könnte aber vielleicht noch der Erklärung bedürfen.",
        "Man könnte sich versucht fühlen zu fragen, ob denn nicht dem Geheimschüler erspart bleiben könnte, durch die Vorspiegelungen seiner eigenen Seele hindurch­zugehen.",
        "Geschähe das, so würde er eben nie zu der für ihn so wünschenswerten selbständigen Unterscheidung kom­men.",
        "Denn durch nichts kann die ganz eigenartige Natur der imaginativen Welt anschaulicher werden als durch die Betrachtung der eigenen Seele.",
        "Der Mensch kennt ja das Innenleben seiner Seele zunächst von der einen Seite.",
        "Er steckt eben darinnen.",
        "Und das muß ja der Geheimschüler gerade lernen: die Dinge nicht nur von außen anzuschauen, sondern sie so zu beobachten, als ob er in ihnen allen darinnensteckte.",
        "Tritt ihm nun seine eigene Gedankenwelt so wie etwas Fremdes entgegen, dann lernt er eben dadurch ein Ding, das er schon von einer Seite her kennt, auch noch von der anderen Seite kennen.",
        "Er muß gewissermaßen"
      ],
      [
        "sich selbst das erste Beispiel einer solchen Erkennt­nis werden.",
        "Von der physischen Welt her ist er ja an etwas ganz anderes gewöhnt.",
        "Da erblickt er alle anderen Dinge immer nur von außen, sich selbst aber erlebt er nur vom Innern.",
        "Er kann, solange er in der physischen Welt ver­bleibt, nie hinter die Oberfläche der Dinge hineinsehen.",
        "Und er kann niemals aus sich herausgehen, gleichsam «aus seiner eigenen Haut fahren», um sich von außen zu beob­achten.",
        "Das letztere obliegt ihm buchstäblich bei der Ge­heimschulung zuerst, und mit Hilfe dessen lernt er dann, auch äußeren Tatsachen und Wesenheiten hinter die Ober­fläche zu schauen."
      ]
    ]
  },
  {
    "order": 6,
    "title_de": "DIE INSPIRATION",
    "paragraphs": [
      "- Die Stufen der höheren Erkenntnis",
      "Aus der Schilderung der Imagination ist ersichtlich gewor­den, wie durch sie der Geheimschüler den Boden der äuße­ren sinnlichen Erlebnisse verläßt. In einem noch viel höhe­ren Grade ist dieses der Fall in der Inspiration.",
      "Bei ihr liegt dem Vorstellen noch viel weniger von dem zugrunde, was man als eine äußere Anregung bezeichnen kann. Der Mensch muß da in sich selbst die Kraft finden, welche es ihm mög­lich macht, über etwas sich Vorstellungen zu bilden.",
      "Er muß in einem viel höheren Grade innerlich tätig sein, als dies bei der äußeren Erkenntnis der Fall ist. Bei dieser gibt er sich eben den äußeren Eindrücken hin, und sie verursa­chen ihm die Vorstellungen.",
      "Diese Hingabe fällt bei der In­spiration weg. Es liefern nunmehr keine Augen Farben, keine Ohren Töne usw. Aller Inhalt des Vorstellens muß gewissermaßen durch eigene Tätigkeit, also durch rein geistig-seelische Vorgänge geschaffen werden.",
      "Und in dasje­nige, was so der Mensch durch die Tätigkeit seines Innern schafft, muß sich die Offenbarung der höheren wirklichen Welt hineinprägen. Ein eigenartiger Widerspruch scheint in einer solchen Beschreibung der höheren Erkenntniswelt aufzutreten.",
      "Der Mensch soll in einer gewissen Art der Schöpfer seiner Vorstellungen sein; und doch dürfen diese Vorstellungen selbstverständlich nicht seine Geschöpfe sein; sondern durch sie müssen sich die Vorgänge der hö­heren Welt ebenso zum Ausdrucke bringen, wie sich in den Wahrnehmungen der Augen, Ohren usw. die Vorgänge der niederen Welt zum Ausdrucke bringen. Es ist das aber ein Widerspruch, der sich in der Schilderung dieser Erkenntnisart finden muß.",
      "Denn das ist es gerade, was sich",
      "der Geheimschüler auf dem Wege zur Inspiration aneignen muß, daß er auf dem Wege seiner inneren Tätigkeit etwas zustande bringt, wozu er in dem gewöhnlichen Leben von außen gezwungen wird. - Warum verlaufen im gewöhnli­chen Leben die Vorstellungen nicht willkürlich? Weil der Mensch sich bei seinem Vorstellen nach den äußeren Ge­genständen richten muß. Alle Willkür des «Ich» fällt weg, weil die Gegenstände sagen: so oder so sind wir. Da spre­chen die Gegenstände, wie sie vorgestellt werden sollen, das «Ich » hat nichts darüber zu bestimmen. Wer sich den Gegenständen nicht fügen will, der stellt sich eben Unrich­tiges vor; und er würde bald gewahr werden, wie wenig er damit in der Welt zurechtkäme. Man kann dieses notwen­dige Verhalten des Menschen zu den Dingen der Außen­welt in der Erkenntnis mit dem Ausdruck «selbstlos» be­zeichnen. Der Mensch muß sich «selbstlos» zu den Din­gen verhalten. Und die Außenwelt ist sein Lehrmeister in dieser Selbstlosigkeit. Sie benimmt ihm alle Illusionen, alle Phantastereien, alle unlogischen Urteile, alles Unsachliche, indem sie ihm einfach ihr richtiges Bild vor die Sinne stellt.",
      "Will der Mensch sich für die Inspiration vorbereiten, so muß er sein Inneres so weit bringen, daß ihm diese Selbstlosigkeit eigen ist, auch wenn nichts von außen dazu zwingt. Er muß innerlich schaffen lernen, jedoch so, daß sein «Ich» bei diesem Schaffen nicht im geringsten eine ei­genmächtige Rolle spielt. Die Schwierigkeiten, welche in Betracht kommen, um eine solche Selbstlosigkeit zu errin­gen, werden um so deutlicher sichtbar, je besser man be­rücksichtigt, welche Seelenkräfte für die Inspiration beson­ders in Betracht kommen. - Man unterscheidet die drei",
      "Grundkräfte des seelischen Lebens: Vorstellen, Fühlen und Wollen. Bei dem gewöhnlichen Sinneserkennen sind die Vorstellungen durch die äußeren Gegenstände angeregt. Und durch diese von außen angeregten Vorstellungen be­kommen auch das Fühlen und das Wollen ihre bestimmten Richtungen.",
      "Der Mensch sieht zum Beispiel einen Gegen­stand; dieser bereitet ihm Lust, infolgedessen begehrt er die betreffende Sache. Die Lust sitzt im Gefühle; durch die­ses wird der Wille erregt, wie es selbst sein Gepräge von dem Vorstellen erhalten hat.",
      "Der letzte Grund aber von Vorstellen, Fühlen und Wollen ist der äußere Gegenstand. - Ein anderer Fall wäre dieser. Ein Mensch erlebt ein Er­eignis. Dieses bereitet ihm Angst. Er läuft von dem Schauplatze des Ereignisses hinweg.",
      "Auch hier sind die äußeren Vorgänge der erste Grund; sie kommen durch die Sinne zur Wahrnehmung, werden Vorstellungen, das Gefühl der Angst stellt sich ein; und der Wille - der sich im Davonlaufen verwirklicht - ist die Folge. Bei der Inspiration fällt ein äußerer Gegenstand in dieser Form weg.",
      "Die Sinne kommen für eine Wahrnehmung nicht in Betracht. Sie also können auch nicht die Anreger von Vorstellungen sein. Von dieser Seite aus wird auf Fühlen und Wollen kein Ein­fluß ausgeübt. - Nun sind es aber gerade diese beiden, aus denen, wie aus einem Mutterboden, bei der Inspiration in­nerlich die Vorstellungen aufsteigen, gleichsam herauswachsen.",
      "Und es werden wahre Vorstellungen erwachsen, wenn der Mutterboden ein gesunder ist, Irrtümer und Wahngebilde, wenn er ein ungesunder ist.",
      "So gewiß als die Inspirationen, welche aus einem gesun­den Fühlen und Wollen entspringen, Offenbarungen einer höheren Welt sein können, so gewiß entspringen aus einem",
      "wüsten Fühlen und Wollen die Irrtümer, Täuschungen und Phantastereien über eine höhere Welt.",
      "Die Geheimschulung stellt sich deshalb die Aufgabe, dem Menschen die Mittel zu zeigen, welche ihn befähigen, seine Gefühle und seine Willensimpulse zu gesund-fruchtbaren für die Inspiration zu machen. Wie in allen Dingen der Ge­heimschulung hat man es auch hier mit einer intimen Rege­lung und Gestaltung des Seelenlebens zu tun.",
      "Man muß sich zunächst gewisse Gefühle aneignen, die man im ge­wöhnlichen Leben nur in einem geringen Grade kennt. Es sollen hier einige von diesen Gefühlen angedeutet werden. Zu den wichtigsten gehört eine höhere Empfindlichkeit gegenüber von «wahr » und «unwahr», von « richtig »und «unrichtig».",
      "Gewiß hat ja auch der gewöhnliche Mensch ähnliche Gefühle. Sie müssen aber eben bei dem Geheimschüler in einem viel höheren Maße ausgebildet wer­den. Man nehme an, jemand begehe einen logischen Feh­ler : ein anderer sieht diesen Fehler ein, und er stellt die Sa­che richtig.",
      "Man mache sich klar, wie groß der Anteil des Urteiles, des Verstandes bei einem solchen Richtigstellen ist und wie gering das Gefühl der Lust beim Richtigen, der Unlust beim Unrichtigen. Wohlgemerkt, es soll durchaus nicht behauptet werden, daß die Lust und entsprechend die Unlust gar nicht vorhanden seien.",
      "Aber der Grad, in dem sie im gewöhnlichen Leben vorhanden sind, muß sich in der Geheimschulung ins Unbegrenzte steigern. Ganz syste­matisch muß der Geheimschüler die Aufmerksamkeit auf sein Seelenleben lenken : und er muß es dahin bringen, daß ihm das logisch Unrichtige eine Quelle des Schmerzes wird, der durchaus nicht hinter einem physischen Schmerze zurückbleibt; und in umgekehrter Art muß ihm das « Richti­ge »",
      "wirkliche Freude oder Lust bereiten. Wo also ein an­derer nur seinen Verstand, seine Urteilskraft in Bewegung bringt, muß der Geheimschüler lernen, die ganze Stufen­folge von Gefühlen, vom Schmerz bis zum Enthusiasmus, von der wehevollen Spannung bis zur entzückenden Lö­sung im Besitz der Wahrheit zu durchleben.",
      "Ja, er muß et­was wie Haß empfinden lernen gegen dasjenige, was beim «normalen » Menschen nur als ein nüchternkaltes «Un­richtiges » erlebt wird; er muß eine Liebe zur Wahrheit in sich entwickeln, welche einen ganz persönlichen Charakter trägt; so persönlich, so warm wie der Liebende der Gelieb­ten gegenüber empfindet. - Man wird ja gewiß auch in den Kreisen unserer «Gebildeten» vielfach von der «Liebe zur Wahrheit» reden; doch ist das, was man da meint, eben gar nicht zu vergleichen mit dem, was der Geheimschüler in stiller, innerer Seelenarbeit nach dieser Richtung durchma­chen muß. Er muß sich geduldig immer wieder probeweise dieses oder jenes «Wahre», dieses oder jenes «Falsche» vor­legen; und sich der Sache hingeben, um nicht bloß seine Urteilskraft zu schulen, die nüchtern unterscheidet zwischen «wahr» und «falsch »; sondern er muß zu dem allen ein ganz persönliches Verhältnis gewinnen. - Es ist durchaus richtig, daß der Mensch im Anfange einer solchen Schu­lung in das verfallen kann, was man «Überempfindlichkeit» nennen mag.",
      "Ein unrichtiges Urteil, das er in seiner Umge­bung hört, eine Inkonsequenz usw. können ihm einen schier unerträglichen Schmerz bereiten. - Es muß deshalb bei der Schulung auf diese Sache Rücksicht genommen werden. Denn geschähe das nicht : dann könnten sich aller­dings große Gefahren für das Seelengleichgewicht des Schülers ergeben.",
      "Wird darauf gesehen, daß der Charakter",
      "fest bleibt, dann können Stürme im Seelenleben sich abspie­len, und der Mensch hat doch die Kraft, in harmonischer Miene und Gebärde mit der Außenwelt zu leben. Ein Feh­ler ist in jedem Falle gemacht, wo der Geheimschüler zu ei­nem Gegensatze gegenüber der Außenwelt gebracht wird, so daß er diese unerträglich findet oder gar aus ihr fliehen will.",
      "Die höhere Gefühlswelt darf sich nicht auf Kosten des gleichmäßigen Wirkens und Arbeitens in der Außenwelt entwickeln; deshalb muß der inneren Erhöhung des Ge­fühlslebens eine Stärkung der Widerstandskraft gegenüber den äußeren Eindrücken entsprechen. Die praktische Geheimschulung weist daher den Menschen an, niemals die obengenannten Übungen zur Schulung seiner Gefühlswelt zu unternehmen, ohne sich zugleich auch nach der Rich­tung zu entwickeln, daß er ein Verständnis dafür gewinnen könne, was das Leben an Toleranzempfindung von dem Menschen fordert.",
      "Er muß zugleich in sich den lebendigsten Schmerz empfinden können, wenn zum Beispiel ein Mensch ein unrichtiges Urteil abgibt, und vollkommen tolerant sein können gegen diesen Menschen, weil der Gedanke in der Seele ebenso lebhaft da ist : dieser Mensch muß so urtei­len, und es ist mit seinem Urteile wie mit einer Tatsache zu rechnen. - Richtig ist allerdings, daß das Innere des Ge­heimwissenschafters sich immer mehr und mehr zu einem Doppelleben umgestalten wird. Immer reichere Vorgänge werden sich in seiner Seele abspielen bei seiner Pilgerschaft durch das Leben, immer selbständiger gegenüber dem, was die äußere Welt gibt, wird eine zweite Welt.",
      "Aber dieses Doppelleben wird gerade das Fruchtbare sein für die echte Lebenspraxis. Was sich dadurch einstellt, ist Schlagfertig­keit des Urteiles, Treffsicherheit in bezug auf die Entschlüsse.",
      "Wo derjenige, der einer solchen Schulung fernesteht, lange Gedankenketten durchmachen muß, zwischen Entschluß und Ratlosigkeit hin- und hergetrieben wird, da wird der Geheimwissenschafter rasch die Lagen des Lebens überschauen, dem gewöhnlichen Blicke verborgene Zu­sammenhänge schnell aufdecken usw. Es gehört für ihn dann oft sogar viel Geduld dazu, sich in die langsame Art hineinzubegeben, wie ein anderer etwas begreifen kann, während bei ihm doch dieses Begreifen pfeilschnell vor sich geht.",
      "Nun ist bisher nur gesprochen von den Eigenschaften, welche das Gefühlsleben erhalten muß, damit die Inspira­tion in der richtigen Art eintreten könne. Die andere Frage ist die: Wie werden die Gefühle fruchtbar, so daß sie aus sich wirkliche, der Inspirationswelt angehörige Vorstellungen gebären? Will man das einsehen, was die Geheimwissenschaft als Antwort auf diese Frage zu geben hat, so muß man sich mit der Tatsache bekannt machen, daß des Menschen Seelenleben immer einen gewissen Schatz von Gefühlen hat, welche über das Maß dessen hinausgehen, was durch die sinnlichen Wahrnehmungen angeregt wird. Der Mensch fühlt gleichsam mehr, als das ist, wozu ihn die Dinge zwingen. Nur wird in dem gewöhnlichen Leben die­ses Übermaß in einer solchen Richtung angewendet, wel­che durch die Geheimschulung in eine andere verwandelt werden muß. Man nehme zum Beispiel ein Angst- oder Furchtgefühl. Man wird sich leicht klarmachen können, daß in vielen Fällen die Furcht oder die Angst größer ist, als sie sein würde, wenn sie einem entsprechenden äußeren Vorgange ganz angemessen wäre. Man stelle sich nun vor : der Geheimschüler arbeite energisch an sich, um in keinem ihm",
      "vorkommenden Falle größere Furcht oder Angst zu haben, als gegenüber den entsprechenden äußeren Vorgängen wirklich gerechtfertigt ist. Nun wird ein gewisses Maß von Furcht oder Angst immer aus der Aufwendung von Seelenkraft erzeugt. Diese Seelenkraft geht tatsächlich dadurch verloren, daß eben Furcht oder Angst erzeugt werden. Der Geheimschüler erspart diese Seelenkraft wirklich, wenn er sich die Furcht oder die Angst - und anderes - versagt. Und sie bleibt ihm für etwas anderes verfügbar. Wieder­holt er solche Vorgänge oft, so wird aus den fortlaufend er­sparten Seelenkräften ein innerer Schatz gebildet; und der Geheimschüler wird bald erleben, daß ihm aus solchen Ge­fühlsersparnissen die Keime zu Vorstellungen erwachsen, welche Offenbarungen des höheren Lebens zum Ausdrucke bringen. Dergleichen kann man im gewöhnlichen Sinne nicht «beweisen »; man kann nur dem Geheimschüler die Anweisung geben: tue dies oder jenes - und er wird, wenn er die Sache ausführt, schon sehen, daß sich die untrügli­chen Früchte einstellen.",
      "Einer ungenauen Betrachtung des soeben Geschilderten könnte es leicht als ein Widerspruch erscheinen, daß auf der einen Seite eine Bereicherung der Gefühlswelt gefordert wird, indem durch das, was sonst nur das Verstandesurteil wachruft, Gefühle der Lust, des Schmerzes usw. erregt werden sollen - und auf der anderen Seite gerade von Ersparnissen an Gefühlen gesprochen wird. Dieser Widerspruch ver­schwindet sofort, wenn man bedenkt, daß die Ersparnisse bei denjenigen Gefühlen gemacht werden sollen, welche durch die äußeren Sinne angeregt werden. Eben das, was da erspart wird, erscheint als Bereicherung gegenüber den geistigen Erlebnissen. Und es ist durchaus richtig, daß auf",
      "diese Art an der sinnlichen Wahrnehmungswelt ersparte Gefühle nicht nur auf dem anderen Gebiete freiwerden, sondern daß sie sich auf diesem Gebiete als schöpferisch er­weisen. - Sie schaffen das Material zu den Vorstellungen, in denen sich die geistige Welt offenbart.",
      "Es wurde allerdings nicht besonders weit gehen, wenn man nur bei solchen Ersparnissen stehenbleiben wollte, wie sie oben angedeutet worden sind. Zu größeren Erfolgen ist noch mehr nötig. Man muß der Seele einen noch weit grö­ßeren Schatz von Gefühlerzeugender Kraft zuführen, als auf diesem Wege möglich ist. Man muß zum Beispiel sich ge­wissen äußeren Eindrücken probeweise aussetzen und sich dann die Gefühle ganz versagen, die im sogenannten «nor­malen » Zustande eintreten. Man muß sich zum Beispiel ei­nem Ereignisse gegenüberstellen, welches «normalerwei­se » die Seele erregt, und sich diese Erregung ganz und gar verbieten. Man kann das so machen, daß man sich tatsäch­lich einem solchen Ereignisse gegenüberstellt oder sich bloß mit der Vorstellung behilft. Das letztere ist sogar für die fruchtbare Geheimschulung das bessere. Da der Schü­ler ja in die Imagination eingeweiht wird, entweder vor sei­ner Vorbereitung zur Inspiration oder mit der letzteren gleichzeitig, so muß er eigentlich imstande sein, sich imagi­nativ ein Ereignis mit derselben Kraft vor die Seele zu stel­len, wie wenn es wirklich da wäre. - Wenn nun in langer innerer Arbeit der Schüler sich immer wieder und wieder Dingen und Vorgängen aussetzt und es sich verbietet, entsprechende «normale » Gefühle zuhaben, so wird in sei­ner Seele der Mutterboden für die Inspiration geschaffen. - Nur als Zwischenbemerkung sei hier angeführt, daß derje­nige, welcher eine solche Schulung zur Inspiration beschreibt,",
      "es voll würdigen kann, wenn vom Standpunkte unserer ge­genwärtigen Zeitbildung aus manches gegen eine solche Beschreibung eingewendet wird. Und man kann da nicht nur das oder jenes einwenden, sogar kann man überlegen lächeln und sagen : «Inspiration kann doch nicht pedan­tisch anerzogen werden; sie ist eine Naturgabe des Genies. »Ja, gewiß, vom Standpunkte dieser Zeitbildung mag es recht komisch anmuten, wenn viel über die Heranbildung dessen geredet wird, bei dem diese Bildung von einer Er­klärung nichts wissen will; aber diese Zeitbildung ist sich nicht bewußt, wie wenig sie ihre eigenen Gedankengänge zu Ende zu denken vermag.",
      "Wer es einem Bekenner dieser Zeitbildung zumuten wollte, daß er daran glauben solle, ir­gendein höher entwickeltes Tier habe sich nicht langsam entwickelt, sondern sei «plötzlich » da gewesen : der würde bald hören, daß der im modernen Sinne Gebildete an ein solches «Wunder » nicht glaube. So etwas sei «Aberglau­ben » Nun, auf dem Gebiete des Seelenlebens ist aber ein solcher modern Gebildeter, ganz im Stile seiner eigenen Ansichten, ein von krassem Aberglauben Befallener.",
      "Er will nämlich nicht daran denken, daß sich eine vollkommenere Seele auch entwickelt haben muß, daß sie nicht plötzlich als eine Naturgabe da sein könne. Äußerlich erscheint allerdings manches Genie wie «aus dem Nichts » geboren, auf unerklärliche Weise da; doch erscheint es eben so nur für den materialistischen Aberglauben; der Geisteswissenschaf­ter weiß, daß eine genialische Veranlagung, die in einem Leben bei einem Menschen wie aus dem Nichts heraus ge­boren ist, einfach die Folge von dessen Erziehung zur In­spiration in einem früheren Erdenleben ist. - Auf theoreti­schem Gebiete ist der materialistische Aberglaube schlimm;",
      "bei weitem schlimmer aber ist er noch auf einem solchen praktischen Gebiete wie hier. Da er annimmt, daß die Ge­nies in alle Zukunft «vom Himmel fallen » müssen, küm­mert er sich nicht um derlei « okkultistischen Unfug » oder solch «phantastische Mystik», die von Vorbereitung zur Inspiration sprechen. Dadurch hält aber der Aberglaube der Materialisten den wahren Fortschritt der Menschheit auf. Er sorgt nicht dafür, daß die in den Menschen schlum­mernden Fähigkeiten entwickelt werden.",
      "In Wirklichkeit sind nämlich oft diejenigen, welche sich Fortschrittler und Freidenker nennen, solche, welche die Feinde der wahren Fortentwickelung sind. Doch dies soll",
      "- wie gesagt - nur eine Zwischenbemerkung sein, die not­wendig ist mit Rücksicht auf das Verhältnis der Geheimwissenschaft zur gegenwärtigen Zeitbildung.",
      "Nun wurden die Seelenkräfte, welche durch das gekenn­zeichnete Sich-Versagen der «normalen» Gefühle als Schatz im Innern des Schülers sich aufspeichern, gewiß, auch ohne daß etwas anderes zu Hilfe käme, sich in Inspirationen um­setzen. Und der Geheimschüler wurde erleben, wie in sei­ner Seele wahre Vorstellungen aufsteigen, welche Erleb­nisse in höheren Welten darstellen. Mit den einfachsten Er­fahrungen übersinnlicher Vorgänge wurde die Sache beginnen, und langsam käme Komplizierteres und Höheres zum Vorschein, wenn der Schüler in der angedeuteten Richtung innerlich weiterlebte. - In Wirklichkeit wäre aber eine solche Geheimschulung heute ganz unpraktisch, und sie wird daher wohl nirgends durchgeführt, wo man ernst­haft zu Werke geht. Wollte nämlich der Schüler auf diese Art alles «aus sich selbst heraus» entwickeln, was die Inspiration geben kann: er würde ganz sicher dazu kommen,",
      "alles so aus sich «herauszuspinnen», was je zum Beispiel auch hier über das Wesen des Menschen, über des Men­schen Leben nach dem Tode, über die Entwickelung des Menschengeschlechts und der Planeten usw. gesagt wor­den ist. Aber ein solcher Schüler würde eben unermeßlich lange Zeiträume dazu brauchen.",
      "Es wäre so, wie wenn zum Beispiel jemand die ganze Geometrie aus sich selbst heraus­spinnen wollte, ohne Rücksicht darauf, was Menschen vor ihm auf diesem Gebiete schon gearbeitet haben. Gewiß, «in der Theorie » ist so etwas durchaus möglich.",
      "In der Praxis es auszuführen wäre Torheit. Auch in der Geheimwissen­schaft verfährt man nicht so, sondern man läßt sich durch einen Lehrer diejenigen Dinge überliefern, welche durch inspirierte Vorgänger für die Menschheit errungen worden sind.",
      "Diese Überlieferung muß gegenwärtig die Grundlage abgeben für die eigene Inspiration. Dasjenige, was in der einschlägigen Literatur und in Vorträgen usw. heute aus dem Gebiet der Geheimwissenschaft geboten wird, das kann durchaus eine solche Inspirationsgrundlage abgeben.",
      "Es sind zum Beispiel die Lehren über die verschiedenen Grundteile des Menschen (physischer Leib, Ätherleib, Astralleib usw.), die Erkenntnisse über das Leben nach dem Tode bis zu einer neuen Verkörperung, dann zum Bei­spiel alles, was unter dem Titel «Aus der Akasha-Chronik» gedruckt wurde. Man muß nämlich gegenüber der Inspira­tion durchaus festhalten, daß man sie braucht zum Auffin­den und Selbsterleben der höheren Wahrheiten, nicht aber zum Verstehen derselben.",
      "Man kann ohne Inspiration das nicht zuerst auffinden, was unter dem Titel «Aus der Akasha-Chronik» mitgeteilt ist. Empfängt man es aber durch Mitteilung, dann kann man es einsehen durch das",
      "ganz gewöhnliche logische Urteil. Niemand sollte behaup­ten: es würden da Dinge behauptet, die man ohne Inspira­tion nicht logisch begreifen könne. Man findet sie nicht des­halb unbegreiflich, weil man nicht inspiriert ist, sondern nur, weil man nicht genügend nachdenken will. - Erhält man also solche Wahrheiten mitgeteilt, dann erregen sie in der Seele durch ihre eigene Kraft die Inspiration.",
      "Man muß nur versuchen, wenn man solcher Inspiration teilhaftig wer­den will, diese Erkenntnisse nicht nüchtern und verstandesmäßig zu empfangen, sondern sich von dem Hochschwung der Ideen in alle nur möglichen Gefühlserlebnisse versetzen lassen. Und wie sollte man dies nicht können!",
      "Kann das Gefühl stumpf bleiben, wenn man die überwältigenden Vorgänge im Geiste vor sich vorüberziehen läßt, wie die Erde sich aus Mond, Sonne und Saturn entwickelt hat, oder wenn man die unendlichen Tiefen der Menschennatur durch eine Erkenntnis seines Äther-, Astralleibes usw. durchschaut? Man möchte fast sagen : schlimm genug für einen solchen, welcher in Nüchternheit solche Gedankengebäude erleben kann.",
      "Denn erlebte er sie nicht in Nüch­ternheit, sondern durchlebte er alle durch sie möglichen Gefühlsspannungen und Gefühlslösungen, alle Steigerun­gen und Krisen, alle Fortschritte und Rückschritte, alle Ka­tastrophen und Verkündigungen : dann eben würde in ihm der Mutterboden zur Inspiration selbst zubereitet. Aller­dings wird man das notwendige Leben in Gefühlen gegen­über solchen Mitteilungen aus einer höheren Welt nur wirk­lich entfalten können, wenn man Übungen solcher Art, wie sie oben angedeutet sind, macht.",
      "Wer alle seine Gefühls­kräfte an die äußere sinnliche Wahrnehmungswelt wendet, dem werden die Erzählungen aus einer höheren Welt als",
      "«trockene Begriffe», als «graue Theorie » erscheinen. Er wird niemals begreifen können, warum es dem andern warm ums Herz wird, wenn er die Mitteilungen der Ge­heimwissenschaft vernimmt, während er doch «kühl bis ans Herz hinan» bleibt. Er wird sogar sagen: «Das ist doch alles nur für den Verstand, das ist intellektuell; ich möchte etwas für das Gemüt.» Er sagt sich aber nicht, daß es an ihm liegt, daß sein Herz kalt bleibt.",
      "Viele unterschätzen noch immer die Gewalt dessen, was in diesen Mitteilungen aus einer höheren Welt allein schon verborgen liegt. Und im Zusammenhange damit überschät­zen sie allerlei andere Übungen und Prozeduren. Ja, was nützt es mir, sagen sie, wenn mir andere erzählen, wie es in höheren Welten aussieht: ich möchte doch selbst da hinein­schauen. Solchen fehlt nur zumeist die Geduld, sich immer wieder und wieder in solche Erzählungen aus höheren Wel­ten zu vertiefen. Täten sie es, dann würden sie sehen, wel­che Zündekraft diese «bloßen Erzählungen» haben, und wie wirklich die eigene Inspiration angeregt wird, wenn man die Inspirationen anderer mitgeteilt erhält. - Gewiß, es müssen zum «Lernen» andere Übungen hinzukommen, wenn der Schüler rasche Fortschritte in dem Erleben der höheren Welten machen will; es sollte aber niemand die unbegrenzt große Bedeutung gerade des «Lernens» unter­schätzen. Und jedenfalls kann niemandem Hoffnung gege­ben werden, daß er durch irgendwelche Übungen rasche Eroberungen in den höheren Welten machen werde, der es nicht zugleich über sich bringt : unablässig sich in die Mit­teilungen zu vertiefen, die, rein erzählend, von den Vorgän­gen und Wesen der höheren Welten von berufener Seite gemacht werden. - Dadurch, daß gegenwärtig solche Mitteilungen",
      "in der Literatur und in Vorträgen usw. gemacht werden, und daß auch die ersten Andeutungen gegeben werden über die Übungen, welche zur Erkenntnis höherer Welten führen (zum Beispiel sind eben die Darstellungen in «Wie erlangt man Erkenntnisse der höheren Welten?» solche erste Andeutungen), kann man jetzt einiges von dem erfahren, was ehedem nur in streng geschlossenen Geheimschulen mitgeteilt worden ist. Wie schon öfters erwähnt worden ist, rührt eine solche Veröffentlichung von den Verhältnissen in unserer Zeit her und muß geschehen. Es muß aber immer wieder auch das andere betont werden, daß dadurch zwar Erleichterungen in bezug auf das Aneig­nen des Geheimwissens geschaffen sind, daß aber die siche­re Führung durch den erfahrenen Geheimlehrer doch noch nicht völlig zu ersetzen ist.",
      "Die Erkenntnis durch Inspiration führt den Menschen zum Erleben der Vorgänge in den unsichtbaren Welten, also zum Beispiel der Entwickelung des Menschen, derjenigen der Erde und ihrer planetarischen Verkörperungen; kom­men aber innerhalb dieser höheren Welten nicht bloß Vorgänge, sondern Wesen in Betracht, dann muß die Intuition als Erkenntnisart eintreten. Was durch solche Wesen geschieht, das erkennt man im Bilde durch die Imagination, den Ge­setzen und Verhältnissen nach durch die Inspiration; will man den Wesen selbst gegenübertreten, dann braucht man die Intuition. - Wie sich die Inspiration hineingliedert in die Welt der Imaginationen, wie sie die letzteren durch­dringt als eine «geistige Musik» und dadurch das Aus­drucksmittel der durch die Intuition zu erkennenden We­sen wird, davon soll noch gesprochen werden. Dann wird auch die Intuition selbst behandelt werden. Hier soll nur",
      "noch darauf hingewiesen werden, daß dasjenige, was man in der Geheimwissenschaft als «Intuition» bezeichnet, nichts zu tun hat mit dem, wofür man gegenwärtig oft im populären Sprachgebrauch das Wort «Intuition» anwen­det. Man bezeichnet so einen mehr oder weniger unsiche­ren «Einfall» im Gegensatz zu einer klaren, folgerichtig gewonnenen Verstandes- oder Vernunfterkenntnis. In der Geheimwissenschaft ist die «Intuition» nichts Unklares und Unsicheres, sondern eine hohe Erkenntnisart, voll der lichtesten Klarheit und der unbezweifelbarsten Sicherheit."
    ],
    "sentences": [
      [
        "- Die Stufen der höheren Erkenntnis"
      ],
      [
        "Aus der Schilderung der Imagination ist ersichtlich gewor­den, wie durch sie der Geheimschüler den Boden der äuße­ren sinnlichen Erlebnisse verläßt.",
        "In einem noch viel höhe­ren Grade ist dieses der Fall in der Inspiration."
      ],
      [
        "Bei ihr liegt dem Vorstellen noch viel weniger von dem zugrunde, was man als eine äußere Anregung bezeichnen kann.",
        "Der Mensch muß da in sich selbst die Kraft finden, welche es ihm mög­lich macht, über etwas sich Vorstellungen zu bilden."
      ],
      [
        "Er muß in einem viel höheren Grade innerlich tätig sein, als dies bei der äußeren Erkenntnis der Fall ist.",
        "Bei dieser gibt er sich eben den äußeren Eindrücken hin, und sie verursa­chen ihm die Vorstellungen."
      ],
      [
        "Diese Hingabe fällt bei der In­spiration weg.",
        "Es liefern nunmehr keine Augen Farben, keine Ohren Töne usw.",
        "Aller Inhalt des Vorstellens muß gewissermaßen durch eigene Tätigkeit, also durch rein geistig-seelische Vorgänge geschaffen werden."
      ],
      [
        "Und in dasje­nige, was so der Mensch durch die Tätigkeit seines Innern schafft, muß sich die Offenbarung der höheren wirklichen Welt hineinprägen.",
        "Ein eigenartiger Widerspruch scheint in einer solchen Beschreibung der höheren Erkenntniswelt aufzutreten."
      ],
      [
        "Der Mensch soll in einer gewissen Art der Schöpfer seiner Vorstellungen sein; und doch dürfen diese Vorstellungen selbstverständlich nicht seine Geschöpfe sein; sondern durch sie müssen sich die Vorgänge der hö­heren Welt ebenso zum Ausdrucke bringen, wie sich in den Wahrnehmungen der Augen, Ohren usw. die Vorgänge der niederen Welt zum Ausdrucke bringen.",
        "Es ist das aber ein Widerspruch, der sich in der Schilderung dieser Erkenntnisart finden muß."
      ],
      [
        "Denn das ist es gerade, was sich"
      ],
      [
        "der Geheimschüler auf dem Wege zur Inspiration aneignen muß, daß er auf dem Wege seiner inneren Tätigkeit etwas zustande bringt, wozu er in dem gewöhnlichen Leben von außen gezwungen wird. - Warum verlaufen im gewöhnli­chen Leben die Vorstellungen nicht willkürlich?",
        "Weil der Mensch sich bei seinem Vorstellen nach den äußeren Ge­genständen richten muß.",
        "Alle Willkür des «Ich» fällt weg, weil die Gegenstände sagen: so oder so sind wir.",
        "Da spre­chen die Gegenstände, wie sie vorgestellt werden sollen, das «Ich » hat nichts darüber zu bestimmen.",
        "Wer sich den Gegenständen nicht fügen will, der stellt sich eben Unrich­tiges vor; und er würde bald gewahr werden, wie wenig er damit in der Welt zurechtkäme.",
        "Man kann dieses notwen­dige Verhalten des Menschen zu den Dingen der Außen­welt in der Erkenntnis mit dem Ausdruck «selbstlos» be­zeichnen.",
        "Der Mensch muß sich «selbstlos» zu den Din­gen verhalten.",
        "Und die Außenwelt ist sein Lehrmeister in dieser Selbstlosigkeit.",
        "Sie benimmt ihm alle Illusionen, alle Phantastereien, alle unlogischen Urteile, alles Unsachliche, indem sie ihm einfach ihr richtiges Bild vor die Sinne stellt."
      ],
      [
        "Will der Mensch sich für die Inspiration vorbereiten, so muß er sein Inneres so weit bringen, daß ihm diese Selbstlosigkeit eigen ist, auch wenn nichts von außen dazu zwingt.",
        "Er muß innerlich schaffen lernen, jedoch so, daß sein «Ich» bei diesem Schaffen nicht im geringsten eine ei­genmächtige Rolle spielt.",
        "Die Schwierigkeiten, welche in Betracht kommen, um eine solche Selbstlosigkeit zu errin­gen, werden um so deutlicher sichtbar, je besser man be­rücksichtigt, welche Seelenkräfte für die Inspiration beson­ders in Betracht kommen. - Man unterscheidet die drei"
      ],
      [
        "Grundkräfte des seelischen Lebens: Vorstellen, Fühlen und Wollen.",
        "Bei dem gewöhnlichen Sinneserkennen sind die Vorstellungen durch die äußeren Gegenstände angeregt.",
        "Und durch diese von außen angeregten Vorstellungen be­kommen auch das Fühlen und das Wollen ihre bestimmten Richtungen."
      ],
      [
        "Der Mensch sieht zum Beispiel einen Gegen­stand; dieser bereitet ihm Lust, infolgedessen begehrt er die betreffende Sache.",
        "Die Lust sitzt im Gefühle; durch die­ses wird der Wille erregt, wie es selbst sein Gepräge von dem Vorstellen erhalten hat."
      ],
      [
        "Der letzte Grund aber von Vorstellen, Fühlen und Wollen ist der äußere Gegenstand. - Ein anderer Fall wäre dieser.",
        "Ein Mensch erlebt ein Er­eignis.",
        "Dieses bereitet ihm Angst.",
        "Er läuft von dem Schauplatze des Ereignisses hinweg."
      ],
      [
        "Auch hier sind die äußeren Vorgänge der erste Grund; sie kommen durch die Sinne zur Wahrnehmung, werden Vorstellungen, das Gefühl der Angst stellt sich ein; und der Wille - der sich im Davonlaufen verwirklicht - ist die Folge.",
        "Bei der Inspiration fällt ein äußerer Gegenstand in dieser Form weg."
      ],
      [
        "Die Sinne kommen für eine Wahrnehmung nicht in Betracht.",
        "Sie also können auch nicht die Anreger von Vorstellungen sein.",
        "Von dieser Seite aus wird auf Fühlen und Wollen kein Ein­fluß ausgeübt. - Nun sind es aber gerade diese beiden, aus denen, wie aus einem Mutterboden, bei der Inspiration in­nerlich die Vorstellungen aufsteigen, gleichsam herauswachsen."
      ],
      [
        "Und es werden wahre Vorstellungen erwachsen, wenn der Mutterboden ein gesunder ist, Irrtümer und Wahngebilde, wenn er ein ungesunder ist."
      ],
      [
        "So gewiß als die Inspirationen, welche aus einem gesun­den Fühlen und Wollen entspringen, Offenbarungen einer höheren Welt sein können, so gewiß entspringen aus einem"
      ],
      [
        "wüsten Fühlen und Wollen die Irrtümer, Täuschungen und Phantastereien über eine höhere Welt."
      ],
      [
        "Die Geheimschulung stellt sich deshalb die Aufgabe, dem Menschen die Mittel zu zeigen, welche ihn befähigen, seine Gefühle und seine Willensimpulse zu gesund-fruchtbaren für die Inspiration zu machen.",
        "Wie in allen Dingen der Ge­heimschulung hat man es auch hier mit einer intimen Rege­lung und Gestaltung des Seelenlebens zu tun."
      ],
      [
        "Man muß sich zunächst gewisse Gefühle aneignen, die man im ge­wöhnlichen Leben nur in einem geringen Grade kennt.",
        "Es sollen hier einige von diesen Gefühlen angedeutet werden.",
        "Zu den wichtigsten gehört eine höhere Empfindlichkeit gegenüber von «wahr » und «unwahr», von « richtig »und «unrichtig»."
      ],
      [
        "Gewiß hat ja auch der gewöhnliche Mensch ähnliche Gefühle.",
        "Sie müssen aber eben bei dem Geheimschüler in einem viel höheren Maße ausgebildet wer­den.",
        "Man nehme an, jemand begehe einen logischen Feh­ler : ein anderer sieht diesen Fehler ein, und er stellt die Sa­che richtig."
      ],
      [
        "Man mache sich klar, wie groß der Anteil des Urteiles, des Verstandes bei einem solchen Richtigstellen ist und wie gering das Gefühl der Lust beim Richtigen, der Unlust beim Unrichtigen.",
        "Wohlgemerkt, es soll durchaus nicht behauptet werden, daß die Lust und entsprechend die Unlust gar nicht vorhanden seien."
      ],
      [
        "Aber der Grad, in dem sie im gewöhnlichen Leben vorhanden sind, muß sich in der Geheimschulung ins Unbegrenzte steigern.",
        "Ganz syste­matisch muß der Geheimschüler die Aufmerksamkeit auf sein Seelenleben lenken : und er muß es dahin bringen, daß ihm das logisch Unrichtige eine Quelle des Schmerzes wird, der durchaus nicht hinter einem physischen Schmerze zurückbleibt; und in umgekehrter Art muß ihm das « Richti­ge »"
      ],
      [
        "wirkliche Freude oder Lust bereiten.",
        "Wo also ein an­derer nur seinen Verstand, seine Urteilskraft in Bewegung bringt, muß der Geheimschüler lernen, die ganze Stufen­folge von Gefühlen, vom Schmerz bis zum Enthusiasmus, von der wehevollen Spannung bis zur entzückenden Lö­sung im Besitz der Wahrheit zu durchleben."
      ],
      [
        "Ja, er muß et­was wie Haß empfinden lernen gegen dasjenige, was beim «normalen » Menschen nur als ein nüchternkaltes «Un­richtiges » erlebt wird; er muß eine Liebe zur Wahrheit in sich entwickeln, welche einen ganz persönlichen Charakter trägt; so persönlich, so warm wie der Liebende der Gelieb­ten gegenüber empfindet. - Man wird ja gewiß auch in den Kreisen unserer «Gebildeten» vielfach von der «Liebe zur Wahrheit» reden; doch ist das, was man da meint, eben gar nicht zu vergleichen mit dem, was der Geheimschüler in stiller, innerer Seelenarbeit nach dieser Richtung durchma­chen muß.",
        "Er muß sich geduldig immer wieder probeweise dieses oder jenes «Wahre», dieses oder jenes «Falsche» vor­legen; und sich der Sache hingeben, um nicht bloß seine Urteilskraft zu schulen, die nüchtern unterscheidet zwischen «wahr» und «falsch »; sondern er muß zu dem allen ein ganz persönliches Verhältnis gewinnen. - Es ist durchaus richtig, daß der Mensch im Anfange einer solchen Schu­lung in das verfallen kann, was man «Überempfindlichkeit» nennen mag."
      ],
      [
        "Ein unrichtiges Urteil, das er in seiner Umge­bung hört, eine Inkonsequenz usw. können ihm einen schier unerträglichen Schmerz bereiten. - Es muß deshalb bei der Schulung auf diese Sache Rücksicht genommen werden.",
        "Denn geschähe das nicht : dann könnten sich aller­dings große Gefahren für das Seelengleichgewicht des Schülers ergeben."
      ],
      [
        "Wird darauf gesehen, daß der Charakter"
      ],
      [
        "fest bleibt, dann können Stürme im Seelenleben sich abspie­len, und der Mensch hat doch die Kraft, in harmonischer Miene und Gebärde mit der Außenwelt zu leben.",
        "Ein Feh­ler ist in jedem Falle gemacht, wo der Geheimschüler zu ei­nem Gegensatze gegenüber der Außenwelt gebracht wird, so daß er diese unerträglich findet oder gar aus ihr fliehen will."
      ],
      [
        "Die höhere Gefühlswelt darf sich nicht auf Kosten des gleichmäßigen Wirkens und Arbeitens in der Außenwelt entwickeln; deshalb muß der inneren Erhöhung des Ge­fühlslebens eine Stärkung der Widerstandskraft gegenüber den äußeren Eindrücken entsprechen.",
        "Die praktische Geheimschulung weist daher den Menschen an, niemals die obengenannten Übungen zur Schulung seiner Gefühlswelt zu unternehmen, ohne sich zugleich auch nach der Rich­tung zu entwickeln, daß er ein Verständnis dafür gewinnen könne, was das Leben an Toleranzempfindung von dem Menschen fordert."
      ],
      [
        "Er muß zugleich in sich den lebendigsten Schmerz empfinden können, wenn zum Beispiel ein Mensch ein unrichtiges Urteil abgibt, und vollkommen tolerant sein können gegen diesen Menschen, weil der Gedanke in der Seele ebenso lebhaft da ist : dieser Mensch muß so urtei­len, und es ist mit seinem Urteile wie mit einer Tatsache zu rechnen. - Richtig ist allerdings, daß das Innere des Ge­heimwissenschafters sich immer mehr und mehr zu einem Doppelleben umgestalten wird.",
        "Immer reichere Vorgänge werden sich in seiner Seele abspielen bei seiner Pilgerschaft durch das Leben, immer selbständiger gegenüber dem, was die äußere Welt gibt, wird eine zweite Welt."
      ],
      [
        "Aber dieses Doppelleben wird gerade das Fruchtbare sein für die echte Lebenspraxis.",
        "Was sich dadurch einstellt, ist Schlagfertig­keit des Urteiles, Treffsicherheit in bezug auf die Entschlüsse."
      ],
      [
        "Wo derjenige, der einer solchen Schulung fernesteht, lange Gedankenketten durchmachen muß, zwischen Entschluß und Ratlosigkeit hin- und hergetrieben wird, da wird der Geheimwissenschafter rasch die Lagen des Lebens überschauen, dem gewöhnlichen Blicke verborgene Zu­sammenhänge schnell aufdecken usw.",
        "Es gehört für ihn dann oft sogar viel Geduld dazu, sich in die langsame Art hineinzubegeben, wie ein anderer etwas begreifen kann, während bei ihm doch dieses Begreifen pfeilschnell vor sich geht."
      ],
      [
        "Nun ist bisher nur gesprochen von den Eigenschaften, welche das Gefühlsleben erhalten muß, damit die Inspira­tion in der richtigen Art eintreten könne.",
        "Die andere Frage ist die: Wie werden die Gefühle fruchtbar, so daß sie aus sich wirkliche, der Inspirationswelt angehörige Vorstellungen gebären?",
        "Will man das einsehen, was die Geheimwissenschaft als Antwort auf diese Frage zu geben hat, so muß man sich mit der Tatsache bekannt machen, daß des Menschen Seelenleben immer einen gewissen Schatz von Gefühlen hat, welche über das Maß dessen hinausgehen, was durch die sinnlichen Wahrnehmungen angeregt wird.",
        "Der Mensch fühlt gleichsam mehr, als das ist, wozu ihn die Dinge zwingen.",
        "Nur wird in dem gewöhnlichen Leben die­ses Übermaß in einer solchen Richtung angewendet, wel­che durch die Geheimschulung in eine andere verwandelt werden muß.",
        "Man nehme zum Beispiel ein Angst- oder Furchtgefühl.",
        "Man wird sich leicht klarmachen können, daß in vielen Fällen die Furcht oder die Angst größer ist, als sie sein würde, wenn sie einem entsprechenden äußeren Vorgange ganz angemessen wäre.",
        "Man stelle sich nun vor : der Geheimschüler arbeite energisch an sich, um in keinem ihm"
      ],
      [
        "vorkommenden Falle größere Furcht oder Angst zu haben, als gegenüber den entsprechenden äußeren Vorgängen wirklich gerechtfertigt ist.",
        "Nun wird ein gewisses Maß von Furcht oder Angst immer aus der Aufwendung von Seelenkraft erzeugt.",
        "Diese Seelenkraft geht tatsächlich dadurch verloren, daß eben Furcht oder Angst erzeugt werden.",
        "Der Geheimschüler erspart diese Seelenkraft wirklich, wenn er sich die Furcht oder die Angst - und anderes - versagt.",
        "Und sie bleibt ihm für etwas anderes verfügbar.",
        "Wieder­holt er solche Vorgänge oft, so wird aus den fortlaufend er­sparten Seelenkräften ein innerer Schatz gebildet; und der Geheimschüler wird bald erleben, daß ihm aus solchen Ge­fühlsersparnissen die Keime zu Vorstellungen erwachsen, welche Offenbarungen des höheren Lebens zum Ausdrucke bringen.",
        "Dergleichen kann man im gewöhnlichen Sinne nicht «beweisen »; man kann nur dem Geheimschüler die Anweisung geben: tue dies oder jenes - und er wird, wenn er die Sache ausführt, schon sehen, daß sich die untrügli­chen Früchte einstellen."
      ],
      [
        "Einer ungenauen Betrachtung des soeben Geschilderten könnte es leicht als ein Widerspruch erscheinen, daß auf der einen Seite eine Bereicherung der Gefühlswelt gefordert wird, indem durch das, was sonst nur das Verstandesurteil wachruft, Gefühle der Lust, des Schmerzes usw. erregt werden sollen - und auf der anderen Seite gerade von Ersparnissen an Gefühlen gesprochen wird.",
        "Dieser Widerspruch ver­schwindet sofort, wenn man bedenkt, daß die Ersparnisse bei denjenigen Gefühlen gemacht werden sollen, welche durch die äußeren Sinne angeregt werden.",
        "Eben das, was da erspart wird, erscheint als Bereicherung gegenüber den geistigen Erlebnissen.",
        "Und es ist durchaus richtig, daß auf"
      ],
      [
        "diese Art an der sinnlichen Wahrnehmungswelt ersparte Gefühle nicht nur auf dem anderen Gebiete freiwerden, sondern daß sie sich auf diesem Gebiete als schöpferisch er­weisen. - Sie schaffen das Material zu den Vorstellungen, in denen sich die geistige Welt offenbart."
      ],
      [
        "Es wurde allerdings nicht besonders weit gehen, wenn man nur bei solchen Ersparnissen stehenbleiben wollte, wie sie oben angedeutet worden sind.",
        "Zu größeren Erfolgen ist noch mehr nötig.",
        "Man muß der Seele einen noch weit grö­ßeren Schatz von Gefühlerzeugender Kraft zuführen, als auf diesem Wege möglich ist.",
        "Man muß zum Beispiel sich ge­wissen äußeren Eindrücken probeweise aussetzen und sich dann die Gefühle ganz versagen, die im sogenannten «nor­malen » Zustande eintreten.",
        "Man muß sich zum Beispiel ei­nem Ereignisse gegenüberstellen, welches «normalerwei­se » die Seele erregt, und sich diese Erregung ganz und gar verbieten.",
        "Man kann das so machen, daß man sich tatsäch­lich einem solchen Ereignisse gegenüberstellt oder sich bloß mit der Vorstellung behilft.",
        "Das letztere ist sogar für die fruchtbare Geheimschulung das bessere.",
        "Da der Schü­ler ja in die Imagination eingeweiht wird, entweder vor sei­ner Vorbereitung zur Inspiration oder mit der letzteren gleichzeitig, so muß er eigentlich imstande sein, sich imagi­nativ ein Ereignis mit derselben Kraft vor die Seele zu stel­len, wie wenn es wirklich da wäre. - Wenn nun in langer innerer Arbeit der Schüler sich immer wieder und wieder Dingen und Vorgängen aussetzt und es sich verbietet, entsprechende «normale » Gefühle zuhaben, so wird in sei­ner Seele der Mutterboden für die Inspiration geschaffen. - Nur als Zwischenbemerkung sei hier angeführt, daß derje­nige, welcher eine solche Schulung zur Inspiration beschreibt,"
      ],
      [
        "es voll würdigen kann, wenn vom Standpunkte unserer ge­genwärtigen Zeitbildung aus manches gegen eine solche Beschreibung eingewendet wird.",
        "Und man kann da nicht nur das oder jenes einwenden, sogar kann man überlegen lächeln und sagen : «Inspiration kann doch nicht pedan­tisch anerzogen werden; sie ist eine Naturgabe des Genies. »Ja, gewiß, vom Standpunkte dieser Zeitbildung mag es recht komisch anmuten, wenn viel über die Heranbildung dessen geredet wird, bei dem diese Bildung von einer Er­klärung nichts wissen will; aber diese Zeitbildung ist sich nicht bewußt, wie wenig sie ihre eigenen Gedankengänge zu Ende zu denken vermag."
      ],
      [
        "Wer es einem Bekenner dieser Zeitbildung zumuten wollte, daß er daran glauben solle, ir­gendein höher entwickeltes Tier habe sich nicht langsam entwickelt, sondern sei «plötzlich » da gewesen : der würde bald hören, daß der im modernen Sinne Gebildete an ein solches «Wunder » nicht glaube.",
        "So etwas sei «Aberglau­ben » Nun, auf dem Gebiete des Seelenlebens ist aber ein solcher modern Gebildeter, ganz im Stile seiner eigenen Ansichten, ein von krassem Aberglauben Befallener."
      ],
      [
        "Er will nämlich nicht daran denken, daß sich eine vollkommenere Seele auch entwickelt haben muß, daß sie nicht plötzlich als eine Naturgabe da sein könne.",
        "Äußerlich erscheint allerdings manches Genie wie «aus dem Nichts » geboren, auf unerklärliche Weise da; doch erscheint es eben so nur für den materialistischen Aberglauben; der Geisteswissenschaf­ter weiß, daß eine genialische Veranlagung, die in einem Leben bei einem Menschen wie aus dem Nichts heraus ge­boren ist, einfach die Folge von dessen Erziehung zur In­spiration in einem früheren Erdenleben ist. - Auf theoreti­schem Gebiete ist der materialistische Aberglaube schlimm;"
      ],
      [
        "bei weitem schlimmer aber ist er noch auf einem solchen praktischen Gebiete wie hier.",
        "Da er annimmt, daß die Ge­nies in alle Zukunft «vom Himmel fallen » müssen, küm­mert er sich nicht um derlei « okkultistischen Unfug » oder solch «phantastische Mystik», die von Vorbereitung zur Inspiration sprechen.",
        "Dadurch hält aber der Aberglaube der Materialisten den wahren Fortschritt der Menschheit auf.",
        "Er sorgt nicht dafür, daß die in den Menschen schlum­mernden Fähigkeiten entwickelt werden."
      ],
      [
        "In Wirklichkeit sind nämlich oft diejenigen, welche sich Fortschrittler und Freidenker nennen, solche, welche die Feinde der wahren Fortentwickelung sind.",
        "Doch dies soll"
      ],
      [
        "- wie gesagt - nur eine Zwischenbemerkung sein, die not­wendig ist mit Rücksicht auf das Verhältnis der Geheimwissenschaft zur gegenwärtigen Zeitbildung."
      ],
      [
        "Nun wurden die Seelenkräfte, welche durch das gekenn­zeichnete Sich-Versagen der «normalen» Gefühle als Schatz im Innern des Schülers sich aufspeichern, gewiß, auch ohne daß etwas anderes zu Hilfe käme, sich in Inspirationen um­setzen.",
        "Und der Geheimschüler wurde erleben, wie in sei­ner Seele wahre Vorstellungen aufsteigen, welche Erleb­nisse in höheren Welten darstellen.",
        "Mit den einfachsten Er­fahrungen übersinnlicher Vorgänge wurde die Sache beginnen, und langsam käme Komplizierteres und Höheres zum Vorschein, wenn der Schüler in der angedeuteten Richtung innerlich weiterlebte. - In Wirklichkeit wäre aber eine solche Geheimschulung heute ganz unpraktisch, und sie wird daher wohl nirgends durchgeführt, wo man ernst­haft zu Werke geht.",
        "Wollte nämlich der Schüler auf diese Art alles «aus sich selbst heraus» entwickeln, was die Inspiration geben kann: er würde ganz sicher dazu kommen,"
      ],
      [
        "alles so aus sich «herauszuspinnen», was je zum Beispiel auch hier über das Wesen des Menschen, über des Men­schen Leben nach dem Tode, über die Entwickelung des Menschengeschlechts und der Planeten usw. gesagt wor­den ist.",
        "Aber ein solcher Schüler würde eben unermeßlich lange Zeiträume dazu brauchen."
      ],
      [
        "Es wäre so, wie wenn zum Beispiel jemand die ganze Geometrie aus sich selbst heraus­spinnen wollte, ohne Rücksicht darauf, was Menschen vor ihm auf diesem Gebiete schon gearbeitet haben.",
        "Gewiß, «in der Theorie » ist so etwas durchaus möglich."
      ],
      [
        "In der Praxis es auszuführen wäre Torheit.",
        "Auch in der Geheimwissen­schaft verfährt man nicht so, sondern man läßt sich durch einen Lehrer diejenigen Dinge überliefern, welche durch inspirierte Vorgänger für die Menschheit errungen worden sind."
      ],
      [
        "Diese Überlieferung muß gegenwärtig die Grundlage abgeben für die eigene Inspiration.",
        "Dasjenige, was in der einschlägigen Literatur und in Vorträgen usw. heute aus dem Gebiet der Geheimwissenschaft geboten wird, das kann durchaus eine solche Inspirationsgrundlage abgeben."
      ],
      [
        "Es sind zum Beispiel die Lehren über die verschiedenen Grundteile des Menschen (physischer Leib, Ätherleib, Astralleib usw.), die Erkenntnisse über das Leben nach dem Tode bis zu einer neuen Verkörperung, dann zum Bei­spiel alles, was unter dem Titel «Aus der Akasha-Chronik» gedruckt wurde.",
        "Man muß nämlich gegenüber der Inspira­tion durchaus festhalten, daß man sie braucht zum Auffin­den und Selbsterleben der höheren Wahrheiten, nicht aber zum Verstehen derselben."
      ],
      [
        "Man kann ohne Inspiration das nicht zuerst auffinden, was unter dem Titel «Aus der Akasha-Chronik» mitgeteilt ist.",
        "Empfängt man es aber durch Mitteilung, dann kann man es einsehen durch das"
      ],
      [
        "ganz gewöhnliche logische Urteil.",
        "Niemand sollte behaup­ten: es würden da Dinge behauptet, die man ohne Inspira­tion nicht logisch begreifen könne.",
        "Man findet sie nicht des­halb unbegreiflich, weil man nicht inspiriert ist, sondern nur, weil man nicht genügend nachdenken will. - Erhält man also solche Wahrheiten mitgeteilt, dann erregen sie in der Seele durch ihre eigene Kraft die Inspiration."
      ],
      [
        "Man muß nur versuchen, wenn man solcher Inspiration teilhaftig wer­den will, diese Erkenntnisse nicht nüchtern und verstandesmäßig zu empfangen, sondern sich von dem Hochschwung der Ideen in alle nur möglichen Gefühlserlebnisse versetzen lassen.",
        "Und wie sollte man dies nicht können!"
      ],
      [
        "Kann das Gefühl stumpf bleiben, wenn man die überwältigenden Vorgänge im Geiste vor sich vorüberziehen läßt, wie die Erde sich aus Mond, Sonne und Saturn entwickelt hat, oder wenn man die unendlichen Tiefen der Menschennatur durch eine Erkenntnis seines Äther-, Astralleibes usw. durchschaut?",
        "Man möchte fast sagen : schlimm genug für einen solchen, welcher in Nüchternheit solche Gedankengebäude erleben kann."
      ],
      [
        "Denn erlebte er sie nicht in Nüch­ternheit, sondern durchlebte er alle durch sie möglichen Gefühlsspannungen und Gefühlslösungen, alle Steigerun­gen und Krisen, alle Fortschritte und Rückschritte, alle Ka­tastrophen und Verkündigungen : dann eben würde in ihm der Mutterboden zur Inspiration selbst zubereitet.",
        "Aller­dings wird man das notwendige Leben in Gefühlen gegen­über solchen Mitteilungen aus einer höheren Welt nur wirk­lich entfalten können, wenn man Übungen solcher Art, wie sie oben angedeutet sind, macht."
      ],
      [
        "Wer alle seine Gefühls­kräfte an die äußere sinnliche Wahrnehmungswelt wendet, dem werden die Erzählungen aus einer höheren Welt als"
      ],
      [
        "«trockene Begriffe», als «graue Theorie » erscheinen.",
        "Er wird niemals begreifen können, warum es dem andern warm ums Herz wird, wenn er die Mitteilungen der Ge­heimwissenschaft vernimmt, während er doch «kühl bis ans Herz hinan» bleibt.",
        "Er wird sogar sagen: «Das ist doch alles nur für den Verstand, das ist intellektuell; ich möchte etwas für das Gemüt.» Er sagt sich aber nicht, daß es an ihm liegt, daß sein Herz kalt bleibt."
      ],
      [
        "Viele unterschätzen noch immer die Gewalt dessen, was in diesen Mitteilungen aus einer höheren Welt allein schon verborgen liegt.",
        "Und im Zusammenhange damit überschät­zen sie allerlei andere Übungen und Prozeduren.",
        "Ja, was nützt es mir, sagen sie, wenn mir andere erzählen, wie es in höheren Welten aussieht: ich möchte doch selbst da hinein­schauen.",
        "Solchen fehlt nur zumeist die Geduld, sich immer wieder und wieder in solche Erzählungen aus höheren Wel­ten zu vertiefen.",
        "Täten sie es, dann würden sie sehen, wel­che Zündekraft diese «bloßen Erzählungen» haben, und wie wirklich die eigene Inspiration angeregt wird, wenn man die Inspirationen anderer mitgeteilt erhält. - Gewiß, es müssen zum «Lernen» andere Übungen hinzukommen, wenn der Schüler rasche Fortschritte in dem Erleben der höheren Welten machen will; es sollte aber niemand die unbegrenzt große Bedeutung gerade des «Lernens» unter­schätzen.",
        "Und jedenfalls kann niemandem Hoffnung gege­ben werden, daß er durch irgendwelche Übungen rasche Eroberungen in den höheren Welten machen werde, der es nicht zugleich über sich bringt : unablässig sich in die Mit­teilungen zu vertiefen, die, rein erzählend, von den Vorgän­gen und Wesen der höheren Welten von berufener Seite gemacht werden. - Dadurch, daß gegenwärtig solche Mitteilungen"
      ],
      [
        "in der Literatur und in Vorträgen usw. gemacht werden, und daß auch die ersten Andeutungen gegeben werden über die Übungen, welche zur Erkenntnis höherer Welten führen (zum Beispiel sind eben die Darstellungen in «Wie erlangt man Erkenntnisse der höheren Welten?» solche erste Andeutungen), kann man jetzt einiges von dem erfahren, was ehedem nur in streng geschlossenen Geheimschulen mitgeteilt worden ist.",
        "Wie schon öfters erwähnt worden ist, rührt eine solche Veröffentlichung von den Verhältnissen in unserer Zeit her und muß geschehen.",
        "Es muß aber immer wieder auch das andere betont werden, daß dadurch zwar Erleichterungen in bezug auf das Aneig­nen des Geheimwissens geschaffen sind, daß aber die siche­re Führung durch den erfahrenen Geheimlehrer doch noch nicht völlig zu ersetzen ist."
      ],
      [
        "Die Erkenntnis durch Inspiration führt den Menschen zum Erleben der Vorgänge in den unsichtbaren Welten, also zum Beispiel der Entwickelung des Menschen, derjenigen der Erde und ihrer planetarischen Verkörperungen; kom­men aber innerhalb dieser höheren Welten nicht bloß Vorgänge, sondern Wesen in Betracht, dann muß die Intuition als Erkenntnisart eintreten.",
        "Was durch solche Wesen geschieht, das erkennt man im Bilde durch die Imagination, den Ge­setzen und Verhältnissen nach durch die Inspiration; will man den Wesen selbst gegenübertreten, dann braucht man die Intuition. - Wie sich die Inspiration hineingliedert in die Welt der Imaginationen, wie sie die letzteren durch­dringt als eine «geistige Musik» und dadurch das Aus­drucksmittel der durch die Intuition zu erkennenden We­sen wird, davon soll noch gesprochen werden.",
        "Dann wird auch die Intuition selbst behandelt werden.",
        "Hier soll nur"
      ],
      [
        "noch darauf hingewiesen werden, daß dasjenige, was man in der Geheimwissenschaft als «Intuition» bezeichnet, nichts zu tun hat mit dem, wofür man gegenwärtig oft im populären Sprachgebrauch das Wort «Intuition» anwen­det.",
        "Man bezeichnet so einen mehr oder weniger unsiche­ren «Einfall» im Gegensatz zu einer klaren, folgerichtig gewonnenen Verstandes- oder Vernunfterkenntnis.",
        "In der Geheimwissenschaft ist die «Intuition» nichts Unklares und Unsicheres, sondern eine hohe Erkenntnisart, voll der lichtesten Klarheit und der unbezweifelbarsten Sicherheit."
      ]
    ]
  },
  {
    "order": 7,
    "title_de": "INSPIRATION UND INTUITION",
    "paragraphs": [
      "Wie man die Imagination ein geistiges Schauen nennen kann, so die Inspiration ein geistiges Hören. Man muß allerdings bei diesem Ausdrucke «Hören » sich darüber klar sein, daß damit ein Wahrnehmen gemeint ist, welches dem sinnlichen Hören in der physischen Welt noch viel ferner steht als das «Schauen» in der imaginativen (astralen) Welt dem Sehen mit den physischen Augen.",
      "Von den Licht- und Farbenerscheinungen der letzteren Welt kann man sagen : sie seien so, wie wenn die leuchtenden Oberflächen und die Farben der sinnlichen Gegenstände sich von diesen abhöben und von ihnen losgelöst frei im Raume schwebten. Dies gibt aber doch nur eine annähernde Vorstellung.",
      "Denn der Raum der imaginativen Welt ist keineswegs so wie derjenige der physischen. Wer sich also einbildete, daß er imaginative Farbenbilder vor sich habe, wenn er freischwebende Farbenflocken mit gewöhnlicher Raumausdehnung sieht, der ist im Irrtum.",
      "Dennoch ist aber die Bildung von solchen Farbenvorstellungen der Weg zum imaginativen Leben. Wer versucht, sich eine Blume vorzustellen, und dann in seiner Vorstellung alles beiseite läßt, was nicht Farbenvorstellung ist, so daß vor seiner Seele ein Bild schwebt wie die von der Blume abgezogene farbige Oberfläche, der kann durch solche Übungen allmählich zu einer Imagination gelangen.",
      "Dies Bild selbst ist noch keine solche Imagination, sondern ein mehr oder weniger vorbereitendes Phantasiegemälde. Imagination - das ist wirkliches astrales Erlebnis - wird es erst, wenn nicht nur die Farbe ganz abgehoben ist von dem Sinneseindrucke, sondern wenn auch die dreidimensionale Raumausdehnung sich völlig verloren",
      "hat. Daß dies letztere der Fall ist, kann nur durch ein gewisses Gefühl wahrgenommen werden. Zu beschreiben ist dieses Gefühl nur dadurch, daß man sagt, man fühlt sich nicht mehr außerhalb, sondern innerhalb des Farbenbildes, und man hat das Bewußtsein, daß man an seiner Entstehung teilnimmt.",
      "Wenn dies Gefühl nicht da ist, wenn man sich also der Sache gegenüberstehend glaubt wie einem sinnlichen Farbenbild gegenüber, dann hat man es noch nicht mit einer wirklichen Imagination, sondern mit etwas Phantastischem zu tun. Damit soll jedoch nicht gesagt sein, daß solche Phantasiegemälde ganz wertlos seien.",
      "Sie können nämlich ätherische Abbilder - gleichsam Schatten - wirklicher Strahler Tatsachen sein. Und als solchen kommt ihnen für die geheimwissenschaftliche Schulung immerhin einiger Wert zu. Sie können eine Brücke bilden zu den wahren astralen (imaginativen) Erlebnissen. - Eine gewisse Gefahr schließt ihre Beobachtung nur in sich, wenn der Beobachter an diesem Grenzgebiet zwischen Sinnlichem und Übersinnlichem seinen gesunden Menschenverstand nicht voll zur Anwendung bringt.",
      "Man soll nur nicht erwarten, daß irgend jemandem ein allgemeines Kennzeichen gegeben werden kann, wie er in diesem Grenzgebiete Illusion, Halluzination, Phantastik von Wirklichkeit unterscheiden könne. Bequem wäre ja eine solche allgemeine Regel.",
      "Aber Bequemlichkeit ist ein Wort, das der Geheimschüler in seinem Sprachschatze streichen sollte. - man kann nur sagen, daß derjenige, welcher sich für dieses Gebiet Klarheit der Unterscheidung aneignen will, schon in dem gewöhnlichen Leben der physischen Welt darauf bedacht sein muß. Wer in diesem gewöhnlichen Leben keine Sorgfalt darauf verwendet, scharf und klar zu denken, der wird beim Aufsteigen",
      "in höhere Welten allen möglichen Illusionen zum Opfer fallen. Man bedenke nur, wie viele Fallen dieses gewöhnliche Leben dem gesunden Urteile bietet. Wie oft kommt es doch vor, daß die Menschen nicht das ungetrübt sehen, was ist, sondern was sie zu sehen begehren. In wie vielen Fällen glauben die Menschen etwas, nicht weil sie erkannt haben, sondern weil es ihnen angenehm ist, zu glauben. Oder welche Irrtümer ergeben sich, weil man einer Sache nicht auf den Grund geht, sondern sich vorschnell ein Urteil bildet. Alle diese Gründe von Täuschungen im gewöhnlichen Leben könnten durch andere schier ins Unendliche vermehrt werden. Was für Streiche spielen Parteinahme, Leidenschaft usw. usw. einem gesunden Urteile. Wenn derlei Urteilstäuschungen im gewöhnlichen Leben störend und oft verhängnisvoll sind: für die Gesundheit des übersinnlichen Erlebens sind sie die denkbar größte Gefahr. Nicht eine allgemeine Regel kann der Geheimschüler als Leitfaden mit in höhere Welten erhalten, sondern lediglich die Anweisung, für seine gesunde Unterscheidungskraft, für sein freies, unabhängiges Urteil alles mögliche zu tun.",
      "Wenn der Beobachter höherer Welten einmal weiß, was wirklich Imagination ist, dann erhält er auch sehr bald die Empfindung, daß die bildet der astralen Welt nicht bloße Bilder, sondern die Kundgebungen geistiger Wesenheiten sind. Er lernt erkennen, daß er die imaginativen Bilder ebenso auf geistige oder seelische Wesenheiten zu beziehen hat wie die sinnlichen Farben auf sinnliche Dinge oder Wesenheiten. Im einzelnen wird er allerdings da noch viel zu lernen haben. Er wird unterscheiden müssen zwischen Farbengebilden, die wie undurchsichtig sind, und solchen, die ganz durchsichtig und wie in ihrem Innern ganz durchleuchtet",
      "sind. Ja, auch solche Gebilde wird er wahrnehmen, die ihr Farbenlicht gleichsam in ihrem Innern immer neu erzeugen, die also nicht nur ganz durchleuchtet und durchsichtig (transparent) sind, sondern die immerfort in sich selbst aufstrahlen. Und er wird die mehr undurchsichtigen Gebilde auf niedrige, die durchleuchteten auf mittlere Wesenheiten beziehen; die in sich aufstrahlenden Bilder werden ihm Kundgebungen höherer geistiger Wesenheiten sein.",
      "Will man die Wahrheit der imaginativen Welt treffen, so darf man den Begriff des geistigen Schauens nicht zu eng fassen. Denn es finden sich in dieser Welt nicht etwa bloß Licht- und Farbenwahrnehmungen, die sich also den Gesichtserlebnissen der physischen Welt vergleichen lassen, sondern auch Eindrücke von Wärme und Kälte, von Geschmack und Geruch, ja noch andere Erlebnisse der imaginativen «Sinne», für die es etwas ähnliches in der physischen Welt nicht gibt. Die Eindrücke des Warmen und Kalten sind in der imaginativen (astralen) Welt die Offenbarungen des Willens und der Absichten seelischer und geistiger Wesen. Ob ein solches Wesen etwas Gutes oder Böses bezweckt, das kommt in einer bestimmten Wärme- oder Kältewirkung zum Vorschein. Auch «schmecken» und «riechen » kann man die astralen Wesenheiten. - nur dasjenige, was in eigentlichem Sinne das Physische des Tones und Schalles ausmacht, fehlt fast ganz in der wirklich imaginativen Welt. In dieser Beziehung herrscht da lautlose Stille. Dafür aber bietet sich etwas ganz anderes dem in der geistigen Beobachtung Fortschreitenden dar, was sich mit dem Tönen und Klingen, mit Musik und Sprache der sinnlichen Welt vergleichen läßt. Und gerade dann tritt dieses Höhere auf, wenn alles Tönen und Klingen der äußeren",
      "physischen Welt völlig verstummt, ja wenn auch der geringste innere seelische Nachhall an dieses Gebiet der äußeren Welt zum Schweigen gekommen ist. Dann tritt für den Beobachter das ein, was man ein Verstehen der Bedeutung der imaginativen Erlebnisse nennen kann.",
      "Wollte man dasjenige, was hier erfahren wird, mit etwas in der physischen Welt vergleichen, so könnte man nur zur Verdeutlichung etwas heranziehen, was es in dieser Welt gar nicht gibt. Man versuche sich einmal vorzustellen, daß man wahrnehmen könnte die Gedanken und Gefühle eines Menschen, ohne seine Worte mit dem physischen Ohre zu hören, so wäre ein solches Wahrnehmen zu vergleichen mit jenem unmittelbaren Verstehen des Imaginativen, das man als «Hören » in geistigem Sinne bezeichnet.",
      "Das «Sprechende »sind die Farben- und Lichteindrücke. In dem Aufglänzen und Verlöschen, in der Farbenwandlung der Bilder offenbaren sich Harmonien und Disharmonien, welche die Gefühle, Vorstellungen und Gedanken seelischer und geistiger Wesenheiten enthüllen.",
      "Und wie sich der Ton beim physischen Menschen zum Worte steigert, wenn sich ihm der Gedanke einprägt, so steigern sich die Harmonien und Disharmonien der geistigen Welt zu Offenbarungen, welche wesenhafte Gedanken selbst sind. Dazu muß es allerdings «dunkel werden » in dieser Welt, wenn der Gedanke in seiner Unmittelbarkeit sich offenbaren soll.",
      "Das hier auftretende Erlebnis stellt sich so dar : Man sieht die hellen Farbentöne, das Rot, Gelb und Orange, ersterben und nimmt wahr, wie sich die höhere Welt durch Grün hindurch abdunkelt zum Blauen und Violetten; dabei erlebt man in sich selbst eine Steigerung der inneren Willensenergie. Man erlebt eine völlige Freiheit in bezug auf Ort und",
      "Zeit; man fühlt sich in Bewegung. Es sind gewisse Linienformen, Gestalten, die man erlebt. Doch nicht etwa so erlebt man sie, daß man sie vor sich in irgendeinem Raume gezeichnet sähe, sondern so, als ob man in fortwährender Bewegung mit seinem Ich jedem Linienschwung, jeder Gestaltung selbst folgte. Ja man fühlt das Ich als den Zeichner und zugleich als das Material, mit dem gezeichnet wird. Und jede Linienführung, jede Ortsänderung sind zugleich Erlebnis dieses Ich. Man lernt erkennen, daß man mit seinem bewegten Ich hineingeflochten ist in die schaffenden Weltenkräfte. Die Weltgesetze sind nun dem Ich nicht mehr etwas äußerlich Wahrgenommenes, sondern ein wirkliches Wundergewebe, an dem man spinnt. - die Geheimwissenschaft entwirft allerlei sinnbildliche Zeichnungen und Bilder. Wenn diese den Tatsachen wirklich entsprechen und nicht bloße ausgedachte Figuren sind, so liegen ihnen Erlebnisse des Beobachters in höheren Welten zugrunde, die in der oben beschriebenen Art anzusehen sind.",
      "So stellt sich die inspirierte Welt in die imaginierte hinein. Wenn die Imaginationen beginnen dem Beobachter in «stummer Sprache » ihre Bedeutungen zu enthüllen, dann geht innerhalb des Imaginativen die Welt der Inspiration auf.",
      "Von derjenigen Welt, in welche der geistige Beobachter auf diese Art eindringt, ist die physische eine Offenbarung. Was von dieser physischen Welt den Sinnen und dem auf sie beschränkten Verstand zugänglich ist, das ist nur die Außenseite. Um nur ein Beispiel anzuführen : die Pflanze, wie sie mit den physischen Sinnen und dem physischen Verstande beobachtet wird, ist nicht das vollständige Pflanzenwesen. Wer nur diese physische Pflanze kennt, der hat etwas Ähnliches vorliegen, wie ein Wesen haben würde, das",
      "den Fingernagel eines Menschen wahrnehmen könnte, dem aber die Wahrnehmung des Menschen selbst unzugänglich wäre. Bau und Wesenheit des Fingernagels können aber nur verstanden werden, wenn man sie aus der ganzen menschlichen Wesenheit erklärt. So ist in Wahrheit die Pflanze nur verständlich, wenn man das kennt, was zu ihr gehört wie die ganze menschliche Wesenheit zum Fingernagel des Menschen. Dieses zur Pflanze Gehörige kann man aber nicht in der physischen Welt finden. Der Pflanze liegt zunächst etwas zugrunde, was sich nur durch die Imagination in der astralen Welt enthüllt, und ferner etwas, was nur durch die Inspiration in der geistigen Welt offenbar wird.",
      "- So ist also die Pflanze als physisches Wesen die Offenbarung einer Wesenheit, die durch Imagination und Inspiration zu begreifen ist.",
      "Es eröffnet sich für den Beobachter der höheren Welten, wie aus Vorstehendem ersichtlich ist, ein Weg, der in der physischen Welt beginnt. Er kann nämlich zunächst von dieser physischen Welt ausgehen und von deren Offenbarungen aufsteigen zu den ihnen zugrunde liegenden höheren Wesenheiten. Wenn er vom Tierreiche ausgeht, so kann er aufsteigen zur imaginativen Welt; wenn er von der Pflanzenwelt seinen Ausgang nimmt, so führt ihn die geistige Beobachtung durch die Imagination zur Welt der Inspiration. Wenn man diesen Weg geht, dann findet man nämlich bald innerhalb der imaginativen und Inspirationswelt auch Wesenheiten und Tatsachen, welche sich gar nicht in der physischen Welt offenbaren. Man darf also nicht glauben, daß man auf diese Art nur diejenigen Wesenheiten der höheren Welten kennenlernt, welche ihre Offenbarungen in der physischen Welt haben. Wer einmal die",
      "imaginative Welt betreten hat, der lernt eine Fülle von Wesen und Ereignissen kennen, von denen sich der bloße physische Beobachter nichts träumen läßt.",
      "Es gibt nun allerdings auch einen anderen Weg. Einen solchen, der nicht von der physischen Welt seinen Ausgang nimmt. Der den Menschen unmittelbar hellsichtig macht in den höheren Gebieten des Daseins. Für viele Menschen möchte dieser Weg mehr Anziehungskraft haben als der vorhin angedeutete.",
      "Doch sollte für unsere Lebensverhältnisse nur der Aufstieg aus der physischen Welt gewählt werden. Er legt dem Beobachter die Entsagung auf, welche nötig ist, wenn er sich zunächst in der physischen Welt umschauen und da einige Erkenntnisse und namentlich Erfahrungen sammeln soll.",
      "Doch ist er auf alle Fälle für unsere Kulturverhältnisse der Gegenwart der angemessene. Der andere setzt die vorhergängige Aneignung von Seeleneigenschaften voraus, welche innerhalb der gegenwärtigen Lebensverhältnisse äußerst schwer zu erreichen sind.",
      "Wenn auch in einschlägigen Schriften mit aller Schärfe und Deutlichkeit solche Seeleneigenschaften immer wieder und wieder betont werden : von dem Grade, in dem man sich dergleichen (zum Beispiel Selbstlosigkeit, hingebungsvolle Liebe usw.> aneignen muß, wenn man zur Erreichung der höheren Welten nicht von dem festen Boden der physischen ausgehen wollte, machen sich doch die meisten Menschen gar keine auch nur einigermaßen hinreichende Vorstellung. Und wenn dann jemand in den höheren Welten erweckt wird ohne den erforderlichen Grad der entsprechenden Seeleneigenschaften, so müßte unsägliches Elend die Folge sein.",
      "Nun darf man nicht etwa glauben, daß man beim Ausgehen von der physischen Welt und ihren Erfahrungen der",
      "gekennzeichneten Seeleneigenschaften entraten könnte. Solches zu glauben, wäre auch ein folgenschwerer Irrtum. Aber solcher Ausgang gestattet, daß man sich diese Seelen-Eigenschaften in dem Maße und vor allem in der Form aneigne, in denen es in unseren gegenwärtigen Lebensverhältnissen möglich ist.",
      "Und noch etwas kommt dabei in Betracht. Geht man in der angedeuteten Art von der physischen Welt aus, so bleibt man auch trotz seines Aufsteigens in die höheren Welten in einem lebendigen Zusammenhange mit dieser physischen Welt. Man wahrt sich das volle Verständnis für alles, was in ihr vorgeht, und die volle Tatkraft, in ihr zu wirken. Ja, dieses Verständnis und diese Tatkraft wachsen in der förderlichsten Art gerade durch die Erkenntnis der höheren Welten. In jedem Gebiete des Lebens, und wenn es auch noch so prosaisch-praktisch erscheint, wird der Kenner der höheren Welten förderlicher, besser wirken als der Nichtkenner, wenn sich der erstere nur den lebensvollen Zusammenhang mit der physischen Welt bewahrt hat.",
      "Wer aber, ohne von der physischen Welt auszugehen, in den höheren Gebieten des Daseins erweckt wird, der wird allerdings nur zu leicht dem Leben entfremdet; er wird zum Einsiedler, der seiner Mitwelt ohne Verständnis und Anteil gegenübersteht. Ja, es tritt bei unvollständig in dieser Art Ausgebildeten - allerdings nicht bei vollkommen Entwickelten - sogar oft ein, daß sie mit einer gewissen Geringschätzung auf die Erlebnisse der physischen Welt herabsehen, daß sie sich zu vornehm für diese fühlen usw. Statt daß sich ihr Anteil an der Welt erhöhte, werden solche in sich verhärtete, im geistigen Sinne selbstsüchtige Naturen. Die Verführung zu alledem ist nämlich wahrlich nicht gering.",
      "Und diejenigen, welche den Aufstieg in die höheren Welten erstreben, sollten wohl gerade darauf achten.",
      "Von der Inspiration kann der geistige Beobachter zur Intuition aufsteigen. In der Ausdrucksart der Geheimwissenschaft bedeutet dieses Wort in vieler Beziehung das genaue Gegenteil von dem, wofür man es im gewöhnlichen Leben oft anwendet. In letzterem spricht man von Intuition, wenn man einen dunkel als wahr gefühlten Einfall im Auge hat, dem an sich die klare, begriffliche Feststellung noch fehlt. Man sieht darinnen mehr eine Vorstufe der Erkenntnis denn eine solche selbst. Solch ein entsprechender «Einfall» mag - nach dieser Begriffsbestimmung - eine große Wahrheit wie in einem Blitzlicht erleuchten; als Erkenntnis kann er erst gelten, wenn er durch begriffliche Urteile begründet wird. Bisweilen bezeichnet man auch als Intuition etwas, was man als Wahrheit «fühlt», wovon man ganz überzeugt ist, was man aber durch Verstandesurteile nicht belasten will. Menschen, an welche die geheimwissenschaftlichen Erkenntnisse herankommen, sagen gar oft : Das war mir «intuitiv » schon immer klar. Von all dem muß ganz abgesehen werden, wenn man den Ausdruck «Intuition » in seiner hier gemeinten wahren Bedeutung ins Auge fassen will. Intuition ist, in dieser Anwendung, nicht eine Erkenntnis, die an Klarheit hinter der Verstandeserkenntis zurückbleibt, sondern welche diese weit überragt.",
      "In der Inspiration sprechen die Erlebnisse der höheren Welten ihre Bedeutung aus. Der Beobachter lebt in den Eigenschaften und Taten der Wesen dieser höheren Welten. Wenn er, wie oben charakterisiert worden ist, mit seinem Ich einer Linienführung oder einer Gestaltform folgt, so weiß er doch, daß er nicht innerhalb des Wesens selbst",
      "ist, sondern innerhalb dessen Eigenschaften und Verrichtungen. Schon in der imaginativen Erkenntnis erlebt er es ja, daß er sich zum Beispiel nicht außerhalb, sondern innerhalb der Farbenbilder fühlt; aber er weiß auch ebenso genau, daß diese Farbenbilder nicht in sich selbständige Wesen, sondern Eigenschaften solcher Wesen sind.",
      "In der Inspiration wird er sich bewußt, daß er eins wird mit den Taten solcher Wesen, mit den Offenbarungen ihres Willens; erst in der Intuition verschmilzt er mit Wesen, die in sich geschlossen sind, selbst. Im richtigen Sinne kann das nur geschehen, wenn diese Verschmelzung nicht unter Auslöschung, sondern unter völliger Aufrechterhaltung seiner eigenen Wesenheit der Fall ist.",
      "Alles «Sich-Verlieren » an ein fremdes Wesen ist vom Übel. Daher kann nur ein Ich, das in sich bis zu einem hohen Grade gefestigt ist, in ein anderes Wesen ohne Schaden untertauchen. - man hat erst dann etwas intuitiv erfaßt, wenn man diesem «Etwas » gegenüber zu der Empfindung gekommen ist : es äußert sich in ihm ein Wesen, das von derselben Art und inneren Geschlossenheit wie das eigene Ich ist.",
      "Wer einen Stein mit den Sinnen betrachtet und ihn nach seinen Eigenheiten mit dem Verstande - und den gewöhnlichen wissenschaftlichen Hilfsmitteln - zu begreifen sucht, der lernt nur die Außenseite des Steines kennen. Als geistiger Beobachter schreitet er zu der imaginativen und inspirierten Erkenntnis vor.",
      "Lebt er innerhalb der letzteren, so kann er zu einer weiteren Empfindung kommen. Diese Empfindung möchte man durch einen Vergleich in der folgenden Art charakterisieren. Man stelle sich vor, man sehe einen Menschen auf der Straße.",
      "Er macht zunächst auf den Beobachter einen flüchtigen Eindruck. Später lernt man ihn näher kennen; und es",
      "kommt der Augenblick, in dem man mit ihm so befreundet wird, daß sich Seele der Seele aufschließt. Mit dem Erlebnis, das man durchmacht, wenn so die Hüllen der Seelen fallen und Ich dem Ich gegenübersteht, ist dasjenige zu vergleichen, wenn dem geistigen Beobachter der Stein nur wie eine äußere Offenbarung erscheint und er vorschreitet zu etwas, zu dem der Stein gehört, wie der Fingernagel zum menschlichen Leibe gehört, und das sich auslebt als ein «Ich», wie das eigene Ich eines ist.",
      "Erst in der Intuition ist diejenige Erkenntnisart durch den Menschen erreicht, die ihn ins «Innere » der Wesen führt. Bei Besprechung der Inspiration ist einiges angegeben worden über die Umwandlung, welche die innere Seelenverfassung des geistigen Beobachters erfahren muß, wenn er zu dieser Erkenntnisform gelangen will. Es ist da gesagt worden, daß zum Beispiel ein unrichtiges Urteil nicht bloß zum Verstande sprechen darf, sondern zu der Empfindung, daß es Leid, Schmerz bereiten muß. Und der Beobachter muß solches inneres Erleben systematisch ausbilden. Solange allerdings dieser Schmerz entspringt aus den Sympathien und Antipathien des Ich, aus dessen Parteinahme, so lange kann nicht von einer dadurch zu erlangenden Vorbereitung für die Inspiration gesprochen werden. Solches Berührtwerden des Gemütes ist noch weit, sehr weit von dem inneren Anteil entfernt, den das Ich an der bloßen Wahrheit - als Wahrheit - nehmen muß, wenn es die genannten Ziele erreichen will. Es kann gar nicht scharf genug betont werden, daß eigentlich alle Formen des Interesses, die sich im gewöhnlichen Leben als Lust und Leid gegenüber von Wahrheit und Irrtum ausleben, erst schweigen müssen und dann eine ganz andere Interessenart,",
      "die ohne alle Selbstsucht ist, eintreten muß, wenn etwas für die Erkenntnis durch Inspiration geschehen soll. Diese eine Eigenschaft des inneren Seelenlebens ist aber eben nur eines unter den Mitteln zur Vorbereitung für die Inspiration. Es gibt eine unbegrenzte Anzahl anderer, die hinzukommen müssen zu der einen. Und je weiter sich der geistige Beobachter in bezug auf das verfeinert, was ihm schon für die Inspiration gedient hat, desto mehr vermag er sich der Intuition zu nähern. Von der gesetzmäßigen Anweisung, welche die Geheimwissenschaft für die Intuition gibt, wird in weiteren Aufsätzen noch die Rede sein."
    ],
    "sentences": [
      [
        "Wie man die Imagination ein geistiges Schauen nennen kann, so die Inspiration ein geistiges Hören.",
        "Man muß allerdings bei diesem Ausdrucke «Hören » sich darüber klar sein, daß damit ein Wahrnehmen gemeint ist, welches dem sinnlichen Hören in der physischen Welt noch viel ferner steht als das «Schauen» in der imaginativen (astralen) Welt dem Sehen mit den physischen Augen."
      ],
      [
        "Von den Licht- und Farbenerscheinungen der letzteren Welt kann man sagen : sie seien so, wie wenn die leuchtenden Oberflächen und die Farben der sinnlichen Gegenstände sich von diesen abhöben und von ihnen losgelöst frei im Raume schwebten.",
        "Dies gibt aber doch nur eine annähernde Vorstellung."
      ],
      [
        "Denn der Raum der imaginativen Welt ist keineswegs so wie derjenige der physischen.",
        "Wer sich also einbildete, daß er imaginative Farbenbilder vor sich habe, wenn er freischwebende Farbenflocken mit gewöhnlicher Raumausdehnung sieht, der ist im Irrtum."
      ],
      [
        "Dennoch ist aber die Bildung von solchen Farbenvorstellungen der Weg zum imaginativen Leben.",
        "Wer versucht, sich eine Blume vorzustellen, und dann in seiner Vorstellung alles beiseite läßt, was nicht Farbenvorstellung ist, so daß vor seiner Seele ein Bild schwebt wie die von der Blume abgezogene farbige Oberfläche, der kann durch solche Übungen allmählich zu einer Imagination gelangen."
      ],
      [
        "Dies Bild selbst ist noch keine solche Imagination, sondern ein mehr oder weniger vorbereitendes Phantasiegemälde.",
        "Imagination - das ist wirkliches astrales Erlebnis - wird es erst, wenn nicht nur die Farbe ganz abgehoben ist von dem Sinneseindrucke, sondern wenn auch die dreidimensionale Raumausdehnung sich völlig verloren"
      ],
      [
        "hat.",
        "Daß dies letztere der Fall ist, kann nur durch ein gewisses Gefühl wahrgenommen werden.",
        "Zu beschreiben ist dieses Gefühl nur dadurch, daß man sagt, man fühlt sich nicht mehr außerhalb, sondern innerhalb des Farbenbildes, und man hat das Bewußtsein, daß man an seiner Entstehung teilnimmt."
      ],
      [
        "Wenn dies Gefühl nicht da ist, wenn man sich also der Sache gegenüberstehend glaubt wie einem sinnlichen Farbenbild gegenüber, dann hat man es noch nicht mit einer wirklichen Imagination, sondern mit etwas Phantastischem zu tun.",
        "Damit soll jedoch nicht gesagt sein, daß solche Phantasiegemälde ganz wertlos seien."
      ],
      [
        "Sie können nämlich ätherische Abbilder - gleichsam Schatten - wirklicher Strahler Tatsachen sein.",
        "Und als solchen kommt ihnen für die geheimwissenschaftliche Schulung immerhin einiger Wert zu.",
        "Sie können eine Brücke bilden zu den wahren astralen (imaginativen) Erlebnissen. - Eine gewisse Gefahr schließt ihre Beobachtung nur in sich, wenn der Beobachter an diesem Grenzgebiet zwischen Sinnlichem und Übersinnlichem seinen gesunden Menschenverstand nicht voll zur Anwendung bringt."
      ],
      [
        "Man soll nur nicht erwarten, daß irgend jemandem ein allgemeines Kennzeichen gegeben werden kann, wie er in diesem Grenzgebiete Illusion, Halluzination, Phantastik von Wirklichkeit unterscheiden könne.",
        "Bequem wäre ja eine solche allgemeine Regel."
      ],
      [
        "Aber Bequemlichkeit ist ein Wort, das der Geheimschüler in seinem Sprachschatze streichen sollte. - man kann nur sagen, daß derjenige, welcher sich für dieses Gebiet Klarheit der Unterscheidung aneignen will, schon in dem gewöhnlichen Leben der physischen Welt darauf bedacht sein muß.",
        "Wer in diesem gewöhnlichen Leben keine Sorgfalt darauf verwendet, scharf und klar zu denken, der wird beim Aufsteigen"
      ],
      [
        "in höhere Welten allen möglichen Illusionen zum Opfer fallen.",
        "Man bedenke nur, wie viele Fallen dieses gewöhnliche Leben dem gesunden Urteile bietet.",
        "Wie oft kommt es doch vor, daß die Menschen nicht das ungetrübt sehen, was ist, sondern was sie zu sehen begehren.",
        "In wie vielen Fällen glauben die Menschen etwas, nicht weil sie erkannt haben, sondern weil es ihnen angenehm ist, zu glauben.",
        "Oder welche Irrtümer ergeben sich, weil man einer Sache nicht auf den Grund geht, sondern sich vorschnell ein Urteil bildet.",
        "Alle diese Gründe von Täuschungen im gewöhnlichen Leben könnten durch andere schier ins Unendliche vermehrt werden.",
        "Was für Streiche spielen Parteinahme, Leidenschaft usw. usw. einem gesunden Urteile.",
        "Wenn derlei Urteilstäuschungen im gewöhnlichen Leben störend und oft verhängnisvoll sind: für die Gesundheit des übersinnlichen Erlebens sind sie die denkbar größte Gefahr.",
        "Nicht eine allgemeine Regel kann der Geheimschüler als Leitfaden mit in höhere Welten erhalten, sondern lediglich die Anweisung, für seine gesunde Unterscheidungskraft, für sein freies, unabhängiges Urteil alles mögliche zu tun."
      ],
      [
        "Wenn der Beobachter höherer Welten einmal weiß, was wirklich Imagination ist, dann erhält er auch sehr bald die Empfindung, daß die bildet der astralen Welt nicht bloße Bilder, sondern die Kundgebungen geistiger Wesenheiten sind.",
        "Er lernt erkennen, daß er die imaginativen Bilder ebenso auf geistige oder seelische Wesenheiten zu beziehen hat wie die sinnlichen Farben auf sinnliche Dinge oder Wesenheiten.",
        "Im einzelnen wird er allerdings da noch viel zu lernen haben.",
        "Er wird unterscheiden müssen zwischen Farbengebilden, die wie undurchsichtig sind, und solchen, die ganz durchsichtig und wie in ihrem Innern ganz durchleuchtet"
      ],
      [
        "sind.",
        "Ja, auch solche Gebilde wird er wahrnehmen, die ihr Farbenlicht gleichsam in ihrem Innern immer neu erzeugen, die also nicht nur ganz durchleuchtet und durchsichtig (transparent) sind, sondern die immerfort in sich selbst aufstrahlen.",
        "Und er wird die mehr undurchsichtigen Gebilde auf niedrige, die durchleuchteten auf mittlere Wesenheiten beziehen; die in sich aufstrahlenden Bilder werden ihm Kundgebungen höherer geistiger Wesenheiten sein."
      ],
      [
        "Will man die Wahrheit der imaginativen Welt treffen, so darf man den Begriff des geistigen Schauens nicht zu eng fassen.",
        "Denn es finden sich in dieser Welt nicht etwa bloß Licht- und Farbenwahrnehmungen, die sich also den Gesichtserlebnissen der physischen Welt vergleichen lassen, sondern auch Eindrücke von Wärme und Kälte, von Geschmack und Geruch, ja noch andere Erlebnisse der imaginativen «Sinne», für die es etwas ähnliches in der physischen Welt nicht gibt.",
        "Die Eindrücke des Warmen und Kalten sind in der imaginativen (astralen) Welt die Offenbarungen des Willens und der Absichten seelischer und geistiger Wesen.",
        "Ob ein solches Wesen etwas Gutes oder Böses bezweckt, das kommt in einer bestimmten Wärme- oder Kältewirkung zum Vorschein.",
        "Auch «schmecken» und «riechen » kann man die astralen Wesenheiten. - nur dasjenige, was in eigentlichem Sinne das Physische des Tones und Schalles ausmacht, fehlt fast ganz in der wirklich imaginativen Welt.",
        "In dieser Beziehung herrscht da lautlose Stille.",
        "Dafür aber bietet sich etwas ganz anderes dem in der geistigen Beobachtung Fortschreitenden dar, was sich mit dem Tönen und Klingen, mit Musik und Sprache der sinnlichen Welt vergleichen läßt.",
        "Und gerade dann tritt dieses Höhere auf, wenn alles Tönen und Klingen der äußeren"
      ],
      [
        "physischen Welt völlig verstummt, ja wenn auch der geringste innere seelische Nachhall an dieses Gebiet der äußeren Welt zum Schweigen gekommen ist.",
        "Dann tritt für den Beobachter das ein, was man ein Verstehen der Bedeutung der imaginativen Erlebnisse nennen kann."
      ],
      [
        "Wollte man dasjenige, was hier erfahren wird, mit etwas in der physischen Welt vergleichen, so könnte man nur zur Verdeutlichung etwas heranziehen, was es in dieser Welt gar nicht gibt.",
        "Man versuche sich einmal vorzustellen, daß man wahrnehmen könnte die Gedanken und Gefühle eines Menschen, ohne seine Worte mit dem physischen Ohre zu hören, so wäre ein solches Wahrnehmen zu vergleichen mit jenem unmittelbaren Verstehen des Imaginativen, das man als «Hören » in geistigem Sinne bezeichnet."
      ],
      [
        "Das «Sprechende »sind die Farben- und Lichteindrücke.",
        "In dem Aufglänzen und Verlöschen, in der Farbenwandlung der Bilder offenbaren sich Harmonien und Disharmonien, welche die Gefühle, Vorstellungen und Gedanken seelischer und geistiger Wesenheiten enthüllen."
      ],
      [
        "Und wie sich der Ton beim physischen Menschen zum Worte steigert, wenn sich ihm der Gedanke einprägt, so steigern sich die Harmonien und Disharmonien der geistigen Welt zu Offenbarungen, welche wesenhafte Gedanken selbst sind.",
        "Dazu muß es allerdings «dunkel werden » in dieser Welt, wenn der Gedanke in seiner Unmittelbarkeit sich offenbaren soll."
      ],
      [
        "Das hier auftretende Erlebnis stellt sich so dar : Man sieht die hellen Farbentöne, das Rot, Gelb und Orange, ersterben und nimmt wahr, wie sich die höhere Welt durch Grün hindurch abdunkelt zum Blauen und Violetten; dabei erlebt man in sich selbst eine Steigerung der inneren Willensenergie.",
        "Man erlebt eine völlige Freiheit in bezug auf Ort und"
      ],
      [
        "Zeit; man fühlt sich in Bewegung.",
        "Es sind gewisse Linienformen, Gestalten, die man erlebt.",
        "Doch nicht etwa so erlebt man sie, daß man sie vor sich in irgendeinem Raume gezeichnet sähe, sondern so, als ob man in fortwährender Bewegung mit seinem Ich jedem Linienschwung, jeder Gestaltung selbst folgte.",
        "Ja man fühlt das Ich als den Zeichner und zugleich als das Material, mit dem gezeichnet wird.",
        "Und jede Linienführung, jede Ortsänderung sind zugleich Erlebnis dieses Ich.",
        "Man lernt erkennen, daß man mit seinem bewegten Ich hineingeflochten ist in die schaffenden Weltenkräfte.",
        "Die Weltgesetze sind nun dem Ich nicht mehr etwas äußerlich Wahrgenommenes, sondern ein wirkliches Wundergewebe, an dem man spinnt. - die Geheimwissenschaft entwirft allerlei sinnbildliche Zeichnungen und Bilder.",
        "Wenn diese den Tatsachen wirklich entsprechen und nicht bloße ausgedachte Figuren sind, so liegen ihnen Erlebnisse des Beobachters in höheren Welten zugrunde, die in der oben beschriebenen Art anzusehen sind."
      ],
      [
        "So stellt sich die inspirierte Welt in die imaginierte hinein.",
        "Wenn die Imaginationen beginnen dem Beobachter in «stummer Sprache » ihre Bedeutungen zu enthüllen, dann geht innerhalb des Imaginativen die Welt der Inspiration auf."
      ],
      [
        "Von derjenigen Welt, in welche der geistige Beobachter auf diese Art eindringt, ist die physische eine Offenbarung.",
        "Was von dieser physischen Welt den Sinnen und dem auf sie beschränkten Verstand zugänglich ist, das ist nur die Außenseite.",
        "Um nur ein Beispiel anzuführen : die Pflanze, wie sie mit den physischen Sinnen und dem physischen Verstande beobachtet wird, ist nicht das vollständige Pflanzenwesen.",
        "Wer nur diese physische Pflanze kennt, der hat etwas Ähnliches vorliegen, wie ein Wesen haben würde, das"
      ],
      [
        "den Fingernagel eines Menschen wahrnehmen könnte, dem aber die Wahrnehmung des Menschen selbst unzugänglich wäre.",
        "Bau und Wesenheit des Fingernagels können aber nur verstanden werden, wenn man sie aus der ganzen menschlichen Wesenheit erklärt.",
        "So ist in Wahrheit die Pflanze nur verständlich, wenn man das kennt, was zu ihr gehört wie die ganze menschliche Wesenheit zum Fingernagel des Menschen.",
        "Dieses zur Pflanze Gehörige kann man aber nicht in der physischen Welt finden.",
        "Der Pflanze liegt zunächst etwas zugrunde, was sich nur durch die Imagination in der astralen Welt enthüllt, und ferner etwas, was nur durch die Inspiration in der geistigen Welt offenbar wird."
      ],
      [
        "- So ist also die Pflanze als physisches Wesen die Offenbarung einer Wesenheit, die durch Imagination und Inspiration zu begreifen ist."
      ],
      [
        "Es eröffnet sich für den Beobachter der höheren Welten, wie aus Vorstehendem ersichtlich ist, ein Weg, der in der physischen Welt beginnt.",
        "Er kann nämlich zunächst von dieser physischen Welt ausgehen und von deren Offenbarungen aufsteigen zu den ihnen zugrunde liegenden höheren Wesenheiten.",
        "Wenn er vom Tierreiche ausgeht, so kann er aufsteigen zur imaginativen Welt; wenn er von der Pflanzenwelt seinen Ausgang nimmt, so führt ihn die geistige Beobachtung durch die Imagination zur Welt der Inspiration.",
        "Wenn man diesen Weg geht, dann findet man nämlich bald innerhalb der imaginativen und Inspirationswelt auch Wesenheiten und Tatsachen, welche sich gar nicht in der physischen Welt offenbaren.",
        "Man darf also nicht glauben, daß man auf diese Art nur diejenigen Wesenheiten der höheren Welten kennenlernt, welche ihre Offenbarungen in der physischen Welt haben.",
        "Wer einmal die"
      ],
      [
        "imaginative Welt betreten hat, der lernt eine Fülle von Wesen und Ereignissen kennen, von denen sich der bloße physische Beobachter nichts träumen läßt."
      ],
      [
        "Es gibt nun allerdings auch einen anderen Weg.",
        "Einen solchen, der nicht von der physischen Welt seinen Ausgang nimmt.",
        "Der den Menschen unmittelbar hellsichtig macht in den höheren Gebieten des Daseins.",
        "Für viele Menschen möchte dieser Weg mehr Anziehungskraft haben als der vorhin angedeutete."
      ],
      [
        "Doch sollte für unsere Lebensverhältnisse nur der Aufstieg aus der physischen Welt gewählt werden.",
        "Er legt dem Beobachter die Entsagung auf, welche nötig ist, wenn er sich zunächst in der physischen Welt umschauen und da einige Erkenntnisse und namentlich Erfahrungen sammeln soll."
      ],
      [
        "Doch ist er auf alle Fälle für unsere Kulturverhältnisse der Gegenwart der angemessene.",
        "Der andere setzt die vorhergängige Aneignung von Seeleneigenschaften voraus, welche innerhalb der gegenwärtigen Lebensverhältnisse äußerst schwer zu erreichen sind."
      ],
      [
        "Wenn auch in einschlägigen Schriften mit aller Schärfe und Deutlichkeit solche Seeleneigenschaften immer wieder und wieder betont werden : von dem Grade, in dem man sich dergleichen (zum Beispiel Selbstlosigkeit, hingebungsvolle Liebe usw.> aneignen muß, wenn man zur Erreichung der höheren Welten nicht von dem festen Boden der physischen ausgehen wollte, machen sich doch die meisten Menschen gar keine auch nur einigermaßen hinreichende Vorstellung.",
        "Und wenn dann jemand in den höheren Welten erweckt wird ohne den erforderlichen Grad der entsprechenden Seeleneigenschaften, so müßte unsägliches Elend die Folge sein."
      ],
      [
        "Nun darf man nicht etwa glauben, daß man beim Ausgehen von der physischen Welt und ihren Erfahrungen der"
      ],
      [
        "gekennzeichneten Seeleneigenschaften entraten könnte.",
        "Solches zu glauben, wäre auch ein folgenschwerer Irrtum.",
        "Aber solcher Ausgang gestattet, daß man sich diese Seelen-Eigenschaften in dem Maße und vor allem in der Form aneigne, in denen es in unseren gegenwärtigen Lebensverhältnissen möglich ist."
      ],
      [
        "Und noch etwas kommt dabei in Betracht.",
        "Geht man in der angedeuteten Art von der physischen Welt aus, so bleibt man auch trotz seines Aufsteigens in die höheren Welten in einem lebendigen Zusammenhange mit dieser physischen Welt.",
        "Man wahrt sich das volle Verständnis für alles, was in ihr vorgeht, und die volle Tatkraft, in ihr zu wirken.",
        "Ja, dieses Verständnis und diese Tatkraft wachsen in der förderlichsten Art gerade durch die Erkenntnis der höheren Welten.",
        "In jedem Gebiete des Lebens, und wenn es auch noch so prosaisch-praktisch erscheint, wird der Kenner der höheren Welten förderlicher, besser wirken als der Nichtkenner, wenn sich der erstere nur den lebensvollen Zusammenhang mit der physischen Welt bewahrt hat."
      ],
      [
        "Wer aber, ohne von der physischen Welt auszugehen, in den höheren Gebieten des Daseins erweckt wird, der wird allerdings nur zu leicht dem Leben entfremdet; er wird zum Einsiedler, der seiner Mitwelt ohne Verständnis und Anteil gegenübersteht.",
        "Ja, es tritt bei unvollständig in dieser Art Ausgebildeten - allerdings nicht bei vollkommen Entwickelten - sogar oft ein, daß sie mit einer gewissen Geringschätzung auf die Erlebnisse der physischen Welt herabsehen, daß sie sich zu vornehm für diese fühlen usw.",
        "Statt daß sich ihr Anteil an der Welt erhöhte, werden solche in sich verhärtete, im geistigen Sinne selbstsüchtige Naturen.",
        "Die Verführung zu alledem ist nämlich wahrlich nicht gering."
      ],
      [
        "Und diejenigen, welche den Aufstieg in die höheren Welten erstreben, sollten wohl gerade darauf achten."
      ],
      [
        "Von der Inspiration kann der geistige Beobachter zur Intuition aufsteigen.",
        "In der Ausdrucksart der Geheimwissenschaft bedeutet dieses Wort in vieler Beziehung das genaue Gegenteil von dem, wofür man es im gewöhnlichen Leben oft anwendet.",
        "In letzterem spricht man von Intuition, wenn man einen dunkel als wahr gefühlten Einfall im Auge hat, dem an sich die klare, begriffliche Feststellung noch fehlt.",
        "Man sieht darinnen mehr eine Vorstufe der Erkenntnis denn eine solche selbst.",
        "Solch ein entsprechender «Einfall» mag - nach dieser Begriffsbestimmung - eine große Wahrheit wie in einem Blitzlicht erleuchten; als Erkenntnis kann er erst gelten, wenn er durch begriffliche Urteile begründet wird.",
        "Bisweilen bezeichnet man auch als Intuition etwas, was man als Wahrheit «fühlt», wovon man ganz überzeugt ist, was man aber durch Verstandesurteile nicht belasten will.",
        "Menschen, an welche die geheimwissenschaftlichen Erkenntnisse herankommen, sagen gar oft : Das war mir «intuitiv » schon immer klar.",
        "Von all dem muß ganz abgesehen werden, wenn man den Ausdruck «Intuition » in seiner hier gemeinten wahren Bedeutung ins Auge fassen will.",
        "Intuition ist, in dieser Anwendung, nicht eine Erkenntnis, die an Klarheit hinter der Verstandeserkenntis zurückbleibt, sondern welche diese weit überragt."
      ],
      [
        "In der Inspiration sprechen die Erlebnisse der höheren Welten ihre Bedeutung aus.",
        "Der Beobachter lebt in den Eigenschaften und Taten der Wesen dieser höheren Welten.",
        "Wenn er, wie oben charakterisiert worden ist, mit seinem Ich einer Linienführung oder einer Gestaltform folgt, so weiß er doch, daß er nicht innerhalb des Wesens selbst"
      ],
      [
        "ist, sondern innerhalb dessen Eigenschaften und Verrichtungen.",
        "Schon in der imaginativen Erkenntnis erlebt er es ja, daß er sich zum Beispiel nicht außerhalb, sondern innerhalb der Farbenbilder fühlt; aber er weiß auch ebenso genau, daß diese Farbenbilder nicht in sich selbständige Wesen, sondern Eigenschaften solcher Wesen sind."
      ],
      [
        "In der Inspiration wird er sich bewußt, daß er eins wird mit den Taten solcher Wesen, mit den Offenbarungen ihres Willens; erst in der Intuition verschmilzt er mit Wesen, die in sich geschlossen sind, selbst.",
        "Im richtigen Sinne kann das nur geschehen, wenn diese Verschmelzung nicht unter Auslöschung, sondern unter völliger Aufrechterhaltung seiner eigenen Wesenheit der Fall ist."
      ],
      [
        "Alles «Sich-Verlieren » an ein fremdes Wesen ist vom Übel.",
        "Daher kann nur ein Ich, das in sich bis zu einem hohen Grade gefestigt ist, in ein anderes Wesen ohne Schaden untertauchen. - man hat erst dann etwas intuitiv erfaßt, wenn man diesem «Etwas » gegenüber zu der Empfindung gekommen ist : es äußert sich in ihm ein Wesen, das von derselben Art und inneren Geschlossenheit wie das eigene Ich ist."
      ],
      [
        "Wer einen Stein mit den Sinnen betrachtet und ihn nach seinen Eigenheiten mit dem Verstande - und den gewöhnlichen wissenschaftlichen Hilfsmitteln - zu begreifen sucht, der lernt nur die Außenseite des Steines kennen.",
        "Als geistiger Beobachter schreitet er zu der imaginativen und inspirierten Erkenntnis vor."
      ],
      [
        "Lebt er innerhalb der letzteren, so kann er zu einer weiteren Empfindung kommen.",
        "Diese Empfindung möchte man durch einen Vergleich in der folgenden Art charakterisieren.",
        "Man stelle sich vor, man sehe einen Menschen auf der Straße."
      ],
      [
        "Er macht zunächst auf den Beobachter einen flüchtigen Eindruck.",
        "Später lernt man ihn näher kennen; und es"
      ],
      [
        "kommt der Augenblick, in dem man mit ihm so befreundet wird, daß sich Seele der Seele aufschließt.",
        "Mit dem Erlebnis, das man durchmacht, wenn so die Hüllen der Seelen fallen und Ich dem Ich gegenübersteht, ist dasjenige zu vergleichen, wenn dem geistigen Beobachter der Stein nur wie eine äußere Offenbarung erscheint und er vorschreitet zu etwas, zu dem der Stein gehört, wie der Fingernagel zum menschlichen Leibe gehört, und das sich auslebt als ein «Ich», wie das eigene Ich eines ist."
      ],
      [
        "Erst in der Intuition ist diejenige Erkenntnisart durch den Menschen erreicht, die ihn ins «Innere » der Wesen führt.",
        "Bei Besprechung der Inspiration ist einiges angegeben worden über die Umwandlung, welche die innere Seelenverfassung des geistigen Beobachters erfahren muß, wenn er zu dieser Erkenntnisform gelangen will.",
        "Es ist da gesagt worden, daß zum Beispiel ein unrichtiges Urteil nicht bloß zum Verstande sprechen darf, sondern zu der Empfindung, daß es Leid, Schmerz bereiten muß.",
        "Und der Beobachter muß solches inneres Erleben systematisch ausbilden.",
        "Solange allerdings dieser Schmerz entspringt aus den Sympathien und Antipathien des Ich, aus dessen Parteinahme, so lange kann nicht von einer dadurch zu erlangenden Vorbereitung für die Inspiration gesprochen werden.",
        "Solches Berührtwerden des Gemütes ist noch weit, sehr weit von dem inneren Anteil entfernt, den das Ich an der bloßen Wahrheit - als Wahrheit - nehmen muß, wenn es die genannten Ziele erreichen will.",
        "Es kann gar nicht scharf genug betont werden, daß eigentlich alle Formen des Interesses, die sich im gewöhnlichen Leben als Lust und Leid gegenüber von Wahrheit und Irrtum ausleben, erst schweigen müssen und dann eine ganz andere Interessenart,"
      ],
      [
        "die ohne alle Selbstsucht ist, eintreten muß, wenn etwas für die Erkenntnis durch Inspiration geschehen soll.",
        "Diese eine Eigenschaft des inneren Seelenlebens ist aber eben nur eines unter den Mitteln zur Vorbereitung für die Inspiration.",
        "Es gibt eine unbegrenzte Anzahl anderer, die hinzukommen müssen zu der einen.",
        "Und je weiter sich der geistige Beobachter in bezug auf das verfeinert, was ihm schon für die Inspiration gedient hat, desto mehr vermag er sich der Intuition zu nähern.",
        "Von der gesetzmäßigen Anweisung, welche die Geheimwissenschaft für die Intuition gibt, wird in weiteren Aufsätzen noch die Rede sein."
      ]
    ]
  },
  {
    "order": 8,
    "title_de": "AUS DEM NACHWORT VON MARIE STEINER",
    "paragraphs": [
      "Rudolf Steiner hat die hier nicht zum Abschluß gebrachten Gedankengänge in anderen Werken weitergeführt. Als eine Art Fortsetzung des hier Gegebenen bezeichnet er selbst die Schriften «Ein Weg zur Selbsterkenntnis des Menschen» und «Die Schwelle der geistigen Welt». - «Kosmologie, Religion und Philosophie» ist eine weitere Steigerung in der Kraft der lichtvollen Schilderung meditativer Erkenntnisvorgänge, ebenso das Büchlein «Vom Seelenleben »Den Höhepunkt in der Formulierung übersinnlicher Erkenntnisse erreichte Rudolf Steiner in seinem letzten Lebensjahr, als er uns wie ein Vermächtnis hinterließ seine «Leitsätze für die Anthroposophische Gesellschaft » und seine «Briefe an die Mitglieder», die nun erschienen sind unter dem Titel «Das Michael-Mysterium». Sie sind der Abschluß und die Krönung des hier begonnenen Werkes für die esoterische Bewußtseinserziehung der Menschheit. Wem es noch zu schwer wird, sich hier allein durchzuarbeiten, der lese und erlebe die tiefgreifenden Ausführungen Carl Ungers in seinem Werk «Aus der Sprache der Bewußtseinsseele» Er wird einen nie genug einzuschätzenden Gewinn davon haben. Diese Briefe, die Unger für einen Kreis von Mitgliedern, dann für die Zeitschrift «Anthroposophie» geschrieben hat, und die nach seinem Tode als Buch gesammelt erschienen sind, sind die lebendigste Erarbeitung des gewaltigen Stoffes, bilden Erkenntnisvorgänge um zu Lebensvorgängen. Hier hat sich in einer Seele das vollzogen, was Rudolf Steiner in seinen Schülern wachrufen wollte: das Denken ist wieder Leben geworden. Die Sprache der Bewußtseinsseele findet den Weg zum verlorenen Wort,",
      "das Rudolf Steiner dem Sterben entrissen und der Menschheit wiedergegeben hat."
    ],
    "sentences": [
      [
        "Rudolf Steiner hat die hier nicht zum Abschluß gebrachten Gedankengänge in anderen Werken weitergeführt.",
        "Als eine Art Fortsetzung des hier Gegebenen bezeichnet er selbst die Schriften «Ein Weg zur Selbsterkenntnis des Menschen» und «Die Schwelle der geistigen Welt». - «Kosmologie, Religion und Philosophie» ist eine weitere Steigerung in der Kraft der lichtvollen Schilderung meditativer Erkenntnisvorgänge, ebenso das Büchlein «Vom Seelenleben »Den Höhepunkt in der Formulierung übersinnlicher Erkenntnisse erreichte Rudolf Steiner in seinem letzten Lebensjahr, als er uns wie ein Vermächtnis hinterließ seine «Leitsätze für die Anthroposophische Gesellschaft » und seine «Briefe an die Mitglieder», die nun erschienen sind unter dem Titel «Das Michael-Mysterium».",
        "Sie sind der Abschluß und die Krönung des hier begonnenen Werkes für die esoterische Bewußtseinserziehung der Menschheit.",
        "Wem es noch zu schwer wird, sich hier allein durchzuarbeiten, der lese und erlebe die tiefgreifenden Ausführungen Carl Ungers in seinem Werk «Aus der Sprache der Bewußtseinsseele» Er wird einen nie genug einzuschätzenden Gewinn davon haben.",
        "Diese Briefe, die Unger für einen Kreis von Mitgliedern, dann für die Zeitschrift «Anthroposophie» geschrieben hat, und die nach seinem Tode als Buch gesammelt erschienen sind, sind die lebendigste Erarbeitung des gewaltigen Stoffes, bilden Erkenntnisvorgänge um zu Lebensvorgängen.",
        "Hier hat sich in einer Seele das vollzogen, was Rudolf Steiner in seinen Schülern wachrufen wollte: das Denken ist wieder Leben geworden.",
        "Die Sprache der Bewußtseinsseele findet den Weg zum verlorenen Wort,"
      ],
      [
        "das Rudolf Steiner dem Sterben entrissen und der Menschheit wiedergegeben hat."
      ]
    ]
  },
  {
    "order": 9,
    "title_de": "ZUR NEUAUFLAGE 1959",
    "paragraphs": [
      "Als Rudolf Steiner im Jahre 1914 die Neuauflage des Buches «Wie erlangt man Erkenntnisse der höheren Welten? »vorbereitete, hatte er vor, auch die Aufsätze «Die Stufen der höheren Erkenntnis», die von 1905 in der Zeitschrift «Lucifer-Gnosis» erschienen waren, neu durchzuarbeiten und in Buchform erscheinen zu lassen. Diese Neuauflage mußte wegen des Krieges unterbleiben.",
      "Im Jahre 1931 gab Frau Marie Steiner zum erstenmal diese Aufsätze in Buchform heraus. Im Sinne dessen, was Rudolf Steiner in seinen Vorreden über die Umarbeitung des Buches «Wie erlangt man Erkenntnisse der höheren Welten?» zum Ausdruck bringt, wurden an zwei Stellen Änderungen vorgenommen; die Unabhängigkeit des Schülers vom Lehrer sollte betont werden.",
      "Der hier vorliegenden zweiten Buchausgabe im Rahmen der Gesamtausgabe der Werke Rudolf Steiners liegt der Wortlaut der Aufsätze aus der Zeitschrift «Lucifer-Gnosis »zugrunde mit Ausnahme der von Rudolf Steiner 1914 vorgenommenen Korrekturen. Vorangestellt wurden Bemerkungen Rudolf Steiners aus dem gleichen Jahre zur fünften Auflage des Buches «Wie erlangt man Erkenntnisse der höheren Welten?»; sie können auch für die Aufsätze «Die Stufen der höheren Erkenntnis» gelten."
    ],
    "sentences": [
      [
        "Als Rudolf Steiner im Jahre 1914 die Neuauflage des Buches «Wie erlangt man Erkenntnisse der höheren Welten? »vorbereitete, hatte er vor, auch die Aufsätze «Die Stufen der höheren Erkenntnis», die von 1905 in der Zeitschrift «Lucifer-Gnosis» erschienen waren, neu durchzuarbeiten und in Buchform erscheinen zu lassen.",
        "Diese Neuauflage mußte wegen des Krieges unterbleiben."
      ],
      [
        "Im Jahre 1931 gab Frau Marie Steiner zum erstenmal diese Aufsätze in Buchform heraus.",
        "Im Sinne dessen, was Rudolf Steiner in seinen Vorreden über die Umarbeitung des Buches «Wie erlangt man Erkenntnisse der höheren Welten?» zum Ausdruck bringt, wurden an zwei Stellen Änderungen vorgenommen; die Unabhängigkeit des Schülers vom Lehrer sollte betont werden."
      ],
      [
        "Der hier vorliegenden zweiten Buchausgabe im Rahmen der Gesamtausgabe der Werke Rudolf Steiners liegt der Wortlaut der Aufsätze aus der Zeitschrift «Lucifer-Gnosis »zugrunde mit Ausnahme der von Rudolf Steiner 1914 vorgenommenen Korrekturen.",
        "Vorangestellt wurden Bemerkungen Rudolf Steiners aus dem gleichen Jahre zur fünften Auflage des Buches «Wie erlangt man Erkenntnisse der höheren Welten?»; sie können auch für die Aufsätze «Die Stufen der höheren Erkenntnis» gelten."
      ]
    ]
  }
]

# === SQL GENERATION ===
def generate_sql():
    """Generate SQL using PL/pgSQL DO block."""
    sql_lines = []
    sql_lines.append("-- Auto-generated import for " + GA_NUMBER)
    sql_lines.append("BEGIN;")
    sql_lines.append("")
    sql_lines.append("DO $$")
    sql_lines.append("DECLARE")
    sql_lines.append("    v_book_id INT;")
    sql_lines.append("    v_lecture_id INT;")
    sql_lines.append("    v_para_id INT;")
    sql_lines.append("BEGIN")
    sql_lines.append("    -- Create or get book")
    te = BOOK_TITLE.replace("'", "''")
    sql_lines.append("    v_book_id := (SELECT id FROM books WHERE ga_number = '%s');" % GA_NUMBER)
    sql_lines.append("    IF v_book_id IS NULL THEN")
    sql_lines.append("        INSERT INTO books (ga_number, title_de, pdf_filename)")
    sql_lines.append("        VALUES ('%s', '%s', '%s.epub')" % (GA_NUMBER, te, GA_NUMBER))
    sql_lines.append("        RETURNING id INTO v_book_id;")
    sql_lines.append("    ELSE")
    sql_lines.append("        UPDATE books SET title_de = '%s' WHERE id = v_book_id;" % te)
    sql_lines.append("    END IF;")
    sql_lines.append("")
    sql_lines.append("    -- Delete old data (cascades to paragraphs/sentences)")
    sql_lines.append("    DELETE FROM lectures WHERE book_id = v_book_id;")
    sql_lines.append("")

    for ch in CHAPTERS:
        te = ch["title_de"].replace("'", "''")
        sql_lines.append("    -- Chapter %d: %s" % (ch["order"], te))
        sql_lines.append("    INSERT INTO lectures (book_id, title_de, order_index, level)")
        sql_lines.append("    VALUES (v_book_id, '%s', %d, 'lecture')" % (te, ch["order"]))
        sql_lines.append("    RETURNING id INTO v_lecture_id;")
        sql_lines.append("")

        for pi, para_text in enumerate(ch["paragraphs"], 1):
            sentences = ch["sentences"][pi - 1] if pi - 1 < len(ch["sentences"]) else []
            if not sentences:
                continue

            sql_lines.append("    INSERT INTO paragraphs (lecture_id, order_index)")
            sql_lines.append("    VALUES (v_lecture_id, %d)" % pi)
            sql_lines.append("    RETURNING id INTO v_para_id;")
            sql_lines.append("")

            for si, sent in enumerate(sentences, 1):
                se = sent.replace("'", "''")
                sql_lines.append("    INSERT INTO sentences (paragraph_id, order_index, text_de)")
                sql_lines.append("    VALUES (v_para_id, %d, '%s');" % (si, se))
                sql_lines.append("")

    sql_lines.append("END $$;")
    sql_lines.append("COMMIT;")
    sql_lines.append("")

    return "\n".join(sql_lines)


def import_to_db():
    """Run the SQL import via docker exec psql."""
    print("Generating SQL for %s..." % GA_NUMBER)
    sql = generate_sql()
    sql_path = "/tmp/%s_import.sql" % GA_NUMBER
    Path(sql_path).write_text(sql, encoding='utf-8')
    ln = len(sql.split('\n'))
    sk = len(sql) / 1024
    print("  SQL written: %s (%d lines, %d KB)" % (sql_path, ln, sk))

    result = subprocess.run(
        ["docker", "cp", sql_path, "%s:/tmp/%s_import.sql" % (DOCKER_CONTAINER, GA_NUMBER)],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        print("  FAILED COPY: %s" % result.stderr)
        return False

    print("  Importing into Docker PostgreSQL...")
    with open(sql_path, 'r') as f:
        proc = subprocess.Popen(
            ["docker", "exec", "-i", DOCKER_CONTAINER, "psql", "-U", DB_USER, "-d", DB_NAME],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            text=True
        )
        stdout, stderr = proc.communicate(input=sql)

    if proc.returncode != 0:
        sl = stderr.strip().split('\n')
        print("  psql error (exit=%d):" % proc.returncode)
        for line in sl[-5:]:
            print("     %s" % line)
        return False
    else:
        print("  IMPORTED %s successfully!" % GA_NUMBER)
        if stdout.strip():
            for line in stdout.strip().split('\n')[-3:]:
                print("     %s" % line)
        return True


if __name__ == "__main__":
    print()
    print("=" * 60)
    print("Importing %s: %s" % (GA_NUMBER, BOOK_TITLE))
    print("=" * 60)

    tp = sum(len(c["paragraphs"]) for c in CHAPTERS)
    ts = sum(sum(len(s) for s in c["sentences"]) for c in CHAPTERS)
    print("  %d chapters, %d paragraphs, %d sentences" % (len(CHAPTERS), tp, ts))

    success = import_to_db()
    sys.exit(0 if success else 1)
